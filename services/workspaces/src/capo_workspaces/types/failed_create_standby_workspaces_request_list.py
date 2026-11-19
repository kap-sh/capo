"""Generated from Smithy shape ``com.amazonaws.workspaces#FailedCreateStandbyWorkspacesRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.failed_create_standby_workspaces_request

FailedCreateStandbyWorkspacesRequestList: TypeAlias = list[
    "capo_workspaces.types.failed_create_standby_workspaces_request.FailedCreateStandbyWorkspacesRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedCreateStandbyWorkspacesRequestList) -> list:
    import capo_workspaces.types.failed_create_standby_workspaces_request

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.failed_create_standby_workspaces_request.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FailedCreateStandbyWorkspacesRequestList:
    import capo_workspaces.types.failed_create_standby_workspaces_request

    out: FailedCreateStandbyWorkspacesRequestList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.failed_create_standby_workspaces_request.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FailedCreateStandbyWorkspacesRequestList) -> list:
    import capo_workspaces.types.failed_create_standby_workspaces_request

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.failed_create_standby_workspaces_request.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> FailedCreateStandbyWorkspacesRequestList:
    import capo_workspaces.types.failed_create_standby_workspaces_request

    out: FailedCreateStandbyWorkspacesRequestList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.failed_create_standby_workspaces_request.deserialize_cbor(
                item
            )
        )
    return out
