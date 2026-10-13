"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayServiceConfigurations``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.express_gateway_service_configuration

ExpressGatewayServiceConfigurations: TypeAlias = list[
    "capo_ecs.types.express_gateway_service_configuration.ExpressGatewayServiceConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpressGatewayServiceConfigurations) -> list:
    import capo_ecs.types.express_gateway_service_configuration

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.express_gateway_service_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExpressGatewayServiceConfigurations:
    import capo_ecs.types.express_gateway_service_configuration

    out: ExpressGatewayServiceConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.express_gateway_service_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: ExpressGatewayServiceConfigurations) -> list[Any]:
    import capo_ecs.types.express_gateway_service_configuration

    return [
        capo_ecs.types.express_gateway_service_configuration.redact_sensitive(item)
        for item in value
    ]
