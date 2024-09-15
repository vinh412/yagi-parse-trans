package com.vinhdd.yagi.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDate;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "transactions1")
public class Transaction {
    @Id
    @Column(name = "id")
    private int id;
    @Column(name = "date_created")
    private LocalDate dateCreated;
    @Column(name = "doc_no")
    private String docNo;
    @Column(name = "amount")
    private Long amount;
    @Column(name = "message", length = 1023)
    private String message;
    @Column(name = "sender")
    private String sender;
    @OneToOne
    @JoinColumn(name = "file_id", referencedColumnName = "id")
    private File file;
    @Column(name = "page")
    private int page;
    @Column(length = 1023)
    private String search;
}
