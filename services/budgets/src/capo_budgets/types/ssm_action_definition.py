"""Generated from Smithy shape ``com.amazonaws.budgets#SsmActionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_budgets.types.action_sub_type
    import capo_budgets.types.instance_ids
    import capo_budgets.types.region


class SsmActionDefinition(TypedDict, closed=True):
    action_sub_type: "capo_budgets.types.action_sub_type.ActionSubType"
    """<p>The action subType. </p>"""
    region: "capo_budgets.types.region.Region"
    """<p>The Region to run the SSM document. </p>"""
    instance_ids: "capo_budgets.types.instance_ids.InstanceIds"
    """<p>The EC2 and RDS instance IDs. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SsmActionDefinition) -> dict:
    out: dict = {}
    import capo_budgets.types.action_sub_type

    out["ActionSubType"] = capo_budgets.types.action_sub_type.serialize_aws_json_1_1(
        value["action_sub_type"]
    )
    out["Region"] = value["region"]
    import capo_budgets.types.instance_ids

    out["InstanceIds"] = capo_budgets.types.instance_ids.serialize_aws_json_1_1(
        value["instance_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SsmActionDefinition:
    out: SsmActionDefinition = {}  # type: ignore[typeddict-item]
    if data.get("ActionSubType") is not None:
        import capo_budgets.types.action_sub_type

        out["action_sub_type"] = (
            capo_budgets.types.action_sub_type.deserialize_aws_json_1_1(
                data["ActionSubType"]
            )
        )
    else:
        import typing

        out["action_sub_type"] = typing.cast(
            "capo_budgets.types.action_sub_type.ActionSubType", ""
        )
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    else:
        out["region"] = ""
    if data.get("InstanceIds") is not None:
        import capo_budgets.types.instance_ids

        out["instance_ids"] = capo_budgets.types.instance_ids.deserialize_aws_json_1_1(
            data["InstanceIds"]
        )
    else:
        out["instance_ids"] = []
    return out
