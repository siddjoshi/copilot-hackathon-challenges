package com.siemens.copilothackathonchallenge4.repository;

import com.siemens.copilothackathonchallenge4.entity.Product;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ProductRepository extends JpaRepository<Product, String> {
}