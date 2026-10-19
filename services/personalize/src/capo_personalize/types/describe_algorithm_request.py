"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeAlgorithmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn


class DescribeAlgorithmRequest(TypedDict, closed=True):
    algorithm_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the algorithm to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAlgorithmRequest) -> dict:
    out: dict = {}
    out["algorithmArn"] = value["algorithm_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAlgorithmRequest:
    out: DescribeAlgorithmRequest = {}  # type: ignore[typeddict-item]
    if data.get("algorithmArn") is not None:
        out["algorithm_arn"] = data["algorithmArn"]
    else:
        out["algorithm_arn"] = ""
    return out
