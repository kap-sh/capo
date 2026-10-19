"""Generated from Smithy shape ``com.amazonaws.opensearch#ListVpcEndpointsForDomainResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.next_token
    import capo_opensearch.types.vpc_endpoint_summary_list


class ListVpcEndpointsForDomainResponse(TypedDict, closed=True):
    vpc_endpoint_summary_list: (
        "capo_opensearch.types.vpc_endpoint_summary_list.VpcEndpointSummaryList"
    )
    """<p>Information about each endpoint associated with the domain.</p>"""
    next_token: "capo_opensearch.types.next_token.NextToken"
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVpcEndpointsForDomainResponse) -> dict:
    out: dict = {}
    import capo_opensearch.types.vpc_endpoint_summary_list

    out["VpcEndpointSummaryList"] = (
        capo_opensearch.types.vpc_endpoint_summary_list.serialize_json(
            value["vpc_endpoint_summary_list"]
        )
    )
    out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVpcEndpointsForDomainResponse:
    out: ListVpcEndpointsForDomainResponse = {}  # type: ignore[typeddict-item]
    if data.get("VpcEndpointSummaryList") is not None:
        import capo_opensearch.types.vpc_endpoint_summary_list

        out["vpc_endpoint_summary_list"] = (
            capo_opensearch.types.vpc_endpoint_summary_list.deserialize_json(
                data["VpcEndpointSummaryList"]
            )
        )
    else:
        out["vpc_endpoint_summary_list"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    else:
        out["next_token"] = ""
    return out
