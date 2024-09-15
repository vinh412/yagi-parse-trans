package com.vinhdd.yagi.repository;

import com.vinhdd.yagi.model.Transaction;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

import java.time.LocalDate;

public interface TransactionRepository extends JpaRepository<Transaction, Integer> {
    Page<Transaction> findAllByDateCreatedBetween(LocalDate from, LocalDate to, Pageable pageable);
    Page<Transaction> findAllByMessageContainingIgnoreCase(String message, Pageable pageable);
    Page<Transaction> findAllByMessageContainingIgnoreCaseAndDateCreatedBetween(String message, LocalDate from, LocalDate to, Pageable pageable);
}
