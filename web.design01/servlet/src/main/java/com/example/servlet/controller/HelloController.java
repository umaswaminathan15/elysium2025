package com.example.servlet.controller;


import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;


import java.io.PrintWriter;

@WebServlet
public class HelloController extends HttpServlet {

        protected void doGet(HttpServletRequest request,
                             HttpServletResponse response)
                throws ServletException, IOException {

            response.setContentType("text/html");
            PrintWriter out = response.getWriter();
            out.println("<h1>Hello from Servlet</h1>");
        }
}


