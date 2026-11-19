"""Generated from Smithy shape ``com.amazonaws.lambdacore#PlatformList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_core.types.platform

PlatformList: TypeAlias = list["capo_lambda_core.types.platform.Platform"]


# --- restJson1 ser/de ---
def serialize_json(value: PlatformList) -> list:
    import capo_lambda_core.types.platform

    out: list = []
    for item in value:
        out.append(capo_lambda_core.types.platform.serialize_json(item))
    return out


def deserialize_json(data: list) -> PlatformList:
    import capo_lambda_core.types.platform

    out: PlatformList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda_core.types.platform.deserialize_json(item))
    return out
