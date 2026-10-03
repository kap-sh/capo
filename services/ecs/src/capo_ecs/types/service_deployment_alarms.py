"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceDeploymentAlarms``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.service_deployment_rollback_monitors_status
    import capo_ecs.types.string_list


class ServiceDeploymentAlarms(TypedDict, closed=True):
    status: NotRequired[
        "capo_ecs.types.service_deployment_rollback_monitors_status.ServiceDeploymentRollbackMonitorsStatus"
    ]
    """<p>The status of the alarms check. Amazon ECS is not using alarms for service deployment failures when the status is <code>DISABLED</code>.</p>"""
    alarm_names: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The name of the CloudWatch alarms that determine when a service deployment failed. A "," separates the alarms.</p>"""
    triggered_alarm_names: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>One or more CloudWatch alarm names that have been triggered during the service deployment. A "," separates the alarm names.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceDeploymentAlarms) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_ecs.types.service_deployment_rollback_monitors_status

        out["status"] = (
            capo_ecs.types.service_deployment_rollback_monitors_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "alarm_names" in value:
        import capo_ecs.types.string_list

        out["alarmNames"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["alarm_names"]
        )
    if "triggered_alarm_names" in value:
        import capo_ecs.types.string_list

        out["triggeredAlarmNames"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["triggered_alarm_names"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceDeploymentAlarms:
    out: ServiceDeploymentAlarms = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_ecs.types.service_deployment_rollback_monitors_status

        out["status"] = (
            capo_ecs.types.service_deployment_rollback_monitors_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("alarmNames") is not None:
        import capo_ecs.types.string_list

        out["alarm_names"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["alarmNames"]
        )
    if data.get("triggeredAlarmNames") is not None:
        import capo_ecs.types.string_list

        out["triggered_alarm_names"] = (
            capo_ecs.types.string_list.deserialize_aws_json_1_1(
                data["triggeredAlarmNames"]
            )
        )
    return out
