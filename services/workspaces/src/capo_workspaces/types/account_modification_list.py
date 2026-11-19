"""Generated from Smithy shape ``com.amazonaws.workspaces#AccountModificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.account_modification

AccountModificationList: TypeAlias = list[
    "capo_workspaces.types.account_modification.AccountModification"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountModificationList) -> list:
    import capo_workspaces.types.account_modification

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.account_modification.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AccountModificationList:
    import capo_workspaces.types.account_modification

    out: AccountModificationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.account_modification.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccountModificationList) -> list:
    import capo_workspaces.types.account_modification

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.account_modification.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AccountModificationList:
    import capo_workspaces.types.account_modification

    out: AccountModificationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.account_modification.deserialize_cbor(item))
    return out
