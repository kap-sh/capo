"""Generated from Smithy shape ``com.amazonaws.workspaces#AccountLinkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.account_link

AccountLinkList: TypeAlias = list["capo_workspaces.types.account_link.AccountLink"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountLinkList) -> list:
    import capo_workspaces.types.account_link

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.account_link.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AccountLinkList:
    import capo_workspaces.types.account_link

    out: AccountLinkList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.account_link.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccountLinkList) -> list:
    import capo_workspaces.types.account_link

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.account_link.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AccountLinkList:
    import capo_workspaces.types.account_link

    out: AccountLinkList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.account_link.deserialize_cbor(item))
    return out
