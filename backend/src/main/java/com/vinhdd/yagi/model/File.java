package com.vinhdd.yagi.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Entity
@Table(name = "files")
public class File {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private int id;
    @Column(name = "filename")
    private String filename;
    @Column(name = "account_no")
    private String accountNo;
    @Column(name = "account_name")
    private String accountName;
    @Column(name = "bank")
    private String bank;
}
