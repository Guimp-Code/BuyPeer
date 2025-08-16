<?php

namespace App\Services;

use App\Models\Product;
use App\Models\ProductCategory;
use App\Models\Brand;
use App\Models\Unit;
use App\Enums\Status;
use App\Enums\Activity;
use Illuminate\Http\Request;
use Illuminate\Pagination\LengthAwarePaginator;
use Exception;

class ProductService
{
    /**
     * Get paginated list of products
     */
    public function list(Request $request): LengthAwarePaginator
    {
        try {
            $perPage = $request->get('per_page', 20);
            $searchTerm = $request->get('search');

            $query = Product::with(['category', 'brand', 'unit'])
                           ->where('status', Status::ACTIVE);

            if ($searchTerm) {
                $query->where(function($q) use ($searchTerm) {
                    $q->where('name', 'LIKE', "%{$searchTerm}%")
                      ->orWhere('sku', 'LIKE', "%{$searchTerm}%");
                });
            }

            return $query->orderBy('created_at', 'desc')
                        ->paginate($perPage);
        } catch (Exception $e) {
            throw new Exception('Failed to retrieve products: ' . $e->getMessage());
        }
    }

    /**
     * Create new product
     */
    public function create(array $data): Product
    {
        try {
            return Product::create([
                'name' => $data['name'],
                'sku' => $data['sku'],
                'description' => $data['description'] ?? '',
                'price' => $data['price'],
                'category_id' => $data['category_id'],
                'brand_id' => $data['brand_id'] ?? null,
                'unit_id' => $data['unit_id'] ?? null,
                'stock_quantity' => $data['stock_quantity'] ?? 0,
                'status' => $data['status'] ?? Status::ACTIVE,
                'is_featured' => $data['is_featured'] ?? Activity::DISABLE,
            ]);
        } catch (Exception $e) {
            throw new Exception('Failed to create product: ' . $e->getMessage());
        }
    }

    /**
     * Update existing product
     */
    public function update(Product $product, array $data): Product
    {
        try {
            $product->update([
                'name' => $data['name'],
                'sku' => $data['sku'],
                'description' => $data['description'] ?? $product->description,
                'price' => $data['price'],
                'category_id' => $data['category_id'],
                'brand_id' => $data['brand_id'] ?? $product->brand_id,
                'unit_id' => $data['unit_id'] ?? $product->unit_id,
                'stock_quantity' => $data['stock_quantity'] ?? $product->stock_quantity,
                'status' => $data['status'] ?? $product->status,
                'is_featured' => $data['is_featured'] ?? $product->is_featured,
            ]);

            return $product->fresh();
        } catch (Exception $e) {
            throw new Exception('Failed to update product: ' . $e->getMessage());
        }
    }

    /**
     * Delete product
     */
    public function delete(Product $product): bool
    {
        try {
            return $product->delete();
        } catch (Exception $e) {
            throw new Exception('Failed to delete product: ' . $e->getMessage());
        }
    }

    /**
     * Get product with relationships
     */
    public function getWithRelations(int $id): Product
    {
        try {
            return Product::with(['category', 'brand', 'unit', 'images', 'variations'])
                         ->findOrFail($id);
        } catch (Exception $e) {
            throw new Exception('Product not found: ' . $e->getMessage());
        }
    }

    /**
     * Update stock quantity
     */
    public function updateStock(Product $product, int $quantity): Product
    {
        try {
            $product->update(['stock_quantity' => $quantity]);
            return $product->fresh();
        } catch (Exception $e) {
            throw new Exception('Failed to update stock: ' . $e->getMessage());
        }
    }

    /**
     * Check if product has sufficient stock
     */
    public function hasStock(Product $product, int $requestedQuantity): bool
    {
        return $product->stock_quantity >= $requestedQuantity;
    }

    /**
     * Get featured products
     */
    public function getFeatured(int $limit = 10): \Illuminate\Database\Eloquent\Collection
    {
        try {
            return Product::with(['category', 'brand'])
                         ->where('status', Status::ACTIVE)
                         ->where('is_featured', Activity::ENABLE)
                         ->limit($limit)
                         ->get();
        } catch (Exception $e) {
            throw new Exception('Failed to get featured products: ' . $e->getMessage());
        }
    }

    /**
     * Top products for dashboard widgets
     * Fallback simples: ordena por vendas se houver coluna, senão por created_at/visibilidade.
     */
    public function topProducts(int $limit = 10): \Illuminate\Database\Eloquent\Collection
    {
        try {
            $query = Product::with(['variations'])
                ->where('status', Status::ACTIVE);

            // Se existir coluna total_sold/total_orders, preferir
            $columns = \Schema::getColumnListing((new Product())->getTable());
            if (in_array('total_sold', $columns)) {
                $query->orderByDesc('total_sold');
            } elseif (in_array('total_orders', $columns)) {
                $query->orderByDesc('total_orders');
            } else {
                $query->orderByDesc('created_at');
            }

            return $query->limit($limit)->get();
        } catch (Exception $e) {
            throw new Exception('Failed to get top products: ' . $e->getMessage());
        }
    }
}
