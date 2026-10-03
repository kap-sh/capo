"""Generated from Smithy shape ``com.amazonaws.connect#ListAssociatedContactsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id
    import capo_connect.types.list_associated_contacts_request_max_results
    import capo_connect.types.next_token


class ListAssociatedContactsRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    max_results: NotRequired[
        "capo_connect.types.list_associated_contacts_request_max_results.ListAssociatedContactsRequestMaxResults"
    ]
    """<p>The maximum number of results to return per page. </p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociatedContactsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssociatedContactsRequest:
    out: ListAssociatedContactsRequest = {}  # type: ignore[typeddict-item]
    return out
