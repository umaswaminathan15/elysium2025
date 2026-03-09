package com.example.springbootbackend.service;


import com.example.springbootbackend.model.User;
import com.example.springbootbackend.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
public class UserService {

    @Autowired
    private PasswordEncoder encoder;

    @Autowired
    private UserRepository repo;

    public User register(User user){
        User u = new User();

        u.setUsername(user.getUsername());
        u.setRole(user.getRole());
        u.setPassword(encoder.encode(user.getPassword()));
        return repo.save(u);

    }
}
