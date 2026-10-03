"""Generated from Smithy shape ``com.amazonaws.s3#PutBucketInventoryConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name
    import capo_s3.types.inventory_configuration
    import capo_s3.types.inventory_id


class PutBucketInventoryConfigurationRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The name of the bucket where the inventory configuration will be stored.</p> <p> <b>Directory buckets </b> - When you use this operation with a directory bucket, you must use path-style requests in the format <code>https://s3express-control.<i>region-code</i>.amazonaws.com/<i>bucket-name</i> </code>. Virtual-hosted-style requests aren't supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must also follow the format <code> <i>bucket-base-name</i>--<i>zone-id</i>--x-s3</code> (for example, <code> <i>DOC-EXAMPLE-BUCKET</i>--<i>usw2-az1</i>--x-s3</code>). For information about bucket naming restrictions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html">Directory bucket naming rules</a> in the <i>Amazon S3 User Guide</i> </p>"""
    id: "capo_s3.types.inventory_id.InventoryId"
    """<p>The ID used to identify the inventory configuration.</p>"""
    inventory_configuration: (
        "capo_s3.types.inventory_configuration.InventoryConfiguration"
    )
    """<p>Specifies the inventory configuration.</p>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p> <note> <p>For directory buckets, this header is not supported in this API operation. If you specify this header, the request fails with the HTTP status code <code>501 Not Implemented</code>.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PutBucketInventoryConfigurationRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.inventory_configuration

    capo_s3.types.inventory_configuration.serialize_xml(
        value["inventory_configuration"], el, "InventoryConfiguration"
    )


def deserialize_xml(el: Element) -> PutBucketInventoryConfigurationRequest:
    out: PutBucketInventoryConfigurationRequest = {}  # type: ignore[typeddict-item]
    child_inventory_configuration = el.find("InventoryConfiguration")
    if child_inventory_configuration is not None:
        import capo_s3.types.inventory_configuration

        out["inventory_configuration"] = (
            capo_s3.types.inventory_configuration.deserialize_xml(
                child_inventory_configuration
            )
        )
    else:
        raise DeserializationError(
            "PutBucketInventoryConfigurationRequest.inventory_configuration required"
        )
    return out
