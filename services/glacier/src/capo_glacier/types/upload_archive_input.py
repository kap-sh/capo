"""Generated from Smithy shape ``com.amazonaws.glacier#UploadArchiveInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.stream
    import capo_glacier.types.string


class UploadArchiveInput(TypedDict, closed=True):
    vault_name: "capo_glacier.types.string.string"
    """<p>The name of the vault.</p>"""
    account_id: "capo_glacier.types.string.string"
    """<p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. </p>"""
    archive_description: NotRequired["capo_glacier.types.string.string"]
    """<p>The optional description of the archive you are uploading.</p>"""
    checksum: NotRequired["capo_glacier.types.string.string"]
    """<p>The SHA256 tree hash of the data being uploaded.</p>"""
    body: NotRequired["capo_glacier.types.stream.Stream"]
    """<p>The data to upload.</p>"""


def redact_sensitive(value: UploadArchiveInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "body" in value:
        out["body"] = "*** Streaming Data Redacted ***"
    return out
