package com.example.studentServlet;

import java.sql.Connection;
import java.sql.DriverManager;

public class DBConnection {
    public static Connection getConnection() {
        try {
            String url="jdbc:mysql://localhost:3306/schooldb";
            String username="root";
            String password="";
            return DriverManager.getConnection(url,username,password);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}




