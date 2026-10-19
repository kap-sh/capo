"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ConverseMetrics``."""

from typing_extensions import TypedDict


class ConverseMetrics(TypedDict, closed=True):
    latency_ms: "int"
    """<p>The latency of the call to <code>Converse</code>, in milliseconds. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConverseMetrics) -> dict:
    out: dict = {}
    out["latencyMs"] = value["latency_ms"]
    return out


def deserialize_json(data: dict) -> ConverseMetrics:
    out: ConverseMetrics = {}  # type: ignore[typeddict-item]
    if data.get("latencyMs") is not None:
        out["latency_ms"] = data["latencyMs"]
    else:
        out["latency_ms"] = 0
    return out
