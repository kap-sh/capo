"""Generated from Smithy shape ``com.amazonaws.transfer#ListAgreementsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.max_results
    import capo_transfer.types.next_token
    import capo_transfer.types.server_id


class ListAgreementsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_transfer.types.max_results.MaxResults"]
    """<p>The maximum number of items to return.</p>"""
    next_token: NotRequired["capo_transfer.types.next_token.NextToken"]
    """<p>When you can get additional results from the <code>ListAgreements</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional agreements.</p>"""
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>The identifier of the server for which you want a list of agreements.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAgreementsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["ServerId"] = value["server_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAgreementsRequest:
    out: ListAgreementsRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ServerId") is not None:
        out["server_id"] = data["ServerId"]
    else:
        out["server_id"] = ""
    return out
