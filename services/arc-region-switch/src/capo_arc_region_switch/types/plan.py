"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Plan``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_arc_region_switch.types.account_id
    import capo_arc_region_switch.types.associated_alarm_map
    import capo_arc_region_switch.types.iam_role_arn
    import capo_arc_region_switch.types.plan_arn
    import capo_arc_region_switch.types.plan_name
    import capo_arc_region_switch.types.recovery_approach
    import capo_arc_region_switch.types.region
    import capo_arc_region_switch.types.region_list
    import capo_arc_region_switch.types.report_configuration
    import capo_arc_region_switch.types.trigger_list
    import capo_arc_region_switch.types.workflow_list


class Plan(TypedDict, closed=True):
    arn: "capo_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the plan.</p>"""
    description: NotRequired["str"]
    """<p>The description for a plan.</p>"""
    workflows: "capo_arc_region_switch.types.workflow_list.WorkflowList"
    """<p>The workflows for a plan.</p>"""
    execution_role: "capo_arc_region_switch.types.iam_role_arn.IamRoleArn"
    """<p>The execution role for a plan.</p>"""
    recovery_time_objective_minutes: NotRequired["int"]
    """<p>The recovery time objective for a plan.</p>"""
    associated_alarms: NotRequired[
        "capo_arc_region_switch.types.associated_alarm_map.AssociatedAlarmMap"
    ]
    """<p>The associated application health alarms for a plan.</p>"""
    triggers: NotRequired["capo_arc_region_switch.types.trigger_list.TriggerList"]
    """<p>The triggers for a plan.</p>"""
    report_configuration: NotRequired[
        "capo_arc_region_switch.types.report_configuration.ReportConfiguration"
    ]
    """<p>The report configuration for a plan.</p>"""
    service_quota_checks_enabled: NotRequired["bool"]
    """<p>Indicates whether service quota checks are enabled for the Region switch plan. When enabled, Region switch compares the applied service quota values across the plan's Amazon Web Services Regions and creates a warning when a quota in one Region is lower than the value required for the matching resource in another Region. Service quota checks are advisory and don't prevent you from creating, evaluating, or executing a plan.</p>"""
    name: "capo_arc_region_switch.types.plan_name.PlanName"
    """<p>The name for a plan.</p>"""
    regions: "capo_arc_region_switch.types.region_list.RegionList"
    """<p>The Amazon Web Services Regions for a plan.</p>"""
    recovery_approach: "capo_arc_region_switch.types.recovery_approach.RecoveryApproach"
    """<p>The recovery approach for a Region switch plan, which can be active/active (activeActive) or active/passive (activePassive).</p>"""
    primary_region: NotRequired["capo_arc_region_switch.types.region.Region"]
    """<p>The primary Region for a plan.</p>"""
    owner: "capo_arc_region_switch.types.account_id.AccountId"
    """<p>The owner of a plan.</p>"""
    version: NotRequired["str"]
    """<p>The version for the plan.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the plan was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Plan) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_arc_region_switch.types.workflow_list

    out["workflows"] = (
        capo_arc_region_switch.types.workflow_list.serialize_aws_json_1_0(
            value["workflows"]
        )
    )
    out["executionRole"] = value["execution_role"]
    if "recovery_time_objective_minutes" in value:
        out["recoveryTimeObjectiveMinutes"] = value["recovery_time_objective_minutes"]
    if "associated_alarms" in value:
        import capo_arc_region_switch.types.associated_alarm_map

        out["associatedAlarms"] = (
            capo_arc_region_switch.types.associated_alarm_map.serialize_aws_json_1_0(
                value["associated_alarms"]
            )
        )
    if "triggers" in value:
        import capo_arc_region_switch.types.trigger_list

        out["triggers"] = (
            capo_arc_region_switch.types.trigger_list.serialize_aws_json_1_0(
                value["triggers"]
            )
        )
    if "report_configuration" in value:
        import capo_arc_region_switch.types.report_configuration

        out["reportConfiguration"] = (
            capo_arc_region_switch.types.report_configuration.serialize_aws_json_1_0(
                value["report_configuration"]
            )
        )
    if "service_quota_checks_enabled" in value:
        out["serviceQuotaChecksEnabled"] = value["service_quota_checks_enabled"]
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
    out["owner"] = value["owner"]
    if "version" in value:
        out["version"] = value["version"]
    if "updated_at" in value:
        import capo_arc_region_switch.types._prelude.timestamp

        out["updatedAt"] = (
            capo_arc_region_switch.types._prelude.timestamp.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Plan:
    out: Plan = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Plan.arn required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("workflows") is not None:
        import capo_arc_region_switch.types.workflow_list

        out["workflows"] = (
            capo_arc_region_switch.types.workflow_list.deserialize_aws_json_1_0(
                data["workflows"]
            )
        )
    else:
        raise DeserializationError("Plan.workflows required")
    if data.get("executionRole") is not None:
        out["execution_role"] = data["executionRole"]
    else:
        raise DeserializationError("Plan.execution_role required")
    if data.get("recoveryTimeObjectiveMinutes") is not None:
        out["recovery_time_objective_minutes"] = data["recoveryTimeObjectiveMinutes"]
    if data.get("associatedAlarms") is not None:
        import capo_arc_region_switch.types.associated_alarm_map

        out["associated_alarms"] = (
            capo_arc_region_switch.types.associated_alarm_map.deserialize_aws_json_1_0(
                data["associatedAlarms"]
            )
        )
    if data.get("triggers") is not None:
        import capo_arc_region_switch.types.trigger_list

        out["triggers"] = (
            capo_arc_region_switch.types.trigger_list.deserialize_aws_json_1_0(
                data["triggers"]
            )
        )
    if data.get("reportConfiguration") is not None:
        import capo_arc_region_switch.types.report_configuration

        out["report_configuration"] = (
            capo_arc_region_switch.types.report_configuration.deserialize_aws_json_1_0(
                data["reportConfiguration"]
            )
        )
    if data.get("serviceQuotaChecksEnabled") is not None:
        out["service_quota_checks_enabled"] = data["serviceQuotaChecksEnabled"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Plan.name required")
    if data.get("regions") is not None:
        import capo_arc_region_switch.types.region_list

        out["regions"] = (
            capo_arc_region_switch.types.region_list.deserialize_aws_json_1_0(
                data["regions"]
            )
        )
    else:
        raise DeserializationError("Plan.regions required")
    if data.get("recoveryApproach") is not None:
        import capo_arc_region_switch.types.recovery_approach

        out["recovery_approach"] = (
            capo_arc_region_switch.types.recovery_approach.deserialize_aws_json_1_0(
                data["recoveryApproach"]
            )
        )
    else:
        raise DeserializationError("Plan.recovery_approach required")
    if data.get("primaryRegion") is not None:
        out["primary_region"] = data["primaryRegion"]
    if data.get("owner") is not None:
        out["owner"] = data["owner"]
    else:
        raise DeserializationError("Plan.owner required")
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("updatedAt") is not None:
        import capo_arc_region_switch.types._prelude.timestamp

        out["updated_at"] = (
            capo_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    return out
