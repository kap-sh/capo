"""Generated from Smithy shape ``com.amazonaws.workspaces#StartWorkspaceRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.start_request

StartWorkspaceRequests: TypeAlias = list[
    "capo_workspaces.types.start_request.StartRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartWorkspaceRequests) -> list:
    import capo_workspaces.types.start_request

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.start_request.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StartWorkspaceRequests:
    import capo_workspaces.types.start_request

    out: StartWorkspaceRequests = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.start_request.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartWorkspaceRequests) -> list:
    import capo_workspaces.types.start_request

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.start_request.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> StartWorkspaceRequests:
    import capo_workspaces.types.start_request

    out: StartWorkspaceRequests = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.start_request.deserialize_cbor(item))
    return out
