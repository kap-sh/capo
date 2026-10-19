"""Generated from Smithy shape ``com.amazonaws.pcs#ListQueuesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pcs.types.queue_list


class ListQueuesResponse(TypedDict, closed=True):
    queues: "capo_pcs.types.queue_list.QueueList"
    """<p>The list of queues associated with the cluster.</p>"""
    next_token: NotRequired["str"]
    """<p>The value of <code>nextToken</code> is a unique pagination token for each page of results returned. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token returns an <code>HTTP 400 InvalidToken</code> error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListQueuesResponse) -> dict:
    out: dict = {}
    import capo_pcs.types.queue_list

    out["queues"] = capo_pcs.types.queue_list.serialize_aws_json_1_0(value["queues"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListQueuesResponse:
    out: ListQueuesResponse = {}  # type: ignore[typeddict-item]
    if data.get("queues") is not None:
        import capo_pcs.types.queue_list

        out["queues"] = capo_pcs.types.queue_list.deserialize_aws_json_1_0(
            data["queues"]
        )
    else:
        out["queues"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
