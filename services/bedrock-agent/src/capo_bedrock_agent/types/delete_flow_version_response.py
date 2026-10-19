"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteFlowVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.numerical_version


class DeleteFlowVersionResponse(TypedDict, closed=True):
    id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the flow.</p>"""
    version: "capo_bedrock_agent.types.numerical_version.NumericalVersion"
    """<p>The version of the flow being deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFlowVersionResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> DeleteFlowVersionResponse:
    out: DeleteFlowVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    return out
