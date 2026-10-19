"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#FailureSpanDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.insights_failure_signal_list


class FailureSpanDetail(TypedDict, closed=True):
    span_id: "str"
    """<p>The unique identifier of the span where the failure occurred.</p>"""
    trace_id: "str"
    """<p>The trace identifier associated with the failure span.</p>"""
    signals: "capo_bedrock_agentcore.types.insights_failure_signal_list.InsightsFailureSignalList"
    """<p>The failure signals detected in this span.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailureSpanDetail) -> dict:
    out: dict = {}
    out["spanId"] = value["span_id"]
    out["traceId"] = value["trace_id"]
    import capo_bedrock_agentcore.types.insights_failure_signal_list

    out["signals"] = (
        capo_bedrock_agentcore.types.insights_failure_signal_list.serialize_json(
            value["signals"]
        )
    )
    return out


def deserialize_json(data: dict) -> FailureSpanDetail:
    out: FailureSpanDetail = {}  # type: ignore[typeddict-item]
    if data.get("spanId") is not None:
        out["span_id"] = data["spanId"]
    else:
        out["span_id"] = ""
    if data.get("traceId") is not None:
        out["trace_id"] = data["traceId"]
    else:
        out["trace_id"] = ""
    if data.get("signals") is not None:
        import capo_bedrock_agentcore.types.insights_failure_signal_list

        out["signals"] = (
            capo_bedrock_agentcore.types.insights_failure_signal_list.deserialize_json(
                data["signals"]
            )
        )
    else:
        out["signals"] = []
    return out
