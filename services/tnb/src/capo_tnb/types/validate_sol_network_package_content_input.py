"""Generated from Smithy shape ``com.amazonaws.tnb#ValidateSolNetworkPackageContentInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.nsd_info_id
    import capo_tnb.types.package_content_type
    import capo_tnb.types.sensitive_blob


class ValidateSolNetworkPackageContentInput(TypedDict, closed=True):
    nsd_info_id: "capo_tnb.types.nsd_info_id.NsdInfoId"
    """<p>Network service descriptor file.</p>"""
    content_type: NotRequired["capo_tnb.types.package_content_type.PackageContentType"]
    """<p>Network package content type.</p>"""
    file: "capo_tnb.types.sensitive_blob.SensitiveBlob"
    """<p>Network package file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidateSolNetworkPackageContentInput) -> dict:
    out: dict = {}
    import capo_tnb.types.sensitive_blob

    out["file"] = capo_tnb.types.sensitive_blob.serialize_json(value["file"])
    return out


def deserialize_json(data: dict) -> ValidateSolNetworkPackageContentInput:
    out: ValidateSolNetworkPackageContentInput = {}  # type: ignore[typeddict-item]
    if data.get("file") is not None:
        import capo_tnb.types.sensitive_blob

        out["file"] = capo_tnb.types.sensitive_blob.deserialize_json(data["file"])
    else:
        out["file"] = b""
    return out


def redact_sensitive(value: ValidateSolNetworkPackageContentInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "file" in value:
        out["file"] = "*** Sensitive Data Redacted ***"
    return out
