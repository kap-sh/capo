"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedLoadBalancer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.managed_resource_status
    import capo_ecs.types.string
    import capo_ecs.types.string_list
    import capo_ecs.types.timestamp


class ManagedLoadBalancer(TypedDict, closed=True):
    arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the load balancer.</p>"""
    status: "capo_ecs.types.managed_resource_status.ManagedResourceStatus"
    """<p>The status of the load balancer.</p>"""
    status_reason: NotRequired["capo_ecs.types.string.String"]
    """<p>Information about why the load balancer is in the current status.</p>"""
    updated_at: "capo_ecs.types.timestamp.Timestamp"
    """<p>The Unix timestamp for when this load balancer was most recently updated.</p>"""
    scheme: "capo_ecs.types.string.String"
    """<p>The scheme of the load balancer. By default, the scheme of the load balancer is <code>internet-facing</code>.</p>"""
    subnet_ids: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The IDs of the subnets associated with the load balancer.</p>"""
    security_group_ids: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The IDs of the security groups associated with the load balancer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedLoadBalancer) -> dict:
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
    out["scheme"] = value["scheme"]
    if "subnet_ids" in value:
        import capo_ecs.types.string_list

        out["subnetIds"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import capo_ecs.types.string_list

        out["securityGroupIds"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["security_group_ids"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedLoadBalancer:
    out: ManagedLoadBalancer = {}  # type: ignore[typeddict-item]
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
    if data.get("scheme") is not None:
        out["scheme"] = data["scheme"]
    else:
        out["scheme"] = ""
    if data.get("subnetIds") is not None:
        import capo_ecs.types.string_list

        out["subnet_ids"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["subnetIds"]
        )
    if data.get("securityGroupIds") is not None:
        import capo_ecs.types.string_list

        out["security_group_ids"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["securityGroupIds"]
        )
    return out
