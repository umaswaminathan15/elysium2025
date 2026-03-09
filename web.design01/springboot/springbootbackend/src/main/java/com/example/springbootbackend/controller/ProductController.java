package com.example.springbootbackend.controller;


import com.example.springbootbackend.model.Product;
import com.example.springbootbackend.service.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.util.List;

@RestController
public class ProductController {

    @Autowired
    private ProductService service;

    @PostMapping("/add")
    public Product addproduct(@RequestParam String name, @RequestParam String des, @RequestParam int qty, @RequestParam double price, @RequestParam MultipartFile file) throws IOException {
        return service.addproduct(name, qty, price, des, file);
    }

    @GetMapping("/get")
    public List<Product> getall(){
        return service.getall();
    }

    @GetMapping("/get/{id}")
    public Product getsingle(@PathVariable Long id){
        return service.getsingle(id);
    }

    @PutMapping("/update/{id}")
    public Product updateprod(@PathVariable Long id,@RequestParam String name, @RequestParam String des, @RequestParam int qty, @RequestParam double price, @RequestParam MultipartFile file) throws IOException{
        return service.updateproduct(id, name, qty, price, des, file);
    }

    @DeleteMapping("/delete/{id}")

    public String deleteprod(@PathVariable Long id){
        return service.deleteproduct(id);
    }
}


