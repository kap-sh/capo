"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#RegionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_instances.types.region

RegionList: TypeAlias = list["capo_workspaces_instances.types.region.Region"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegionList) -> list:
    import capo_workspaces_instances.types.region

    out: list = []
    for item in value:
        out.append(capo_workspaces_instances.types.region.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> RegionList:
    import capo_workspaces_instances.types.region

    out: RegionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces_instances.types.region.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RegionList) -> list:
    import capo_workspaces_instances.types.region

    out: list = []
    for item in value:
        out.append(capo_workspaces_instances.types.region.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RegionList:
    import capo_workspaces_instances.types.region

    out: RegionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces_instances.types.region.deserialize_cbor(item))
    return out
