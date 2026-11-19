"""Generated from Smithy shape ``com.amazonaws.workspaces#ComputeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.compute

ComputeList: TypeAlias = list["capo_workspaces.types.compute.Compute"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeList) -> list:
    import capo_workspaces.types.compute

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.compute.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ComputeList:
    import capo_workspaces.types.compute

    out: ComputeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.compute.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ComputeList) -> list:
    import capo_workspaces.types.compute

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.compute.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ComputeList:
    import capo_workspaces.types.compute

    out: ComputeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.compute.deserialize_cbor(item))
    return out
