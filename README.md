# dj-mem-care

A small reusable Django app for dementia memory care.

A **confabulation** is something a person with dementia says that reflects a distorted or
invented memory ("I have to pick the kids up from school"). They aren't lying; the brain is
filling gaps. This app stores common confabulations so caregivers can later keep a list of
calm, kind responses to each one.

## v0.1.0

- `Confabulation` model: `text` (unique), `created_at`, `updated_at`. Shared by all users.
- Registered in Django admin (searchable).
- Starter set of 20 confabulations in `dj_mem_care/data/confabulations.json`.
- Management command `load_confabulations` (safe to re-run; existing texts are skipped).

## Install (uv, from GitHub, pinned by tag)

    uv add "git+https://github.com/brucestull/dj-mem-care.git@v0.1.0"

Add `"dj_mem_care"` to `INSTALLED_APPS`, then:

    uv run python manage.py migrate
    uv run python manage.py load_confabulations

Load your own list instead: `load_confabulations --file path/to/list.json`
(a JSON list of `{"text": "..."}` objects).

## Roadmap

- Responses: a list of suggested responses per confabulation.
- Optional per-user links (personal lists).

## License

MIT
