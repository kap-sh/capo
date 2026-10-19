"""Generated from Smithy shape ``com.amazonaws.acm#ListAcmeAccountsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.acme_endpoint_arn


class ListAcmeAccountsRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A token for pagination.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return.</p>"""
    acme_endpoint_arn: "capo_acm.types.acme_endpoint_arn.AcmeEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the ACME endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAcmeAccountsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    out["AcmeEndpointArn"] = value["acme_endpoint_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAcmeAccountsRequest:
    out: ListAcmeAccountsRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("AcmeEndpointArn") is not None:
        out["acme_endpoint_arn"] = data["AcmeEndpointArn"]
    else:
        out["acme_endpoint_arn"] = ""
    return out
