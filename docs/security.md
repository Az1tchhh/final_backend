# Security Measures for Authentication Endpoints

## Overview
This document outlines the security measures implemented for `/api/auth/login/` and `/api/auth/register/` endpoints.

### Security Highlights
1. **Transport Layer Security:** All requests are served over HTTPS.
2. **Rate Limiting:** Prevent brute-force attacks on login and registration endpoints.
3. **Token Security:** JWT tokens include minimal information to avoid sensitive data exposure.
4. **CSRF Protection:** Django's CSRF middleware protects against Cross-Site Request Forgery.

### Middleware
The `SecurityMiddleware` enforces:
- HTTPS for all API requests.
- Basic rate limiting.

### Login Endpoint
- Validates user credentials and logs successful login attempts.
- Securely generates JWT tokens with limited payload information.

### Registration Endpoint
- Validates input data to prevent duplicate accounts.
- Ensures secure password hashing before storage.

### Logging
- Suspicious activities are logged for further analysis.
- Failed login attempts trigger alerts to the admin.

## Usage
To test security:
1. Send valid/invalid login and registration requests.
2. Monitor logs for any unauthorized access attempts.
3. Ensure tokens are securely transmitted and stored.