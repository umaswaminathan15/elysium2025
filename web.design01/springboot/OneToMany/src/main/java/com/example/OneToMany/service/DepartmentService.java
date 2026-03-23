package com.example.OneToMany.service;


import com.example.OneToMany.model.Department;
import com.example.OneToMany.repository.DepartmentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class DepartmentService {

    @Autowired
    private DepartmentRepository repo;

    public Department adddept(Department department){
        if (department.getEmployees() != null){
            department.getEmployees().forEach(emp->{
                emp.setDepartment(department);
            });
        }

        return  repo.save(department);
    }

    public List<Department> getall(){
        return repo.findAll();
    }
}
