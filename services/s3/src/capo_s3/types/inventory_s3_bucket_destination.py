"""Generated from Smithy shape ``com.amazonaws.s3#InventoryS3BucketDestination``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name
    import capo_s3.types.inventory_encryption
    import capo_s3.types.inventory_format
    import capo_s3.types.prefix


class InventoryS3BucketDestination(TypedDict, closed=True):
    account_id: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID that owns the destination S3 bucket. If no account ID is provided, the owner is not validated before exporting data. </p> <note> <p> Although this value is optional, we strongly recommend that you set it to help prevent problems if the destination bucket ownership changes. </p> </note>"""
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The Amazon Resource Name (ARN) of the bucket where inventory results will be published.</p>"""
    format: "capo_s3.types.inventory_format.InventoryFormat"
    """<p>Specifies the output format of the inventory results.</p>"""
    prefix: NotRequired["capo_s3.types.prefix.Prefix"]
    """<p>The prefix that is prepended to all inventory results.</p>"""
    encryption: NotRequired["capo_s3.types.inventory_encryption.InventoryEncryption"]
    """<p>Contains the type of server-side encryption used to encrypt the inventory results.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: InventoryS3BucketDestination, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "account_id" in value:
        SubElement(el, "AccountId").text = str(value["account_id"])
    SubElement(el, "Bucket").text = str(value["bucket"])
    import capo_s3.types.inventory_format

    capo_s3.types.inventory_format.serialize_xml(value["format"], el, "Format")
    if "prefix" in value:
        SubElement(el, "Prefix").text = str(value["prefix"])
    if "encryption" in value:
        import capo_s3.types.inventory_encryption

        capo_s3.types.inventory_encryption.serialize_xml(
            value["encryption"], el, "Encryption"
        )


def deserialize_xml(el: Element) -> InventoryS3BucketDestination:
    out: InventoryS3BucketDestination = {}  # type: ignore[typeddict-item]
    child_account_id = el.find("AccountId")
    if child_account_id is not None:
        out["account_id"] = str(child_account_id.text or "")
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    else:
        raise DeserializationError("InventoryS3BucketDestination.bucket required")
    child_format = el.find("Format")
    if child_format is not None:
        import capo_s3.types.inventory_format

        out["format"] = capo_s3.types.inventory_format.deserialize_xml(child_format)
    else:
        raise DeserializationError("InventoryS3BucketDestination.format required")
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    child_encryption = el.find("Encryption")
    if child_encryption is not None:
        import capo_s3.types.inventory_encryption

        out["encryption"] = capo_s3.types.inventory_encryption.deserialize_xml(
            child_encryption
        )
    return out


def redact_sensitive(value: InventoryS3BucketDestination) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "encryption" in value:
        import capo_s3.types.inventory_encryption

        out["encryption"] = capo_s3.types.inventory_encryption.redact_sensitive(
            value["encryption"]
        )
    return out
