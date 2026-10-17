"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#CreatePlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_arc_region_switch.types.associated_alarm_map
    import capo_arc_region_switch.types.iam_role_arn
    import capo_arc_region_switch.types.plan_name
    import capo_arc_region_switch.types.recovery_approach
    import capo_arc_region_switch.types.region
    import capo_arc_region_switch.types.region_list
    import capo_arc_region_switch.types.report_configuration
    import capo_arc_region_switch.types.tags
    import capo_arc_region_switch.types.trigger_list
    import capo_arc_region_switch.types.workflow_list


class CreatePlanRequest(TypedDict, closed=True):
    description: NotRequired["str"]
    """<p>The description of a Region switch plan.</p>"""
    workflows: "capo_arc_region_switch.types.workflow_list.WorkflowList"
    """<p>An array of workflows included in a Region switch plan.</p>"""
    execution_role: "capo_arc_region_switch.types.iam_role_arn.IamRoleArn"
    """<p>An execution role is a way to categorize a Region switch plan.</p>"""
    recovery_time_objective_minutes: NotRequired["int"]
    """<p>Optionally, you can specify an recovery time objective for a Region switch plan, in minutes.</p>"""
    associated_alarms: NotRequired[
        "capo_arc_region_switch.types.associated_alarm_map.AssociatedAlarmMap"
    ]
    """<p>The alarms associated with a Region switch plan.</p>"""
    triggers: NotRequired["capo_arc_region_switch.types.trigger_list.TriggerList"]
    """<p>The triggers associated with a Region switch plan.</p>"""
    report_configuration: NotRequired[
        "capo_arc_region_switch.types.report_configuration.ReportConfiguration"
    ]
    service_quota_checks_enabled: NotRequired["bool"]
    """<p>Specifies whether to enable service quota checks for the Region switch plan.</p>"""
    name: "capo_arc_region_switch.types.plan_name.PlanName"
    """<p>The name of a Region switch plan.</p>"""
    regions: "capo_arc_region_switch.types.region_list.RegionList"
    """<p>An array that specifies the Amazon Web Services Regions for a Region switch plan. Specify two Regions.</p>"""
    recovery_approach: "capo_arc_region_switch.types.recovery_approach.RecoveryApproach"
    """<p>The recovery approach for a Region switch plan, which can be active/active (activeActive) or active/passive (activePassive).</p>"""
    primary_region: NotRequired["capo_arc_region_switch.types.region.Region"]
    """<p>The primary Amazon Web Services Region for the application. This is the Region where the application normally runs before any Region switch occurs.</p>"""
    tags: NotRequired["capo_arc_region_switch.types.tags.Tags"]
    """<p>The tags to apply to the Region switch plan.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreatePlanRequest) -> dict:
    out: dict = {}
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
    if "tags" in value:
        import capo_arc_region_switch.types.tags

        out["tags"] = capo_arc_region_switch.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreatePlanRequest:
    out: CreatePlanRequest = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("CreatePlanRequest.workflows required")
    if data.get("executionRole") is not None:
        out["execution_role"] = data["executionRole"]
    else:
        raise DeserializationError("CreatePlanRequest.execution_role required")
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
        raise DeserializationError("CreatePlanRequest.name required")
    if data.get("regions") is not None:
        import capo_arc_region_switch.types.region_list

        out["regions"] = (
            capo_arc_region_switch.types.region_list.deserialize_aws_json_1_0(
                data["regions"]
            )
        )
    else:
        raise DeserializationError("CreatePlanRequest.regions required")
    if data.get("recoveryApproach") is not None:
        import capo_arc_region_switch.types.recovery_approach

        out["recovery_approach"] = (
            capo_arc_region_switch.types.recovery_approach.deserialize_aws_json_1_0(
                data["recoveryApproach"]
            )
        )
    else:
        raise DeserializationError("CreatePlanRequest.recovery_approach required")
    if data.get("primaryRegion") is not None:
        out["primary_region"] = data["primaryRegion"]
    if data.get("tags") is not None:
        import capo_arc_region_switch.types.tags

        out["tags"] = capo_arc_region_switch.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
