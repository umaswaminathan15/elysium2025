package com.example.servlet.controller;

import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@WebServlet("/demo")
public class DemoServlet extends HttpServlet {

    public void init() {
        System.out.println("Servlet Initialized");
    }

    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response) {
        System.out.println("Request handled");
    }

    public void destroy() {
        System.out.println("Servlet Destroyed");
    }
}

