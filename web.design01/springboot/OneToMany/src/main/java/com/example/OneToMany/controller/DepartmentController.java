package com.example.OneToMany.controller;

import com.example.OneToMany.model.Department;
import com.example.OneToMany.service.DepartmentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("api/department")
public class DepartmentController {

    @Autowired
    private DepartmentService service;

    @PostMapping
    public Department adddept(@RequestBody Department department){
        return service.adddept(department);
    }

    @GetMapping
    public List<Department> getall(){
        return service.getall();
    }
}

