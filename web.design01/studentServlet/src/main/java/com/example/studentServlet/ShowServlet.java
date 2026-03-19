package com.example.studentServlet;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;

import static java.lang.System.out;

@WebServlet("/show")
public class ShowServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response)
            throws ServletException, IOException {
        try {
            Connection con = DBConnection.getConnection();
            String selectquery = "select * from student_detail";
            Statement stmt = con.createStatement();
            stmt.executeQuery(selectquery);
            ResultSet rs = stmt.getResultSet();
            response.setContentType("text/html");
            PrintWriter out = response.getWriter();
            out.println("<h1>student list</h1>");
            out.println("<table border='1'>");
            out.println("<tr><th>Name</th><th>email</th><th>course</th></tr>");
            while (rs.next()) {
                out.println("<tr>");
                out.println("<td>" + rs.getString("name") + "</td>");
                out.println("<td>" + rs.getString("email") + "</td>");
                out.println("<td>" + rs.getString("course") + "</td>");
            }
            out.println("</table>");
        }catch (Exception e) {
            e.printStackTrace();
        }

    }
}
