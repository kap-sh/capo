"""Generated from Smithy shape ``com.amazonaws.workspaces#ModificationStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.modification_state

ModificationStateList: TypeAlias = list[
    "capo_workspaces.types.modification_state.ModificationState"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModificationStateList) -> list:
    import capo_workspaces.types.modification_state

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.modification_state.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ModificationStateList:
    import capo_workspaces.types.modification_state

    out: ModificationStateList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.modification_state.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ModificationStateList) -> list:
    import capo_workspaces.types.modification_state

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.modification_state.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ModificationStateList:
    import capo_workspaces.types.modification_state

    out: ModificationStateList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.modification_state.deserialize_cbor(item))
    return out
