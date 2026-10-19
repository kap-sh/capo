"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#AbbreviatedPlan``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_arc_region_switch.types.account_id
    import capo_arc_region_switch.types.execution_id
    import capo_arc_region_switch.types.plan_arn
    import capo_arc_region_switch.types.plan_name
    import capo_arc_region_switch.types.recovery_approach
    import capo_arc_region_switch.types.region
    import capo_arc_region_switch.types.region_list


class AbbreviatedPlan(TypedDict, closed=True):
    arn: "capo_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the Region switch plan.</p>"""
    owner: "capo_arc_region_switch.types.account_id.AccountId"
    """<p>The owner of a Region switch plan.</p>"""
    name: "capo_arc_region_switch.types.plan_name.PlanName"
    """<p>The name of a Region switch plan.</p>"""
    regions: "capo_arc_region_switch.types.region_list.RegionList"
    """<p>The Amazon Web Services Region specified for a Region switch plan.</p>"""
    recovery_approach: "capo_arc_region_switch.types.recovery_approach.RecoveryApproach"
    """<p>The recovery approach for a Region switch plan, which can be active/active (activeActive) or active/passive (activePassive).</p>"""
    primary_region: NotRequired["capo_arc_region_switch.types.region.Region"]
    """<p>The primary Region for a plan.</p>"""
    version: NotRequired["str"]
    """<p>The version for the plan.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the plan execution was last updated.</p>"""
    description: NotRequired["str"]
    """<p>The description of a Region switch plan.</p>"""
    execution_role: NotRequired["str"]
    """<p>The execution role is a way to categorize a Region switch plan. </p>"""
    active_plan_execution: NotRequired[
        "capo_arc_region_switch.types.execution_id.ExecutionId"
    ]
    """<p>Specifies if this is the active plan execution at this time.</p>"""
    recovery_time_objective_minutes: NotRequired["int"]
    """<p>The recovery time objective that you've specified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AbbreviatedPlan) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["owner"] = value["owner"]
    out["name"] = value["name"]
    import capo_arc_region_switch.types.region_list

    out["regions"] = capo_arc_region_switch.types.region_list.serialize_aws_json_1_0(
        value["regions"]
    )
    import capo_arc_region_switch.types.recovery_approach

    out["recoveryApproach"] = (
        capo_arc_region_switch.types.recovery_approach.serialize_aws_json_1_0(
            value["recovery_approach"]
        )
    )
    if "primary_region" in value:
        out["primaryRegion"] = value["primary_region"]
    if "version" in value:
        out["version"] = value["version"]
    if "updated_at" in value:
        import capo_arc_region_switch.types._prelude.timestamp

        out["updatedAt"] = (
            capo_arc_region_switch.types._prelude.timestamp.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "execution_role" in value:
        out["executionRole"] = value["execution_role"]
    if "active_plan_execution" in value:
        out["activePlanExecution"] = value["active_plan_execution"]
    if "recovery_time_objective_minutes" in value:
        out["recoveryTimeObjectiveMinutes"] = value["recovery_time_objective_minutes"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AbbreviatedPlan:
    out: AbbreviatedPlan = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("owner") is not None:
        out["owner"] = data["owner"]
    else:
        out["owner"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("regions") is not None:
        import capo_arc_region_switch.types.region_list

        out["regions"] = (
            capo_arc_region_switch.types.region_list.deserialize_aws_json_1_0(
                data["regions"]
            )
        )
    else:
        out["regions"] = []
    if data.get("recoveryApproach") is not None:
        import capo_arc_region_switch.types.recovery_approach

        out["recovery_approach"] = (
            capo_arc_region_switch.types.recovery_approach.deserialize_aws_json_1_0(
                data["recoveryApproach"]
            )
        )
    else:
        import typing

        out["recovery_approach"] = typing.cast(
            "capo_arc_region_switch.types.recovery_approach.RecoveryApproach", ""
        )
    if data.get("primaryRegion") is not None:
        out["primary_region"] = data["primaryRegion"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("updatedAt") is not None:
        import capo_arc_region_switch.types._prelude.timestamp

        out["updated_at"] = (
            capo_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("executionRole") is not None:
        out["execution_role"] = data["executionRole"]
    if data.get("activePlanExecution") is not None:
        out["active_plan_execution"] = data["activePlanExecution"]
    if data.get("recoveryTimeObjectiveMinutes") is not None:
        out["recovery_time_objective_minutes"] = data["recoveryTimeObjectiveMinutes"]
    return out
