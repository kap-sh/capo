"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GenerationIdentifierCounts``."""

from typing_extensions import NotRequired, TypedDict


class GenerationIdentifierCounts(TypedDict, closed=True):
    session_id_count: NotRequired["int"]
    """<p>The number of session IDs in the request.</p>"""
    trace_id_count: NotRequired["int"]
    """<p>The number of trace IDs in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerationIdentifierCounts) -> dict:
    out: dict = {}
    if "session_id_count" in value:
        out["sessionIdCount"] = value["session_id_count"]
    if "trace_id_count" in value:
        out["traceIdCount"] = value["trace_id_count"]
    return out


def deserialize_json(data: dict) -> GenerationIdentifierCounts:
    out: GenerationIdentifierCounts = {}  # type: ignore[typeddict-item]
    if data.get("sessionIdCount") is not None:
        out["session_id_count"] = data["sessionIdCount"]
    if data.get("traceIdCount") is not None:
        out["trace_id_count"] = data["traceIdCount"]
    return out
