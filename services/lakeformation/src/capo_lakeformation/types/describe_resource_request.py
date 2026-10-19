"""Generated from Smithy shape ``com.amazonaws.lakeformation#DescribeResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.resource_arn_string


class DescribeResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_lakeformation.types.resource_arn_string.ResourceArnString"
    """<p>The resource ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> DescribeResourceRequest:
    out: DescribeResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out
