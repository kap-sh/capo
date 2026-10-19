"""Generated from Smithy shape ``com.amazonaws.xray#GetTraceGraphRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.string
    import capo_xray.types.trace_id_list


class GetTraceGraphRequest(TypedDict, closed=True):
    trace_ids: "capo_xray.types.trace_id_list.TraceIdList"
    """<p>Trace IDs of requests for which to generate a service graph.</p>"""
    next_token: NotRequired["capo_xray.types.string.String"]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTraceGraphRequest) -> dict:
    out: dict = {}
    import capo_xray.types.trace_id_list

    out["TraceIds"] = capo_xray.types.trace_id_list.serialize_json(value["trace_ids"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetTraceGraphRequest:
    out: GetTraceGraphRequest = {}  # type: ignore[typeddict-item]
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
