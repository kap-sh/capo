"""Generated from Smithy shape ``com.amazonaws.qconnect#ListSpansResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.next_token
    import capo_qconnect.types.span_list


class ListSpansResponse(TypedDict, closed=True):
    spans: "capo_qconnect.types.span_list.SpanList"
    """<p>Array of span objects for the session</p>"""
    next_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>Pagination token for retrieving additional results</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSpansResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.span_list

    out["spans"] = capo_qconnect.types.span_list.serialize_json(value["spans"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSpansResponse:
    out: ListSpansResponse = {}  # type: ignore[typeddict-item]
    if data.get("spans") is not None:
        import capo_qconnect.types.span_list

        out["spans"] = capo_qconnect.types.span_list.deserialize_json(data["spans"])
    else:
        out["spans"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListSpansResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "spans" in value:
        import capo_qconnect.types.span_list

        out["spans"] = capo_qconnect.types.span_list.redact_sensitive(value["spans"])
    return out
