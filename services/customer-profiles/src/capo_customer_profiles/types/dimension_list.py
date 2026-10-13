"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DimensionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.dimension

DimensionList: TypeAlias = list["capo_customer_profiles.types.dimension.Dimension"]


# --- restJson1 ser/de ---
def serialize_json(value: DimensionList) -> list:
    import capo_customer_profiles.types.dimension

    out: list = []
    for item in value:
        out.append(capo_customer_profiles.types.dimension.serialize_json(item))
    return out


def deserialize_json(data: list) -> DimensionList:
    import capo_customer_profiles.types.dimension

    out: DimensionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_customer_profiles.types.dimension.deserialize_json(item))
    return out


def redact_sensitive(value: DimensionList) -> list[Any]:
    import capo_customer_profiles.types.dimension

    return [
        capo_customer_profiles.types.dimension.redact_sensitive(item) for item in value
    ]
