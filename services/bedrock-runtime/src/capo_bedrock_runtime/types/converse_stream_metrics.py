"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ConverseStreamMetrics``."""

from typing_extensions import TypedDict


class ConverseStreamMetrics(TypedDict, closed=True):
    latency_ms: "int"
    """<p>The latency for the streaming request, in milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConverseStreamMetrics) -> dict:
    out: dict = {}
    out["latencyMs"] = value["latency_ms"]
    return out


def deserialize_json(data: dict) -> ConverseStreamMetrics:
    out: ConverseStreamMetrics = {}  # type: ignore[typeddict-item]
    if data.get("latencyMs") is not None:
        out["latency_ms"] = data["latencyMs"]
    else:
        out["latency_ms"] = 0
    return out
