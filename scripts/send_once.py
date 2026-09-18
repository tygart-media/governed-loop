#!/usr/bin/env python3
"""Send-once ledger: idempotency for proactive sends.

Every send is keyed on the work-order key. Before sending, check the
key; after sending, record it. An approval timeout is never proof a
send failed — check the ledger before even considering a retry.

Usage:
    python3 send_once.py check 20260918-q3-pricing-page
    python3 send_once.py record 20260918-q3-pricing-page --note "sent to list"

The ledger lives at .send-once-ledger.json next to this script (gitignored).
"""
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

LEDGER = Path(__file__).resolve().parent / ".send-once-ledger.json"


def load() -> dict:
    if LEDGER.exists():
        return json.loads(LEDGER.read_text())
    return {}


def save(data: dict) -> None:
    LEDGER.write_text(json.dumps(data, indent=2))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("action", choices=["check", "record", "list"])
    ap.add_argument("key", nargs="?")
    ap.add_argument("--note", default="")
    args = ap.parse_args()

    data = load()
    if args.action == "list":
        for k, v in sorted(data.items()):
            print(f"{k}  {v.get('at', '')}  {v.get('note', '')}")
        return
    if not args.key:
        sys.exit("key required for check/record")

    if args.action == "check":
        hit = data.get(args.key)
        if hit:
            print(f"ALREADY SENT: {args.key} at {hit.get('at')} — do not resend")
            sys.exit(2)
        print(f"CLEAR: {args.key} not in ledger")
    elif args.action == "record":
        data[args.key] = {
            "at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "note": args.note,
        }
        save(data)
        print(f"recorded {args.key}")


if __name__ == "__main__":
    main()
