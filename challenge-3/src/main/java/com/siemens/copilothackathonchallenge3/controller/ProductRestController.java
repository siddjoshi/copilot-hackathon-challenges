package com.siemens.copilothackathonchallenge3.controller;

import com.siemens.copilothackathonchallenge3.entity.Product;
import com.siemens.copilothackathonchallenge3.service.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/items")
public class ProductRestController {

    @Autowired
    private ProductService productService;

    @GetMapping
    public List<Product> getAllProducts() {
        return productService.getAllProducts();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Product> getProductById(@PathVariable String id) {
        Product product = productService.getProductById(Long.valueOf(id));
        return ResponseEntity.ok(product);
    }

    @PostMapping
    public Product createProduct(@RequestBody Product product) {
        return productService.saveProduct(product);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Product> updateProduct(@PathVariable String id, @RequestBody Product productDetails) {
        Product updatedProduct = productService.getProductById(Long.valueOf(id));
        updatedProduct.setName(productDetails.getName());
        updatedProduct.setDescription(productDetails.getDescription());
        updatedProduct.setPrice(productDetails.getPrice());
        return ResponseEntity.ok(productService.saveProduct(updatedProduct));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteProduct(@PathVariable String id) {
        productService.deleteProduct(Long.valueOf(id));
        return ResponseEntity.noContent().build();
    }
}