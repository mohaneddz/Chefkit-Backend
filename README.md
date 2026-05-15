<h1 style="font-family: Arial, sans-serif; font-size: 36px; color: #5BA5E8; border-bottom: 3px solid #5BA5E8; padding-bottom: 8px;">
  Chefkit Backend - API and Data Services
</h1>

Chefkit Backend powers the server-side services for the Chefkit ecosystem.
It is a Python backend focused on API, data processing, and service integrations.

---

## Stack

- Python
- FastAPI-style service workflows (project scripts + service entrypoint)
- Structured docs and data assets under `docs/` and `data/`

---

## Repository Structure

```text
main.py                # Main backend entrypoint
utils.py               # Utility helpers
requirements.txt       # Python dependencies
data/                  # Dataset and runtime data
files
scripts
```

---

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

---

## Environment

- Configure local environment variables in `.env` when needed.
- Keep sensitive keys (`serviceAccountKey.json`, etc.) out of public exposure.

---

## Notes

- This backend pairs with `Chefkit-Online` for web-facing UX.
- Review `plan.md` and `docs/` for architecture and feature context.
