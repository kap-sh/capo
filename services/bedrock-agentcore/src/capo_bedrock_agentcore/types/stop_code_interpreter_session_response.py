"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StopCodeInterpreterSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.code_interpreter_session_id
    import capo_bedrock_agentcore.types.date_timestamp


class StopCodeInterpreterSessionResponse(TypedDict, closed=True):
    code_interpreter_identifier: "str"
    """<p>The identifier of the code interpreter.</p>"""
    session_id: "capo_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId"
    """<p>The identifier of the code interpreter session.</p>"""
    last_updated_at: "capo_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the code interpreter session was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopCodeInterpreterSessionResponse) -> dict:
    out: dict = {}
    out["codeInterpreterIdentifier"] = value["code_interpreter_identifier"]
    out["sessionId"] = value["session_id"]
    import capo_bedrock_agentcore.types.date_timestamp

    out["lastUpdatedAt"] = capo_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["last_updated_at"]
    )
    return out


def deserialize_json(data: dict) -> StopCodeInterpreterSessionResponse:
    out: StopCodeInterpreterSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("codeInterpreterIdentifier") is not None:
        out["code_interpreter_identifier"] = data["codeInterpreterIdentifier"]
    else:
        out["code_interpreter_identifier"] = ""
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("lastUpdatedAt") is not None:
        import capo_bedrock_agentcore.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
