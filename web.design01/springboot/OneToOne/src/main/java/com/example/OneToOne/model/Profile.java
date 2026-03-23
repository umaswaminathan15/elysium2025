package com.example.OneToOne.model;


import jakarta.persistence.*;

@Entity
@Table(name = "profiles")

public class Profile {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)

    private Long id;

    private String number;
    private String address;

    public Profile() {
    }

    public Profile(Long id, String number, String address) {
        this.id = id;
        this.number = number;
        this.address = address;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
}
