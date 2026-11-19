"""Generated from Smithy shape ``com.amazonaws.workspaces#ConnectClientAddInList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.connect_client_add_in

ConnectClientAddInList: TypeAlias = list[
    "capo_workspaces.types.connect_client_add_in.ConnectClientAddIn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectClientAddInList) -> list:
    import capo_workspaces.types.connect_client_add_in

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.connect_client_add_in.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectClientAddInList:
    import capo_workspaces.types.connect_client_add_in

    out: ConnectClientAddInList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.connect_client_add_in.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConnectClientAddInList) -> list:
    import capo_workspaces.types.connect_client_add_in

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.connect_client_add_in.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ConnectClientAddInList:
    import capo_workspaces.types.connect_client_add_in

    out: ConnectClientAddInList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.connect_client_add_in.deserialize_cbor(item))
    return out
