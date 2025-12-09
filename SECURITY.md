# 🔐 Security Guide - IA PME Startup

**Last Updated**: December 9, 2025  
**Status**: Phase 0 (MVP) - Groq free tier with local protections

---

## 🛡️ Current Security Posture

### What's Protected Now (Phase 0)

✅ **Secrets Management**
- `.env` is in `.gitignore` (never committed to GitHub)
- `.env.example` provided for developers (no sensitive values)
- All API keys are environment variables (not hardcoded)

✅ **Concurrency Control**
- Semaphore limiting concurrent Groq requests (default: 4 per process)
- Prevents burst attacks / rate limit exhaustion
- Graceful rejection if limit hit (returns fallback)

✅ **Error Handling**
- All LLM calls have timeouts (30 seconds)
- Fallback heuristics if API unavailable (French language maintained)
- Logging of errors for monitoring

✅ **Code Quality**
- All tests passing (26/26)
- Edge cases handled (empty input, invalid data, etc)
- SQL injection prevention (using pydantic models, no raw SQL)

✅ **Demo Infrastructure**
- `demos.html` is 100% client-side (no backend, no data sent to server)
- No tracking cookies or analytics (privacy-first)
- Safe for prospects to test without concerns

---

## 🚨 Known Limitations (MVP)

⚠️ **Authentication**: None (future: JWT/OAuth2)
- Currently: No user login needed
- Action: Add before handling real customer data

⚠️ **Rate Limiting**: Per-process only (local semaphore)
- Currently: No HTTP-level rate limiting
- Action: Add `flask-limiter` or reverse-proxy rules before production

⚠️ **Data Storage**: No encryption at rest
- Currently: SQLite local files (plaintext)
- Action: Add encryption (e.g., `sqlcipher`) before storing PII

⚠️ **HTTPS**: Not yet deployed
- Currently: Works over HTTP locally
- Action: Enforce HTTPS + TLS in production (Railway auto-enables this)

⚠️ **API Keys**: Visible in environment variables
- Currently: No rotation policy
- Action: Implement key rotation + audit logging after first customers

---

## 📋 Deployment Security Checklist (Before Going Live)

### Immediate (Before Phase 1 - Free Tier Launch)

- [ ] **Environment Variables Setup**
  ```bash
  # Railway Dashboard → Settings → Environment
  GROQ_API_KEY=gsk_...     # Add via dashboard (never in code)
  LLM_PROVIDER=groq
  GROQ_MAX_CONCURRENT=4
  JWT_SECRET_KEY=<random-64-char-secret>
  ```

- [ ] **HTTPS Enforcement**
  - [ ] Railway auto-enables HTTPS (default: ✅ enabled)
  - [ ] Verify: `https://app.ia-pme.fr` works
  - [ ] Set `SECURE_COOKIES=true` in config

- [ ] **Secrets Scanning**
  ```bash
  # Before each push, check no secrets leaked:
  git log -p --all -S 'gsk_' | grep 'gsk_'
  # Should return nothing if history is clean
  ```

- [ ] **Dependency Audit**
  ```bash
  pip audit  # Check for vulnerable dependencies
  pytest --cov=src  # Run tests with coverage
  ```

### Phase 1 (With First Customers)

- [ ] **Rate Limiting** (add after 50+ demos)
  ```python
  # In app.py, add:
  from flask_limiter import Limiter
  limiter = Limiter(app, key_func=lambda: request.remote_addr)
  @app.route('/api/classify', methods=['POST'])
  @limiter.limit("10/minute")  # 10 requests per minute per IP
  def classify_email():
      ...
  ```

- [ ] **Authentication** (required for paid tier)
  ```python
  # Simple email-based auth:
  from flask_jwt_extended import JWTManager, create_access_token
  # Users login → get JWT token → use for API calls
  ```

- [ ] **Audit Logging**
  ```python
  # Log all important events (for compliance):
  audit_logger.info(f"User {user_id} classified {count} emails")
  audit_logger.warning(f"API key rotated for {org_id}")
  ```

- [ ] **Data Retention Policy**
  ```
  - Email contents: Delete after 30 days (GDPR)
  - PDF cache: Delete after 7 days
  - User logs: Aggregate after 90 days
  - Document retention per user preference
  ```

### Phase 2+ (Before Series Seed)

- [ ] **OWASP Top 10 Review**
  - [ ] SQL Injection (use ORM/parameterized queries) ✅ Done
  - [ ] XSS (sanitize user input)
  - [ ] CSRF (add CSRF tokens)
  - [ ] Insecure auth (use OAuth2/OIDC)
  - [ ] Sensitive data exposure (encrypt PII)
  - [ ] Broken access control (role-based permissions)
  - [ ] Security misconfiguration (harden server)
  - [ ] Using components with known vulns (regular audits)
  - [ ] Insufficient logging (audit trail)
  - [ ] Using outdated / unpatched software

- [ ] **Third-party Audit**
  - Security audit by external firm (€2-5K)
  - Penetration testing (€5-10K)
  - SOC 2 Type I compliance (€10-20K)

- [ ] **Incident Response Plan**
  ```
  1. If API key leaked: Immediately rotate in Groq console
  2. If customer data exposed: Notify within 72 hours
  3. If service down: Auto-failover to Mistral or local LLM
  4. If DDoS: Activate rate limiting + geo-blocking
  ```

---

## 🔑 API Key Management (Groq)

### Current Status
- **Key**: Created in Groq console (`gsk_...`)
- **Storage**: Locally in `.env` (ignored by git)
- **Rotation**: Manual (no auto-rotation yet)
- **Scope**: Read-only API calls (not delete/update)

### Groq API Limits (Free Tier)
- **Requests**: ~10 requests per minute (burst-friendly)
- **Tokens/month**: Unlimited for free tier (as of Dec 2025)
- **Cost after upgrade**: €0.10 per 1M input tokens

### If Key is Compromised
1. Go to https://console.groq.com → API Keys
2. Delete compromised key
3. Create new key
4. Update `.env` locally (don't commit)
5. Update Railway environment variables
6. Redeploy

---

## 🛠️ Local Development Security

### Setup for New Developer
```bash
# 1. Clone repo
git clone https://github.com/rudy-willoquet/ia-pme.git
cd ia-pme

# 2. Copy template
cp .env.example .env

# 3. Add YOUR OWN Groq key (never share)
# Edit .env, add: GROQ_API_KEY=gsk_your_key_here

# 4. Activate venv
.\.venv\Scripts\Activate.ps1

# 5. Run tests (offline, no API calls needed for basic tests)
pytest tests/ -v

# 6. Run with Groq (requires API key)
python ops/demo_runner.py
```

### Never Do This ❌
- **Don't commit `.env`** (git will refuse, it's in `.gitignore`)
- **Don't share API keys** in Slack, email, or GitHub issues
- **Don't hardcode secrets** in code
- **Don't log API keys** (check logs before sharing)
- **Don't use same key** for dev + production (rotate separately)

### Check Before Push
```bash
# Make sure no secrets in code:
git diff HEAD
# Look for: API keys, passwords, tokens, emails

# Make sure .env not staged:
git status
# Should NOT show ".env"
```

---

## 📊 Monitoring & Alerting (Future)

### What to Monitor (Post-MVP)
- API error rate (target: <1%)
- Groq API latency (target: <500ms p95)
- Concurrent requests (should stay under 4 per process)
- Failed auth attempts (for DDoS detection)
- Data volume processed (for quota tracking)

### Tools Recommended (Phase 2)
- **Errors**: Sentry.io (free tier available)
- **Logs**: Papertrail or Datadog (€50+/month)
- **Metrics**: Prometheus + Grafana (self-hosted, free)
- **Uptime**: UptimeRobot (free)

---

## 🚀 Security Roadmap

| Phase | Timeline | Focus | Investment |
|-------|----------|-------|-----------|
| **0** (NOW) | Dec 2025 | Secrets, basic concurrency | €0 (free tier) |
| **1** | Jan-Feb 2026 | Rate limiting, auth, HTTPS | €0 (Railway free) |
| **2** | Mar-Apr 2026 | Encryption, audit logging | €100-500 |
| **3** | May+ 2026 | SOC 2, security audit | €10-50K |

---

## 💬 Questions?

If you have security concerns:
1. Create a GitHub issue (private if sensitive)
2. Email: rudy@ia-pme.fr
3. Consult OWASP Top 10 guide: https://owasp.org/Top10/

**Remember**: Security is a journey, not a destination. Start with the essentials (this checklist), iterate, and improve as you grow.

---

**Last Review**: December 9, 2025  
**Next Review**: After first 10 customers or January 1, 2026 (whichever comes first)
