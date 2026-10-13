"""Generated from Smithy shape ``com.amazonaws.location#RefererPatternList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.referer_pattern

RefererPatternList: TypeAlias = list[
    "capo_location.types.referer_pattern.RefererPattern"
]


# --- restJson1 ser/de ---
def serialize_json(value: RefererPatternList) -> list:
    return list(value)


def deserialize_json(data: list) -> RefererPatternList:
    return [item for item in data if item is not None]


def redact_sensitive(value: RefererPatternList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
