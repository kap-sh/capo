"""Generated from Smithy shape ``com.amazonaws.acm#DescribeAcmeAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_acm.types.acme_endpoint_arn


class DescribeAcmeAccountRequest(TypedDict, closed=True):
    acme_endpoint_arn: "capo_acm.types.acme_endpoint_arn.AcmeEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the ACME endpoint.</p>"""
    account_url: "str"
    """<p>The URL of the ACME account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAcmeAccountRequest) -> dict:
    out: dict = {}
    out["AcmeEndpointArn"] = value["acme_endpoint_arn"]
    out["AccountUrl"] = value["account_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAcmeAccountRequest:
    out: DescribeAcmeAccountRequest = {}  # type: ignore[typeddict-item]
    if data.get("AcmeEndpointArn") is not None:
        out["acme_endpoint_arn"] = data["AcmeEndpointArn"]
    else:
        out["acme_endpoint_arn"] = ""
    if data.get("AccountUrl") is not None:
        out["account_url"] = data["AccountUrl"]
    else:
        out["account_url"] = ""
    return out
