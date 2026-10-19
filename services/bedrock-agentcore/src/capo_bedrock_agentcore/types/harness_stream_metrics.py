"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessStreamMetrics``."""

from typing_extensions import TypedDict


class HarnessStreamMetrics(TypedDict, closed=True):
    latency_ms: "int"
    """<p>The end-to-end latency of the invocation in milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessStreamMetrics) -> dict:
    out: dict = {}
    out["latencyMs"] = value["latency_ms"]
    return out


def deserialize_json(data: dict) -> HarnessStreamMetrics:
    out: HarnessStreamMetrics = {}  # type: ignore[typeddict-item]
    if data.get("latencyMs") is not None:
        out["latency_ms"] = data["latencyMs"]
    else:
        out["latency_ms"] = 0
    return out
