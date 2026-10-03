"""Generated from Smithy shape ``com.amazonaws.s3control#S3JobManifestGenerator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement
from capo_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.boolean
    import capo_s3_control.types.job_manifest_generator_filter
    import capo_s3_control.types.s3_bucket_arn_string
    import capo_s3_control.types.s3_manifest_output_location


class S3JobManifestGenerator(TypedDict, closed=True):
    expected_bucket_owner: NotRequired["capo_s3_control.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID that owns the source bucket specified in <code>SourceBucket</code>. If provided, the manifest source bucket owner's Amazon Web Services account ID must match this value, else the job fails.</p>"""
    source_bucket: "capo_s3_control.types.s3_bucket_arn_string.S3BucketArnString"
    """<p>The ARN of the source bucket used by the ManifestGenerator.</p> <note> <p> <b>Directory buckets</b> - Directory buckets aren't supported as the source buckets used by <code>S3JobManifestGenerator</code> to generate the job manifest.</p> </note>"""
    manifest_output_location: NotRequired[
        "capo_s3_control.types.s3_manifest_output_location.S3ManifestOutputLocation"
    ]
    """<p>Specifies the location the generated manifest will be written to. Manifests can't be written to directory buckets. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html">Directory buckets</a>.</p>"""
    filter: NotRequired[
        "capo_s3_control.types.job_manifest_generator_filter.JobManifestGeneratorFilter"
    ]
    """<p>Specifies rules the S3JobManifestGenerator should use to decide whether an object in the source bucket should or should not be included in the generated job manifest.</p>"""
    enable_manifest_output: "capo_s3_control.types.boolean.Boolean"
    """<p>Determines whether or not to write the job's generated manifest to a bucket.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: S3JobManifestGenerator, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "expected_bucket_owner" in value:
        SubElement(el, "ExpectedBucketOwner").text = str(value["expected_bucket_owner"])
    SubElement(el, "SourceBucket").text = str(value["source_bucket"])
    if "manifest_output_location" in value:
        import capo_s3_control.types.s3_manifest_output_location

        capo_s3_control.types.s3_manifest_output_location.serialize_xml(
            value["manifest_output_location"], el, "ManifestOutputLocation"
        )
    if "filter" in value:
        import capo_s3_control.types.job_manifest_generator_filter

        capo_s3_control.types.job_manifest_generator_filter.serialize_xml(
            value["filter"], el, "Filter"
        )
    SubElement(el, "EnableManifestOutput").text = (
        "true" if value.get("enable_manifest_output", False) else "false"
    )


def deserialize_xml(el: Element) -> S3JobManifestGenerator:
    out: S3JobManifestGenerator = {}  # type: ignore[typeddict-item]
    child_expected_bucket_owner = el.find("ExpectedBucketOwner")
    if child_expected_bucket_owner is not None:
        out["expected_bucket_owner"] = str(child_expected_bucket_owner.text or "")
    child_source_bucket = el.find("SourceBucket")
    if child_source_bucket is not None:
        out["source_bucket"] = str(child_source_bucket.text or "")
    else:
        raise DeserializationError("S3JobManifestGenerator.source_bucket required")
    child_manifest_output_location = el.find("ManifestOutputLocation")
    if child_manifest_output_location is not None:
        import capo_s3_control.types.s3_manifest_output_location

        out["manifest_output_location"] = (
            capo_s3_control.types.s3_manifest_output_location.deserialize_xml(
                child_manifest_output_location
            )
        )
    child_filter = el.find("Filter")
    if child_filter is not None:
        import capo_s3_control.types.job_manifest_generator_filter

        out["filter"] = (
            capo_s3_control.types.job_manifest_generator_filter.deserialize_xml(
                child_filter
            )
        )
    child_enable_manifest_output = el.find("EnableManifestOutput")
    if child_enable_manifest_output is not None:
        out["enable_manifest_output"] = (
            child_enable_manifest_output.text or ""
        ).lower() == "true"
    else:
        out["enable_manifest_output"] = False
    return out
