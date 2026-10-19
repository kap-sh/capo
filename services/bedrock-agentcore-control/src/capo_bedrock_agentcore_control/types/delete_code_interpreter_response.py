"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteCodeInterpreterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.code_interpreter_id
    import capo_bedrock_agentcore_control.types.code_interpreter_status
    import capo_bedrock_agentcore_control.types.date_timestamp


class DeleteCodeInterpreterResponse(TypedDict, closed=True):
    code_interpreter_id: (
        "capo_bedrock_agentcore_control.types.code_interpreter_id.CodeInterpreterId"
    )
    """<p>The unique identifier of the deleted code interpreter.</p>"""
    status: "capo_bedrock_agentcore_control.types.code_interpreter_status.CodeInterpreterStatus"
    """<p>The current status of the code interpreter deletion.</p>"""
    last_updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the code interpreter was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCodeInterpreterResponse) -> dict:
    out: dict = {}
    out["codeInterpreterId"] = value["code_interpreter_id"]
    import capo_bedrock_agentcore_control.types.code_interpreter_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.code_interpreter_status.serialize_json(
            value["status"]
        )
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["lastUpdatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteCodeInterpreterResponse:
    out: DeleteCodeInterpreterResponse = {}  # type: ignore[typeddict-item]
    if data.get("codeInterpreterId") is not None:
        out["code_interpreter_id"] = data["codeInterpreterId"]
    else:
        out["code_interpreter_id"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.code_interpreter_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.code_interpreter_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.code_interpreter_status.CodeInterpreterStatus",
            "",
        )
    if data.get("lastUpdatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
