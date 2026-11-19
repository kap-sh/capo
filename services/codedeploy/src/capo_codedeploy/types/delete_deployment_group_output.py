"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeleteDeploymentGroupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.auto_scaling_group_list


class DeleteDeploymentGroupOutput(TypedDict, closed=True):
    hooks_not_cleaned_up: NotRequired[
        "capo_codedeploy.types.auto_scaling_group_list.AutoScalingGroupList"
    ]
    """<p>If the output contains no data, and the corresponding deployment group contained at least one Auto Scaling group, CodeDeploy successfully removed all corresponding Auto Scaling lifecycle event hooks from the Amazon EC2 instances in the Auto Scaling group. If the output contains data, CodeDeploy could not remove some Auto Scaling lifecycle event hooks from the Amazon EC2 instances in the Auto Scaling group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDeploymentGroupOutput) -> dict:
    out: dict = {}
    if "hooks_not_cleaned_up" in value:
        import capo_codedeploy.types.auto_scaling_group_list

        out["hooksNotCleanedUp"] = (
            capo_codedeploy.types.auto_scaling_group_list.serialize_aws_json_1_1(
                value["hooks_not_cleaned_up"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDeploymentGroupOutput:
    out: DeleteDeploymentGroupOutput = {}  # type: ignore[typeddict-item]
    if data.get("hooksNotCleanedUp") is not None:
        import capo_codedeploy.types.auto_scaling_group_list

        out["hooks_not_cleaned_up"] = (
            capo_codedeploy.types.auto_scaling_group_list.deserialize_aws_json_1_1(
                data["hooksNotCleanedUp"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteDeploymentGroupOutput) -> dict:
    out: dict = {}
    if "hooks_not_cleaned_up" in value:
        import capo_codedeploy.types.auto_scaling_group_list

        out["hooksNotCleanedUp"] = (
            capo_codedeploy.types.auto_scaling_group_list.serialize_cbor(
                value["hooks_not_cleaned_up"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DeleteDeploymentGroupOutput:
    out: DeleteDeploymentGroupOutput = {}  # type: ignore[typeddict-item]
    if data.get("hooksNotCleanedUp") is not None:
        import capo_codedeploy.types.auto_scaling_group_list

        out["hooks_not_cleaned_up"] = (
            capo_codedeploy.types.auto_scaling_group_list.deserialize_cbor(
                data["hooksNotCleanedUp"]
            )
        )
    return out
