"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeVpcEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.vpc_endpoint_error_list
    import capo_opensearch.types.vpc_endpoints


class DescribeVpcEndpointsResponse(TypedDict, closed=True):
    vpc_endpoints: "capo_opensearch.types.vpc_endpoints.VpcEndpoints"
    """<p>Information about each requested VPC endpoint.</p>"""
    vpc_endpoint_errors: (
        "capo_opensearch.types.vpc_endpoint_error_list.VpcEndpointErrorList"
    )
    """<p>Any errors associated with the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeVpcEndpointsResponse) -> dict:
    out: dict = {}
    import capo_opensearch.types.vpc_endpoints

    out["VpcEndpoints"] = capo_opensearch.types.vpc_endpoints.serialize_json(
        value["vpc_endpoints"]
    )
    import capo_opensearch.types.vpc_endpoint_error_list

    out["VpcEndpointErrors"] = (
        capo_opensearch.types.vpc_endpoint_error_list.serialize_json(
            value["vpc_endpoint_errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeVpcEndpointsResponse:
    out: DescribeVpcEndpointsResponse = {}  # type: ignore[typeddict-item]
    if data.get("VpcEndpoints") is not None:
        import capo_opensearch.types.vpc_endpoints

        out["vpc_endpoints"] = capo_opensearch.types.vpc_endpoints.deserialize_json(
            data["VpcEndpoints"]
        )
    else:
        out["vpc_endpoints"] = []
    if data.get("VpcEndpointErrors") is not None:
        import capo_opensearch.types.vpc_endpoint_error_list

        out["vpc_endpoint_errors"] = (
            capo_opensearch.types.vpc_endpoint_error_list.deserialize_json(
                data["VpcEndpointErrors"]
            )
        )
    else:
        out["vpc_endpoint_errors"] = []
    return out
