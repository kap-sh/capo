"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeAccountModificationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.account_modification_list
    import capo_workspaces.types.pagination_token


class DescribeAccountModificationsResult(TypedDict, closed=True):
    account_modifications: NotRequired[
        "capo_workspaces.types.account_modification_list.AccountModificationList"
    ]
    """<p>The list of modifications to the configuration of BYOL.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAccountModificationsResult) -> dict:
    out: dict = {}
    if "account_modifications" in value:
        import capo_workspaces.types.account_modification_list

        out["AccountModifications"] = (
            capo_workspaces.types.account_modification_list.serialize_aws_json_1_1(
                value["account_modifications"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAccountModificationsResult:
    out: DescribeAccountModificationsResult = {}  # type: ignore[typeddict-item]
    if data.get("AccountModifications") is not None:
        import capo_workspaces.types.account_modification_list

        out["account_modifications"] = (
            capo_workspaces.types.account_modification_list.deserialize_aws_json_1_1(
                data["AccountModifications"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAccountModificationsResult) -> dict:
    out: dict = {}
    if "account_modifications" in value:
        import capo_workspaces.types.account_modification_list

        out["AccountModifications"] = (
            capo_workspaces.types.account_modification_list.serialize_cbor(
                value["account_modifications"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeAccountModificationsResult:
    out: DescribeAccountModificationsResult = {}  # type: ignore[typeddict-item]
    if data.get("AccountModifications") is not None:
        import capo_workspaces.types.account_modification_list

        out["account_modifications"] = (
            capo_workspaces.types.account_modification_list.deserialize_cbor(
                data["AccountModifications"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
