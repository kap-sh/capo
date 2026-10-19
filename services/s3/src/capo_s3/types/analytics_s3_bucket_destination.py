"""Generated from Smithy shape ``com.amazonaws.s3#AnalyticsS3BucketDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.analytics_s3_export_file_format
    import capo_s3.types.bucket_name
    import capo_s3.types.prefix


class AnalyticsS3BucketDestination(TypedDict, closed=True):
    format: "capo_s3.types.analytics_s3_export_file_format.AnalyticsS3ExportFileFormat"
    """<p>Specifies the file format used when exporting data to Amazon S3.</p>"""
    bucket_account_id: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID that owns the destination S3 bucket. If no account ID is provided, the owner is not validated before exporting data.</p> <note> <p> Although this value is optional, we strongly recommend that you set it to help prevent problems if the destination bucket ownership changes. </p> </note>"""
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The Amazon Resource Name (ARN) of the bucket to which data is exported.</p>"""
    prefix: NotRequired["capo_s3.types.prefix.Prefix"]
    """<p>The prefix to use when exporting data. The prefix is prepended to all results.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: AnalyticsS3BucketDestination, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.analytics_s3_export_file_format

    capo_s3.types.analytics_s3_export_file_format.serialize_xml(
        value["format"], el, "Format"
    )
    if "bucket_account_id" in value:
        SubElement(el, "BucketAccountId").text = str(value["bucket_account_id"])
    SubElement(el, "Bucket").text = str(value["bucket"])
    if "prefix" in value:
        SubElement(el, "Prefix").text = str(value["prefix"])


def deserialize_xml(el: Element) -> AnalyticsS3BucketDestination:
    out: AnalyticsS3BucketDestination = {}  # type: ignore[typeddict-item]
    child_format = el.find("Format")
    if child_format is not None:
        import capo_s3.types.analytics_s3_export_file_format

        out["format"] = capo_s3.types.analytics_s3_export_file_format.deserialize_xml(
            child_format
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_s3.types.analytics_s3_export_file_format.AnalyticsS3ExportFileFormat",
            "",
        )
    child_bucket_account_id = el.find("BucketAccountId")
    if child_bucket_account_id is not None:
        out["bucket_account_id"] = str(child_bucket_account_id.text or "")
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    else:
        out["bucket"] = ""
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    return out
