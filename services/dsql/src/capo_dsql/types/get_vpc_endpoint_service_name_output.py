"""Generated from Smithy shape ``com.amazonaws.dsql#GetVpcEndpointServiceNameOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dsql.types.cluster_vpc_endpoint
    import capo_dsql.types.service_name


class GetVpcEndpointServiceNameOutput(TypedDict, closed=True):
    service_name: "capo_dsql.types.service_name.ServiceName"
    """<p>The VPC endpoint service name.</p>"""
    cluster_vpc_endpoint: NotRequired[
        "capo_dsql.types.cluster_vpc_endpoint.ClusterVpcEndpoint"
    ]
    """<p>The VPC connection endpoint for the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVpcEndpointServiceNameOutput) -> dict:
    out: dict = {}
    out["serviceName"] = value["service_name"]
    if "cluster_vpc_endpoint" in value:
        out["clusterVpcEndpoint"] = value["cluster_vpc_endpoint"]
    return out


def deserialize_json(data: dict) -> GetVpcEndpointServiceNameOutput:
    out: GetVpcEndpointServiceNameOutput = {}  # type: ignore[typeddict-item]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    else:
        out["service_name"] = ""
    if data.get("clusterVpcEndpoint") is not None:
        out["cluster_vpc_endpoint"] = data["clusterVpcEndpoint"]
    return out
