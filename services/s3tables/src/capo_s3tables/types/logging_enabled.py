"""Generated from Smithy shape ``com.amazonaws.s3tables#LoggingEnabled``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.logging_target_bucket
    import capo_s3tables.types.logging_target_prefix
    import capo_s3tables.types.target_object_key_format


class LoggingEnabled(TypedDict, closed=True):
    target_bucket: "capo_s3tables.types.logging_target_bucket.LoggingTargetBucket"
    """<p>The name of the general purpose bucket that logs are delivered to. The bucket must be in the same Amazon Web Services Region and owned by the same Amazon Web Services account as the table bucket. The bucket can't use SSE-KMS or DSSE-KMS default encryption, can't have S3 Object Lock enabled, and can't have Requester Pays enabled. You can deliver logs from multiple table buckets to the same target bucket. In this case, choose a different <code>targetPrefix</code> for each table bucket so that you can tell their log objects apart.</p>"""
    target_prefix: "capo_s3tables.types.logging_target_prefix.LoggingTargetPrefix"
    """<p>The prefix for the keys of the log objects that are delivered to the target bucket.</p>"""
    target_object_key_format: (
        "capo_s3tables.types.target_object_key_format.TargetObjectKeyFormat"
    )
    """<p>The key format of the log objects. Log object keys are always partitioned by date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoggingEnabled) -> dict:
    out: dict = {}
    out["targetBucket"] = value["target_bucket"]
    out["targetPrefix"] = value["target_prefix"]
    import capo_s3tables.types.target_object_key_format

    out["targetObjectKeyFormat"] = (
        capo_s3tables.types.target_object_key_format.serialize_json(
            value["target_object_key_format"]
        )
    )
    return out


def deserialize_json(data: dict) -> LoggingEnabled:
    out: LoggingEnabled = {}  # type: ignore[typeddict-item]
    if data.get("targetBucket") is not None:
        out["target_bucket"] = data["targetBucket"]
    else:
        out["target_bucket"] = ""
    if data.get("targetPrefix") is not None:
        out["target_prefix"] = data["targetPrefix"]
    else:
        out["target_prefix"] = ""
    if data.get("targetObjectKeyFormat") is not None:
        import capo_s3tables.types.target_object_key_format

        out["target_object_key_format"] = (
            capo_s3tables.types.target_object_key_format.deserialize_json(
                data["targetObjectKeyFormat"]
            )
        )
    else:
        raise DeserializationError("LoggingEnabled.target_object_key_format required")
    return out
