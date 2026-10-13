"""Generated from Smithy shape ``com.amazonaws.ecs#UpdatedExpressGatewayService``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.express_gateway_service_configuration
    import capo_ecs.types.express_gateway_service_status
    import capo_ecs.types.string
    import capo_ecs.types.timestamp


class UpdatedExpressGatewayService(TypedDict, closed=True):
    service_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN of the Express service that is being updated.</p>"""
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The cluster associated with the Express service that is being updated.</p>"""
    service_name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the Express service that is being updated.</p>"""
    status: NotRequired[
        "capo_ecs.types.express_gateway_service_status.ExpressGatewayServiceStatus"
    ]
    """<p>The status of the Express service that is being updated.</p>"""
    target_configuration: NotRequired[
        "capo_ecs.types.express_gateway_service_configuration.ExpressGatewayServiceConfiguration"
    ]
    """<p>The configuration to which the current Express service is being updated to.</p>"""
    created_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for when the Express service that is being updated was created.</p>"""
    updated_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for when the Express service that is being updated was most recently updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatedExpressGatewayService) -> dict:
    out: dict = {}
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "status" in value:
        import capo_ecs.types.express_gateway_service_status

        out["status"] = (
            capo_ecs.types.express_gateway_service_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "target_configuration" in value:
        import capo_ecs.types.express_gateway_service_configuration

        out["targetConfiguration"] = (
            capo_ecs.types.express_gateway_service_configuration.serialize_aws_json_1_1(
                value["target_configuration"]
            )
        )
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


def deserialize_aws_json_1_1(data: dict) -> UpdatedExpressGatewayService:
    out: UpdatedExpressGatewayService = {}  # type: ignore[typeddict-item]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    if data.get("status") is not None:
        import capo_ecs.types.express_gateway_service_status

        out["status"] = (
            capo_ecs.types.express_gateway_service_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("targetConfiguration") is not None:
        import capo_ecs.types.express_gateway_service_configuration

        out["target_configuration"] = (
            capo_ecs.types.express_gateway_service_configuration.deserialize_aws_json_1_1(
                data["targetConfiguration"]
            )
        )
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


def redact_sensitive(value: UpdatedExpressGatewayService) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "target_configuration" in value:
        import capo_ecs.types.express_gateway_service_configuration

        out["target_configuration"] = (
            capo_ecs.types.express_gateway_service_configuration.redact_sensitive(
                value["target_configuration"]
            )
        )
    return out
