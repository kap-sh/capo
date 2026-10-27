"""Generated from Smithy shape ``com.amazonaws.lightsail#WafStatusCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.integer

WafStatusCodeList: TypeAlias = list["capo_lightsail.types.integer.integer"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WafStatusCodeList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> WafStatusCodeList:
    return [item for item in data if item is not None]
