"""Generated from Smithy shape ``com.amazonaws.ecs#CreateExpressGatewayServiceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.ecs_express_gateway_service


class CreateExpressGatewayServiceResponse(TypedDict, closed=True):
    service: NotRequired[
        "capo_ecs.types.ecs_express_gateway_service.ECSExpressGatewayService"
    ]
    """<p>The full description of your Express service following the create operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateExpressGatewayServiceResponse) -> dict:
    out: dict = {}
    if "service" in value:
        import capo_ecs.types.ecs_express_gateway_service

        out["service"] = (
            capo_ecs.types.ecs_express_gateway_service.serialize_aws_json_1_1(
                value["service"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateExpressGatewayServiceResponse:
    out: CreateExpressGatewayServiceResponse = {}  # type: ignore[typeddict-item]
    if data.get("service") is not None:
        import capo_ecs.types.ecs_express_gateway_service

        out["service"] = (
            capo_ecs.types.ecs_express_gateway_service.deserialize_aws_json_1_1(
                data["service"]
            )
        )
    return out


def redact_sensitive(value: CreateExpressGatewayServiceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "service" in value:
        import capo_ecs.types.ecs_express_gateway_service

        out["service"] = capo_ecs.types.ecs_express_gateway_service.redact_sensitive(
            value["service"]
        )
    return out
