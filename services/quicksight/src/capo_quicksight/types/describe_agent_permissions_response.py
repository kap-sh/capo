"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAgentPermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.agent_arn
    import capo_quicksight.types.agent_id
    import capo_quicksight.types.resource_permission_list


class DescribeAgentPermissionsResponse(TypedDict, closed=True):
    arn: "capo_quicksight.types.agent_arn.AgentArn"
    """<p>The Amazon Resource Name (ARN) of the agent.</p>"""
    agent_id: "capo_quicksight.types.agent_id.AgentId"
    """<p>The unique identifier for the agent.</p>"""
    permissions: "capo_quicksight.types.resource_permission_list.ResourcePermissionList"
    """<p>The resource permissions for the agent.</p>"""
    request_id: "str"
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAgentPermissionsResponse) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["AgentId"] = value["agent_id"]
    import capo_quicksight.types.resource_permission_list

    out["Permissions"] = capo_quicksight.types.resource_permission_list.serialize_json(
        value["permissions"]
    )
    out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeAgentPermissionsResponse:
    out: DescribeAgentPermissionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("AgentId") is not None:
        out["agent_id"] = data["AgentId"]
    else:
        out["agent_id"] = ""
    if data.get("Permissions") is not None:
        import capo_quicksight.types.resource_permission_list

        out["permissions"] = (
            capo_quicksight.types.resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    else:
        out["permissions"] = []
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    else:
        out["request_id"] = ""
    return out
