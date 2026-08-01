import runpy; runpy.run_module('fix_path')  # noqa READ INSIDE WHAT THIS IS FOR

import sys

from src.db.session import get_session
from src.modules.auth.hashing import hasher
from src.modules.auth.models import Admin


class NotEnoughArguments(Exception): ...


def __name_pwd_from_args() -> tuple[str,str]:
    if not len(sys.argv) >= 3:
        raise NotEnoughArguments
    name = sys.argv[1]
    password = sys.argv[2]
    return (name, password)


def main():
    name, password = __name_pwd_from_args()
    password_hash = hasher.encrypt(password)
    with get_session() as session:
        new_admin = Admin(
            name=name,
            password_hash=password_hash.decode()
        )
        session.add(new_admin)
        session.commit()
    print(f"Added new admin: {name}")


if __name__ == '__main__':
    try:
        main()
    except NotEnoughArguments:
        print("Usage: add_admin.py <name> <password>")
        sys.exit(1)
