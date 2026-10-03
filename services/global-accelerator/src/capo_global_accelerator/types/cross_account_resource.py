"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CrossAccountResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.generic_string


class CrossAccountResource(TypedDict, closed=True):
    endpoint_id: NotRequired[
        "capo_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The endpoint ID for the endpoint that is listed in a cross-account attachment and can be added to an accelerator by specified principals.</p>"""
    cidr: NotRequired["capo_global_accelerator.types.generic_string.GenericString"]
    """<p>An IP address range, in CIDR format, that is specified as an Amazon Web Services resource. The address must be provisioned and advertised in Global Accelerator by following the bring your own IP address (BYOIP) process for Global Accelerator.</p> <p> For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html">Bring your own IP addresses (BYOIP)</a> in the Global Accelerator Developer Guide.</p>"""
    attachment_arn: NotRequired[
        "capo_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The Amazon Resource Name (ARN) of the cross-account attachment that specifies the resources (endpoints or CIDR range) that can be added to accelerators and principals that have permission to add them.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrossAccountResource) -> dict:
    out: dict = {}
    if "endpoint_id" in value:
        out["EndpointId"] = value["endpoint_id"]
    if "cidr" in value:
        out["Cidr"] = value["cidr"]
    if "attachment_arn" in value:
        out["AttachmentArn"] = value["attachment_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CrossAccountResource:
    out: CrossAccountResource = {}  # type: ignore[typeddict-item]
    if data.get("EndpointId") is not None:
        out["endpoint_id"] = data["EndpointId"]
    if data.get("Cidr") is not None:
        out["cidr"] = data["Cidr"]
    if data.get("AttachmentArn") is not None:
        out["attachment_arn"] = data["AttachmentArn"]
    return out
