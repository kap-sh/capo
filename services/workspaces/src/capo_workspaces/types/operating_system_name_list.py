"""Generated from Smithy shape ``com.amazonaws.workspaces#OperatingSystemNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.operating_system_name

OperatingSystemNameList: TypeAlias = list[
    "capo_workspaces.types.operating_system_name.OperatingSystemName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperatingSystemNameList) -> list:
    import capo_workspaces.types.operating_system_name

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.operating_system_name.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OperatingSystemNameList:
    import capo_workspaces.types.operating_system_name

    out: OperatingSystemNameList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.operating_system_name.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OperatingSystemNameList) -> list:
    import capo_workspaces.types.operating_system_name

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.operating_system_name.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> OperatingSystemNameList:
    import capo_workspaces.types.operating_system_name

    out: OperatingSystemNameList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.operating_system_name.deserialize_cbor(item))
    return out
