package com.example.service;

import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

@Service
public class VendorService {

    private final AiServiceClient aiServiceClient;

    public VendorService(AiServiceClient aiServiceClient) {
        this.aiServiceClient = aiServiceClient;
    }

    public void createVendor(String vendorDetails) {

        // 1. Save basic data (simulate)
        System.out.println("Vendor saved: " + vendorDetails);

        // 2. Call AI in background
        generateRecommendationsAsync(vendorDetails);
    }


}

  @Async
public void generateRecommendationsAsync(String vendorDetails) {
    if (vendorDetails == null || vendorDetails.isBlank()) {
        System.out.println("Skipping AI call - vendorDetails is empty");
        return;
    }
    String result = aiServiceClient.callRecommendAPI(vendorDetails);

        // 3. Handle null safely
        if (result != null) {
            System.out.println("AI Recommendations: " + result);

            // Here you would save to DB
            // example: vendor.setRecommendations(result);

        } else {
            System.out.println("AI result is null, skipping update");
        }
    }
}