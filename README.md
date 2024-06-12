# Server 

## Python
```bash
python znchat/__init__.py
```
## Vite
```bash
cd app
bun run dev
```

# Celery worker

```bash
celery -A znchat.make_celery.celery_app worker -P eventlet
```
