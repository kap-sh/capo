"""Generated from Smithy shape ``com.amazonaws.tnb#ValidateSolFunctionPackageContentInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.package_content_type
    import capo_tnb.types.sensitive_blob
    import capo_tnb.types.vnf_pkg_id


class ValidateSolFunctionPackageContentInput(TypedDict, closed=True):
    vnf_pkg_id: "capo_tnb.types.vnf_pkg_id.VnfPkgId"
    """<p>Function package ID.</p>"""
    content_type: NotRequired["capo_tnb.types.package_content_type.PackageContentType"]
    """<p>Function package content type.</p>"""
    file: "capo_tnb.types.sensitive_blob.SensitiveBlob"
    """<p>Function package file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidateSolFunctionPackageContentInput) -> dict:
    out: dict = {}
    import capo_tnb.types.sensitive_blob

    out["file"] = capo_tnb.types.sensitive_blob.serialize_json(value["file"])
    return out


def deserialize_json(data: dict) -> ValidateSolFunctionPackageContentInput:
    out: ValidateSolFunctionPackageContentInput = {}  # type: ignore[typeddict-item]
    if data.get("file") is not None:
        import capo_tnb.types.sensitive_blob

        out["file"] = capo_tnb.types.sensitive_blob.deserialize_json(data["file"])
    else:
        out["file"] = b""
    return out


def redact_sensitive(value: ValidateSolFunctionPackageContentInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "file" in value:
        out["file"] = "*** Sensitive Data Redacted ***"
    return out
