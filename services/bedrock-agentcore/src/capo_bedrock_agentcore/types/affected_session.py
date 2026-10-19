"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AffectedSession``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.failure_span_detail_list


class AffectedSession(TypedDict, closed=True):
    session_id: "str"
    """<p>The unique identifier of the affected session.</p>"""
    explanation: "str"
    """<p>An explanation of how the failure manifested in this session.</p>"""
    fix_type: "str"
    """<p>The type of fix recommended for this failure.</p>"""
    recommendation: "str"
    """<p>The specific fix recommendation for this session.</p>"""
    failure_spans: (
        "capo_bedrock_agentcore.types.failure_span_detail_list.FailureSpanDetailList"
    )
    """<p>The list of spans where failures were detected in this session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AffectedSession) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["explanation"] = value["explanation"]
    out["fixType"] = value["fix_type"]
    out["recommendation"] = value["recommendation"]
    import capo_bedrock_agentcore.types.failure_span_detail_list

    out["failureSpans"] = (
        capo_bedrock_agentcore.types.failure_span_detail_list.serialize_json(
            value["failure_spans"]
        )
    )
    return out


def deserialize_json(data: dict) -> AffectedSession:
    out: AffectedSession = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("explanation") is not None:
        out["explanation"] = data["explanation"]
    else:
        out["explanation"] = ""
    if data.get("fixType") is not None:
        out["fix_type"] = data["fixType"]
    else:
        out["fix_type"] = ""
    if data.get("recommendation") is not None:
        out["recommendation"] = data["recommendation"]
    else:
        out["recommendation"] = ""
    if data.get("failureSpans") is not None:
        import capo_bedrock_agentcore.types.failure_span_detail_list

        out["failure_spans"] = (
            capo_bedrock_agentcore.types.failure_span_detail_list.deserialize_json(
                data["failureSpans"]
            )
        )
    else:
        out["failure_spans"] = []
    return out
