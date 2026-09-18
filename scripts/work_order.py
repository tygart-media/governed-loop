#!/usr/bin/env python3
"""Render a governed-loop work order with a deterministic idempotency key.

Usage:
    python3 work_order.py --seat builder --slug "q3-pricing-page" \
        --intent "Rebuild the pricing page from the approved copy deck." \
        --guardrails "no publish, no send" --out work-orders/

The key is <YYYYMMDD>-<slug>: same work, same key, send exactly once.
"""
import argparse
import re
from datetime import date
from pathlib import Path

TEMPLATE = """\
WORK ORDER {key}
To: {seat}
Subject: {seat} {key} {short}

INTENT
  {intent}

GUARDRAILS
  {guardrails}

INPUTS
  {inputs}

DONE CRITERIA
  {done}

REPORT BACK
  What changed, files touched, what needs the verifier's eyes,
  anything uncertain.
"""


def slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60] or "work"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seat", required=True)
    ap.add_argument("--slug", required=True)
    ap.add_argument("--intent", required=True)
    ap.add_argument("--guardrails", default="no send, no publish, no spend, no credentials, no deletions")
    ap.add_argument("--inputs", default="(list links, files, threads the builder should read first)")
    ap.add_argument("--done", default="(checkable done criteria, one per line)")
    ap.add_argument("--date", default=date.today().isoformat())
    ap.add_argument("--out", default="work-orders")
    args = ap.parse_args()

    key = f"{args.date.replace('-', '')}-{slugify(args.slug)}"
    short = " ".join(args.intent.split()[:8])
    body = TEMPLATE.format(
        key=key, seat=args.seat, short=short, intent=args.intent,
        guardrails=args.guardrails, inputs=args.inputs, done=args.done,
    )
    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)
    path = outdir / f"{key}.md"
    if path.exists():
        print(f"exists (send-once): {path} — not overwritten")
        return
    path.write_text(body)
    print(f"wrote {path}  key={key}")


if __name__ == "__main__":
    main()
