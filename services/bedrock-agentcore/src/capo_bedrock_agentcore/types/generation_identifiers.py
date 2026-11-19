"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GenerationIdentifiers``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.generation_session_id_list
    import capo_bedrock_agentcore.types.generation_trace_id_list


class GenerationIdentifiers(TypedDict, closed=True):
    session_ids: NotRequired[
        "capo_bedrock_agentcore.types.generation_session_id_list.GenerationSessionIdList"
    ]
    """<p>The IDs of the sessions to use, up to 25.</p>"""
    trace_ids: NotRequired[
        "capo_bedrock_agentcore.types.generation_trace_id_list.GenerationTraceIdList"
    ]
    """<p>The IDs of the traces to use, up to 25.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerationIdentifiers) -> dict:
    out: dict = {}
    if "session_ids" in value:
        import capo_bedrock_agentcore.types.generation_session_id_list

        out["sessionIds"] = (
            capo_bedrock_agentcore.types.generation_session_id_list.serialize_json(
                value["session_ids"]
            )
        )
    if "trace_ids" in value:
        import capo_bedrock_agentcore.types.generation_trace_id_list

        out["traceIds"] = (
            capo_bedrock_agentcore.types.generation_trace_id_list.serialize_json(
                value["trace_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> GenerationIdentifiers:
    out: GenerationIdentifiers = {}  # type: ignore[typeddict-item]
    if data.get("sessionIds") is not None:
        import capo_bedrock_agentcore.types.generation_session_id_list

        out["session_ids"] = (
            capo_bedrock_agentcore.types.generation_session_id_list.deserialize_json(
                data["sessionIds"]
            )
        )
    if data.get("traceIds") is not None:
        import capo_bedrock_agentcore.types.generation_trace_id_list

        out["trace_ids"] = (
            capo_bedrock_agentcore.types.generation_trace_id_list.deserialize_json(
                data["traceIds"]
            )
        )
    return out
