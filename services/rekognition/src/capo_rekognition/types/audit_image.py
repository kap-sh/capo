"""Generated from Smithy shape ``com.amazonaws.rekognition#AuditImage``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.bounding_box
    import capo_rekognition.types.liveness_image_blob
    import capo_rekognition.types.s3_object


class AuditImage(TypedDict, closed=True):
    bytes: NotRequired["capo_rekognition.types.liveness_image_blob.LivenessImageBlob"]
    """<p>The Base64-encoded bytes representing an image selected from the Face Liveness video and returned for audit purposes.</p>"""
    s3_object: NotRequired["capo_rekognition.types.s3_object.S3Object"]
    bounding_box: NotRequired["capo_rekognition.types.bounding_box.BoundingBox"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuditImage) -> dict:
    out: dict = {}
    if "bytes" in value:
        import capo_rekognition.types.liveness_image_blob

        out["Bytes"] = (
            capo_rekognition.types.liveness_image_blob.serialize_aws_json_1_1(
                value["bytes"]
            )
        )
    if "s3_object" in value:
        import capo_rekognition.types.s3_object

        out["S3Object"] = capo_rekognition.types.s3_object.serialize_aws_json_1_1(
            value["s3_object"]
        )
    if "bounding_box" in value:
        import capo_rekognition.types.bounding_box

        out["BoundingBox"] = capo_rekognition.types.bounding_box.serialize_aws_json_1_1(
            value["bounding_box"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AuditImage:
    out: AuditImage = {}  # type: ignore[typeddict-item]
    if data.get("Bytes") is not None:
        import capo_rekognition.types.liveness_image_blob

        out["bytes"] = (
            capo_rekognition.types.liveness_image_blob.deserialize_aws_json_1_1(
                data["Bytes"]
            )
        )
    if data.get("S3Object") is not None:
        import capo_rekognition.types.s3_object

        out["s3_object"] = capo_rekognition.types.s3_object.deserialize_aws_json_1_1(
            data["S3Object"]
        )
    if data.get("BoundingBox") is not None:
        import capo_rekognition.types.bounding_box

        out["bounding_box"] = (
            capo_rekognition.types.bounding_box.deserialize_aws_json_1_1(
                data["BoundingBox"]
            )
        )
    return out


def redact_sensitive(value: AuditImage) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "bytes" in value:
        out["bytes"] = "*** Sensitive Data Redacted ***"
    return out
