"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportSource``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_body_blob
    import capo_quicksight.types.s3_uri


class AssetBundleImportSource(TypedDict, closed=True):
    body: NotRequired[
        "capo_quicksight.types.asset_bundle_import_body_blob.AssetBundleImportBodyBlob"
    ]
    """<p>The bytes of the base64 encoded asset bundle import zip file. This file can't exceed 20 MB. If the size of the file that you want to upload is more than 20 MB, add the file to your Amazon S3 bucket and use <code>S3Uri</code> of the file for this operation.</p> <p>If you are calling the API operations from the Amazon Web Services SDK for Java, JavaScript, Python, or PHP, the SDK encodes base64 automatically to allow the direct setting of the zip file's bytes. If you are using an SDK for a different language or receiving related errors, try to base64 encode your data.</p>"""
    s3_uri: NotRequired["capo_quicksight.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 URI for an asset bundle import file that exists in an Amazon S3 bucket that the caller has read access to. The file must be a zip format file and can't exceed 1 GB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportSource) -> dict:
    out: dict = {}
    if "body" in value:
        import capo_quicksight.types.asset_bundle_import_body_blob

        out["Body"] = (
            capo_quicksight.types.asset_bundle_import_body_blob.serialize_json(
                value["body"]
            )
        )
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    return out


def deserialize_json(data: dict) -> AssetBundleImportSource:
    out: AssetBundleImportSource = {}  # type: ignore[typeddict-item]
    if data.get("Body") is not None:
        import capo_quicksight.types.asset_bundle_import_body_blob

        out["body"] = (
            capo_quicksight.types.asset_bundle_import_body_blob.deserialize_json(
                data["Body"]
            )
        )
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    return out


def redact_sensitive(value: AssetBundleImportSource) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "body" in value:
        out["body"] = "*** Sensitive Data Redacted ***"
    return out
