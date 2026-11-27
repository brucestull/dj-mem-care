import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from dj_mem_care.models import Confabulation

DEFAULT_FILE = Path(__file__).resolve().parents[2] / "data" / "confabulations.json"


class Command(BaseCommand):
    help = (
        "Load Confabulations from a JSON file (a list of {\"text\": ...} objects). "
        "Safe to run repeatedly: existing texts are skipped."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            default=str(DEFAULT_FILE),
            help="Path to a JSON file. Defaults to the starter set shipped with dj-mem-care.",
        )

    def handle(self, *args, **options):
        path = Path(options["file"])
        if not path.is_file():
            raise CommandError(f"File not found: {path}")

        try:
            items = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise CommandError(f"Invalid JSON in {path}: {exc}") from exc

        if not isinstance(items, list):
            raise CommandError("JSON must be a list of objects with a 'text' key.")

        created = skipped = 0
        for item in items:
            text = (item.get("text") or "").strip() if isinstance(item, dict) else ""
            if not text:
                raise CommandError(f"Every item needs a non-empty 'text': {item!r}")
            _, was_created = Confabulation.objects.get_or_create(text=text)
            if was_created:
                created += 1
            else:
                skipped += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Confabulations: {created} created, {skipped} already existed "
                f"(total now {Confabulation.objects.count()})."
            )
        )
