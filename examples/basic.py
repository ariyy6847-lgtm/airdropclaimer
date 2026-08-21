"""Minimal example for AirdropClaimer."""

from airdropclaimer import airdropclaimer


def main():
 runner = airdropclaimer({"name": "AirdropClaimer", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()