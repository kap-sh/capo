"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#DescribeCustomRoutingAcceleratorAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.generic_string


class DescribeCustomRoutingAcceleratorAttributesRequest(TypedDict, closed=True):
    accelerator_arn: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the custom routing accelerator to describe the attributes for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeCustomRoutingAcceleratorAttributesRequest,
) -> dict:
    out: dict = {}
    out["AcceleratorArn"] = value["accelerator_arn"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeCustomRoutingAcceleratorAttributesRequest:
    out: DescribeCustomRoutingAcceleratorAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("AcceleratorArn") is not None:
        out["accelerator_arn"] = data["AcceleratorArn"]
    else:
        out["accelerator_arn"] = ""
    return out
