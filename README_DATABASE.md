## Database setup

ROKIBUL AI OS uses Flask-SQLAlchemy with Flask-Migrate.

- **Local development:** nothing to configure. SQLite is created at `instance/rokibul_ai_os.db`.
- **Production:** set `DATABASE_URL` (for example `postgresql://USER:PASSWORD@HOST:5432/DBNAME`)
  in your environment or secrets manager and install `psycopg2-binary`. Never commit credentials.

```bash
pip install -r requirements.txt
export FLASK_APP=run.py          # adjust if your app entry point differs
flask db init                    # once, creates migrations/
flask db migrate -m "initial schema"
flask db upgrade
```

Quick local alternative (no migrations): `flask init-db`.

Check connectivity at `GET /health/db` (200 when connected, 503 otherwise, with no details exposed).
The existing `GET /health` endpoint is unchanged.

Tests: `pytest tests/test_database.py -v`

Security notes: passwords are stored only as salted hashes, APIs should expose `public_id` rather than
the numeric `id`, and `User.to_dict()` never includes the hash. Keep `.env` out of git.
