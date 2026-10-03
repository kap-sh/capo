"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListDomainsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.domain_summary_list
    import capo_codeartifact.types.pagination_token


class ListDomainsResult(TypedDict, closed=True):
    domains: NotRequired[
        "capo_codeartifact.types.domain_summary_list.DomainSummaryList"
    ]
    """<p> The returned list of <a href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DomainSummary.html">DomainSummary</a> objects. </p>"""
    next_token: NotRequired["capo_codeartifact.types.pagination_token.PaginationToken"]
    """<p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainsResult) -> dict:
    out: dict = {}
    if "domains" in value:
        import capo_codeartifact.types.domain_summary_list

        out["domains"] = capo_codeartifact.types.domain_summary_list.serialize_json(
            value["domains"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDomainsResult:
    out: ListDomainsResult = {}  # type: ignore[typeddict-item]
    if data.get("domains") is not None:
        import capo_codeartifact.types.domain_summary_list

        out["domains"] = capo_codeartifact.types.domain_summary_list.deserialize_json(
            data["domains"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
