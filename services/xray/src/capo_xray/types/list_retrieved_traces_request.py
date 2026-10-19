"""Generated from Smithy shape ``com.amazonaws.xray#ListRetrievedTracesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.retrieval_token
    import capo_xray.types.string
    import capo_xray.types.trace_format_type


class ListRetrievedTracesRequest(TypedDict, closed=True):
    retrieval_token: "capo_xray.types.retrieval_token.RetrievalToken"
    """<p> Retrieval token. </p>"""
    trace_format: NotRequired["capo_xray.types.trace_format_type.TraceFormatType"]
    """<p> Format of the requested traces. </p>"""
    next_token: NotRequired["capo_xray.types.string.String"]
    """<p> Specify the pagination token returned by a previous request to retrieve the next page of indexes. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRetrievedTracesRequest) -> dict:
    out: dict = {}
    out["RetrievalToken"] = value["retrieval_token"]
    if "trace_format" in value:
        import capo_xray.types.trace_format_type

        out["TraceFormat"] = capo_xray.types.trace_format_type.serialize_json(
            value["trace_format"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRetrievedTracesRequest:
    out: ListRetrievedTracesRequest = {}  # type: ignore[typeddict-item]
    if data.get("RetrievalToken") is not None:
        out["retrieval_token"] = data["RetrievalToken"]
    else:
        out["retrieval_token"] = ""
    if data.get("TraceFormat") is not None:
        import capo_xray.types.trace_format_type

        out["trace_format"] = capo_xray.types.trace_format_type.deserialize_json(
            data["TraceFormat"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
