"""Generated from Smithy shape ``com.amazonaws.securitylake#GetDataLakeSourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.account_list
    import capo_securitylake.types.max_results
    import capo_securitylake.types.next_token


class GetDataLakeSourcesRequest(TypedDict, closed=True):
    accounts: NotRequired["capo_securitylake.types.account_list.AccountList"]
    """<p>The Amazon Web Services account ID for which a static snapshot of the current Amazon Web Services Region, including enabled accounts and log sources, is retrieved.</p>"""
    max_results: NotRequired["capo_securitylake.types.max_results.MaxResults"]
    """<p>The maximum limit of accounts for which the static snapshot of the current Region, including enabled accounts and log sources, is retrieved.</p>"""
    next_token: NotRequired["capo_securitylake.types.next_token.NextToken"]
    """<p>Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.</p> <p>Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataLakeSourcesRequest) -> dict:
    out: dict = {}
    if "accounts" in value:
        import capo_securitylake.types.account_list

        out["accounts"] = capo_securitylake.types.account_list.serialize_json(
            value["accounts"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetDataLakeSourcesRequest:
    out: GetDataLakeSourcesRequest = {}  # type: ignore[typeddict-item]
    if data.get("accounts") is not None:
        import capo_securitylake.types.account_list

        out["accounts"] = capo_securitylake.types.account_list.deserialize_json(
            data["accounts"]
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
