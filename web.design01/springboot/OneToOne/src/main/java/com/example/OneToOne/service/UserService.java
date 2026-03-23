package com.example.OneToOne.service;


import com.example.OneToOne.model.User;
import com.example.OneToOne.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserService {

    @Autowired
    public UserRepository repo;

    public User adduser(User user){
        return repo.save(user);
    }

    public List<User> getall(){
        return repo.findAll();
    }


}
