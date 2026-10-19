"""Generated from Smithy shape ``com.amazonaws.connectcases#ListCasesForContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.contact_arn
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.next_token


class ListCasesForContactRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    contact_arn: "capo_connectcases.types.contact_arn.ContactArn"
    """<p>A unique identifier of a contact in Amazon Connect.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["capo_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCasesForContactRequest) -> dict:
    out: dict = {}
    out["contactArn"] = value["contact_arn"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCasesForContactRequest:
    out: ListCasesForContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("contactArn") is not None:
        out["contact_arn"] = data["contactArn"]
    else:
        out["contact_arn"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
