"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectLabelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.detect_labels_feature_list
    import capo_rekognition.types.detect_labels_settings
    import capo_rekognition.types.image
    import capo_rekognition.types.percent
    import capo_rekognition.types.u_integer


class DetectLabelsRequest(TypedDict, closed=True):
    image: "capo_rekognition.types.image.Image"
    """<p>The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. Images stored in an S3 Bucket do not need to be base64-encoded.</p> <p>If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the <code>Bytes</code> field. For more information, see Images in the Amazon Rekognition developer guide.</p>"""
    max_labels: NotRequired["capo_rekognition.types.u_integer.UInteger"]
    """<p>Maximum number of labels you want the service to return in the response. The service returns the specified number of highest confidence labels. Only valid when GENERAL_LABELS is specified as a feature type in the Feature input parameter.</p>"""
    min_confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>Specifies the minimum confidence level for the labels to return. Amazon Rekognition doesn't return any labels with confidence lower than this specified value.</p> <p>If <code>MinConfidence</code> is not specified, the operation returns labels with a confidence values greater than or equal to 55 percent. Only valid when GENERAL_LABELS is specified as a feature type in the Feature input parameter.</p>"""
    features: NotRequired[
        "capo_rekognition.types.detect_labels_feature_list.DetectLabelsFeatureList"
    ]
    """<p>A list of the types of analysis to perform. Specifying GENERAL_LABELS uses the label detection feature, while specifying IMAGE_PROPERTIES returns information regarding image color and quality. If no option is specified GENERAL_LABELS is used by default.</p>"""
    settings: NotRequired[
        "capo_rekognition.types.detect_labels_settings.DetectLabelsSettings"
    ]
    """<p>A list of the filters to be applied to returned detected labels and image properties. Specified filters can be inclusive, exclusive, or a combination of both. Filters can be used for individual labels or label categories. The exact label names or label categories must be supplied. For a full list of labels and label categories, see <a href="https://docs.aws.amazon.com/rekognition/latest/dg/labels.html">Detecting labels</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectLabelsRequest) -> dict:
    out: dict = {}
    import capo_rekognition.types.image

    out["Image"] = capo_rekognition.types.image.serialize_aws_json_1_1(value["image"])
    if "max_labels" in value:
        out["MaxLabels"] = value["max_labels"]
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
    if "features" in value:
        import capo_rekognition.types.detect_labels_feature_list

        out["Features"] = (
            capo_rekognition.types.detect_labels_feature_list.serialize_aws_json_1_1(
                value["features"]
            )
        )
    if "settings" in value:
        import capo_rekognition.types.detect_labels_settings

        out["Settings"] = (
            capo_rekognition.types.detect_labels_settings.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectLabelsRequest:
    out: DetectLabelsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Image") is not None:
        import capo_rekognition.types.image

        out["image"] = capo_rekognition.types.image.deserialize_aws_json_1_1(
            data["Image"]
        )
    else:
        raise DeserializationError("DetectLabelsRequest.image required")
    if data.get("MaxLabels") is not None:
        out["max_labels"] = data["MaxLabels"]
    if data.get("MinConfidence") is not None:
        out["min_confidence"] = float(data["MinConfidence"])
    if data.get("Features") is not None:
        import capo_rekognition.types.detect_labels_feature_list

        out["features"] = (
            capo_rekognition.types.detect_labels_feature_list.deserialize_aws_json_1_1(
                data["Features"]
            )
        )
    if data.get("Settings") is not None:
        import capo_rekognition.types.detect_labels_settings

        out["settings"] = (
            capo_rekognition.types.detect_labels_settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    return out
