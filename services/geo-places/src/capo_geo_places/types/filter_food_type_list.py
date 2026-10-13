"""Generated from Smithy shape ``com.amazonaws.geoplaces#FilterFoodTypeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.sensitive_string

FilterFoodTypeList: TypeAlias = list[
    "capo_geo_places.types.sensitive_string.SensitiveString"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterFoodTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> FilterFoodTypeList:
    return [item for item in data if item is not None]


def redact_sensitive(value: FilterFoodTypeList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
