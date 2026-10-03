"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectFacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.attributes
    import capo_rekognition.types.image


class DetectFacesRequest(TypedDict, closed=True):
    image: "capo_rekognition.types.image.Image"
    """<p>The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported. </p> <p>If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the <code>Bytes</code> field. For more information, see Images in the Amazon Rekognition developer guide.</p>"""
    attributes: NotRequired["capo_rekognition.types.attributes.Attributes"]
    """<p>An array of facial attributes you want to be returned. A <code>DEFAULT</code> subset of facial attributes - <code>BoundingBox</code>, <code>Confidence</code>, <code>Pose</code>, <code>Quality</code>, and <code>Landmarks</code> - will always be returned. You can request for specific facial attributes (in addition to the default list) - by using [<code>"DEFAULT", "FACE_OCCLUDED"</code>] or just [<code>"FACE_OCCLUDED"</code>]. You can request for all facial attributes by using [<code>"ALL"]</code>. Requesting more attributes may increase response time.</p> <p>If you provide both, <code>["ALL", "DEFAULT"]</code>, the service uses a logical "AND" operator to determine which attributes to return (in this case, all attributes). </p> <p>Note that while the FaceOccluded and EyeDirection attributes are supported when using <code>DetectFaces</code>, they aren't supported when analyzing videos with <code>StartFaceDetection</code> and <code>GetFaceDetection</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectFacesRequest) -> dict:
    out: dict = {}
    import capo_rekognition.types.image

    out["Image"] = capo_rekognition.types.image.serialize_aws_json_1_1(value["image"])
    if "attributes" in value:
        import capo_rekognition.types.attributes

        out["Attributes"] = capo_rekognition.types.attributes.serialize_aws_json_1_1(
            value["attributes"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectFacesRequest:
    out: DetectFacesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Image") is not None:
        import capo_rekognition.types.image

        out["image"] = capo_rekognition.types.image.deserialize_aws_json_1_1(
            data["Image"]
        )
    else:
        raise DeserializationError("DetectFacesRequest.image required")
    if data.get("Attributes") is not None:
        import capo_rekognition.types.attributes

        out["attributes"] = capo_rekognition.types.attributes.deserialize_aws_json_1_1(
            data["Attributes"]
        )
    return out
