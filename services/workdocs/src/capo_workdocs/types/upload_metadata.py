"""Generated from Smithy shape ``com.amazonaws.workdocs#UploadMetadata``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.signed_header_map
    import capo_workdocs.types.url_type


class UploadMetadata(TypedDict, closed=True):
    upload_url: NotRequired["capo_workdocs.types.url_type.UrlType"]
    """<p>The URL of the upload.</p>"""
    signed_headers: NotRequired["capo_workdocs.types.signed_header_map.SignedHeaderMap"]
    """<p>The signed headers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UploadMetadata) -> dict:
    out: dict = {}
    if "upload_url" in value:
        out["UploadUrl"] = value["upload_url"]
    if "signed_headers" in value:
        import capo_workdocs.types.signed_header_map

        out["SignedHeaders"] = capo_workdocs.types.signed_header_map.serialize_json(
            value["signed_headers"]
        )
    return out


def deserialize_json(data: dict) -> UploadMetadata:
    out: UploadMetadata = {}  # type: ignore[typeddict-item]
    if data.get("UploadUrl") is not None:
        out["upload_url"] = data["UploadUrl"]
    if data.get("SignedHeaders") is not None:
        import capo_workdocs.types.signed_header_map

        out["signed_headers"] = capo_workdocs.types.signed_header_map.deserialize_json(
            data["SignedHeaders"]
        )
    return out


def redact_sensitive(value: UploadMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "upload_url" in value:
        out["upload_url"] = "*** Sensitive Data Redacted ***"
    return out
