"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SessionTraceIds``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.trace_id_list


class SessionTraceIds(TypedDict, closed=True):
    session_id: "str"
    """<p>The unique identifier of the session that contains the traces to evaluate.</p>"""
    trace_ids: "capo_bedrock_agentcore.types.trace_id_list.TraceIdList"
    """<p>The list of trace IDs within the session to evaluate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionTraceIds) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    import capo_bedrock_agentcore.types.trace_id_list

    out["traceIds"] = capo_bedrock_agentcore.types.trace_id_list.serialize_json(
        value["trace_ids"]
    )
    return out


def deserialize_json(data: dict) -> SessionTraceIds:
    out: SessionTraceIds = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("traceIds") is not None:
        import capo_bedrock_agentcore.types.trace_id_list

        out["trace_ids"] = capo_bedrock_agentcore.types.trace_id_list.deserialize_json(
            data["traceIds"]
        )
    else:
        out["trace_ids"] = []
    return out
