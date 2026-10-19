"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DescribeResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.resource_arn


class DescribeResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_lookoutequipment.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource that is associated with the resource policy.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeResourcePolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeResourcePolicyRequest:
    out: DescribeResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out
