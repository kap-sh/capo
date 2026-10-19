"""Generated from Smithy shape ``com.amazonaws.s3control#Destination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.access_control_translation
    import capo_s3_control.types.account_id
    import capo_s3_control.types.bucket_identifier_string
    import capo_s3_control.types.encryption_configuration
    import capo_s3_control.types.metrics
    import capo_s3_control.types.replication_storage_class
    import capo_s3_control.types.replication_time


class Destination(TypedDict, closed=True):
    account: NotRequired["capo_s3_control.types.account_id.AccountId"]
    """<p>The destination bucket owner's account ID. </p>"""
    bucket: "capo_s3_control.types.bucket_identifier_string.BucketIdentifierString"
    """<p>The Amazon Resource Name (ARN) of the access point for the destination bucket where you want S3 on Outposts to store the replication results.</p>"""
    replication_time: NotRequired[
        "capo_s3_control.types.replication_time.ReplicationTime"
    ]
    """<p>A container that specifies S3 Replication Time Control (S3 RTC) settings, including whether S3 RTC is enabled and the time when all objects and operations on objects must be replicated. Must be specified together with a <code>Metrics</code> block. </p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>"""
    access_control_translation: NotRequired[
        "capo_s3_control.types.access_control_translation.AccessControlTranslation"
    ]
    """<p>Specify this property only in a cross-account scenario (where the source and destination bucket owners are not the same), and you want to change replica ownership to the Amazon Web Services account that owns the destination bucket. If this property is not specified in the replication configuration, the replicas are owned by same Amazon Web Services account that owns the source object.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>"""
    encryption_configuration: NotRequired[
        "capo_s3_control.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>A container that provides information about encryption. If <code>SourceSelectionCriteria</code> is specified, you must specify this element.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>"""
    metrics: NotRequired["capo_s3_control.types.metrics.Metrics"]
    """<p> A container that specifies replication metrics-related settings. </p>"""
    storage_class: NotRequired[
        "capo_s3_control.types.replication_storage_class.ReplicationStorageClass"
    ]
    """<p> The storage class to use when replicating objects. All objects stored on S3 on Outposts are stored in the <code>OUTPOSTS</code> storage class. S3 on Outposts uses the <code>OUTPOSTS</code> storage class to create the object replicas. </p> <note> <p>Values other than <code>OUTPOSTS</code> aren't supported by Amazon S3 on Outposts. </p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: Destination, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "account" in value:
        SubElement(el, "Account").text = str(value["account"])
    SubElement(el, "Bucket").text = str(value["bucket"])
    if "replication_time" in value:
        import capo_s3_control.types.replication_time

        capo_s3_control.types.replication_time.serialize_xml(
            value["replication_time"], el, "ReplicationTime"
        )
    if "access_control_translation" in value:
        import capo_s3_control.types.access_control_translation

        capo_s3_control.types.access_control_translation.serialize_xml(
            value["access_control_translation"], el, "AccessControlTranslation"
        )
    if "encryption_configuration" in value:
        import capo_s3_control.types.encryption_configuration

        capo_s3_control.types.encryption_configuration.serialize_xml(
            value["encryption_configuration"], el, "EncryptionConfiguration"
        )
    if "metrics" in value:
        import capo_s3_control.types.metrics

        capo_s3_control.types.metrics.serialize_xml(value["metrics"], el, "Metrics")
    if "storage_class" in value:
        import capo_s3_control.types.replication_storage_class

        capo_s3_control.types.replication_storage_class.serialize_xml(
            value["storage_class"], el, "StorageClass"
        )


def deserialize_xml(el: Element) -> Destination:
    out: Destination = {}  # type: ignore[typeddict-item]
    child_account = el.find("Account")
    if child_account is not None:
        out["account"] = str(child_account.text or "")
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    else:
        out["bucket"] = ""
    child_replication_time = el.find("ReplicationTime")
    if child_replication_time is not None:
        import capo_s3_control.types.replication_time

        out["replication_time"] = (
            capo_s3_control.types.replication_time.deserialize_xml(
                child_replication_time
            )
        )
    child_access_control_translation = el.find("AccessControlTranslation")
    if child_access_control_translation is not None:
        import capo_s3_control.types.access_control_translation

        out["access_control_translation"] = (
            capo_s3_control.types.access_control_translation.deserialize_xml(
                child_access_control_translation
            )
        )
    child_encryption_configuration = el.find("EncryptionConfiguration")
    if child_encryption_configuration is not None:
        import capo_s3_control.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_s3_control.types.encryption_configuration.deserialize_xml(
                child_encryption_configuration
            )
        )
    child_metrics = el.find("Metrics")
    if child_metrics is not None:
        import capo_s3_control.types.metrics

        out["metrics"] = capo_s3_control.types.metrics.deserialize_xml(child_metrics)
    child_storage_class = el.find("StorageClass")
    if child_storage_class is not None:
        import capo_s3_control.types.replication_storage_class

        out["storage_class"] = (
            capo_s3_control.types.replication_storage_class.deserialize_xml(
                child_storage_class
            )
        )
    return out
