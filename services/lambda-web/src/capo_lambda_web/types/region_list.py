"""Generated from Smithy shape ``com.amazonaws.lambdaweb#RegionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_web.types.region

RegionList: TypeAlias = list["capo_lambda_web.types.region.Region"]


# --- restJson1 ser/de ---
def serialize_json(value: RegionList) -> list:
    return list(value)


def deserialize_json(data: list) -> RegionList:
    return [item for item in data if item is not None]
