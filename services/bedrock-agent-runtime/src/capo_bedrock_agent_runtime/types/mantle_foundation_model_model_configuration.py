"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#MantleFoundationModelModelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.bedrock_model_arn
    import capo_bedrock_agent_runtime.types.mantle_project_id


class MantleFoundationModelModelConfiguration(TypedDict, closed=True):
    model_arn: "capo_bedrock_agent_runtime.types.bedrock_model_arn.BedrockModelArn"
    """<p>The ARN of the Mantle foundation model.</p>"""
    project_id: NotRequired[
        "capo_bedrock_agent_runtime.types.mantle_project_id.MantleProjectId"
    ]
    """<p>The Amazon Bedrock project ID used for billing and usage attribution. If you don't specify a value, the service uses the default project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MantleFoundationModelModelConfiguration) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    if "project_id" in value:
        out["projectId"] = value["project_id"]
    return out


def deserialize_json(data: dict) -> MantleFoundationModelModelConfiguration:
    out: MantleFoundationModelModelConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("modelArn") is not None:
        out["model_arn"] = data["modelArn"]
    else:
        raise DeserializationError(
            "MantleFoundationModelModelConfiguration.model_arn required"
        )
    if data.get("projectId") is not None:
        out["project_id"] = data["projectId"]
    return out
