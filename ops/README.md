Ops utilities: demo runner and health services

Files:
- `demo_runner.py`: runs quick, safe checks for all three apps without calling external LLMs. Use it to validate a demo environment is OK before showing a client.
- `health_services/`: three small Flask apps exposing `/health` and `/ready` for each app:
  - `email_health.py` -> port 8001
  - `pdf_health.py` -> port 8002
  - `excel_health.py` -> port 8003

Run demo runner (after installing dependencies):

```powershell
Set-Location 'd:\DevPortable\Projects'
.venv\Scripts\Activate.ps1
python ops/demo_runner.py
```

Run a health service (example):

```powershell
Set-Location 'd:\DevPortable\Projects'
python ops/health_services/email_health.py
# then visit http://localhost:8001/health and /ready
```

Notes:
- Health endpoints are intentionally lightweight and avoid calling external LLM providers to remain fast and reliable during demos.
- Ensure `requirements-dev.txt` is installed.
