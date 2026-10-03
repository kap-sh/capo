"""Generated from Smithy shape ``com.amazonaws.s3#PutBucketAccelerateConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.accelerate_configuration
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name
    import capo_s3.types.checksum_algorithm


class PutBucketAccelerateConfigurationRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The name of the bucket for which the accelerate configuration is set.</p>"""
    accelerate_configuration: (
        "capo_s3.types.accelerate_configuration.AccelerateConfiguration"
    )
    """<p>Container for setting the transfer acceleration state.</p>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""
    checksum_algorithm: NotRequired[
        "capo_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p>Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any additional functionality if you don't use the SDK. When you send this header, there must be a corresponding <code>x-amz-checksum</code> or <code>x-amz-trailer</code> header sent. Otherwise, Amazon S3 fails the request with the HTTP status code <code>400 Bad Request</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p> <p>If you provide an individual checksum, Amazon S3 ignores any provided <code>ChecksumAlgorithm</code> parameter.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PutBucketAccelerateConfigurationRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.accelerate_configuration

    capo_s3.types.accelerate_configuration.serialize_xml(
        value["accelerate_configuration"], el, "AccelerateConfiguration"
    )


def deserialize_xml(el: Element) -> PutBucketAccelerateConfigurationRequest:
    out: PutBucketAccelerateConfigurationRequest = {}  # type: ignore[typeddict-item]
    child_accelerate_configuration = el.find("AccelerateConfiguration")
    if child_accelerate_configuration is not None:
        import capo_s3.types.accelerate_configuration

        out["accelerate_configuration"] = (
            capo_s3.types.accelerate_configuration.deserialize_xml(
                child_accelerate_configuration
            )
        )
    else:
        raise DeserializationError(
            "PutBucketAccelerateConfigurationRequest.accelerate_configuration required"
        )
    return out
