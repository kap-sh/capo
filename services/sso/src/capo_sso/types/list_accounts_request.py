"""Generated from Smithy shape ``com.amazonaws.sso#ListAccountsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso.types.access_token_type
    import capo_sso.types.max_result_type
    import capo_sso.types.next_token_type


class ListAccountsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_sso.types.next_token_type.NextTokenType"]
    """<p>(Optional) When requesting subsequent pages, this is the page token from the previous response output.</p>"""
    max_results: NotRequired["capo_sso.types.max_result_type.MaxResultType"]
    """<p>This is the number of items clients can request per page.</p>"""
    access_token: "capo_sso.types.access_token_type.AccessTokenType"
    """<p>The token issued by the <code>CreateToken</code> API call. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html">CreateToken</a> in the <i>IAM Identity Center OIDC API Reference Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccountsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAccountsRequest:
    out: ListAccountsRequest = {}  # type: ignore[typeddict-item]
    return out
