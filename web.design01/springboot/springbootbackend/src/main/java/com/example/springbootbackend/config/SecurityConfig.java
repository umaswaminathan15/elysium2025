package com.example.springbootbackend.config;


import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;

import java.io.IOException;

@Configuration
public class SecurityConfig {

    @Bean
    protected PasswordEncoder encoder(){
        return new BCryptPasswordEncoder();
    }

    @Bean
    protected SecurityFilterChain filterChain(HttpSecurity http) throws IOException {
        http
                .csrf(csrf->csrf.disable())
                .authorizeHttpRequests(auth->auth
                        .requestMatchers("/register").permitAll()
                        .requestMatchers("/user","/get","/get/**").hasAnyRole("USER","ADMIN")
                        .requestMatchers("/admin","/add","/update/**","/delete/**").hasRole("ADMIN")
                        .anyRequest().authenticated()

                )
                .formLogin(httpSecurityFormLoginConfigurer -> {})
                .httpBasic(httpSecurityHttpBasicConfigurer -> {});
        return http.build();
    }
}
