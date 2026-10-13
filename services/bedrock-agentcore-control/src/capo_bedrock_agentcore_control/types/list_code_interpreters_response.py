"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListCodeInterpretersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.code_interpreter_summaries
    import capo_bedrock_agentcore_control.types.next_token


class ListCodeInterpretersResponse(TypedDict, closed=True):
    code_interpreter_summaries: "capo_bedrock_agentcore_control.types.code_interpreter_summaries.CodeInterpreterSummaries"
    """<p>The list of code interpreter summaries.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>A token to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCodeInterpretersResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.code_interpreter_summaries

    out["codeInterpreterSummaries"] = (
        capo_bedrock_agentcore_control.types.code_interpreter_summaries.serialize_json(
            value["code_interpreter_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCodeInterpretersResponse:
    out: ListCodeInterpretersResponse = {}  # type: ignore[typeddict-item]
    if data.get("codeInterpreterSummaries") is not None:
        import capo_bedrock_agentcore_control.types.code_interpreter_summaries

        out["code_interpreter_summaries"] = (
            capo_bedrock_agentcore_control.types.code_interpreter_summaries.deserialize_json(
                data["codeInterpreterSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListCodeInterpretersResponse.code_interpreter_summaries required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListCodeInterpretersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "code_interpreter_summaries" in value:
        import capo_bedrock_agentcore_control.types.code_interpreter_summaries

        out["code_interpreter_summaries"] = (
            capo_bedrock_agentcore_control.types.code_interpreter_summaries.redact_sensitive(
                value["code_interpreter_summaries"]
            )
        )
    return out
