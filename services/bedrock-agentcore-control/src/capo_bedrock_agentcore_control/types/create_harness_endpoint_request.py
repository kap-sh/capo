"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateHarnessEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.harness_endpoint_description
    import capo_bedrock_agentcore_control.types.harness_endpoint_name
    import capo_bedrock_agentcore_control.types.harness_id
    import capo_bedrock_agentcore_control.types.harness_version
    import capo_bedrock_agentcore_control.types.tags_map


class CreateHarnessEndpointRequest(TypedDict, closed=True):
    harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId"
    """<p>The ID of the harness to create an endpoint for.</p>"""
    endpoint_name: (
        "capo_bedrock_agentcore_control.types.harness_endpoint_name.HarnessEndpointName"
    )
    """<p>The name of the endpoint. Must start with a letter and contain only alphanumeric characters and underscores.</p>"""
    target_version: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_version.HarnessVersion"
    ]
    """<p>The harness version that the endpoint points to and serves invocations from.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_endpoint_description.HarnessEndpointDescription"
    ]
    """<p>A description of the endpoint.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""
    tags: NotRequired["capo_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>Tags to apply to the endpoint resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateHarnessEndpointRequest) -> dict:
    out: dict = {}
    out["endpointName"] = value["endpoint_name"]
    if "target_version" in value:
        out["targetVersion"] = value["target_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateHarnessEndpointRequest:
    out: CreateHarnessEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("endpointName") is not None:
        out["endpoint_name"] = data["endpointName"]
    else:
        out["endpoint_name"] = ""
    if data.get("targetVersion") is not None:
        out["target_version"] = data["targetVersion"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
