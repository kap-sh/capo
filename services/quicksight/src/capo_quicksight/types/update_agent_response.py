"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateAgentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.agent_arn
    import capo_quicksight.types.agent_id
    import capo_quicksight.types.agent_status
    import capo_quicksight.types.failed_to_update_association_list


class UpdateAgentResponse(TypedDict, closed=True):
    arn: "capo_quicksight.types.agent_arn.AgentArn"
    """<p>The Amazon Resource Name (ARN) of the agent.</p>"""
    agent_id: "capo_quicksight.types.agent_id.AgentId"
    """<p>The unique identifier for the agent.</p>"""
    agent_status: "capo_quicksight.types.agent_status.AgentStatus"
    """<p>The status of the agent.</p>"""
    failed_to_add_spaces: NotRequired[
        "capo_quicksight.types.failed_to_update_association_list.FailedToUpdateAssociationList"
    ]
    """<p>A list of per-ARN failures from the spaces that were requested to be added.</p>"""
    failed_to_remove_spaces: NotRequired[
        "capo_quicksight.types.failed_to_update_association_list.FailedToUpdateAssociationList"
    ]
    """<p>A list of per-ARN failures from the spaces that were requested to be removed.</p>"""
    failed_to_add_action_connectors: NotRequired[
        "capo_quicksight.types.failed_to_update_association_list.FailedToUpdateAssociationList"
    ]
    """<p>A list of per-ARN failures from the action connectors that were requested to be added.</p>"""
    failed_to_remove_action_connectors: NotRequired[
        "capo_quicksight.types.failed_to_update_association_list.FailedToUpdateAssociationList"
    ]
    """<p>A list of per-ARN failures from the action connectors that were requested to be removed.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentResponse) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["AgentId"] = value["agent_id"]
    import capo_quicksight.types.agent_status

    out["AgentStatus"] = capo_quicksight.types.agent_status.serialize_json(
        value["agent_status"]
    )
    if "failed_to_add_spaces" in value:
        import capo_quicksight.types.failed_to_update_association_list

        out["FailedToAddSpaces"] = (
            capo_quicksight.types.failed_to_update_association_list.serialize_json(
                value["failed_to_add_spaces"]
            )
        )
    if "failed_to_remove_spaces" in value:
        import capo_quicksight.types.failed_to_update_association_list

        out["FailedToRemoveSpaces"] = (
            capo_quicksight.types.failed_to_update_association_list.serialize_json(
                value["failed_to_remove_spaces"]
            )
        )
    if "failed_to_add_action_connectors" in value:
        import capo_quicksight.types.failed_to_update_association_list

        out["FailedToAddActionConnectors"] = (
            capo_quicksight.types.failed_to_update_association_list.serialize_json(
                value["failed_to_add_action_connectors"]
            )
        )
    if "failed_to_remove_action_connectors" in value:
        import capo_quicksight.types.failed_to_update_association_list

        out["FailedToRemoveActionConnectors"] = (
            capo_quicksight.types.failed_to_update_association_list.serialize_json(
                value["failed_to_remove_action_connectors"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateAgentResponse:
    out: UpdateAgentResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("AgentId") is not None:
        out["agent_id"] = data["AgentId"]
    else:
        out["agent_id"] = ""
    if data.get("AgentStatus") is not None:
        import capo_quicksight.types.agent_status

        out["agent_status"] = capo_quicksight.types.agent_status.deserialize_json(
            data["AgentStatus"]
        )
    else:
        import typing

        out["agent_status"] = typing.cast(
            "capo_quicksight.types.agent_status.AgentStatus", ""
        )
    if data.get("FailedToAddSpaces") is not None:
        import capo_quicksight.types.failed_to_update_association_list

        out["failed_to_add_spaces"] = (
            capo_quicksight.types.failed_to_update_association_list.deserialize_json(
                data["FailedToAddSpaces"]
            )
        )
    if data.get("FailedToRemoveSpaces") is not None:
        import capo_quicksight.types.failed_to_update_association_list

        out["failed_to_remove_spaces"] = (
            capo_quicksight.types.failed_to_update_association_list.deserialize_json(
                data["FailedToRemoveSpaces"]
            )
        )
    if data.get("FailedToAddActionConnectors") is not None:
        import capo_quicksight.types.failed_to_update_association_list

        out["failed_to_add_action_connectors"] = (
            capo_quicksight.types.failed_to_update_association_list.deserialize_json(
                data["FailedToAddActionConnectors"]
            )
        )
    if data.get("FailedToRemoveActionConnectors") is not None:
        import capo_quicksight.types.failed_to_update_association_list

        out["failed_to_remove_action_connectors"] = (
            capo_quicksight.types.failed_to_update_association_list.deserialize_json(
                data["FailedToRemoveActionConnectors"]
            )
        )
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out
