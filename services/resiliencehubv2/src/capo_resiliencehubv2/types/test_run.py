"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRun``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.account_targeting
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.experiment_details_list
    import capo_resiliencehubv2.types.iam_role_name
    import capo_resiliencehubv2.types.logging_configuration
    import capo_resiliencehubv2.types.permission_model
    import capo_resiliencehubv2.types.region_list
    import capo_resiliencehubv2.types.region_switch_execution_id
    import capo_resiliencehubv2.types.report_generation_result
    import capo_resiliencehubv2.types.service_owned_arn
    import capo_resiliencehubv2.types.stop_condition_list
    import capo_resiliencehubv2.types.test_id
    import capo_resiliencehubv2.types.test_parameters
    import capo_resiliencehubv2.types.test_run_id
    import capo_resiliencehubv2.types.test_run_policy_snapshot
    import capo_resiliencehubv2.types.test_run_report_configuration
    import capo_resiliencehubv2.types.test_run_status


class TestRun(TypedDict, closed=True):
    test_run_id: "capo_resiliencehubv2.types.test_run_id.TestRunId"
    """<p>The unique identifier of the test run.</p>"""
    test_id: "capo_resiliencehubv2.types.test_id.TestId"
    """<p>The identifier of the test that was run.</p>"""
    status: "capo_resiliencehubv2.types.test_run_status.TestRunStatus"
    """<p>The current status of the test run.</p>"""
    service_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    """<p>The ARN of the service the test run belongs to.</p>"""
    started_at: "datetime.datetime"
    """<p>The timestamp when the test run started.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the test run ended.</p>"""
    experiments: NotRequired[
        "capo_resiliencehubv2.types.experiment_details_list.ExperimentDetailsList"
    ]
    """<p>The AWS Fault Injection Service (AWS FIS) experiments run as part of the test run.</p>"""
    event_count: NotRequired["int"]
    """<p>The number of events recorded for the test run. Use ListTestRunEvents to retrieve the details.</p>"""
    parameters: NotRequired["capo_resiliencehubv2.types.test_parameters.TestParameters"]
    """<p>The parameter values used for the test run.</p>"""
    error_message: NotRequired["str"]
    """<p>A human-readable reason for test run failure. Only present when the status is FAILED or ERROR.</p>"""
    stop_conditions: NotRequired[
        "capo_resiliencehubv2.types.stop_condition_list.StopConditionList"
    ]
    """<p>The stop conditions snapshotted from the test when the run was started.</p>"""
    logging_configuration: NotRequired[
        "capo_resiliencehubv2.types.logging_configuration.LoggingConfiguration"
    ]
    """<p>The logging configuration snapshotted from the test when the run was started.</p>"""
    role_name: NotRequired["capo_resiliencehubv2.types.iam_role_name.IamRoleName"]
    """<p>The IAM execution role name snapshotted from the test when the run was started.</p>"""
    test_template_arn: "capo_resiliencehubv2.types.service_owned_arn.ServiceOwnedArn"
    """<p>The ARN of the test template snapshotted from the test when the run was started.</p>"""
    report_configuration: NotRequired[
        "capo_resiliencehubv2.types.test_run_report_configuration.TestRunReportConfiguration"
    ]
    """<p>The report configuration snapshotted from the service when the run was started.</p>"""
    policy: NotRequired[
        "capo_resiliencehubv2.types.test_run_policy_snapshot.TestRunPolicySnapshot"
    ]
    """<p>The resilience policy snapshotted from the service when the run was started.</p>"""
    report_output: NotRequired[
        "capo_resiliencehubv2.types.report_generation_result.ReportGenerationResult"
    ]
    """<p>The report generation result for the test run. Present after report generation completes or fails.</p>"""
    region_switch_plan_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    """<p>The ARN of the ARC Region switch plan associated with the test run.</p>"""
    region_switch_execution_id: NotRequired[
        "capo_resiliencehubv2.types.region_switch_execution_id.RegionSwitchExecutionId"
    ]
    """<p>The identifier of the ARC Region switch execution detected during the test run.</p>"""
    permission_model: NotRequired[
        "capo_resiliencehubv2.types.permission_model.PermissionModel"
    ]
    """<p>The permission model snapshotted from the service when the run was started.</p>"""
    regions: NotRequired["capo_resiliencehubv2.types.region_list.RegionList"]
    """<p>The Regions snapshotted from the service when the run was started.</p>"""
    account_targeting: NotRequired[
        "capo_resiliencehubv2.types.account_targeting.AccountTargeting"
    ]
    """<p>Indicates whether the test run targets resources in a single AWS account or across multiple accounts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestRun) -> dict:
    out: dict = {}
    out["testRunId"] = value["test_run_id"]
    out["testId"] = value["test_id"]
    import capo_resiliencehubv2.types.test_run_status

    out["status"] = capo_resiliencehubv2.types.test_run_status.serialize_json(
        value["status"]
    )
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    import capo_resiliencehubv2.types._prelude.timestamp

    out["startedAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
        value["started_at"]
    )
    if "ended_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["endedAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["ended_at"]
        )
    if "experiments" in value:
        import capo_resiliencehubv2.types.experiment_details_list

        out["experiments"] = (
            capo_resiliencehubv2.types.experiment_details_list.serialize_json(
                value["experiments"]
            )
        )
    if "event_count" in value:
        out["eventCount"] = value["event_count"]
    if "parameters" in value:
        import capo_resiliencehubv2.types.test_parameters

        out["parameters"] = capo_resiliencehubv2.types.test_parameters.serialize_json(
            value["parameters"]
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "stop_conditions" in value:
        import capo_resiliencehubv2.types.stop_condition_list

        out["stopConditions"] = (
            capo_resiliencehubv2.types.stop_condition_list.serialize_json(
                value["stop_conditions"]
            )
        )
    if "logging_configuration" in value:
        import capo_resiliencehubv2.types.logging_configuration

        out["loggingConfiguration"] = (
            capo_resiliencehubv2.types.logging_configuration.serialize_json(
                value["logging_configuration"]
            )
        )
    if "role_name" in value:
        out["roleName"] = value["role_name"]
    out["testTemplateArn"] = value["test_template_arn"]
    if "report_configuration" in value:
        import capo_resiliencehubv2.types.test_run_report_configuration

        out["reportConfiguration"] = (
            capo_resiliencehubv2.types.test_run_report_configuration.serialize_json(
                value["report_configuration"]
            )
        )
    if "policy" in value:
        import capo_resiliencehubv2.types.test_run_policy_snapshot

        out["policy"] = (
            capo_resiliencehubv2.types.test_run_policy_snapshot.serialize_json(
                value["policy"]
            )
        )
    if "report_output" in value:
        import capo_resiliencehubv2.types.report_generation_result

        out["reportOutput"] = (
            capo_resiliencehubv2.types.report_generation_result.serialize_json(
                value["report_output"]
            )
        )
    if "region_switch_plan_arn" in value:
        out["regionSwitchPlanArn"] = value["region_switch_plan_arn"]
    if "region_switch_execution_id" in value:
        out["regionSwitchExecutionId"] = value["region_switch_execution_id"]
    if "permission_model" in value:
        import capo_resiliencehubv2.types.permission_model

        out["permissionModel"] = (
            capo_resiliencehubv2.types.permission_model.serialize_json(
                value["permission_model"]
            )
        )
    if "regions" in value:
        import capo_resiliencehubv2.types.region_list

        out["regions"] = capo_resiliencehubv2.types.region_list.serialize_json(
            value["regions"]
        )
    if "account_targeting" in value:
        import capo_resiliencehubv2.types.account_targeting

        out["accountTargeting"] = (
            capo_resiliencehubv2.types.account_targeting.serialize_json(
                value["account_targeting"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestRun:
    out: TestRun = {}  # type: ignore[typeddict-item]
    if data.get("testRunId") is not None:
        out["test_run_id"] = data["testRunId"]
    else:
        raise DeserializationError("TestRun.test_run_id required")
    if data.get("testId") is not None:
        out["test_id"] = data["testId"]
    else:
        raise DeserializationError("TestRun.test_id required")
    if data.get("status") is not None:
        import capo_resiliencehubv2.types.test_run_status

        out["status"] = capo_resiliencehubv2.types.test_run_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("TestRun.status required")
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    if data.get("startedAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["started_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["startedAt"]
            )
        )
    else:
        raise DeserializationError("TestRun.started_at required")
    if data.get("endedAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["ended_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["endedAt"]
            )
        )
    if data.get("experiments") is not None:
        import capo_resiliencehubv2.types.experiment_details_list

        out["experiments"] = (
            capo_resiliencehubv2.types.experiment_details_list.deserialize_json(
                data["experiments"]
            )
        )
    if data.get("eventCount") is not None:
        out["event_count"] = data["eventCount"]
    if data.get("parameters") is not None:
        import capo_resiliencehubv2.types.test_parameters

        out["parameters"] = capo_resiliencehubv2.types.test_parameters.deserialize_json(
            data["parameters"]
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    if data.get("stopConditions") is not None:
        import capo_resiliencehubv2.types.stop_condition_list

        out["stop_conditions"] = (
            capo_resiliencehubv2.types.stop_condition_list.deserialize_json(
                data["stopConditions"]
            )
        )
    if data.get("loggingConfiguration") is not None:
        import capo_resiliencehubv2.types.logging_configuration

        out["logging_configuration"] = (
            capo_resiliencehubv2.types.logging_configuration.deserialize_json(
                data["loggingConfiguration"]
            )
        )
    if data.get("roleName") is not None:
        out["role_name"] = data["roleName"]
    if data.get("testTemplateArn") is not None:
        out["test_template_arn"] = data["testTemplateArn"]
    else:
        raise DeserializationError("TestRun.test_template_arn required")
    if data.get("reportConfiguration") is not None:
        import capo_resiliencehubv2.types.test_run_report_configuration

        out["report_configuration"] = (
            capo_resiliencehubv2.types.test_run_report_configuration.deserialize_json(
                data["reportConfiguration"]
            )
        )
    if data.get("policy") is not None:
        import capo_resiliencehubv2.types.test_run_policy_snapshot

        out["policy"] = (
            capo_resiliencehubv2.types.test_run_policy_snapshot.deserialize_json(
                data["policy"]
            )
        )
    if data.get("reportOutput") is not None:
        import capo_resiliencehubv2.types.report_generation_result

        out["report_output"] = (
            capo_resiliencehubv2.types.report_generation_result.deserialize_json(
                data["reportOutput"]
            )
        )
    if data.get("regionSwitchPlanArn") is not None:
        out["region_switch_plan_arn"] = data["regionSwitchPlanArn"]
    if data.get("regionSwitchExecutionId") is not None:
        out["region_switch_execution_id"] = data["regionSwitchExecutionId"]
    if data.get("permissionModel") is not None:
        import capo_resiliencehubv2.types.permission_model

        out["permission_model"] = (
            capo_resiliencehubv2.types.permission_model.deserialize_json(
                data["permissionModel"]
            )
        )
    if data.get("regions") is not None:
        import capo_resiliencehubv2.types.region_list

        out["regions"] = capo_resiliencehubv2.types.region_list.deserialize_json(
            data["regions"]
        )
    if data.get("accountTargeting") is not None:
        import capo_resiliencehubv2.types.account_targeting

        out["account_targeting"] = (
            capo_resiliencehubv2.types.account_targeting.deserialize_json(
                data["accountTargeting"]
            )
        )
    return out
