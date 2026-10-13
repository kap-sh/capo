"""Generated from Smithy shape ``com.amazonaws.ecs#ECSExpressGatewayService``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.express_gateway_service_configurations
    import capo_ecs.types.express_gateway_service_status
    import capo_ecs.types.string
    import capo_ecs.types.tags
    import capo_ecs.types.timestamp


class ECSExpressGatewayService(TypedDict, closed=True):
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The short name or full ARN of the cluster that hosts the Express service.</p>"""
    service_name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the Express service.</p>"""
    service_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN that identifies the Express service.</p>"""
    infrastructure_role_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN of the infrastructure role that manages Amazon Web Services resources for the Express service.</p>"""
    status: NotRequired[
        "capo_ecs.types.express_gateway_service_status.ExpressGatewayServiceStatus"
    ]
    """<p>The current status of the Express service.</p>"""
    current_deployment: NotRequired["capo_ecs.types.string.String"]
    """<p>The current deployment configuration for the Express service.</p>"""
    active_configurations: NotRequired[
        "capo_ecs.types.express_gateway_service_configurations.ExpressGatewayServiceConfigurations"
    ]
    """<p>The list of active service configurations for the Express service.</p>"""
    tags: NotRequired["capo_ecs.types.tags.Tags"]
    """<p>The metadata applied to the Express service.</p>"""
    created_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for when the Express service was created.</p>"""
    updated_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for when the Express service was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ECSExpressGatewayService) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "infrastructure_role_arn" in value:
        out["infrastructureRoleArn"] = value["infrastructure_role_arn"]
    if "status" in value:
        import capo_ecs.types.express_gateway_service_status

        out["status"] = (
            capo_ecs.types.express_gateway_service_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "current_deployment" in value:
        out["currentDeployment"] = value["current_deployment"]
    if "active_configurations" in value:
        import capo_ecs.types.express_gateway_service_configurations

        out["activeConfigurations"] = (
            capo_ecs.types.express_gateway_service_configurations.serialize_aws_json_1_1(
                value["active_configurations"]
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


def deserialize_aws_json_1_1(data: dict) -> ECSExpressGatewayService:
    out: ECSExpressGatewayService = {}  # type: ignore[typeddict-item]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    if data.get("infrastructureRoleArn") is not None:
        out["infrastructure_role_arn"] = data["infrastructureRoleArn"]
    if data.get("status") is not None:
        import capo_ecs.types.express_gateway_service_status

        out["status"] = (
            capo_ecs.types.express_gateway_service_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("currentDeployment") is not None:
        out["current_deployment"] = data["currentDeployment"]
    if data.get("activeConfigurations") is not None:
        import capo_ecs.types.express_gateway_service_configurations

        out["active_configurations"] = (
            capo_ecs.types.express_gateway_service_configurations.deserialize_aws_json_1_1(
                data["activeConfigurations"]
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


def redact_sensitive(value: ECSExpressGatewayService) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "active_configurations" in value:
        import capo_ecs.types.express_gateway_service_configurations

        out["active_configurations"] = (
            capo_ecs.types.express_gateway_service_configurations.redact_sensitive(
                value["active_configurations"]
            )
        )
    return out
