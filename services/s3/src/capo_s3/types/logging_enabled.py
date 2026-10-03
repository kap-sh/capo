"""Generated from Smithy shape ``com.amazonaws.s3#LoggingEnabled``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.target_bucket
    import capo_s3.types.target_grants
    import capo_s3.types.target_object_key_format
    import capo_s3.types.target_prefix


class LoggingEnabled(TypedDict, closed=True):
    target_bucket: "capo_s3.types.target_bucket.TargetBucket"
    """<p>Specifies the bucket where you want Amazon S3 to store server access logs. You can have your logs delivered to any bucket that you own, including the same bucket that is being logged. You can also configure multiple buckets to deliver their logs to the same target bucket. In this case, you should choose a different <code>TargetPrefix</code> for each source bucket so that the delivered log files can be distinguished by key.</p>"""
    target_grants: NotRequired["capo_s3.types.target_grants.TargetGrants"]
    """<p>Container for granting information.</p> <p>Buckets that use the bucket owner enforced setting for Object Ownership don't support target grants. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html#grant-log-delivery-permissions-general">Permissions for server access log delivery</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    target_prefix: "capo_s3.types.target_prefix.TargetPrefix"
    """<p>A prefix for all log object keys. If you store log files from multiple Amazon S3 buckets in a single bucket, you can use a prefix to distinguish which log files came from which bucket.</p>"""
    target_object_key_format: NotRequired[
        "capo_s3.types.target_object_key_format.TargetObjectKeyFormat"
    ]
    """<p>Amazon S3 key format for log objects.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: LoggingEnabled, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "TargetBucket").text = str(value["target_bucket"])
    if "target_grants" in value:
        import capo_s3.types.target_grants

        capo_s3.types.target_grants.serialize_xml(
            value["target_grants"], el, "TargetGrants"
        )
    SubElement(el, "TargetPrefix").text = str(value["target_prefix"])
    if "target_object_key_format" in value:
        import capo_s3.types.target_object_key_format

        capo_s3.types.target_object_key_format.serialize_xml(
            value["target_object_key_format"], el, "TargetObjectKeyFormat"
        )


def deserialize_xml(el: Element) -> LoggingEnabled:
    out: LoggingEnabled = {}  # type: ignore[typeddict-item]
    child_target_bucket = el.find("TargetBucket")
    if child_target_bucket is not None:
        out["target_bucket"] = str(child_target_bucket.text or "")
    else:
        raise DeserializationError("LoggingEnabled.target_bucket required")
    child_target_grants = el.find("TargetGrants")
    if child_target_grants is not None:
        import capo_s3.types.target_grants

        out["target_grants"] = capo_s3.types.target_grants.deserialize_xml(
            child_target_grants
        )
    child_target_prefix = el.find("TargetPrefix")
    if child_target_prefix is not None:
        out["target_prefix"] = str(child_target_prefix.text or "")
    else:
        raise DeserializationError("LoggingEnabled.target_prefix required")
    child_target_object_key_format = el.find("TargetObjectKeyFormat")
    if child_target_object_key_format is not None:
        import capo_s3.types.target_object_key_format

        out["target_object_key_format"] = (
            capo_s3.types.target_object_key_format.deserialize_xml(
                child_target_object_key_format
            )
        )
    return out
