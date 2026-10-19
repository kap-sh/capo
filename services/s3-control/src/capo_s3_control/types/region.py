"""Generated from Smithy shape ``com.amazonaws.s3control#Region``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.bucket_name


class Region(TypedDict, closed=True):
    bucket: "capo_s3_control.types.bucket_name.BucketName"
    """<p>The name of the associated bucket for the Region.</p>"""
    bucket_account_id: NotRequired["capo_s3_control.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID that owns the Amazon S3 bucket that's associated with this Multi-Region Access Point.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Region, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Bucket").text = str(value["bucket"])
    if "bucket_account_id" in value:
        SubElement(el, "BucketAccountId").text = str(value["bucket_account_id"])


def deserialize_xml(el: Element) -> Region:
    out: Region = {}  # type: ignore[typeddict-item]
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    else:
        out["bucket"] = ""
    child_bucket_account_id = el.find("BucketAccountId")
    if child_bucket_account_id is not None:
        out["bucket_account_id"] = str(child_bucket_account_id.text or "")
    return out
