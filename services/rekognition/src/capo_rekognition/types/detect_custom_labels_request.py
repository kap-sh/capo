"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectCustomLabelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.image
    import capo_rekognition.types.percent
    import capo_rekognition.types.project_version_arn
    import capo_rekognition.types.u_integer


class DetectCustomLabelsRequest(TypedDict, closed=True):
    project_version_arn: "capo_rekognition.types.project_version_arn.ProjectVersionArn"
    """<p>The ARN of the model version that you want to use. Only models associated with Custom Labels projects accepted by the operation. If a provided ARN refers to a model version associated with a project for a different feature type, then an InvalidParameterException is returned.</p>"""
    image: "capo_rekognition.types.image.Image"
    max_results: NotRequired["capo_rekognition.types.u_integer.UInteger"]
    """<p>Maximum number of results you want the service to return in the response. The service returns the specified number of highest confidence labels ranked from highest confidence to lowest.</p>"""
    min_confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>Specifies the minimum confidence level for the labels to return. <code>DetectCustomLabels</code> doesn't return any labels with a confidence value that's lower than this specified value. If you specify a value of 0, <code>DetectCustomLabels</code> returns all labels, regardless of the assumed threshold applied to each label. If you don't specify a value for <code>MinConfidence</code>, <code>DetectCustomLabels</code> returns labels based on the assumed threshold of each label.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectCustomLabelsRequest) -> dict:
    out: dict = {}
    out["ProjectVersionArn"] = value["project_version_arn"]
    import capo_rekognition.types.image

    out["Image"] = capo_rekognition.types.image.serialize_aws_json_1_1(value["image"])
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "min_confidence" in value:
        out["MinConfidence"] = (
            "NaN"
            if value["min_confidence"] != value["min_confidence"]
            else "Infinity"
            if value["min_confidence"] == float("inf")
            else "-Infinity"
            if value["min_confidence"] == float("-inf")
            else value["min_confidence"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectCustomLabelsRequest:
    out: DetectCustomLabelsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProjectVersionArn") is not None:
        out["project_version_arn"] = data["ProjectVersionArn"]
    else:
        out["project_version_arn"] = ""
    if data.get("Image") is not None:
        import capo_rekognition.types.image

        out["image"] = capo_rekognition.types.image.deserialize_aws_json_1_1(
            data["Image"]
        )
    else:
        raise DeserializationError("DetectCustomLabelsRequest.image required")
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("MinConfidence") is not None:
        out["min_confidence"] = float(data["MinConfidence"])
    return out
