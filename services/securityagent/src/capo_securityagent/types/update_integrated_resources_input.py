"""Generated from Smithy shape ``com.amazonaws.securityagent#UpdateIntegratedResourcesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.agent_space_id
    import capo_securityagent.types.integrated_resource_input_item_list
    import capo_securityagent.types.integration_id


class UpdateIntegratedResourcesInput(TypedDict, closed=True):
    agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the agent space.</p>"""
    integration_id: "capo_securityagent.types.integration_id.IntegrationId"
    """<p>The unique identifier of the integration.</p>"""
    items: "capo_securityagent.types.integrated_resource_input_item_list.IntegratedResourceInputItemList"
    """<p>The list of integrated resource items to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIntegratedResourcesInput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    out["integrationId"] = value["integration_id"]
    import capo_securityagent.types.integrated_resource_input_item_list

    out["items"] = (
        capo_securityagent.types.integrated_resource_input_item_list.serialize_json(
            value["items"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateIntegratedResourcesInput:
    out: UpdateIntegratedResourcesInput = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("integrationId") is not None:
        out["integration_id"] = data["integrationId"]
    else:
        out["integration_id"] = ""
    if data.get("items") is not None:
        import capo_securityagent.types.integrated_resource_input_item_list

        out["items"] = (
            capo_securityagent.types.integrated_resource_input_item_list.deserialize_json(
                data["items"]
            )
        )
    else:
        out["items"] = []
    return out
