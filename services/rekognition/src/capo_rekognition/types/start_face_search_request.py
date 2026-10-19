"""Generated from Smithy shape ``com.amazonaws.rekognition#StartFaceSearchRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.client_request_token
    import capo_rekognition.types.collection_id
    import capo_rekognition.types.job_tag
    import capo_rekognition.types.notification_channel
    import capo_rekognition.types.percent
    import capo_rekognition.types.video


class StartFaceSearchRequest(TypedDict, closed=True):
    video: "capo_rekognition.types.video.Video"
    """<p>The video you want to search. The video must be stored in an Amazon S3 bucket. </p>"""
    client_request_token: NotRequired[
        "capo_rekognition.types.client_request_token.ClientRequestToken"
    ]
    """<p>Idempotent token used to identify the start request. If you use the same token with multiple <code>StartFaceSearch</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidently started more than once. </p>"""
    face_match_threshold: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>The minimum confidence in the person match to return. For example, don't return any matches where confidence in matches is less than 70%. The default value is 80%.</p>"""
    collection_id: "capo_rekognition.types.collection_id.CollectionId"
    """<p>ID of the collection that contains the faces you want to search for.</p>"""
    notification_channel: NotRequired[
        "capo_rekognition.types.notification_channel.NotificationChannel"
    ]
    """<p>The ARN of the Amazon SNS topic to which you want Amazon Rekognition Video to publish the completion status of the search. The Amazon SNS topic must have a topic name that begins with <i>AmazonRekognition</i> if you are using the AmazonRekognitionServiceRole permissions policy to access the topic.</p>"""
    job_tag: NotRequired["capo_rekognition.types.job_tag.JobTag"]
    """<p>An identifier you specify that's returned in the completion notification that's published to your Amazon Simple Notification Service topic. For example, you can use <code>JobTag</code> to group related jobs and identify them in the completion notification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartFaceSearchRequest) -> dict:
    out: dict = {}
    import capo_rekognition.types.video

    out["Video"] = capo_rekognition.types.video.serialize_aws_json_1_1(value["video"])
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "face_match_threshold" in value:
        out["FaceMatchThreshold"] = (
            "NaN"
            if value["face_match_threshold"] != value["face_match_threshold"]
            else "Infinity"
            if value["face_match_threshold"] == float("inf")
            else "-Infinity"
            if value["face_match_threshold"] == float("-inf")
            else value["face_match_threshold"]
        )
    out["CollectionId"] = value["collection_id"]
    if "notification_channel" in value:
        import capo_rekognition.types.notification_channel

        out["NotificationChannel"] = (
            capo_rekognition.types.notification_channel.serialize_aws_json_1_1(
                value["notification_channel"]
            )
        )
    if "job_tag" in value:
        out["JobTag"] = value["job_tag"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartFaceSearchRequest:
    out: StartFaceSearchRequest = {}  # type: ignore[typeddict-item]
    if data.get("Video") is not None:
        import capo_rekognition.types.video

        out["video"] = capo_rekognition.types.video.deserialize_aws_json_1_1(
            data["Video"]
        )
    else:
        raise DeserializationError("StartFaceSearchRequest.video required")
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("FaceMatchThreshold") is not None:
        out["face_match_threshold"] = float(data["FaceMatchThreshold"])
    if data.get("CollectionId") is not None:
        out["collection_id"] = data["CollectionId"]
    else:
        out["collection_id"] = ""
    if data.get("NotificationChannel") is not None:
        import capo_rekognition.types.notification_channel

        out["notification_channel"] = (
            capo_rekognition.types.notification_channel.deserialize_aws_json_1_1(
                data["NotificationChannel"]
            )
        )
    if data.get("JobTag") is not None:
        out["job_tag"] = data["JobTag"]
    return out
