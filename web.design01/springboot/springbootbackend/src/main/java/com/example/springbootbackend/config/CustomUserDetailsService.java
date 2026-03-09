package com.example.springbootbackend.config;


import com.example.springbootbackend.model.User;
import com.example.springbootbackend.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

@Service
public class CustomUserDetailsService implements UserDetailsService {

    @Autowired
    private UserRepository repo;


    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        User u=repo.findByUsername(username).orElseThrow(()->new UsernameNotFoundException("user not found"));

        return org.springframework.security.core.userdetails.User
                .withUsername(u.getUsername())
                .roles(u.getRole())
                .password(u.getPassword())
                .build();
    }
}
