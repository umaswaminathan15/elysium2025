package com.example.OneToOne.controller;


import com.example.OneToOne.model.User;
import com.example.OneToOne.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class UserController {

    @Autowired
    private UserService service;

    @PostMapping("/user")
    public User adduser(@RequestBody User user){
        return  service.adduser(user);
    }

    @GetMapping
    public List<User> getall(){
        return service.getall();
    }
}
