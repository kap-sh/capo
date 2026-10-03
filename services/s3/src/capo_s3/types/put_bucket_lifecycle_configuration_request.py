"""Generated from Smithy shape ``com.amazonaws.s3#PutBucketLifecycleConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_lifecycle_configuration
    import capo_s3.types.bucket_name
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.transition_default_minimum_object_size


class PutBucketLifecycleConfigurationRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The name of the bucket for which to set the configuration.</p>"""
    checksum_algorithm: NotRequired[
        "capo_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p>Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any additional functionality if you don't use the SDK. When you send this header, there must be a corresponding <code>x-amz-checksum</code> or <code>x-amz-trailer</code> header sent. Otherwise, Amazon S3 fails the request with the HTTP status code <code>400 Bad Request</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p> <p>If you provide an individual checksum, Amazon S3 ignores any provided <code>ChecksumAlgorithm</code> parameter.</p>"""
    lifecycle_configuration: NotRequired[
        "capo_s3.types.bucket_lifecycle_configuration.BucketLifecycleConfiguration"
    ]
    """<p>Container for lifecycle rules. You can add as many as 1,000 rules.</p>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p> <note> <p>This parameter applies to general purpose buckets only. It is not supported for directory bucket lifecycle configurations.</p> </note>"""
    transition_default_minimum_object_size: NotRequired[
        "capo_s3.types.transition_default_minimum_object_size.TransitionDefaultMinimumObjectSize"
    ]
    """<p>Indicates which default minimum object size behavior is applied to the lifecycle configuration.</p> <note> <p>This parameter applies to general purpose buckets only. It is not supported for directory bucket lifecycle configurations.</p> </note> <ul> <li> <p> <code>all_storage_classes_128K</code> - Objects smaller than 128 KB will not transition to any storage class by default. </p> </li> <li> <p> <code>varies_by_storage_class</code> - Objects smaller than 128 KB will transition to Glacier Flexible Retrieval or Glacier Deep Archive storage classes. By default, all other storage classes will prevent transitions smaller than 128 KB. </p> </li> </ul> <p>To customize the minimum object size for any transition you can add a filter that specifies a custom <code>ObjectSizeGreaterThan</code> or <code>ObjectSizeLessThan</code> in the body of your transition rule. Custom filters always take precedence over the default transition behavior.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PutBucketLifecycleConfigurationRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "lifecycle_configuration" in value:
        import capo_s3.types.bucket_lifecycle_configuration

        capo_s3.types.bucket_lifecycle_configuration.serialize_xml(
            value["lifecycle_configuration"], el, "LifecycleConfiguration"
        )


def deserialize_xml(el: Element) -> PutBucketLifecycleConfigurationRequest:
    out: PutBucketLifecycleConfigurationRequest = {}  # type: ignore[typeddict-item]
    child_lifecycle_configuration = el.find("LifecycleConfiguration")
    if child_lifecycle_configuration is not None:
        import capo_s3.types.bucket_lifecycle_configuration

        out["lifecycle_configuration"] = (
            capo_s3.types.bucket_lifecycle_configuration.deserialize_xml(
                child_lifecycle_configuration
            )
        )
    return out
