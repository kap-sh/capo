"""Generated from Smithy shape ``com.amazonaws.s3control#RegionalBucket``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.bucket_name
    import capo_s3_control.types.creation_date
    import capo_s3_control.types.non_empty_max_length64_string
    import capo_s3_control.types.public_access_block_enabled
    import capo_s3_control.types.s3_regional_bucket_arn


class RegionalBucket(TypedDict, closed=True):
    bucket: "capo_s3_control.types.bucket_name.BucketName"
    """<p></p>"""
    bucket_arn: NotRequired[
        "capo_s3_control.types.s3_regional_bucket_arn.S3RegionalBucketArn"
    ]
    """<p>The Amazon Resource Name (ARN) for the regional bucket.</p>"""
    public_access_block_enabled: (
        "capo_s3_control.types.public_access_block_enabled.PublicAccessBlockEnabled"
    )
    """<p></p>"""
    creation_date: "capo_s3_control.types.creation_date.CreationDate"
    """<p>The creation date of the regional bucket</p>"""
    outpost_id: NotRequired[
        "capo_s3_control.types.non_empty_max_length64_string.NonEmptyMaxLength64String"
    ]
    """<p>The Outposts ID of the regional bucket.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: RegionalBucket, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Bucket").text = str(value["bucket"])
    if "bucket_arn" in value:
        SubElement(el, "BucketArn").text = str(value["bucket_arn"])
    SubElement(el, "PublicAccessBlockEnabled").text = (
        "true" if value.get("public_access_block_enabled", False) else "false"
    )
    import capo_s3_control.types.creation_date

    capo_s3_control.types.creation_date.serialize_xml(
        value["creation_date"], el, "CreationDate"
    )
    if "outpost_id" in value:
        SubElement(el, "OutpostId").text = str(value["outpost_id"])


def deserialize_xml(el: Element) -> RegionalBucket:
    out: RegionalBucket = {}  # type: ignore[typeddict-item]
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    else:
        out["bucket"] = ""
    child_bucket_arn = el.find("BucketArn")
    if child_bucket_arn is not None:
        out["bucket_arn"] = str(child_bucket_arn.text or "")
    child_public_access_block_enabled = el.find("PublicAccessBlockEnabled")
    if child_public_access_block_enabled is not None:
        out["public_access_block_enabled"] = (
            child_public_access_block_enabled.text or ""
        ).lower() == "true"
    else:
        out["public_access_block_enabled"] = False
    child_creation_date = el.find("CreationDate")
    if child_creation_date is not None:
        import capo_s3_control.types.creation_date

        out["creation_date"] = capo_s3_control.types.creation_date.deserialize_xml(
            child_creation_date
        )
    else:
        import datetime

        out["creation_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    child_outpost_id = el.find("OutpostId")
    if child_outpost_id is not None:
        out["outpost_id"] = str(child_outpost_id.text or "")
    return out
