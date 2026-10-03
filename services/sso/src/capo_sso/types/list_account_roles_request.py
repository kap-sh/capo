"""Generated from Smithy shape ``com.amazonaws.sso#ListAccountRolesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso.types.access_token_type
    import capo_sso.types.account_id_type
    import capo_sso.types.max_result_type
    import capo_sso.types.next_token_type


class ListAccountRolesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_sso.types.next_token_type.NextTokenType"]
    """<p>The page token from the previous response output when you request subsequent pages.</p>"""
    max_results: NotRequired["capo_sso.types.max_result_type.MaxResultType"]
    """<p>The number of items that clients can request per page.</p>"""
    access_token: "capo_sso.types.access_token_type.AccessTokenType"
    """<p>The token issued by the <code>CreateToken</code> API call. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html">CreateToken</a> in the <i>IAM Identity Center OIDC API Reference Guide</i>.</p>"""
    account_id: "capo_sso.types.account_id_type.AccountIdType"
    """<p>The identifier for the AWS account that is assigned to the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccountRolesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAccountRolesRequest:
    out: ListAccountRolesRequest = {}  # type: ignore[typeddict-item]
    return out
