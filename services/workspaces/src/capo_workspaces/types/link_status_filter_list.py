"""Generated from Smithy shape ``com.amazonaws.workspaces#LinkStatusFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.account_link_status_enum

LinkStatusFilterList: TypeAlias = list[
    "capo_workspaces.types.account_link_status_enum.AccountLinkStatusEnum"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LinkStatusFilterList) -> list:
    import capo_workspaces.types.account_link_status_enum

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.account_link_status_enum.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LinkStatusFilterList:
    import capo_workspaces.types.account_link_status_enum

    out: LinkStatusFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.account_link_status_enum.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LinkStatusFilterList) -> list:
    import capo_workspaces.types.account_link_status_enum

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.account_link_status_enum.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> LinkStatusFilterList:
    import capo_workspaces.types.account_link_status_enum

    out: LinkStatusFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.account_link_status_enum.deserialize_cbor(item)
        )
    return out
