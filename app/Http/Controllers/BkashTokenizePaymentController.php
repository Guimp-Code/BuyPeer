<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BkashTokenizePaymentController extends Controller
{
    public function index()
    {
        return response()->json(['message' => 'Bkash Tokenize Payment Controller']);
    }
} 