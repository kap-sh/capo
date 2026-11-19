"""Generated from Smithy shape ``com.amazonaws.workspaces#RebuildWorkspaceRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.rebuild_request

RebuildWorkspaceRequests: TypeAlias = list[
    "capo_workspaces.types.rebuild_request.RebuildRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RebuildWorkspaceRequests) -> list:
    import capo_workspaces.types.rebuild_request

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.rebuild_request.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RebuildWorkspaceRequests:
    import capo_workspaces.types.rebuild_request

    out: RebuildWorkspaceRequests = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.rebuild_request.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RebuildWorkspaceRequests) -> list:
    import capo_workspaces.types.rebuild_request

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.rebuild_request.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RebuildWorkspaceRequests:
    import capo_workspaces.types.rebuild_request

    out: RebuildWorkspaceRequests = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.rebuild_request.deserialize_cbor(item))
    return out
