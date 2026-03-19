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

@WebServlet("/student")
public class StudentServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request,
        HttpServletResponse response)
        throws ServletException, IOException{
        response.setContentType("text/HTML");
        PrintWriter out = response.getWriter();
        out.println("<html><body>");
        out.println("<h2>Student Registration</h2>");
        out.println("<form method='post' action='student'>");
        out.println("Name: <input type='text' name='name'><br><br>");
        out.println("Email: <input type='email' name='email'><br><br>");
        out.println("Course: <input type='text' name='course'><br><br>");
        out.println("<input type='submit' value='Register'>");
        out.println("</form>");
        out.println("</body></html>");
    }
    protected void doPost(HttpServletRequest request,
                          HttpServletResponse response)
            throws IOException,ServletException {

        String name = request.getParameter("name");
        String email = request.getParameter("email");
        String course = request.getParameter("course");

        try {
            Connection con = DBConnection.getConnection();

            String sql = "insert into student_detail(name,email,course) values(?,?,?)";
            PreparedStatement ps = con.prepareStatement(sql);
            ps.setString(1, name);
            ps.setString(2, email);
            ps.setString(3, course);

            ps.executeUpdate();

            response.setContentType("text/html");
            PrintWriter out = response.getWriter();

            out.println("<html><body>");
            out.println("<h3>Student Registered Successfully!</h3>");
            out.println("<a href='student'>Register Another student</a>");
            out.println("<a href='show'>View</a>");
            out.println("</body></html>");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}





