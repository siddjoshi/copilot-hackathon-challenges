package com.siemens.copilothackathonchallenge3.repository;

import com.siemens.copilothackathonchallenge3.entity.Product;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ProductRepository extends JpaRepository<Product, Long> {
}