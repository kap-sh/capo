"""Generated from Smithy shape ``com.amazonaws.rekognition#FaceDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.age_range
    import capo_rekognition.types.beard
    import capo_rekognition.types.bounding_box
    import capo_rekognition.types.emotions
    import capo_rekognition.types.eye_direction
    import capo_rekognition.types.eye_open
    import capo_rekognition.types.eyeglasses
    import capo_rekognition.types.face_occluded
    import capo_rekognition.types.gender
    import capo_rekognition.types.image_quality
    import capo_rekognition.types.landmarks
    import capo_rekognition.types.mouth_open
    import capo_rekognition.types.mustache
    import capo_rekognition.types.percent
    import capo_rekognition.types.pose
    import capo_rekognition.types.smile
    import capo_rekognition.types.sunglasses


class FaceDetail(TypedDict, closed=True):
    bounding_box: NotRequired["capo_rekognition.types.bounding_box.BoundingBox"]
    """<p>Bounding box of the face. Default attribute.</p>"""
    age_range: NotRequired["capo_rekognition.types.age_range.AgeRange"]
    """<p>The estimated age range, in years, for the face. Low represents the lowest estimated age and High represents the highest estimated age.</p>"""
    smile: NotRequired["capo_rekognition.types.smile.Smile"]
    """<p>Indicates whether or not the face is smiling, and the confidence level in the determination.</p>"""
    eyeglasses: NotRequired["capo_rekognition.types.eyeglasses.Eyeglasses"]
    """<p>Indicates whether or not the face is wearing eye glasses, and the confidence level in the determination.</p>"""
    sunglasses: NotRequired["capo_rekognition.types.sunglasses.Sunglasses"]
    """<p>Indicates whether or not the face is wearing sunglasses, and the confidence level in the determination.</p>"""
    gender: NotRequired["capo_rekognition.types.gender.Gender"]
    """<p>The predicted gender of a detected face. </p>"""
    beard: NotRequired["capo_rekognition.types.beard.Beard"]
    """<p>Indicates whether or not the face has a beard, and the confidence level in the determination.</p>"""
    mustache: NotRequired["capo_rekognition.types.mustache.Mustache"]
    """<p>Indicates whether or not the face has a mustache, and the confidence level in the determination.</p>"""
    eyes_open: NotRequired["capo_rekognition.types.eye_open.EyeOpen"]
    """<p>Indicates whether or not the eyes on the face are open, and the confidence level in the determination.</p>"""
    mouth_open: NotRequired["capo_rekognition.types.mouth_open.MouthOpen"]
    """<p>Indicates whether or not the mouth on the face is open, and the confidence level in the determination.</p>"""
    emotions: NotRequired["capo_rekognition.types.emotions.Emotions"]
    """<p>The emotions that appear to be expressed on the face, and the confidence level in the determination. The API is only making a determination of the physical appearance of a person's face. It is not a determination of the person’s internal emotional state and should not be used in such a way. For example, a person pretending to have a sad face might not be sad emotionally.</p>"""
    landmarks: NotRequired["capo_rekognition.types.landmarks.Landmarks"]
    """<p>Indicates the location of landmarks on the face. Default attribute.</p>"""
    pose: NotRequired["capo_rekognition.types.pose.Pose"]
    """<p>Indicates the pose of the face as determined by its pitch, roll, and yaw. Default attribute.</p>"""
    quality: NotRequired["capo_rekognition.types.image_quality.ImageQuality"]
    """<p>Identifies image brightness and sharpness. Default attribute.</p>"""
    confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>Confidence level that the bounding box contains a face (and not a different object such as a tree). Default attribute.</p>"""
    face_occluded: NotRequired["capo_rekognition.types.face_occluded.FaceOccluded"]
    """<p> <code>FaceOccluded</code> should return "true" with a high confidence score if a detected face’s eyes, nose, and mouth are partially captured or if they are covered by masks, dark sunglasses, cell phones, hands, or other objects. <code>FaceOccluded</code> should return "false" with a high confidence score if common occurrences that do not impact face verification are detected, such as eye glasses, lightly tinted sunglasses, strands of hair, and others. </p>"""
    eye_direction: NotRequired["capo_rekognition.types.eye_direction.EyeDirection"]
    """<p>Indicates the direction the eyes are gazing in, as defined by pitch and yaw.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FaceDetail) -> dict:
    out: dict = {}
    if "bounding_box" in value:
        import capo_rekognition.types.bounding_box

        out["BoundingBox"] = capo_rekognition.types.bounding_box.serialize_aws_json_1_1(
            value["bounding_box"]
        )
    if "age_range" in value:
        import capo_rekognition.types.age_range

        out["AgeRange"] = capo_rekognition.types.age_range.serialize_aws_json_1_1(
            value["age_range"]
        )
    if "smile" in value:
        import capo_rekognition.types.smile

        out["Smile"] = capo_rekognition.types.smile.serialize_aws_json_1_1(
            value["smile"]
        )
    if "eyeglasses" in value:
        import capo_rekognition.types.eyeglasses

        out["Eyeglasses"] = capo_rekognition.types.eyeglasses.serialize_aws_json_1_1(
            value["eyeglasses"]
        )
    if "sunglasses" in value:
        import capo_rekognition.types.sunglasses

        out["Sunglasses"] = capo_rekognition.types.sunglasses.serialize_aws_json_1_1(
            value["sunglasses"]
        )
    if "gender" in value:
        import capo_rekognition.types.gender

        out["Gender"] = capo_rekognition.types.gender.serialize_aws_json_1_1(
            value["gender"]
        )
    if "beard" in value:
        import capo_rekognition.types.beard

        out["Beard"] = capo_rekognition.types.beard.serialize_aws_json_1_1(
            value["beard"]
        )
    if "mustache" in value:
        import capo_rekognition.types.mustache

        out["Mustache"] = capo_rekognition.types.mustache.serialize_aws_json_1_1(
            value["mustache"]
        )
    if "eyes_open" in value:
        import capo_rekognition.types.eye_open

        out["EyesOpen"] = capo_rekognition.types.eye_open.serialize_aws_json_1_1(
            value["eyes_open"]
        )
    if "mouth_open" in value:
        import capo_rekognition.types.mouth_open

        out["MouthOpen"] = capo_rekognition.types.mouth_open.serialize_aws_json_1_1(
            value["mouth_open"]
        )
    if "emotions" in value:
        import capo_rekognition.types.emotions

        out["Emotions"] = capo_rekognition.types.emotions.serialize_aws_json_1_1(
            value["emotions"]
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
    if "face_occluded" in value:
        import capo_rekognition.types.face_occluded

        out["FaceOccluded"] = (
            capo_rekognition.types.face_occluded.serialize_aws_json_1_1(
                value["face_occluded"]
            )
        )
    if "eye_direction" in value:
        import capo_rekognition.types.eye_direction

        out["EyeDirection"] = (
            capo_rekognition.types.eye_direction.serialize_aws_json_1_1(
                value["eye_direction"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FaceDetail:
    out: FaceDetail = {}  # type: ignore[typeddict-item]
    if data.get("BoundingBox") is not None:
        import capo_rekognition.types.bounding_box

        out["bounding_box"] = (
            capo_rekognition.types.bounding_box.deserialize_aws_json_1_1(
                data["BoundingBox"]
            )
        )
    if data.get("AgeRange") is not None:
        import capo_rekognition.types.age_range

        out["age_range"] = capo_rekognition.types.age_range.deserialize_aws_json_1_1(
            data["AgeRange"]
        )
    if data.get("Smile") is not None:
        import capo_rekognition.types.smile

        out["smile"] = capo_rekognition.types.smile.deserialize_aws_json_1_1(
            data["Smile"]
        )
    if data.get("Eyeglasses") is not None:
        import capo_rekognition.types.eyeglasses

        out["eyeglasses"] = capo_rekognition.types.eyeglasses.deserialize_aws_json_1_1(
            data["Eyeglasses"]
        )
    if data.get("Sunglasses") is not None:
        import capo_rekognition.types.sunglasses

        out["sunglasses"] = capo_rekognition.types.sunglasses.deserialize_aws_json_1_1(
            data["Sunglasses"]
        )
    if data.get("Gender") is not None:
        import capo_rekognition.types.gender

        out["gender"] = capo_rekognition.types.gender.deserialize_aws_json_1_1(
            data["Gender"]
        )
    if data.get("Beard") is not None:
        import capo_rekognition.types.beard

        out["beard"] = capo_rekognition.types.beard.deserialize_aws_json_1_1(
            data["Beard"]
        )
    if data.get("Mustache") is not None:
        import capo_rekognition.types.mustache

        out["mustache"] = capo_rekognition.types.mustache.deserialize_aws_json_1_1(
            data["Mustache"]
        )
    if data.get("EyesOpen") is not None:
        import capo_rekognition.types.eye_open

        out["eyes_open"] = capo_rekognition.types.eye_open.deserialize_aws_json_1_1(
            data["EyesOpen"]
        )
    if data.get("MouthOpen") is not None:
        import capo_rekognition.types.mouth_open

        out["mouth_open"] = capo_rekognition.types.mouth_open.deserialize_aws_json_1_1(
            data["MouthOpen"]
        )
    if data.get("Emotions") is not None:
        import capo_rekognition.types.emotions

        out["emotions"] = capo_rekognition.types.emotions.deserialize_aws_json_1_1(
            data["Emotions"]
        )
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
    if data.get("Confidence") is not None:
        out["confidence"] = float(data["Confidence"])
    if data.get("FaceOccluded") is not None:
        import capo_rekognition.types.face_occluded

        out["face_occluded"] = (
            capo_rekognition.types.face_occluded.deserialize_aws_json_1_1(
                data["FaceOccluded"]
            )
        )
    if data.get("EyeDirection") is not None:
        import capo_rekognition.types.eye_direction

        out["eye_direction"] = (
            capo_rekognition.types.eye_direction.deserialize_aws_json_1_1(
                data["EyeDirection"]
            )
        )
    return out
