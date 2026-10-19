"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeletePromptResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.numerical_version
    import capo_bedrock_agent.types.prompt_id


class DeletePromptResponse(TypedDict, closed=True):
    id: "capo_bedrock_agent.types.prompt_id.PromptId"
    """<p>The unique identifier of the prompt that was deleted.</p>"""
    version: NotRequired["capo_bedrock_agent.types.numerical_version.NumericalVersion"]
    """<p>The version of the prompt that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePromptResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> DeletePromptResponse:
    out: DeletePromptResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    return out
