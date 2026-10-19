"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#TestRoleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.bucket_name
    import capo_elastic_transcoder.types.role
    import capo_elastic_transcoder.types.sns_topics


class TestRoleRequest(TypedDict, closed=True):
    role: "capo_elastic_transcoder.types.role.Role"
    """<p>The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to test.</p>"""
    input_bucket: "capo_elastic_transcoder.types.bucket_name.BucketName"
    """<p>The Amazon S3 bucket that contains media files to be transcoded. The action attempts to read from this bucket.</p>"""
    output_bucket: "capo_elastic_transcoder.types.bucket_name.BucketName"
    """<p>The Amazon S3 bucket that Elastic Transcoder writes transcoded media files to. The action attempts to read from this bucket.</p>"""
    topics: "capo_elastic_transcoder.types.sns_topics.SnsTopics"
    """<p>The ARNs of one or more Amazon Simple Notification Service (Amazon SNS) topics that you want the action to send a test notification to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestRoleRequest) -> dict:
    out: dict = {}
    out["Role"] = value["role"]
    out["InputBucket"] = value["input_bucket"]
    out["OutputBucket"] = value["output_bucket"]
    import capo_elastic_transcoder.types.sns_topics

    out["Topics"] = capo_elastic_transcoder.types.sns_topics.serialize_json(
        value["topics"]
    )
    return out


def deserialize_json(data: dict) -> TestRoleRequest:
    out: TestRoleRequest = {}  # type: ignore[typeddict-item]
    if data.get("Role") is not None:
        out["role"] = data["Role"]
    else:
        out["role"] = ""
    if data.get("InputBucket") is not None:
        out["input_bucket"] = data["InputBucket"]
    else:
        out["input_bucket"] = ""
    if data.get("OutputBucket") is not None:
        out["output_bucket"] = data["OutputBucket"]
    else:
        out["output_bucket"] = ""
    if data.get("Topics") is not None:
        import capo_elastic_transcoder.types.sns_topics

        out["topics"] = capo_elastic_transcoder.types.sns_topics.deserialize_json(
            data["Topics"]
        )
    else:
        out["topics"] = []
    return out
