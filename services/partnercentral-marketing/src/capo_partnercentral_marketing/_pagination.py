"""Runtime helpers for generated paginated ``iter_*`` operation methods."""

from __future__ import annotations

from typing import Any


def resolve_path(obj: Any, path: tuple[str, ...]) -> Any:
    """Walk ``path`` segments on a nested ``dict`` (TypedDict at runtime).

    Returns ``None`` as soon as any intermediate value is missing or non-dict —
    the generated iter loop uses a falsy token as the terminate signal, so this
    short-circuit gives the same semantics for dotted paths as for top-level ones.
    """
    for key in path:
        if not isinstance(obj, dict):
            return None
        obj = obj.get(key)
        if obj is None:
            return None
    return obj
