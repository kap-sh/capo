"""Generated from Smithy shape ``com.amazonaws.workspaces#StopWorkspaceRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.stop_request

StopWorkspaceRequests: TypeAlias = list[
    "capo_workspaces.types.stop_request.StopRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopWorkspaceRequests) -> list:
    import capo_workspaces.types.stop_request

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.stop_request.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StopWorkspaceRequests:
    import capo_workspaces.types.stop_request

    out: StopWorkspaceRequests = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.stop_request.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StopWorkspaceRequests) -> list:
    import capo_workspaces.types.stop_request

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.stop_request.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> StopWorkspaceRequests:
    import capo_workspaces.types.stop_request

    out: StopWorkspaceRequests = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.stop_request.deserialize_cbor(item))
    return out
