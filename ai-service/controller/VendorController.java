package com.example.controller;

import com.example.service.VendorService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/vendor")
public class VendorController {

    private final VendorService vendorService;

    public VendorController(VendorService vendorService) {
        this.vendorService = vendorService;
    }

    @PostMapping("/create")
    public String create(@RequestBody String input) {

        vendorService.createVendor(input);

        return "Vendor created, AI processing in background";
    }
}