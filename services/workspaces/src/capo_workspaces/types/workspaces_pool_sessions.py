"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspacesPoolSessions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.workspaces_pool_session

WorkspacesPoolSessions: TypeAlias = list[
    "capo_workspaces.types.workspaces_pool_session.WorkspacesPoolSession"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspacesPoolSessions) -> list:
    import capo_workspaces.types.workspaces_pool_session

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.workspaces_pool_session.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WorkspacesPoolSessions:
    import capo_workspaces.types.workspaces_pool_session

    out: WorkspacesPoolSessions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.workspaces_pool_session.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkspacesPoolSessions) -> list:
    import capo_workspaces.types.workspaces_pool_session

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.workspaces_pool_session.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> WorkspacesPoolSessions:
    import capo_workspaces.types.workspaces_pool_session

    out: WorkspacesPoolSessions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.workspaces_pool_session.deserialize_cbor(item))
    return out
