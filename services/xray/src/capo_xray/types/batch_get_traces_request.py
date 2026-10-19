"""Generated from Smithy shape ``com.amazonaws.xray#BatchGetTracesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.string
    import capo_xray.types.trace_id_list


class BatchGetTracesRequest(TypedDict, closed=True):
    trace_ids: "capo_xray.types.trace_id_list.TraceIdList"
    """<p>Specify the trace IDs of requests for which to retrieve segments.</p>"""
    next_token: NotRequired["capo_xray.types.string.String"]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTracesRequest) -> dict:
    out: dict = {}
    import capo_xray.types.trace_id_list

    out["TraceIds"] = capo_xray.types.trace_id_list.serialize_json(value["trace_ids"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> BatchGetTracesRequest:
    out: BatchGetTracesRequest = {}  # type: ignore[typeddict-item]
    if data.get("TraceIds") is not None:
        import capo_xray.types.trace_id_list

        out["trace_ids"] = capo_xray.types.trace_id_list.deserialize_json(
            data["TraceIds"]
        )
    else:
        out["trace_ids"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
