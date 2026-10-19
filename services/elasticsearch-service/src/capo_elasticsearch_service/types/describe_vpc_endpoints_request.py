"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribeVpcEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.vpc_endpoint_id_list


class DescribeVpcEndpointsRequest(TypedDict, closed=True):
    vpc_endpoint_ids: (
        "capo_elasticsearch_service.types.vpc_endpoint_id_list.VpcEndpointIdList"
    )
    """<p>The unique identifiers of the endpoints to get information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeVpcEndpointsRequest) -> dict:
    out: dict = {}
    import capo_elasticsearch_service.types.vpc_endpoint_id_list

    out["VpcEndpointIds"] = (
        capo_elasticsearch_service.types.vpc_endpoint_id_list.serialize_json(
            value["vpc_endpoint_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeVpcEndpointsRequest:
    out: DescribeVpcEndpointsRequest = {}  # type: ignore[typeddict-item]
    if data.get("VpcEndpointIds") is not None:
        import capo_elasticsearch_service.types.vpc_endpoint_id_list

        out["vpc_endpoint_ids"] = (
            capo_elasticsearch_service.types.vpc_endpoint_id_list.deserialize_json(
                data["VpcEndpointIds"]
            )
        )
    else:
        out["vpc_endpoint_ids"] = []
    return out
