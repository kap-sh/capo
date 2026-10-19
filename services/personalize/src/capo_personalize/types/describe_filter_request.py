"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn


class DescribeFilterRequest(TypedDict, closed=True):
    filter_arn: "capo_personalize.types.arn.Arn"
    """<p>The ARN of the filter to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFilterRequest) -> dict:
    out: dict = {}
    out["filterArn"] = value["filter_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFilterRequest:
    out: DescribeFilterRequest = {}  # type: ignore[typeddict-item]
    if data.get("filterArn") is not None:
        out["filter_arn"] = data["filterArn"]
    else:
        out["filter_arn"] = ""
    return out
