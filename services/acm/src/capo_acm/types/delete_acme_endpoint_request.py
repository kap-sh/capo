"""Generated from Smithy shape ``com.amazonaws.acm#DeleteAcmeEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_acm.types.acme_endpoint_arn


class DeleteAcmeEndpointRequest(TypedDict, closed=True):
    acme_endpoint_arn: "capo_acm.types.acme_endpoint_arn.AcmeEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the ACME endpoint to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAcmeEndpointRequest) -> dict:
    out: dict = {}
    out["AcmeEndpointArn"] = value["acme_endpoint_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAcmeEndpointRequest:
    out: DeleteAcmeEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("AcmeEndpointArn") is not None:
        out["acme_endpoint_arn"] = data["AcmeEndpointArn"]
    else:
        out["acme_endpoint_arn"] = ""
    return out
