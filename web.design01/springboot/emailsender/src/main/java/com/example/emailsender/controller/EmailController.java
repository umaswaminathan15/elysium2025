package com.example.emailsender.controller;


import com.example.emailsender.service.EmailService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class EmailController {

    @Autowired
    private EmailService service;

    @PostMapping("/send")
    public String sendmail(@RequestParam String to, @RequestParam String subject, @RequestParam String message){

        service.sendmail(to, subject, message);
        return "mail send success";
    }
}
