package com.example.springbootbackend.service;


import com.example.springbootbackend.model.Product;
import com.example.springbootbackend.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

@Service
public class ProductService {

    @Autowired
    private ProductRepository repo;

    @Value("${upload.path}")
    private String uploadpath;

    public Product addproduct(String name, int qty,  double price, String des, MultipartFile file) throws IOException{

        try {
            Product p = new Product();
            p.setName(name);
            p.setDes(des);
            p.setQty(qty);
            p.setPrice(price);

            String filename= file.getOriginalFilename();
            String uploadDir = System.getProperty("user.dir")+ File.separator+uploadpath;

            Files.createDirectories(Paths.get(uploadDir));
            String filepath=uploadDir+File.separator+filename;
            File f=new File(filepath);
            file.transferTo(f);
            p.setImage(filename);

            return repo.save(p);

        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public List<Product> getall(){
        return repo.findAll();
    }
    public  Product getsingle(Long id){
        return repo.findById(id).orElseThrow();
    }
    public Product updateproduct(Long id, String name, int qty,  double price, String des, MultipartFile file) throws IOException{
        Product p = getsingle(id);

        try{
            p.setName(name);
            p.setPrice(price);
            p.setQty(qty);
            p.setDes(des);

            String filename=file.getOriginalFilename();
            String uploadDir=System.getProperty("user.dir")+ File.separator+uploadpath;
            String filepath=uploadDir+File.separator+filename;

            File f=new File(filepath);
            file.transferTo(f);
            p.setImage(filename);
            return  repo.save(p);

        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public String deleteproduct(Long id){
        repo.findById(id);
        return  "product deleted success";
    }
}
