"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GenerationErrorDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.generation_error_code
    import capo_bedrock_agentcore.types.generation_error_message
    import capo_bedrock_agentcore.types.generation_error_session_id_list


class GenerationErrorDetail(TypedDict, closed=True):
    error_code: NotRequired[
        "capo_bedrock_agentcore.types.generation_error_code.GenerationErrorCode"
    ]
    """<p>The error code, for example <code>ACCESS_DENIED</code> or <code>EXPIRED_CREDENTIALS</code>. New codes can be added.</p>"""
    error_message: NotRequired[
        "capo_bedrock_agentcore.types.generation_error_message.GenerationErrorMessage"
    ]
    """<p>A description of the error.</p>"""
    count: NotRequired["int"]
    """<p>The number of sessions and traces that failed with this error code. Absent for a generation that finished before failures were counted by code. In that case, <code>sessionIds</code> is a sample.</p>"""
    session_ids: NotRequired[
        "capo_bedrock_agentcore.types.generation_error_session_id_list.GenerationErrorSessionIdList"
    ]
    """<p>Up to 10 of the sessions that failed with this error code. Each entry is a session ID, or the ID of a trace named in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerationErrorDetail) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "count" in value:
        out["count"] = value["count"]
    if "session_ids" in value:
        import capo_bedrock_agentcore.types.generation_error_session_id_list

        out["sessionIds"] = (
            capo_bedrock_agentcore.types.generation_error_session_id_list.serialize_json(
                value["session_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> GenerationErrorDetail:
    out: GenerationErrorDetail = {}  # type: ignore[typeddict-item]
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    if data.get("count") is not None:
        out["count"] = data["count"]
    if data.get("sessionIds") is not None:
        import capo_bedrock_agentcore.types.generation_error_session_id_list

        out["session_ids"] = (
            capo_bedrock_agentcore.types.generation_error_session_id_list.deserialize_json(
                data["sessionIds"]
            )
        )
    return out
