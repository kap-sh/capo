"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteFlowVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_identifier
    import capo_bedrock_agent.types.numerical_version


class DeleteFlowVersionRequest(TypedDict, closed=True):
    flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier"
    """<p>The unique identifier of the flow whose version that you want to delete</p>"""
    flow_version: "capo_bedrock_agent.types.numerical_version.NumericalVersion"
    """<p>The version of the flow that you want to delete.</p>"""
    skip_resource_in_use_check: NotRequired["bool"]
    """<p>By default, this value is <code>false</code> and deletion is stopped if the resource is in use. If you set it to <code>true</code>, the resource will be deleted even if the resource is in use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFlowVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFlowVersionRequest:
    out: DeleteFlowVersionRequest = {}  # type: ignore[typeddict-item]
    return out
