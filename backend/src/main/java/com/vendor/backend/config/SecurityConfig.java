package com.vendor.backend.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.boot.web.servlet.FilterRegistrationBean;
import org.springframework.web.filter.OncePerRequestFilter;

import jakarta.servlet.*;
import jakarta.servlet.http.*;
import java.io.IOException;

@Configuration
public class SecurityConfig {

    @Bean
    public FilterRegistrationBean<OncePerRequestFilter> securityHeadersFilter() {

        FilterRegistrationBean<OncePerRequestFilter> registration = new FilterRegistrationBean<>();

        registration.setFilter(new OncePerRequestFilter() {
            @Override
            protected void doFilterInternal(HttpServletRequest request,
                                            HttpServletResponse response,
                                            FilterChain filterChain)
                    throws ServletException, IOException {

                response.setHeader("X-Content-Type-Options", "nosniff");
                response.setHeader("X-Frame-Options", "DENY");
                response.setHeader("X-XSS-Protection", "1; mode=block");

                filterChain.doFilter(request, response);
            }
        });

        registration.addUrlPatterns("/*"); // apply to all endpoints
        registration.setOrder(1);

        return registration;
    }
}