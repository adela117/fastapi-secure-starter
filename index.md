---
title: Secure API FastAPI CI
---

# Secure API FastAPI CI

A tiny FastAPI service with CI-enforced quality and security:

- Tests (pytest) on every push/PR
- Style gates (Black + Flake8)
- Container build + health-check in CI
- ZAP baseline DAST
- CycloneDX SBOM (Syft) + pip-audit
- Trivy image scan (HIGH/CRITICAL fail)
- Bandit static analysis
- Runtime hardening: API key, rate limit, security headers, Prometheus /metrics

**Repo:** https://github.com/adela117/secure-api-fastapi-ci  
**Docs:** /docs when running locally or in demo

> Contact: [LinkedIn](linkedin.com/in/albert-de-la-cruz-282-fiu/?skipRedirect=true) · [Email](delacruz.albert@proton.me)
