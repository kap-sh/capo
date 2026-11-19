"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspacesPoolErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.workspaces_pool_error

WorkspacesPoolErrors: TypeAlias = list[
    "capo_workspaces.types.workspaces_pool_error.WorkspacesPoolError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspacesPoolErrors) -> list:
    import capo_workspaces.types.workspaces_pool_error

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.workspaces_pool_error.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WorkspacesPoolErrors:
    import capo_workspaces.types.workspaces_pool_error

    out: WorkspacesPoolErrors = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.workspaces_pool_error.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkspacesPoolErrors) -> list:
    import capo_workspaces.types.workspaces_pool_error

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.workspaces_pool_error.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> WorkspacesPoolErrors:
    import capo_workspaces.types.workspaces_pool_error

    out: WorkspacesPoolErrors = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.workspaces_pool_error.deserialize_cbor(item))
    return out
