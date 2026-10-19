"""Generated from Smithy shape ``com.amazonaws.s3control#S3BucketDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.format
    import capo_s3_control.types.output_schema_version
    import capo_s3_control.types.prefix
    import capo_s3_control.types.s3_bucket_arn_string
    import capo_s3_control.types.storage_lens_data_export_encryption


class S3BucketDestination(TypedDict, closed=True):
    format: "capo_s3_control.types.format.Format"
    """<p></p>"""
    output_schema_version: (
        "capo_s3_control.types.output_schema_version.OutputSchemaVersion"
    )
    """<p>The schema version of the export file.</p>"""
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The account ID of the owner of the S3 Storage Lens metrics export bucket.</p>"""
    arn: "capo_s3_control.types.s3_bucket_arn_string.S3BucketArnString"
    """<p>The Amazon Resource Name (ARN) of the bucket. This property is read-only and follows the following format: <code> arn:aws:s3:<i>us-east-1</i>:<i>example-account-id</i>:bucket/<i>your-destination-bucket-name</i> </code> </p>"""
    prefix: NotRequired["capo_s3_control.types.prefix.Prefix"]
    """<p>The prefix of the destination bucket where the metrics export will be delivered.</p>"""
    encryption: NotRequired[
        "capo_s3_control.types.storage_lens_data_export_encryption.StorageLensDataExportEncryption"
    ]
    """<p>The container for the type encryption of the metrics exports in this bucket.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: S3BucketDestination, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3_control.types.format

    capo_s3_control.types.format.serialize_xml(value["format"], el, "Format")
    import capo_s3_control.types.output_schema_version

    capo_s3_control.types.output_schema_version.serialize_xml(
        value["output_schema_version"], el, "OutputSchemaVersion"
    )
    SubElement(el, "AccountId").text = str(value["account_id"])
    SubElement(el, "Arn").text = str(value["arn"])
    if "prefix" in value:
        SubElement(el, "Prefix").text = str(value["prefix"])
    if "encryption" in value:
        import capo_s3_control.types.storage_lens_data_export_encryption

        capo_s3_control.types.storage_lens_data_export_encryption.serialize_xml(
            value["encryption"], el, "Encryption"
        )


def deserialize_xml(el: Element) -> S3BucketDestination:
    out: S3BucketDestination = {}  # type: ignore[typeddict-item]
    child_format = el.find("Format")
    if child_format is not None:
        import capo_s3_control.types.format

        out["format"] = capo_s3_control.types.format.deserialize_xml(child_format)
    else:
        import typing

        out["format"] = typing.cast("capo_s3_control.types.format.Format", "")
    child_output_schema_version = el.find("OutputSchemaVersion")
    if child_output_schema_version is not None:
        import capo_s3_control.types.output_schema_version

        out["output_schema_version"] = (
            capo_s3_control.types.output_schema_version.deserialize_xml(
                child_output_schema_version
            )
        )
    else:
        import typing

        out["output_schema_version"] = typing.cast(
            "capo_s3_control.types.output_schema_version.OutputSchemaVersion", ""
        )
    child_account_id = el.find("AccountId")
    if child_account_id is not None:
        out["account_id"] = str(child_account_id.text or "")
    else:
        out["account_id"] = ""
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        out["arn"] = ""
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    child_encryption = el.find("Encryption")
    if child_encryption is not None:
        import capo_s3_control.types.storage_lens_data_export_encryption

        out["encryption"] = (
            capo_s3_control.types.storage_lens_data_export_encryption.deserialize_xml(
                child_encryption
            )
        )
    return out
