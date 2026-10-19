"""Generated from Smithy shape ``com.amazonaws.rekognition#StartSegmentDetectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.client_request_token
    import capo_rekognition.types.job_tag
    import capo_rekognition.types.notification_channel
    import capo_rekognition.types.segment_types
    import capo_rekognition.types.start_segment_detection_filters
    import capo_rekognition.types.video


class StartSegmentDetectionRequest(TypedDict, closed=True):
    video: "capo_rekognition.types.video.Video"
    client_request_token: NotRequired[
        "capo_rekognition.types.client_request_token.ClientRequestToken"
    ]
    """<p>Idempotent token used to identify the start request. If you use the same token with multiple <code>StartSegmentDetection</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidently started more than once. </p>"""
    notification_channel: NotRequired[
        "capo_rekognition.types.notification_channel.NotificationChannel"
    ]
    """<p>The ARN of the Amazon SNS topic to which you want Amazon Rekognition Video to publish the completion status of the segment detection operation. Note that the Amazon SNS topic must have a topic name that begins with <i>AmazonRekognition</i> if you are using the AmazonRekognitionServiceRole permissions policy to access the topic.</p>"""
    job_tag: NotRequired["capo_rekognition.types.job_tag.JobTag"]
    """<p>An identifier you specify that's returned in the completion notification that's published to your Amazon Simple Notification Service topic. For example, you can use <code>JobTag</code> to group related jobs and identify them in the completion notification.</p>"""
    filters: NotRequired[
        "capo_rekognition.types.start_segment_detection_filters.StartSegmentDetectionFilters"
    ]
    """<p>Filters for technical cue or shot detection.</p>"""
    segment_types: "capo_rekognition.types.segment_types.SegmentTypes"
    """<p>An array of segment types to detect in the video. Valid values are TECHNICAL_CUE and SHOT.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSegmentDetectionRequest) -> dict:
    out: dict = {}
    import capo_rekognition.types.video

    out["Video"] = capo_rekognition.types.video.serialize_aws_json_1_1(value["video"])
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "notification_channel" in value:
        import capo_rekognition.types.notification_channel

        out["NotificationChannel"] = (
            capo_rekognition.types.notification_channel.serialize_aws_json_1_1(
                value["notification_channel"]
            )
        )
    if "job_tag" in value:
        out["JobTag"] = value["job_tag"]
    if "filters" in value:
        import capo_rekognition.types.start_segment_detection_filters

        out["Filters"] = (
            capo_rekognition.types.start_segment_detection_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    import capo_rekognition.types.segment_types

    out["SegmentTypes"] = capo_rekognition.types.segment_types.serialize_aws_json_1_1(
        value["segment_types"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSegmentDetectionRequest:
    out: StartSegmentDetectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Video") is not None:
        import capo_rekognition.types.video

        out["video"] = capo_rekognition.types.video.deserialize_aws_json_1_1(
            data["Video"]
        )
    else:
        raise DeserializationError("StartSegmentDetectionRequest.video required")
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("NotificationChannel") is not None:
        import capo_rekognition.types.notification_channel

        out["notification_channel"] = (
            capo_rekognition.types.notification_channel.deserialize_aws_json_1_1(
                data["NotificationChannel"]
            )
        )
    if data.get("JobTag") is not None:
        out["job_tag"] = data["JobTag"]
    if data.get("Filters") is not None:
        import capo_rekognition.types.start_segment_detection_filters

        out["filters"] = (
            capo_rekognition.types.start_segment_detection_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("SegmentTypes") is not None:
        import capo_rekognition.types.segment_types

        out["segment_types"] = (
            capo_rekognition.types.segment_types.deserialize_aws_json_1_1(
                data["SegmentTypes"]
            )
        )
    else:
        out["segment_types"] = []
    return out
