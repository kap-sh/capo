"""Generated from Smithy shape ``com.amazonaws.connect#AssociateWorkspaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.workspace_id
    import capo_connect.types.workspace_resource_arn_list


class AssociateWorkspaceRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Amazon Connect instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    workspace_id: "capo_connect.types.workspace_id.WorkspaceId"
    """<p>The identifier of the workspace.</p>"""
    resource_arns: (
        "capo_connect.types.workspace_resource_arn_list.WorkspaceResourceArnList"
    )
    """<p>The Amazon Resource Names (ARNs) of the resources to associate with the workspace. Valid resource types are users and routing profiles.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateWorkspaceRequest) -> dict:
    out: dict = {}
    import capo_connect.types.workspace_resource_arn_list

    out["ResourceArns"] = capo_connect.types.workspace_resource_arn_list.serialize_json(
        value["resource_arns"]
    )
    return out


def deserialize_json(data: dict) -> AssociateWorkspaceRequest:
    out: AssociateWorkspaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArns") is not None:
        import capo_connect.types.workspace_resource_arn_list

        out["resource_arns"] = (
            capo_connect.types.workspace_resource_arn_list.deserialize_json(
                data["ResourceArns"]
            )
        )
    else:
        raise DeserializationError("AssociateWorkspaceRequest.resource_arns required")
    return out
