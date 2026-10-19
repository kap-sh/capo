"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#EndSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.session_arn
    import capo_bedrock_agent_runtime.types.session_status
    import capo_bedrock_agent_runtime.types.uuid


class EndSessionResponse(TypedDict, closed=True):
    session_id: "capo_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>The unique identifier of the session you ended.</p>"""
    session_arn: "capo_bedrock_agent_runtime.types.session_arn.SessionArn"
    """<p>The Amazon Resource Name (ARN) of the session you ended.</p>"""
    session_status: "capo_bedrock_agent_runtime.types.session_status.SessionStatus"
    """<p>The current status of the session you ended.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndSessionResponse) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["sessionArn"] = value["session_arn"]
    import capo_bedrock_agent_runtime.types.session_status

    out["sessionStatus"] = (
        capo_bedrock_agent_runtime.types.session_status.serialize_json(
            value["session_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> EndSessionResponse:
    out: EndSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("sessionArn") is not None:
        out["session_arn"] = data["sessionArn"]
    else:
        out["session_arn"] = ""
    if data.get("sessionStatus") is not None:
        import capo_bedrock_agent_runtime.types.session_status

        out["session_status"] = (
            capo_bedrock_agent_runtime.types.session_status.deserialize_json(
                data["sessionStatus"]
            )
        )
    else:
        import typing

        out["session_status"] = typing.cast(
            "capo_bedrock_agent_runtime.types.session_status.SessionStatus", ""
        )
    return out
