"""Generated from Smithy shape ``com.amazonaws.workspaces#PendingCreateStandbyWorkspacesRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.pending_create_standby_workspaces_request

PendingCreateStandbyWorkspacesRequestList: TypeAlias = list[
    "capo_workspaces.types.pending_create_standby_workspaces_request.PendingCreateStandbyWorkspacesRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PendingCreateStandbyWorkspacesRequestList) -> list:
    import capo_workspaces.types.pending_create_standby_workspaces_request

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.pending_create_standby_workspaces_request.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PendingCreateStandbyWorkspacesRequestList:
    import capo_workspaces.types.pending_create_standby_workspaces_request

    out: PendingCreateStandbyWorkspacesRequestList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.pending_create_standby_workspaces_request.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PendingCreateStandbyWorkspacesRequestList) -> list:
    import capo_workspaces.types.pending_create_standby_workspaces_request

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.pending_create_standby_workspaces_request.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> PendingCreateStandbyWorkspacesRequestList:
    import capo_workspaces.types.pending_create_standby_workspaces_request

    out: PendingCreateStandbyWorkspacesRequestList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.pending_create_standby_workspaces_request.deserialize_cbor(
                item
            )
        )
    return out
