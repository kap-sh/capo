"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SpanContext``."""

from typing_extensions import NotRequired, TypedDict


class SpanContext(TypedDict, closed=True):
    session_id: "str"
    """<p> The unique identifier of the session containing this span. Sessions represent complete conversation flows and are detected using configurable <code>SessionTimeoutMinutes</code> (default 15 minutes). </p>"""
    trace_id: NotRequired["str"]
    """<p> The unique identifier of the trace containing this span. Traces represent individual request-response interactions within a session and group related spans together. </p>"""
    span_id: NotRequired["str"]
    """<p> The unique identifier of the specific span being referenced. Spans represent individual operations like tool calls, model invocations, or other discrete actions within the agent's execution. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpanContext) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    if "trace_id" in value:
        out["traceId"] = value["trace_id"]
    if "span_id" in value:
        out["spanId"] = value["span_id"]
    return out


def deserialize_json(data: dict) -> SpanContext:
    out: SpanContext = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("traceId") is not None:
        out["trace_id"] = data["traceId"]
    if data.get("spanId") is not None:
        out["span_id"] = data["spanId"]
    return out
