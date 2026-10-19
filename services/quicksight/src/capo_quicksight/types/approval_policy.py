"""Generated from Smithy shape ``com.amazonaws.quicksight#ApprovalPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.applicable_to
    import capo_quicksight.types.approval_group_list
    import capo_quicksight.types.arn
    import capo_quicksight.types.asset_type_list
    import capo_quicksight.types.governed_action_list
    import capo_quicksight.types.policy_description
    import capo_quicksight.types.policy_id
    import capo_quicksight.types.policy_name
    import capo_quicksight.types.timestamp


class ApprovalPolicy(TypedDict, closed=True):
    policy_id: "capo_quicksight.types.policy_id.PolicyId"
    """<p>The unique identifier of the approval policy.</p>"""
    policy_arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the approval policy.</p>"""
    name: "capo_quicksight.types.policy_name.PolicyName"
    """<p>The name of the approval policy.</p>"""
    description: NotRequired[
        "capo_quicksight.types.policy_description.PolicyDescription"
    ]
    """<p>A description of the approval policy.</p>"""
    actions: "capo_quicksight.types.governed_action_list.GovernedActionList"
    """<p>The list of governed actions that trigger the approval workflow.</p>"""
    asset_types: "capo_quicksight.types.asset_type_list.AssetTypeList"
    """<p>The list of asset types that the approval policy applies to.</p>"""
    applicable_to: "capo_quicksight.types.applicable_to.ApplicableTo"
    """<p>The scoping configuration that determines who the approval policy applies to.</p>"""
    approval_groups: "capo_quicksight.types.approval_group_list.ApprovalGroupList"
    """<p>The list of group ARNs whose members can approve requests.</p>"""
    created_at: "capo_quicksight.types.timestamp.Timestamp"
    """<p>The date and time that the approval policy was created.</p>"""
    updated_at: "capo_quicksight.types.timestamp.Timestamp"
    """<p>The date and time that the approval policy was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApprovalPolicy) -> dict:
    out: dict = {}
    out["PolicyId"] = value["policy_id"]
    out["PolicyArn"] = value["policy_arn"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_quicksight.types.governed_action_list

    out["Actions"] = capo_quicksight.types.governed_action_list.serialize_json(
        value["actions"]
    )
    import capo_quicksight.types.asset_type_list

    out["AssetTypes"] = capo_quicksight.types.asset_type_list.serialize_json(
        value["asset_types"]
    )
    import capo_quicksight.types.applicable_to

    out["ApplicableTo"] = capo_quicksight.types.applicable_to.serialize_json(
        value["applicable_to"]
    )
    import capo_quicksight.types.approval_group_list

    out["ApprovalGroups"] = capo_quicksight.types.approval_group_list.serialize_json(
        value["approval_groups"]
    )
    import capo_quicksight.types.timestamp

    out["CreatedAt"] = capo_quicksight.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_quicksight.types.timestamp

    out["UpdatedAt"] = capo_quicksight.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> ApprovalPolicy:
    out: ApprovalPolicy = {}  # type: ignore[typeddict-item]
    if data.get("PolicyId") is not None:
        out["policy_id"] = data["PolicyId"]
    else:
        out["policy_id"] = ""
    if data.get("PolicyArn") is not None:
        out["policy_arn"] = data["PolicyArn"]
    else:
        out["policy_arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Actions") is not None:
        import capo_quicksight.types.governed_action_list

        out["actions"] = capo_quicksight.types.governed_action_list.deserialize_json(
            data["Actions"]
        )
    else:
        out["actions"] = []
    if data.get("AssetTypes") is not None:
        import capo_quicksight.types.asset_type_list

        out["asset_types"] = capo_quicksight.types.asset_type_list.deserialize_json(
            data["AssetTypes"]
        )
    else:
        out["asset_types"] = []
    if data.get("ApplicableTo") is not None:
        import capo_quicksight.types.applicable_to

        out["applicable_to"] = capo_quicksight.types.applicable_to.deserialize_json(
            data["ApplicableTo"]
        )
    else:
        raise DeserializationError("ApprovalPolicy.applicable_to required")
    if data.get("ApprovalGroups") is not None:
        import capo_quicksight.types.approval_group_list

        out["approval_groups"] = (
            capo_quicksight.types.approval_group_list.deserialize_json(
                data["ApprovalGroups"]
            )
        )
    else:
        out["approval_groups"] = []
    if data.get("CreatedAt") is not None:
        import capo_quicksight.types.timestamp

        out["created_at"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("UpdatedAt") is not None:
        import capo_quicksight.types.timestamp

        out["updated_at"] = capo_quicksight.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
