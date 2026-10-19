"""Generated from Smithy shape ``com.amazonaws.quicksight#Permission``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.actions_list
    import capo_quicksight.types.permission_principal_string


class Permission(TypedDict, closed=True):
    actions: "capo_quicksight.types.actions_list.ActionsList"
    """<p>A list of actions that the principal can perform against the flow.</p> <p>The following are the list of values to set a principal as a flow owner:</p> <ul> <li> <p>quicksight:PublishFlow</p> </li> <li> <p>quicksight:GetFlow</p> </li> <li> <p>quicksight:UpdateFlowPermissions</p> </li> <li> <p>quicksight:GetFlowSession</p> </li> <li> <p>quicksight:StartFlowSession</p> </li> <li> <p>quicksight:StopFlowSession</p> </li> <li> <p>quicksight:UpdateFlowSession</p> </li> <li> <p>quicksight:UnpublishFlow</p> </li> <li> <p>quicksight:GetFlowStages</p> </li> <li> <p>quicksight:DeleteFlow</p> </li> <li> <p>quicksight:DescribeFlowPermissions</p> </li> <li> <p>quicksight:UpdateFlow</p> </li> <li> <p>quicksight:CreatePresignedUrl</p> </li> </ul> <p>The following are the list of values to set a principal as a flow viewer:</p> <ul> <li> <p>quicksight:GetFlow</p> </li> <li> <p>quicksight:UpdateFlowSession</p> </li> <li> <p>quicksight:StartFlowSession</p> </li> <li> <p>quicksight:StopFlowSession</p> </li> <li> <p>quicksight:GetFlowSession</p> </li> <li> <p>quicksight:CreatePresignedUrl</p> </li> <li> <p>quicksight:GetFlowStages</p> </li> </ul>"""
    principal: (
        "capo_quicksight.types.permission_principal_string.PermissionPrincipalString"
    )
    """<p>The Amazon Resource Name (ARN) of the principal. This can be an Amazon Quick user, group or namespace associated with the flow. Namespace principal can only be set as a viewer and will grant everyone in the same namespace viewer permissions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Permission) -> dict:
    out: dict = {}
    import capo_quicksight.types.actions_list

    out["Actions"] = capo_quicksight.types.actions_list.serialize_json(value["actions"])
    out["Principal"] = value["principal"]
    return out


def deserialize_json(data: dict) -> Permission:
    out: Permission = {}  # type: ignore[typeddict-item]
    if data.get("Actions") is not None:
        import capo_quicksight.types.actions_list

        out["actions"] = capo_quicksight.types.actions_list.deserialize_json(
            data["Actions"]
        )
    else:
        out["actions"] = []
    if data.get("Principal") is not None:
        out["principal"] = data["Principal"]
    else:
        out["principal"] = ""
    return out
