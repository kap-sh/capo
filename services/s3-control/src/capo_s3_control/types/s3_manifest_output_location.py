"""Generated from Smithy shape ``com.amazonaws.s3control#S3ManifestOutputLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.generated_manifest_encryption
    import capo_s3_control.types.generated_manifest_format
    import capo_s3_control.types.manifest_prefix_string
    import capo_s3_control.types.s3_bucket_arn_string


class S3ManifestOutputLocation(TypedDict, closed=True):
    expected_manifest_bucket_owner: NotRequired[
        "capo_s3_control.types.account_id.AccountId"
    ]
    """<p>The Account ID that owns the bucket the generated manifest is written to.</p>"""
    bucket: "capo_s3_control.types.s3_bucket_arn_string.S3BucketArnString"
    """<p>The bucket ARN the generated manifest should be written to.</p> <note> <p> <b>Directory buckets</b> - Directory buckets aren't supported as the buckets to store the generated manifest.</p> </note>"""
    manifest_prefix: NotRequired[
        "capo_s3_control.types.manifest_prefix_string.ManifestPrefixString"
    ]
    """<p>Prefix identifying one or more objects to which the manifest applies.</p>"""
    manifest_encryption: NotRequired[
        "capo_s3_control.types.generated_manifest_encryption.GeneratedManifestEncryption"
    ]
    """<p>Specifies what encryption should be used when the generated manifest objects are written.</p>"""
    manifest_format: (
        "capo_s3_control.types.generated_manifest_format.GeneratedManifestFormat"
    )
    """<p>The format of the generated manifest.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: S3ManifestOutputLocation, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "expected_manifest_bucket_owner" in value:
        SubElement(el, "ExpectedManifestBucketOwner").text = str(
            value["expected_manifest_bucket_owner"]
        )
    SubElement(el, "Bucket").text = str(value["bucket"])
    if "manifest_prefix" in value:
        SubElement(el, "ManifestPrefix").text = str(value["manifest_prefix"])
    if "manifest_encryption" in value:
        import capo_s3_control.types.generated_manifest_encryption

        capo_s3_control.types.generated_manifest_encryption.serialize_xml(
            value["manifest_encryption"], el, "ManifestEncryption"
        )
    import capo_s3_control.types.generated_manifest_format

    capo_s3_control.types.generated_manifest_format.serialize_xml(
        value["manifest_format"], el, "ManifestFormat"
    )


def deserialize_xml(el: Element) -> S3ManifestOutputLocation:
    out: S3ManifestOutputLocation = {}  # type: ignore[typeddict-item]
    child_expected_manifest_bucket_owner = el.find("ExpectedManifestBucketOwner")
    if child_expected_manifest_bucket_owner is not None:
        out["expected_manifest_bucket_owner"] = str(
            child_expected_manifest_bucket_owner.text or ""
        )
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    else:
        out["bucket"] = ""
    child_manifest_prefix = el.find("ManifestPrefix")
    if child_manifest_prefix is not None:
        out["manifest_prefix"] = str(child_manifest_prefix.text or "")
    child_manifest_encryption = el.find("ManifestEncryption")
    if child_manifest_encryption is not None:
        import capo_s3_control.types.generated_manifest_encryption

        out["manifest_encryption"] = (
            capo_s3_control.types.generated_manifest_encryption.deserialize_xml(
                child_manifest_encryption
            )
        )
    child_manifest_format = el.find("ManifestFormat")
    if child_manifest_format is not None:
        import capo_s3_control.types.generated_manifest_format

        out["manifest_format"] = (
            capo_s3_control.types.generated_manifest_format.deserialize_xml(
                child_manifest_format
            )
        )
    else:
        import typing

        out["manifest_format"] = typing.cast(
            "capo_s3_control.types.generated_manifest_format.GeneratedManifestFormat",
            "",
        )
    return out
