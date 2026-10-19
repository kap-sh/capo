"""Generated from Smithy shape ``com.amazonaws.ssmsap#DeleteResourcePermissionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.arn
    import capo_ssm_sap.types.permission_action_type


class DeleteResourcePermissionInput(TypedDict, closed=True):
    action_type: NotRequired[
        "capo_ssm_sap.types.permission_action_type.PermissionActionType"
    ]
    """<p>Delete or restore the permissions on the target database.</p>"""
    source_resource_arn: NotRequired["capo_ssm_sap.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the source resource.</p>"""
    resource_arn: "capo_ssm_sap.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourcePermissionInput) -> dict:
    out: dict = {}
    if "action_type" in value:
        import capo_ssm_sap.types.permission_action_type

        out["ActionType"] = capo_ssm_sap.types.permission_action_type.serialize_json(
            value["action_type"]
        )
    if "source_resource_arn" in value:
        out["SourceResourceArn"] = value["source_resource_arn"]
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> DeleteResourcePermissionInput:
    out: DeleteResourcePermissionInput = {}  # type: ignore[typeddict-item]
    if data.get("ActionType") is not None:
        import capo_ssm_sap.types.permission_action_type

        out["action_type"] = capo_ssm_sap.types.permission_action_type.deserialize_json(
            data["ActionType"]
        )
    if data.get("SourceResourceArn") is not None:
        out["source_resource_arn"] = data["SourceResourceArn"]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out
