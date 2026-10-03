"""Generated from Smithy shape ``com.amazonaws.s3#Destination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.access_control_translation
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name
    import capo_s3.types.encryption_configuration
    import capo_s3.types.metrics
    import capo_s3.types.replication_time
    import capo_s3.types.storage_class


class Destination(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p> The Amazon Resource Name (ARN) of the bucket where you want Amazon S3 to store the results.</p>"""
    account: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>Destination bucket owner account ID. In a cross-account scenario, if you direct Amazon S3 to change replica ownership to the Amazon Web Services account that owns the destination bucket by specifying the <code>AccessControlTranslation</code> property, this is the account ID of the destination bucket owner. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-change-owner.html">Replication Additional Configuration: Changing the Replica Owner</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    storage_class: NotRequired["capo_s3.types.storage_class.StorageClass"]
    """<p> The storage class to use when replicating objects, such as S3 Standard or reduced redundancy. By default, Amazon S3 uses the storage class of the source object to create the object replica. </p> <p>For valid values, see the <code>StorageClass</code> element of the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTreplication.html">PUT Bucket replication</a> action in the <i>Amazon S3 API Reference</i>.</p> <p> <code>FSX_OPENZFS</code> is not an accepted value when replicating objects.</p>"""
    access_control_translation: NotRequired[
        "capo_s3.types.access_control_translation.AccessControlTranslation"
    ]
    """<p>Specify this only in a cross-account scenario (where source and destination bucket owners are not the same), and you want to change replica ownership to the Amazon Web Services account that owns the destination bucket. If this is not specified in the replication configuration, the replicas are owned by same Amazon Web Services account that owns the source object.</p>"""
    encryption_configuration: NotRequired[
        "capo_s3.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>A container that provides information about encryption. If <code>SourceSelectionCriteria</code> is specified, you must specify this element.</p>"""
    replication_time: NotRequired["capo_s3.types.replication_time.ReplicationTime"]
    """<p> A container specifying S3 Replication Time Control (S3 RTC), including whether S3 RTC is enabled and the time when all objects and operations on objects must be replicated. Must be specified together with a <code>Metrics</code> block. </p>"""
    metrics: NotRequired["capo_s3.types.metrics.Metrics"]
    """<p> A container specifying replication metrics-related settings enabling replication metrics and events. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: Destination, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Bucket").text = str(value["bucket"])
    if "account" in value:
        SubElement(el, "Account").text = str(value["account"])
    if "storage_class" in value:
        import capo_s3.types.storage_class

        capo_s3.types.storage_class.serialize_xml(
            value["storage_class"], el, "StorageClass"
        )
    if "access_control_translation" in value:
        import capo_s3.types.access_control_translation

        capo_s3.types.access_control_translation.serialize_xml(
            value["access_control_translation"], el, "AccessControlTranslation"
        )
    if "encryption_configuration" in value:
        import capo_s3.types.encryption_configuration

        capo_s3.types.encryption_configuration.serialize_xml(
            value["encryption_configuration"], el, "EncryptionConfiguration"
        )
    if "replication_time" in value:
        import capo_s3.types.replication_time

        capo_s3.types.replication_time.serialize_xml(
            value["replication_time"], el, "ReplicationTime"
        )
    if "metrics" in value:
        import capo_s3.types.metrics

        capo_s3.types.metrics.serialize_xml(value["metrics"], el, "Metrics")


def deserialize_xml(el: Element) -> Destination:
    out: Destination = {}  # type: ignore[typeddict-item]
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    else:
        raise DeserializationError("Destination.bucket required")
    child_account = el.find("Account")
    if child_account is not None:
        out["account"] = str(child_account.text or "")
    child_storage_class = el.find("StorageClass")
    if child_storage_class is not None:
        import capo_s3.types.storage_class

        out["storage_class"] = capo_s3.types.storage_class.deserialize_xml(
            child_storage_class
        )
    child_access_control_translation = el.find("AccessControlTranslation")
    if child_access_control_translation is not None:
        import capo_s3.types.access_control_translation

        out["access_control_translation"] = (
            capo_s3.types.access_control_translation.deserialize_xml(
                child_access_control_translation
            )
        )
    child_encryption_configuration = el.find("EncryptionConfiguration")
    if child_encryption_configuration is not None:
        import capo_s3.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_s3.types.encryption_configuration.deserialize_xml(
                child_encryption_configuration
            )
        )
    child_replication_time = el.find("ReplicationTime")
    if child_replication_time is not None:
        import capo_s3.types.replication_time

        out["replication_time"] = capo_s3.types.replication_time.deserialize_xml(
            child_replication_time
        )
    child_metrics = el.find("Metrics")
    if child_metrics is not None:
        import capo_s3.types.metrics

        out["metrics"] = capo_s3.types.metrics.deserialize_xml(child_metrics)
    return out
