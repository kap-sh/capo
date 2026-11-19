"""Generated from Smithy shape ``com.amazonaws.gamelift#LinuxCapabilityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.linux_capability

LinuxCapabilityList: TypeAlias = list[
    "capo_gamelift.types.linux_capability.LinuxCapability"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LinuxCapabilityList) -> list:
    import capo_gamelift.types.linux_capability

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.linux_capability.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LinuxCapabilityList:
    import capo_gamelift.types.linux_capability

    out: LinuxCapabilityList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.linux_capability.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LinuxCapabilityList) -> list:
    import capo_gamelift.types.linux_capability

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.linux_capability.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> LinuxCapabilityList:
    import capo_gamelift.types.linux_capability

    out: LinuxCapabilityList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.linux_capability.deserialize_cbor(item))
    return out
