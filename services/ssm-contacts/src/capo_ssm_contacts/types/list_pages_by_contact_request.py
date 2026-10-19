"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ListPagesByContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.max_results
    import capo_ssm_contacts.types.pagination_token
    import capo_ssm_contacts.types.ssm_contacts_arn


class ListPagesByContactRequest(TypedDict, closed=True):
    contact_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact you are retrieving engagements for.</p>"""
    next_token: NotRequired["capo_ssm_contacts.types.pagination_token.PaginationToken"]
    """<p>The pagination token to continue to the next page of results.</p>"""
    max_results: NotRequired["capo_ssm_contacts.types.max_results.MaxResults"]
    """<p>The maximum number of engagements to contact channels to list per page of results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPagesByContactRequest) -> dict:
    out: dict = {}
    out["ContactId"] = value["contact_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPagesByContactRequest:
    out: ListPagesByContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    else:
        out["contact_id"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
