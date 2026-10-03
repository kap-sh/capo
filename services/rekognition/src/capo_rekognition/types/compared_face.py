"""Generated from Smithy shape ``com.amazonaws.rekognition#ComparedFace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.bounding_box
    import capo_rekognition.types.emotions
    import capo_rekognition.types.image_quality
    import capo_rekognition.types.landmarks
    import capo_rekognition.types.percent
    import capo_rekognition.types.pose
    import capo_rekognition.types.smile


class ComparedFace(TypedDict, closed=True):
    bounding_box: NotRequired["capo_rekognition.types.bounding_box.BoundingBox"]
    """<p>Bounding box of the face.</p>"""
    confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>Level of confidence that what the bounding box contains is a face.</p>"""
    landmarks: NotRequired["capo_rekognition.types.landmarks.Landmarks"]
    """<p>An array of facial landmarks.</p>"""
    pose: NotRequired["capo_rekognition.types.pose.Pose"]
    """<p>Indicates the pose of the face as determined by its pitch, roll, and yaw.</p>"""
    quality: NotRequired["capo_rekognition.types.image_quality.ImageQuality"]
    """<p>Identifies face image brightness and sharpness. </p>"""
    emotions: NotRequired["capo_rekognition.types.emotions.Emotions"]
    """<p> The emotions that appear to be expressed on the face, and the confidence level in the determination. Valid values include "Happy", "Sad", "Angry", "Confused", "Disgusted", "Surprised", "Calm", "Unknown", and "Fear". </p>"""
    smile: NotRequired["capo_rekognition.types.smile.Smile"]
    """<p> Indicates whether or not the face is smiling, and the confidence level in the determination. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComparedFace) -> dict:
    out: dict = {}
    if "bounding_box" in value:
        import capo_rekognition.types.bounding_box

        out["BoundingBox"] = capo_rekognition.types.bounding_box.serialize_aws_json_1_1(
            value["bounding_box"]
        )
    if "confidence" in value:
        out["Confidence"] = (
            "NaN"
            if value["confidence"] != value["confidence"]
            else "Infinity"
            if value["confidence"] == float("inf")
            else "-Infinity"
            if value["confidence"] == float("-inf")
            else value["confidence"]
        )
    if "landmarks" in value:
        import capo_rekognition.types.landmarks

        out["Landmarks"] = capo_rekognition.types.landmarks.serialize_aws_json_1_1(
            value["landmarks"]
        )
    if "pose" in value:
        import capo_rekognition.types.pose

        out["Pose"] = capo_rekognition.types.pose.serialize_aws_json_1_1(value["pose"])
    if "quality" in value:
        import capo_rekognition.types.image_quality

        out["Quality"] = capo_rekognition.types.image_quality.serialize_aws_json_1_1(
            value["quality"]
        )
    if "emotions" in value:
        import capo_rekognition.types.emotions

        out["Emotions"] = capo_rekognition.types.emotions.serialize_aws_json_1_1(
            value["emotions"]
        )
    if "smile" in value:
        import capo_rekognition.types.smile

        out["Smile"] = capo_rekognition.types.smile.serialize_aws_json_1_1(
            value["smile"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ComparedFace:
    out: ComparedFace = {}  # type: ignore[typeddict-item]
    if data.get("BoundingBox") is not None:
        import capo_rekognition.types.bounding_box

        out["bounding_box"] = (
            capo_rekognition.types.bounding_box.deserialize_aws_json_1_1(
                data["BoundingBox"]
            )
        )
    if data.get("Confidence") is not None:
        out["confidence"] = float(data["Confidence"])
    if data.get("Landmarks") is not None:
        import capo_rekognition.types.landmarks

        out["landmarks"] = capo_rekognition.types.landmarks.deserialize_aws_json_1_1(
            data["Landmarks"]
        )
    if data.get("Pose") is not None:
        import capo_rekognition.types.pose

        out["pose"] = capo_rekognition.types.pose.deserialize_aws_json_1_1(data["Pose"])
    if data.get("Quality") is not None:
        import capo_rekognition.types.image_quality

        out["quality"] = capo_rekognition.types.image_quality.deserialize_aws_json_1_1(
            data["Quality"]
        )
    if data.get("Emotions") is not None:
        import capo_rekognition.types.emotions

        out["emotions"] = capo_rekognition.types.emotions.deserialize_aws_json_1_1(
            data["Emotions"]
        )
    if data.get("Smile") is not None:
        import capo_rekognition.types.smile

        out["smile"] = capo_rekognition.types.smile.deserialize_aws_json_1_1(
            data["Smile"]
        )
    return out
