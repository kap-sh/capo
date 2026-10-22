"""Generated from Smithy shape ``com.amazonaws.ecs#Gateway``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.access_type
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.describe_gateway_configuration
    import capo_ecs.types.gateway_resource_failure_list
    import capo_ecs.types.gateway_status
    import capo_ecs.types.propagate_gateway_tags
    import capo_ecs.types.string
    import capo_ecs.types.tags
    import capo_ecs.types.timestamp


class Gateway(TypedDict, closed=True):
    gateway_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the gateway.</p>"""
    name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the gateway.</p>"""
    status: NotRequired["capo_ecs.types.gateway_status.GatewayStatus"]
    """<p>The status of the gateway.</p>"""
    status_reason: NotRequired["capo_ecs.types.string.String"]
    """<p>A human-readable explanation of the current status. This value is populated when the gateway is in a failure state, such as <code>UPDATE_FAILED</code>.</p>"""
    failures: NotRequired[
        "capo_ecs.types.gateway_resource_failure_list.GatewayResourceFailureList"
    ]
    """<p>The per-resource failure details for asynchronous gateway processes, such as an <code>UpdateGateway</code> operation that couldn't update every load balancer.</p>"""
    infrastructure_role_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that the gateway uses to manage infrastructure on your behalf.</p>"""
    deletion_protection: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>Specifies whether deletion protection is enabled for the gateway.</p>"""
    configuration: NotRequired[
        "capo_ecs.types.describe_gateway_configuration.DescribeGatewayConfiguration"
    ]
    """<p>The type-specific configuration for the gateway.</p>"""
    access_type: NotRequired["capo_ecs.types.access_type.AccessType"]
    """<p>Specifies whether the gateway is publicly accessible (<code>PUBLIC</code>) or private (<code>PRIVATE</code>). The gateway derives this value from its scheme when you create the gateway, and the value is immutable.</p>"""
    propagate_tags: NotRequired[
        "capo_ecs.types.propagate_gateway_tags.PropagateGatewayTags"
    ]
    """<p>Specifies whether the gateway propagates its tags to the infrastructure it manages.</p>"""
    tags: NotRequired["capo_ecs.types.tags.Tags"]
    """<p>The metadata applied to the gateway. Each tag consists of a key and an optional value.</p>"""
    created_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the gateway was created.</p>"""
    updated_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the gateway was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Gateway) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["gatewayArn"] = value["gateway_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        import capo_ecs.types.gateway_status

        out["status"] = capo_ecs.types.gateway_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "failures" in value:
        import capo_ecs.types.gateway_resource_failure_list

        out["failures"] = (
            capo_ecs.types.gateway_resource_failure_list.serialize_aws_json_1_1(
                value["failures"]
            )
        )
    if "infrastructure_role_arn" in value:
        out["infrastructureRoleArn"] = value["infrastructure_role_arn"]
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    if "configuration" in value:
        import capo_ecs.types.describe_gateway_configuration

        out["configuration"] = (
            capo_ecs.types.describe_gateway_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "access_type" in value:
        import capo_ecs.types.access_type

        out["accessType"] = capo_ecs.types.access_type.serialize_aws_json_1_1(
            value["access_type"]
        )
    if "propagate_tags" in value:
        import capo_ecs.types.propagate_gateway_tags

        out["propagateTags"] = (
            capo_ecs.types.propagate_gateway_tags.serialize_aws_json_1_1(
                value["propagate_tags"]
            )
        )
    if "tags" in value:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.serialize_aws_json_1_1(value["tags"])
    if "created_at" in value:
        import capo_ecs.types.timestamp

        out["createdAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_ecs.types.timestamp

        out["updatedAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Gateway:
    out: Gateway = {}  # type: ignore[typeddict-item]
    if data.get("gatewayArn") is not None:
        out["gateway_arn"] = data["gatewayArn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("status") is not None:
        import capo_ecs.types.gateway_status

        out["status"] = capo_ecs.types.gateway_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("failures") is not None:
        import capo_ecs.types.gateway_resource_failure_list

        out["failures"] = (
            capo_ecs.types.gateway_resource_failure_list.deserialize_aws_json_1_1(
                data["failures"]
            )
        )
    if data.get("infrastructureRoleArn") is not None:
        out["infrastructure_role_arn"] = data["infrastructureRoleArn"]
    if data.get("deletionProtection") is not None:
        out["deletion_protection"] = data["deletionProtection"]
    if data.get("configuration") is not None:
        import capo_ecs.types.describe_gateway_configuration

        out["configuration"] = (
            capo_ecs.types.describe_gateway_configuration.deserialize_aws_json_1_1(
                data["configuration"]
            )
        )
    if data.get("accessType") is not None:
        import capo_ecs.types.access_type

        out["access_type"] = capo_ecs.types.access_type.deserialize_aws_json_1_1(
            data["accessType"]
        )
    if data.get("propagateTags") is not None:
        import capo_ecs.types.propagate_gateway_tags

        out["propagate_tags"] = (
            capo_ecs.types.propagate_gateway_tags.deserialize_aws_json_1_1(
                data["propagateTags"]
            )
        )
    if data.get("tags") is not None:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.deserialize_aws_json_1_1(data["tags"])
    if data.get("createdAt") is not None:
        import capo_ecs.types.timestamp

        out["created_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_ecs.types.timestamp

        out["updated_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["updatedAt"]
        )
    return out
