"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateTaskProtectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.boolean
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.string
    import capo_ecs.types.string_list


class UpdateTaskProtectionRequest(TypedDict, closed=True):
    cluster: "capo_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task sets exist in.</p>"""
    tasks: "capo_ecs.types.string_list.StringList"
    """<p>A list of up to 10 task IDs or full ARN entries.</p>"""
    protection_enabled: "capo_ecs.types.boolean.Boolean"
    """<p>Specify <code>true</code> to mark a task for protection and <code>false</code> to unset protection, making it eligible for termination.</p>"""
    expires_in_minutes: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>If you set <code>protectionEnabled</code> to <code>true</code>, you can specify the duration for task protection in minutes. You can specify a value from 1 minute to up to 2,880 minutes (48 hours). During this time, your task will not be terminated by scale-in events from Service Auto Scaling or deployments. After this time period lapses, <code>protectionEnabled</code> will be reset to <code>false</code>.</p> <p>If you don’t specify the time, then the task is automatically protected for 120 minutes (2 hours).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTaskProtectionRequest) -> dict:
    out: dict = {}
    out["cluster"] = value["cluster"]
    import capo_ecs.types.string_list

    out["tasks"] = capo_ecs.types.string_list.serialize_aws_json_1_1(value["tasks"])
    out["protectionEnabled"] = value["protection_enabled"]
    if "expires_in_minutes" in value:
        out["expiresInMinutes"] = value["expires_in_minutes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTaskProtectionRequest:
    out: UpdateTaskProtectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    else:
        raise DeserializationError("UpdateTaskProtectionRequest.cluster required")
    if data.get("tasks") is not None:
        import capo_ecs.types.string_list

        out["tasks"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["tasks"]
        )
    else:
        raise DeserializationError("UpdateTaskProtectionRequest.tasks required")
    if data.get("protectionEnabled") is not None:
        out["protection_enabled"] = data["protectionEnabled"]
    else:
        raise DeserializationError(
            "UpdateTaskProtectionRequest.protection_enabled required"
        )
    if data.get("expiresInMinutes") is not None:
        out["expires_in_minutes"] = data["expiresInMinutes"]
    return out
