"""Generated from Smithy shape ``com.amazonaws.eks#ElasticLoadBalancing``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.boxed_boolean
    import capo_eks.types.gateway_api_configuration


class ElasticLoadBalancing(TypedDict, closed=True):
    enabled: NotRequired["capo_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>Indicates if the load balancing capability is enabled on your EKS Auto Mode cluster. If the load balancing capability is enabled, EKS Auto Mode will create and delete load balancers in your Amazon Web Services account.</p>"""
    gateway_api: NotRequired[
        "capo_eks.types.gateway_api_configuration.GatewayApiConfiguration"
    ]
    """<p>Indicates the current configuration of the Kubernetes Gateway API for the load balancing capability on your EKS Auto Mode cluster. For more information, see EKS Auto Mode load balancing capability in the <i>Amazon EKS User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ElasticLoadBalancing) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "gateway_api" in value:
        import capo_eks.types.gateway_api_configuration

        out["gatewayApi"] = capo_eks.types.gateway_api_configuration.serialize_json(
            value["gateway_api"]
        )
    return out


def deserialize_json(data: dict) -> ElasticLoadBalancing:
    out: ElasticLoadBalancing = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    if data.get("gatewayApi") is not None:
        import capo_eks.types.gateway_api_configuration

        out["gateway_api"] = capo_eks.types.gateway_api_configuration.deserialize_json(
            data["gatewayApi"]
        )
    return out
