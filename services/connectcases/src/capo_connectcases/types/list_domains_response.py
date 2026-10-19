"""Generated from Smithy shape ``com.amazonaws.connectcases#ListDomainsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.domain_summary_list
    import capo_connectcases.types.next_token


class ListDomainsResponse(TypedDict, closed=True):
    domains: "capo_connectcases.types.domain_summary_list.DomainSummaryList"
    """<p>The Cases domain.</p>"""
    next_token: NotRequired["capo_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. This is null if there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainsResponse) -> dict:
    out: dict = {}
    import capo_connectcases.types.domain_summary_list

    out["domains"] = capo_connectcases.types.domain_summary_list.serialize_json(
        value["domains"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDomainsResponse:
    out: ListDomainsResponse = {}  # type: ignore[typeddict-item]
    if data.get("domains") is not None:
        import capo_connectcases.types.domain_summary_list

        out["domains"] = capo_connectcases.types.domain_summary_list.deserialize_json(
            data["domains"]
        )
    else:
        out["domains"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
