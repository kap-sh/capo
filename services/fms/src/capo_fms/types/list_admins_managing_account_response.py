"""Generated from Smithy shape ``com.amazonaws.fms#ListAdminsManagingAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.account_id_list
    import capo_fms.types.pagination_token


class ListAdminsManagingAccountResponse(TypedDict, closed=True):
    admin_accounts: NotRequired["capo_fms.types.account_id_list.AccountIdList"]
    """<p>The list of accounts who manage member accounts within their <a>AdminScope</a>.</p>"""
    next_token: NotRequired["capo_fms.types.pagination_token.PaginationToken"]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Firewall Manager returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAdminsManagingAccountResponse) -> dict:
    out: dict = {}
    if "admin_accounts" in value:
        import capo_fms.types.account_id_list

        out["AdminAccounts"] = capo_fms.types.account_id_list.serialize_aws_json_1_1(
            value["admin_accounts"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAdminsManagingAccountResponse:
    out: ListAdminsManagingAccountResponse = {}  # type: ignore[typeddict-item]
    if data.get("AdminAccounts") is not None:
        import capo_fms.types.account_id_list

        out["admin_accounts"] = capo_fms.types.account_id_list.deserialize_aws_json_1_1(
            data["AdminAccounts"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAdminsManagingAccountResponse) -> dict:
    out: dict = {}
    if "admin_accounts" in value:
        import capo_fms.types.account_id_list

        out["AdminAccounts"] = capo_fms.types.account_id_list.serialize_cbor(
            value["admin_accounts"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAdminsManagingAccountResponse:
    out: ListAdminsManagingAccountResponse = {}  # type: ignore[typeddict-item]
    if data.get("AdminAccounts") is not None:
        import capo_fms.types.account_id_list

        out["admin_accounts"] = capo_fms.types.account_id_list.deserialize_cbor(
            data["AdminAccounts"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
