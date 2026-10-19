"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ListDomainsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controlcatalog.types.domain_summary_list
    import capo_controlcatalog.types.pagination_token


class ListDomainsResponse(TypedDict, closed=True):
    domains: "capo_controlcatalog.types.domain_summary_list.DomainSummaryList"
    """<p>The list of domains that the <code>ListDomains</code> API returns.</p>"""
    next_token: NotRequired[
        "capo_controlcatalog.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainsResponse) -> dict:
    out: dict = {}
    import capo_controlcatalog.types.domain_summary_list

    out["Domains"] = capo_controlcatalog.types.domain_summary_list.serialize_json(
        value["domains"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDomainsResponse:
    out: ListDomainsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Domains") is not None:
        import capo_controlcatalog.types.domain_summary_list

        out["domains"] = capo_controlcatalog.types.domain_summary_list.deserialize_json(
            data["Domains"]
        )
    else:
        out["domains"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
