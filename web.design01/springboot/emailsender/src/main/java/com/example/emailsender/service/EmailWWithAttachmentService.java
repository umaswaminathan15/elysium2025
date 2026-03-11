package com.example.emailsender.service;


import jakarta.mail.internet.MimeMessage;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.mail.javamail.MimeMessageHelper;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

@Service
public class EmailWWithAttachmentService {

    @Autowired
    private JavaMailSender mailSender;

    public void sendEmail(String to, String subject, String message, MultipartFile file) throws Exception{

        MimeMessage message1=mailSender.createMimeMessage();
        MimeMessageHelper helper=new MimeMessageHelper(message1, true);

        helper.setFrom("umaswaminathan15@gmail.com");
        helper.setTo(to);
        helper.setSubject(subject);
        helper.setText(message);

        if(file!=null && !file.isEmpty()){
            helper.addAttachment(file.getOriginalFilename(), file);
        }
        mailSender.send(message1);
    }

}
