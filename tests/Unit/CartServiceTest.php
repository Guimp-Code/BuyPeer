<?php

namespace Tests\Unit;

use Tests\TestCase;
use App\Services\CartService;
use App\Models\Product;
use App\Models\User;
use App\Enums\Status;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\DatabaseTransactions;

class CartServiceTest extends TestCase
{
    use DatabaseTransactions;

    protected CartService $cartService;
    protected User $user;
    protected Product $product;

    protected function setUp(): void
    {
        parent::setUp();
        $this->cartService = new CartService();
        
        // Criar usuário de teste
        $this->user = User::factory()->create();
        
        // Criar produto de teste
        $this->product = Product::factory()->create([
            'name' => 'Produto Teste',
            'sku' => 'TEST-001',
            'stock_quantity' => 10,
            'price' => 99.90,
            'status' => Status::ACTIVE,
        ]);
    }

    /** @test */
    public function pode_adicionar_item_ao_carrinho_com_sucesso()
    {
        $this->actingAs($this->user);
        
        $result = $this->cartService->addItem([
            'product_id' => $this->product->id,
            'quantity' => 2,
            'variation_id' => null
        ]);

        $this->assertTrue($result);
        $this->assertDatabaseHas('cart_items', [
            'user_id' => $this->user->id,
            'product_id' => $this->product->id,
            'quantity' => 2
        ]);
    }

    /** @test */
    public function nao_pode_adicionar_item_sem_estoque_suficiente()
    {
        $this->actingAs($this->user);
        
        $this->expectException(\Exception::class);
        $this->expectExceptionMessage('Estoque insuficiente');
        
        $this->cartService->addItem([
            'product_id' => $this->product->id,
            'quantity' => 15, // Mais que o estoque (10)
            'variation_id' => null
        ]);
    }

    /** @test */
    public function incrementa_quantidade_se_item_ja_existe_no_carrinho()
    {
        $this->actingAs($this->user);
        
        // Adicionar item pela primeira vez
        $this->cartService->addItem([
            'product_id' => $this->product->id,
            'quantity' => 2,
            'variation_id' => null
        ]);
        
        // Adicionar o mesmo item novamente
        $this->cartService->addItem([
            'product_id' => $this->product->id,
            'quantity' => 3,
            'variation_id' => null
        ]);

        $this->assertDatabaseHas('cart_items', [
            'user_id' => $this->user->id,
            'product_id' => $this->product->id,
            'quantity' => 5 // 2 + 3
        ]);
    }

    /** @test */
    public function nao_pode_adicionar_produto_inativo()
    {
        $this->product->update(['status' => Status::INACTIVE]);
        $this->actingAs($this->user);
        
        $this->expectException(\Exception::class);
        $this->expectExceptionMessage('Produto não disponível');
        
        $this->cartService->addItem([
            'product_id' => $this->product->id,
            'quantity' => 1,
            'variation_id' => null
        ]);
    }

    /** @test */
    public function nao_pode_adicionar_quantidade_zero_ou_negativa()
    {
        $this->actingAs($this->user);
        
        $this->expectException(\Exception::class);
        $this->expectExceptionMessage('Quantidade deve ser maior que zero');
        
        $this->cartService->addItem([
            'product_id' => $this->product->id,
            'quantity' => 0,
            'variation_id' => null
        ]);
    }

    /** @test */
    public function nao_pode_adicionar_produto_inexistente()
    {
        $this->actingAs($this->user);
        
        $this->expectException(\Exception::class);
        $this->expectExceptionMessage('Produto não encontrado');
        
        $this->cartService->addItem([
            'product_id' => 99999, // ID inexistente
            'quantity' => 1,
            'variation_id' => null
        ]);
    }

    /** @test */
    public function usuario_nao_autenticado_nao_pode_adicionar_item()
    {
        $this->expectException(\Exception::class);
        $this->expectExceptionMessage('Usuário não autenticado');
        
        $this->cartService->addItem([
            'product_id' => $this->product->id,
            'quantity' => 1,
            'variation_id' => null
        ]);
    }
} 