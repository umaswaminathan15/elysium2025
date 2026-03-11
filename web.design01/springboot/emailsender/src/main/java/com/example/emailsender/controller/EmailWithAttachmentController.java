package com.example.emailsender.controller;

import com.example.emailsender.service.EmailWWithAttachmentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
@RestController
public class EmailWithAttachmentController {

    @Autowired
    private EmailWWithAttachmentService Service;


    @PostMapping("/attach")
    public String sendEmail(@RequestParam String to, @RequestParam String subject, @RequestParam String message, @RequestParam MultipartFile file) throws IOException {
        try{
            Service.sendEmail(to, subject, message, file);
            return "Email send success with attachement!";
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
