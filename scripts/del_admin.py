import runpy; runpy.run_module('fix_path')  # noqa READ INSIDE WHAT THIS IS FOR

import sys

from src.db.session import get_session
from src.modules.auth.models import Admin


class NotEnoughArguments(Exception): ...


def __name_from_args() -> str:
    if not len(sys.argv) >= 2:
        raise NotEnoughArguments
    name = sys.argv[1]
    return name


def main():
    name = __name_from_args()
    with get_session() as session:
        deleted = session.query(Admin).filter_by(name=name).delete()
        session.commit()
    print(f"Deleted {deleted} rows")


if __name__ == '__main__':
    try:
        main()
    except NotEnoughArguments:
        print("Usage: del_admin.py <name>")
        sys.exit(1)
