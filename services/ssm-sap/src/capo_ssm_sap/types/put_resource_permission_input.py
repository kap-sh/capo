"""Generated from Smithy shape ``com.amazonaws.ssmsap#PutResourcePermissionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.arn
    import capo_ssm_sap.types.permission_action_type


class PutResourcePermissionInput(TypedDict, closed=True):
    action_type: "capo_ssm_sap.types.permission_action_type.PermissionActionType"
    """<p/>"""
    source_resource_arn: "capo_ssm_sap.types.arn.Arn"
    """<p/>"""
    resource_arn: "capo_ssm_sap.types.arn.Arn"
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePermissionInput) -> dict:
    out: dict = {}
    import capo_ssm_sap.types.permission_action_type

    out["ActionType"] = capo_ssm_sap.types.permission_action_type.serialize_json(
        value["action_type"]
    )
    out["SourceResourceArn"] = value["source_resource_arn"]
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> PutResourcePermissionInput:
    out: PutResourcePermissionInput = {}  # type: ignore[typeddict-item]
    if data.get("ActionType") is not None:
        import capo_ssm_sap.types.permission_action_type

        out["action_type"] = capo_ssm_sap.types.permission_action_type.deserialize_json(
            data["ActionType"]
        )
    else:
        import typing

        out["action_type"] = typing.cast(
            "capo_ssm_sap.types.permission_action_type.PermissionActionType", ""
        )
    if data.get("SourceResourceArn") is not None:
        out["source_resource_arn"] = data["SourceResourceArn"]
    else:
        out["source_resource_arn"] = ""
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out
