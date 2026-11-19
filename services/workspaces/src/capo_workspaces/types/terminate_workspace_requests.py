"""Generated from Smithy shape ``com.amazonaws.workspaces#TerminateWorkspaceRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.terminate_request

TerminateWorkspaceRequests: TypeAlias = list[
    "capo_workspaces.types.terminate_request.TerminateRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateWorkspaceRequests) -> list:
    import capo_workspaces.types.terminate_request

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.terminate_request.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TerminateWorkspaceRequests:
    import capo_workspaces.types.terminate_request

    out: TerminateWorkspaceRequests = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.terminate_request.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TerminateWorkspaceRequests) -> list:
    import capo_workspaces.types.terminate_request

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.terminate_request.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> TerminateWorkspaceRequests:
    import capo_workspaces.types.terminate_request

    out: TerminateWorkspaceRequests = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.terminate_request.deserialize_cbor(item))
    return out
