"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#CapabilityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_microvms.types.capability

CapabilityList: TypeAlias = list["capo_lambda_microvms.types.capability.Capability"]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityList) -> list:
    import capo_lambda_microvms.types.capability

    out: list = []
    for item in value:
        out.append(capo_lambda_microvms.types.capability.serialize_json(item))
    return out


def deserialize_json(data: list) -> CapabilityList:
    import capo_lambda_microvms.types.capability

    out: CapabilityList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda_microvms.types.capability.deserialize_json(item))
    return out
