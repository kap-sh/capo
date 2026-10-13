"""Generated from Smithy shape ``com.amazonaws.acm#ListAcmeAccountsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.acme_account_list


class ListAcmeAccountsResponse(TypedDict, closed=True):
    acme_accounts: NotRequired["capo_acm.types.acme_account_list.AcmeAccountList"]
    """<p>The list of ACME accounts.</p>"""
    next_token: NotRequired["str"]
    """<p>A token for pagination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAcmeAccountsResponse) -> dict:
    out: dict = {}
    if "acme_accounts" in value:
        import capo_acm.types.acme_account_list

        out["AcmeAccounts"] = capo_acm.types.acme_account_list.serialize_aws_json_1_1(
            value["acme_accounts"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAcmeAccountsResponse:
    out: ListAcmeAccountsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AcmeAccounts") is not None:
        import capo_acm.types.acme_account_list

        out["acme_accounts"] = (
            capo_acm.types.acme_account_list.deserialize_aws_json_1_1(
                data["AcmeAccounts"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListAcmeAccountsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "acme_accounts" in value:
        import capo_acm.types.acme_account_list

        out["acme_accounts"] = capo_acm.types.acme_account_list.redact_sensitive(
            value["acme_accounts"]
        )
    return out
