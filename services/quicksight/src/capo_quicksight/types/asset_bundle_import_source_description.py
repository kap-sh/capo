"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportSourceDescription``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.s3_uri
    import capo_quicksight.types.sensitive_s3_uri


class AssetBundleImportSourceDescription(TypedDict, closed=True):
    body: NotRequired["capo_quicksight.types.sensitive_s3_uri.SensitiveS3Uri"]
    """<p>An HTTPS download URL for the provided asset bundle that you optionally provided at the start of the import job. This URL is valid for five minutes after issuance. Call <code>DescribeAssetBundleExportJob</code> again for a fresh URL if needed. The downloaded asset bundle is a <code>.qs</code> zip file.</p>"""
    s3_uri: NotRequired["capo_quicksight.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 URI that you provided at the start of the import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportSourceDescription) -> dict:
    out: dict = {}
    if "body" in value:
        out["Body"] = value["body"]
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    return out


def deserialize_json(data: dict) -> AssetBundleImportSourceDescription:
    out: AssetBundleImportSourceDescription = {}  # type: ignore[typeddict-item]
    if data.get("Body") is not None:
        out["body"] = data["Body"]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    return out


def redact_sensitive(value: AssetBundleImportSourceDescription) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "body" in value:
        out["body"] = "*** Sensitive Data Redacted ***"
    return out
