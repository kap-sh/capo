"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayConnector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.gateway_connector_filters
    import capo_ecs.types.gateway_connector_health_check
    import capo_ecs.types.string


class GatewayConnector(TypedDict, closed=True):
    port_name: "capo_ecs.types.string.String"
    """<p>The name of the service port that the gateway routes ingress traffic to.</p>"""
    health_check: NotRequired[
        "capo_ecs.types.gateway_connector_health_check.GatewayConnectorHealthCheck"
    ]
    """<p>The health check that the gateway uses to determine whether the targets for this connector are healthy.</p>"""
    filters: NotRequired[
        "capo_ecs.types.gateway_connector_filters.GatewayConnectorFilters"
    ]
    """<p>The filters that control which gateway ingress paths the connector applies to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayConnector) -> dict:
    out: dict = {}
    out["portName"] = value["port_name"]
    if "health_check" in value:
        import capo_ecs.types.gateway_connector_health_check

        out["healthCheck"] = (
            capo_ecs.types.gateway_connector_health_check.serialize_aws_json_1_1(
                value["health_check"]
            )
        )
    if "filters" in value:
        import capo_ecs.types.gateway_connector_filters

        out["filters"] = (
            capo_ecs.types.gateway_connector_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GatewayConnector:
    out: GatewayConnector = {}  # type: ignore[typeddict-item]
    if data.get("portName") is not None:
        out["port_name"] = data["portName"]
    else:
        out["port_name"] = ""
    if data.get("healthCheck") is not None:
        import capo_ecs.types.gateway_connector_health_check

        out["health_check"] = (
            capo_ecs.types.gateway_connector_health_check.deserialize_aws_json_1_1(
                data["healthCheck"]
            )
        )
    if data.get("filters") is not None:
        import capo_ecs.types.gateway_connector_filters

        out["filters"] = (
            capo_ecs.types.gateway_connector_filters.deserialize_aws_json_1_1(
                data["filters"]
            )
        )
    return out
