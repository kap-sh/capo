"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateExpressGatewayServiceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.updated_express_gateway_service


class UpdateExpressGatewayServiceResponse(TypedDict, closed=True):
    service: NotRequired[
        "capo_ecs.types.updated_express_gateway_service.UpdatedExpressGatewayService"
    ]
    """<p>The full description of your express gateway service following the update call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateExpressGatewayServiceResponse) -> dict:
    out: dict = {}
    if "service" in value:
        import capo_ecs.types.updated_express_gateway_service

        out["service"] = (
            capo_ecs.types.updated_express_gateway_service.serialize_aws_json_1_1(
                value["service"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateExpressGatewayServiceResponse:
    out: UpdateExpressGatewayServiceResponse = {}  # type: ignore[typeddict-item]
    if data.get("service") is not None:
        import capo_ecs.types.updated_express_gateway_service

        out["service"] = (
            capo_ecs.types.updated_express_gateway_service.deserialize_aws_json_1_1(
                data["service"]
            )
        )
    return out


def redact_sensitive(value: UpdateExpressGatewayServiceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "service" in value:
        import capo_ecs.types.updated_express_gateway_service

        out["service"] = (
            capo_ecs.types.updated_express_gateway_service.redact_sensitive(
                value["service"]
            )
        )
    return out
