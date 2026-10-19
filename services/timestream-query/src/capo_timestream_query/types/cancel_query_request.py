"""Generated from Smithy shape ``com.amazonaws.timestreamquery#CancelQueryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.query_id


class CancelQueryRequest(TypedDict, closed=True):
    query_id: "capo_timestream_query.types.query_id.QueryId"
    """<p> The ID of the query that needs to be cancelled. <code>QueryID</code> is returned as part of the query result. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelQueryRequest) -> dict:
    out: dict = {}
    out["QueryId"] = value["query_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelQueryRequest:
    out: CancelQueryRequest = {}  # type: ignore[typeddict-item]
    if data.get("QueryId") is not None:
        out["query_id"] = data["QueryId"]
    else:
        out["query_id"] = ""
    return out
