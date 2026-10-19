"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeFeatureTransformationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn


class DescribeFeatureTransformationRequest(TypedDict, closed=True):
    feature_transformation_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the feature transformation to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFeatureTransformationRequest) -> dict:
    out: dict = {}
    out["featureTransformationArn"] = value["feature_transformation_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFeatureTransformationRequest:
    out: DescribeFeatureTransformationRequest = {}  # type: ignore[typeddict-item]
    if data.get("featureTransformationArn") is not None:
        out["feature_transformation_arn"] = data["featureTransformationArn"]
    else:
        out["feature_transformation_arn"] = ""
    return out
