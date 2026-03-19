package com.example.jspdemo;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

    @GetMapping
    public String demo(Model model){
        model.addAttribute("name","admin");
        model.addAttribute("course","full stack development");
        return "home";
    }
}
