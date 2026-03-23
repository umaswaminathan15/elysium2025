package com.example.OneToMany.model;


import com.fasterxml.jackson.annotation.JsonManagedReference;
import jakarta.persistence.*;

import java.util.ArrayList;
import java.util.List;

@Entity
public class Department {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String deptname;

    @OneToMany(mappedBy = "department",cascade = CascadeType.ALL)
    @JsonManagedReference
    private List<Employee> employees = new ArrayList<>();

    public Department() {
    }

    public Department(Long id, String deptname, List<Employee> employees) {
        this.id = id;
        this.deptname = deptname;
        this.employees = employees;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getDeptname() {
        return deptname;
    }

    public void setDeptname(String deptname) {
        this.deptname = deptname;
    }

    public List<Employee> getEmployees() {
        return employees;
    }

    public void setEmployees(List<Employee> employees) {
        this.employees = employees;
    }
}
