"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProductionVariantRoutingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.prefix_aware_routing_config
    import capo_sagemaker.types.routing_strategy


class ProductionVariantRoutingConfig(TypedDict, closed=True):
    routing_strategy: NotRequired[
        "capo_sagemaker.types.routing_strategy.RoutingStrategy"
    ]
    """<p>Sets how the endpoint routes incoming traffic:</p> <ul> <li> <p> <code>LEAST_OUTSTANDING_REQUESTS</code>: The endpoint routes requests to the specific instances that have more capacity to process them.</p> </li> <li> <p> <code>RANDOM</code>: The endpoint routes each request to a randomly chosen instance.</p> </li> <li> <p> <code>PREFIX_AWARE</code>: The endpoint routes requests that share the same prompt prefix to the same instance. When the number of in-flight requests on the selected instance reaches the configured threshold, the endpoint routes the request to an instance with more available capacity.</p> </li> </ul>"""
    prefix_aware_routing_config: NotRequired[
        "capo_sagemaker.types.prefix_aware_routing_config.PrefixAwareRoutingConfig"
    ]
    """<p>The configuration for prefix-aware routing. Specify this parameter only when you set <code>RoutingStrategy</code> to <code>PREFIX_AWARE</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductionVariantRoutingConfig) -> dict:
    out: dict = {}
    if "routing_strategy" in value:
        import capo_sagemaker.types.routing_strategy

        out["RoutingStrategy"] = (
            capo_sagemaker.types.routing_strategy.serialize_aws_json_1_1(
                value["routing_strategy"]
            )
        )
    if "prefix_aware_routing_config" in value:
        import capo_sagemaker.types.prefix_aware_routing_config

        out["PrefixAwareRoutingConfig"] = (
            capo_sagemaker.types.prefix_aware_routing_config.serialize_aws_json_1_1(
                value["prefix_aware_routing_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProductionVariantRoutingConfig:
    out: ProductionVariantRoutingConfig = {}  # type: ignore[typeddict-item]
    if data.get("RoutingStrategy") is not None:
        import capo_sagemaker.types.routing_strategy

        out["routing_strategy"] = (
            capo_sagemaker.types.routing_strategy.deserialize_aws_json_1_1(
                data["RoutingStrategy"]
            )
        )
    if data.get("PrefixAwareRoutingConfig") is not None:
        import capo_sagemaker.types.prefix_aware_routing_config

        out["prefix_aware_routing_config"] = (
            capo_sagemaker.types.prefix_aware_routing_config.deserialize_aws_json_1_1(
                data["PrefixAwareRoutingConfig"]
            )
        )
    return out
