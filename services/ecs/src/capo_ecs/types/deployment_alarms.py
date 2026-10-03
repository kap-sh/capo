"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentAlarms``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.boolean
    import capo_ecs.types.string_list


class DeploymentAlarms(TypedDict, closed=True):
    alarm_names: "capo_ecs.types.string_list.StringList"
    """<p>One or more CloudWatch alarm names. Use a "," to separate the alarms.</p>"""
    rollback: "capo_ecs.types.boolean.Boolean"
    """<p>Determines whether to configure Amazon ECS to roll back the service if a service deployment fails. If rollback is used, when a service deployment fails, the service is rolled back to the last deployment that completed successfully.</p>"""
    enable: "capo_ecs.types.boolean.Boolean"
    """<p>Determines whether to use the CloudWatch alarm option in the service deployment process.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentAlarms) -> dict:
    out: dict = {}
    import capo_ecs.types.string_list

    out["alarmNames"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
        value["alarm_names"]
    )
    out["rollback"] = value.get("rollback", False)
    out["enable"] = value.get("enable", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentAlarms:
    out: DeploymentAlarms = {}  # type: ignore[typeddict-item]
    if data.get("alarmNames") is not None:
        import capo_ecs.types.string_list

        out["alarm_names"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["alarmNames"]
        )
    else:
        raise DeserializationError("DeploymentAlarms.alarm_names required")
    if data.get("rollback") is not None:
        out["rollback"] = data["rollback"]
    else:
        out["rollback"] = False
    if data.get("enable") is not None:
        out["enable"] = data["enable"]
    else:
        out["enable"] = False
    return out
