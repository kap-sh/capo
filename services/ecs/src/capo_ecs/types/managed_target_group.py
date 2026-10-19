"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedTargetGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.integer
    import capo_ecs.types.managed_resource_status
    import capo_ecs.types.string
    import capo_ecs.types.timestamp


class ManagedTargetGroup(TypedDict, closed=True):
    arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the target group.</p>"""
    status: "capo_ecs.types.managed_resource_status.ManagedResourceStatus"
    """<p>The status of the target group.</p>"""
    status_reason: NotRequired["capo_ecs.types.string.String"]
    """<p>Information about why the target group is in the current status.</p>"""
    updated_at: "capo_ecs.types.timestamp.Timestamp"
    """<p>The Unix timestamp for when the target group was last updated.</p>"""
    health_check_path: "capo_ecs.types.string.String"
    """<p>The destination for health checks on the targets.</p>"""
    health_check_port: "capo_ecs.types.integer.Integer"
    """<p>The port the load balancer uses when performing health checks on targets.</p>"""
    port: "capo_ecs.types.integer.Integer"
    """<p>The port on which the targets receive traffic.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedTargetGroup) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    import capo_ecs.types.managed_resource_status

    out["status"] = capo_ecs.types.managed_resource_status.serialize_aws_json_1_1(
        value["status"]
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import capo_ecs.types.timestamp

    out["updatedAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
        value["updated_at"]
    )
    out["healthCheckPath"] = value["health_check_path"]
    out["healthCheckPort"] = value.get("health_check_port", 0)
    out["port"] = value.get("port", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedTargetGroup:
    out: ManagedTargetGroup = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("status") is not None:
        import capo_ecs.types.managed_resource_status

        out["status"] = capo_ecs.types.managed_resource_status.deserialize_aws_json_1_1(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_ecs.types.managed_resource_status.ManagedResourceStatus", ""
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("updatedAt") is not None:
        import capo_ecs.types.timestamp

        out["updated_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("healthCheckPath") is not None:
        out["health_check_path"] = data["healthCheckPath"]
    else:
        out["health_check_path"] = ""
    if data.get("healthCheckPort") is not None:
        out["health_check_port"] = data["healthCheckPort"]
    else:
        out["health_check_port"] = 0
    if data.get("port") is not None:
        out["port"] = data["port"]
    else:
        out["port"] = 0
    return out
