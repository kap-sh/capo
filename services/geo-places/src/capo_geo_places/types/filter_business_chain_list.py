"""Generated from Smithy shape ``com.amazonaws.geoplaces#FilterBusinessChainList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.sensitive_string

FilterBusinessChainList: TypeAlias = list[
    "capo_geo_places.types.sensitive_string.SensitiveString"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterBusinessChainList) -> list:
    return list(value)


def deserialize_json(data: list) -> FilterBusinessChainList:
    return [item for item in data if item is not None]


def redact_sensitive(value: FilterBusinessChainList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
