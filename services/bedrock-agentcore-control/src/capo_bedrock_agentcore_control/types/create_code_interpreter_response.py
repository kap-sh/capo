"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateCodeInterpreterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.code_interpreter_arn
    import capo_bedrock_agentcore_control.types.code_interpreter_id
    import capo_bedrock_agentcore_control.types.code_interpreter_status
    import capo_bedrock_agentcore_control.types.date_timestamp


class CreateCodeInterpreterResponse(TypedDict, closed=True):
    code_interpreter_id: (
        "capo_bedrock_agentcore_control.types.code_interpreter_id.CodeInterpreterId"
    )
    """<p>The unique identifier of the created code interpreter.</p>"""
    code_interpreter_arn: (
        "capo_bedrock_agentcore_control.types.code_interpreter_arn.CodeInterpreterArn"
    )
    """<p>The Amazon Resource Name (ARN) of the created code interpreter.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the code interpreter was created.</p>"""
    status: "capo_bedrock_agentcore_control.types.code_interpreter_status.CodeInterpreterStatus"
    """<p>The current status of the code interpreter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCodeInterpreterResponse) -> dict:
    out: dict = {}
    out["codeInterpreterId"] = value["code_interpreter_id"]
    out["codeInterpreterArn"] = value["code_interpreter_arn"]
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.code_interpreter_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.code_interpreter_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateCodeInterpreterResponse:
    out: CreateCodeInterpreterResponse = {}  # type: ignore[typeddict-item]
    if data.get("codeInterpreterId") is not None:
        out["code_interpreter_id"] = data["codeInterpreterId"]
    else:
        out["code_interpreter_id"] = ""
    if data.get("codeInterpreterArn") is not None:
        out["code_interpreter_arn"] = data["codeInterpreterArn"]
    else:
        out["code_interpreter_arn"] = ""
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
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
    return out
