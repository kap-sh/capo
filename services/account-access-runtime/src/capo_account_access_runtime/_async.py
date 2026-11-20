from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import trio
else:
    try:
        import trio
    except ImportError:
        trio = None


def in_trio_run() -> bool:
    if trio is None:
        return False
    return trio.lowlevel.in_trio_run()


async def anysleep(delay: float) -> None:
    if in_trio_run():
        await trio.sleep(delay)
    else:
        await asyncio.sleep(delay)
