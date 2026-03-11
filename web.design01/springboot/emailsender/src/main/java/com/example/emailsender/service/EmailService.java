package com.example.emailsender.service;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.stereotype.Service;

@Service
public class EmailService {

    @Autowired
    private JavaMailSender mailsender;

    public void sendmail(String to, String subject, String message){

        SimpleMailMessage mail = new SimpleMailMessage();
        mail.setFrom("umaswaminathan15@gmail.com");
        mail.setTo(to);
        mail.setSubject(subject);
        mail.setText(message);
        mailsender.send(mail);
    }
}
