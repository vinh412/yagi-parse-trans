package com.vinhdd.yagi.controller;

import com.vinhdd.yagi.model.File;
import com.vinhdd.yagi.model.Transaction;
import com.vinhdd.yagi.repository.FileRepository;
import com.vinhdd.yagi.repository.TransactionRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

@RestController()
@RequestMapping("/")
@RequiredArgsConstructor
public class TransactionsController {
    private final TransactionRepository transactionRepository;
    private final FileRepository fileRepository;
    @Cacheable("trans")
    @GetMapping("/")
    @CrossOrigin("http://localhost:5173")
    public Page<Transaction> getTransactions(@RequestParam(defaultValue = "1") int page,
                                             @RequestParam(required = false) Optional<String> search,
                                             @RequestParam(defaultValue = "2024-09-01") @DateTimeFormat(iso = DateTimeFormat.ISO.DATE) LocalDate startDate,
                                             @RequestParam(defaultValue = "2024-09-15") @DateTimeFormat(iso = DateTimeFormat.ISO.DATE) LocalDate endDate,
                                             @RequestParam(defaultValue = "10") int rowsPerPage,
                                             @RequestParam(defaultValue = "amount") String sortBy,
                                             @RequestParam(defaultValue = "desc") String sortOrder,
                                             @RequestParam(defaultValue = "all") String account) {
        Sort sort = Sort.by(sortBy).descending();
        if(sortOrder.equals("asc"))
            sort = Sort.by(sortBy).ascending();
        Pageable pageable = PageRequest.of(page-1, rowsPerPage, sort);
        if(search.isPresent()) {
            return transactionRepository.findAllByMessageContainingIgnoreCaseAndDateCreatedGreaterThanEqualAndDateCreatedLessThanEqual(search.get(), startDate, endDate, pageable);
        }
        return transactionRepository.findAllByDateCreatedBetween(startDate, endDate, pageable);
    }

    @Cacheable("files")
    @GetMapping("/files")
    @CrossOrigin("http://localhost:5173")
    public List<File> getAllFiles() {
        return fileRepository.findAll();
    }

    @Cacheable("number")
    @GetMapping("/cache/{a}")
    public int testCache(@PathVariable int a){
        simulateSlowService();
        return a;
    }

    private void simulateSlowService() {
        try {
            long time = 3000L;
            Thread.sleep(time);
        } catch (InterruptedException e) {
            throw new IllegalStateException(e);
        }
    }
}
