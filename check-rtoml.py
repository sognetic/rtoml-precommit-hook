from __future__ import annotations

import argparse
from typing import Sequence

import rtoml


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        try:
            rtoml.load(filename)
        except (rtoml.TOMLParsingError, rtoml.TOMLSerializationError) as exc:
            print(f'{filename}: {exc}')
            retval = 1
    return retval


if __name__ == '__main__':
    raise SystemExit(main())
