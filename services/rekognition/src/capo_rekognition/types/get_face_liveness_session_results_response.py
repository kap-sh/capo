"""Generated from Smithy shape ``com.amazonaws.rekognition#GetFaceLivenessSessionResultsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.audit_image
    import capo_rekognition.types.audit_images
    import capo_rekognition.types.challenge
    import capo_rekognition.types.feedback_list
    import capo_rekognition.types.liveness_session_id
    import capo_rekognition.types.liveness_session_status
    import capo_rekognition.types.percent
    import capo_rekognition.types.session_metadata


class GetFaceLivenessSessionResultsResponse(TypedDict, closed=True):
    session_id: "capo_rekognition.types.liveness_session_id.LivenessSessionId"
    """<p>The sessionId for which this request was called.</p>"""
    status: "capo_rekognition.types.liveness_session_status.LivenessSessionStatus"
    """<p>Represents a status corresponding to the state of the session. Possible statuses are: CREATED, IN_PROGRESS, SUCCEEDED, FAILED, EXPIRED.</p>"""
    confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>Probabalistic confidence score for if the person in the given video was live, represented as a float value between 0 to 100.</p>"""
    reference_image: NotRequired["capo_rekognition.types.audit_image.AuditImage"]
    """<p>A high-quality image from the Face Liveness video that can be used for face comparison or search. It includes a bounding box of the face and the Base64-encoded bytes that return an image. If the CreateFaceLivenessSession request included an OutputConfig argument, the image will be uploaded to an S3Object specified in the output configuration. In case the reference image is not returned, it's recommended to retry the Liveness check.</p>"""
    audit_images: NotRequired["capo_rekognition.types.audit_images.AuditImages"]
    """<p>A set of images from the Face Liveness video that can be used for audit purposes. It includes a bounding box of the face and the Base64-encoded bytes that return an image. If the CreateFaceLivenessSession request included an OutputConfig argument, the image will be uploaded to an S3Object specified in the output configuration. If no Amazon S3 bucket is defined, raw bytes are sent instead.</p>"""
    challenge: NotRequired["capo_rekognition.types.challenge.Challenge"]
    """<p>Contains information regarding the challenge type used for the Face Liveness check.</p>"""
    feedback: NotRequired["capo_rekognition.types.feedback_list.FeedbackList"]
    """<p>A list of conditions that were detected in the Face Liveness video and that contributed to the returned <code>Confidence</code> score. Each item contains a code and a human-readable message. Feedback is returned only for sessions with a <code>Status</code> of <code>SUCCEEDED</code>, and the list is empty when no such conditions were detected.</p>"""
    metadata: NotRequired["capo_rekognition.types.session_metadata.SessionMetadata"]
    """<p>Metadata about the client that streamed the video for the Face Liveness session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFaceLivenessSessionResultsResponse) -> dict:
    out: dict = {}
    out["SessionId"] = value["session_id"]
    import capo_rekognition.types.liveness_session_status

    out["Status"] = (
        capo_rekognition.types.liveness_session_status.serialize_aws_json_1_1(
            value["status"]
        )
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
    if "reference_image" in value:
        import capo_rekognition.types.audit_image

        out["ReferenceImage"] = (
            capo_rekognition.types.audit_image.serialize_aws_json_1_1(
                value["reference_image"]
            )
        )
    if "audit_images" in value:
        import capo_rekognition.types.audit_images

        out["AuditImages"] = capo_rekognition.types.audit_images.serialize_aws_json_1_1(
            value["audit_images"]
        )
    if "challenge" in value:
        import capo_rekognition.types.challenge

        out["Challenge"] = capo_rekognition.types.challenge.serialize_aws_json_1_1(
            value["challenge"]
        )
    if "feedback" in value:
        import capo_rekognition.types.feedback_list

        out["Feedback"] = capo_rekognition.types.feedback_list.serialize_aws_json_1_1(
            value["feedback"]
        )
    if "metadata" in value:
        import capo_rekognition.types.session_metadata

        out["Metadata"] = (
            capo_rekognition.types.session_metadata.serialize_aws_json_1_1(
                value["metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFaceLivenessSessionResultsResponse:
    out: GetFaceLivenessSessionResultsResponse = {}  # type: ignore[typeddict-item]
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    else:
        raise DeserializationError(
            "GetFaceLivenessSessionResultsResponse.session_id required"
        )
    if data.get("Status") is not None:
        import capo_rekognition.types.liveness_session_status

        out["status"] = (
            capo_rekognition.types.liveness_session_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError(
            "GetFaceLivenessSessionResultsResponse.status required"
        )
    if data.get("Confidence") is not None:
        out["confidence"] = float(data["Confidence"])
    if data.get("ReferenceImage") is not None:
        import capo_rekognition.types.audit_image

        out["reference_image"] = (
            capo_rekognition.types.audit_image.deserialize_aws_json_1_1(
                data["ReferenceImage"]
            )
        )
    if data.get("AuditImages") is not None:
        import capo_rekognition.types.audit_images

        out["audit_images"] = (
            capo_rekognition.types.audit_images.deserialize_aws_json_1_1(
                data["AuditImages"]
            )
        )
    if data.get("Challenge") is not None:
        import capo_rekognition.types.challenge

        out["challenge"] = capo_rekognition.types.challenge.deserialize_aws_json_1_1(
            data["Challenge"]
        )
    if data.get("Feedback") is not None:
        import capo_rekognition.types.feedback_list

        out["feedback"] = capo_rekognition.types.feedback_list.deserialize_aws_json_1_1(
            data["Feedback"]
        )
    if data.get("Metadata") is not None:
        import capo_rekognition.types.session_metadata

        out["metadata"] = (
            capo_rekognition.types.session_metadata.deserialize_aws_json_1_1(
                data["Metadata"]
            )
        )
    return out


def redact_sensitive(value: GetFaceLivenessSessionResultsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "reference_image" in value:
        import capo_rekognition.types.audit_image

        out["reference_image"] = capo_rekognition.types.audit_image.redact_sensitive(
            value["reference_image"]
        )
    if "audit_images" in value:
        import capo_rekognition.types.audit_images

        out["audit_images"] = capo_rekognition.types.audit_images.redact_sensitive(
            value["audit_images"]
        )
    return out
