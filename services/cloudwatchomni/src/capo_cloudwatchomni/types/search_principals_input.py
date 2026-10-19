"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#SearchPrincipalsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.domain_id
    import capo_cloudwatchomni.types.search_principals_next_token


class SearchPrincipalsInput(TypedDict, closed=True):
    domain_id: "capo_cloudwatchomni.types.domain_id.DomainId"
    """The ID of the domain to search within."""
    search_query: "str"
    """A search term to match against user names, display names, and IDs. Pass * to list all principals. Maximum 128 characters."""
    max_results: NotRequired["int"]
    """The maximum number of results to return. Defaults to 10. Valid only when searchQuery is *; other searches reject this parameter and return at most 10 results."""
    next_token: NotRequired[
        "capo_cloudwatchomni.types.search_principals_next_token.SearchPrincipalsNextToken"
    ]
    """A token to retrieve the next page of results. Valid only when searchQuery is *; other searches do not paginate and reject this parameter. Tokens expire after 24 hours."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SearchPrincipalsInput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["searchQuery"] = value["search_query"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> SearchPrincipalsInput:
    out: SearchPrincipalsInput = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("searchQuery") is not None:
        out["search_query"] = data["searchQuery"]
    else:
        out["search_query"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
