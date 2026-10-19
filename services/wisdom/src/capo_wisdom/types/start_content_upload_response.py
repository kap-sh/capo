"""Generated from Smithy shape ``com.amazonaws.wisdom#StartContentUploadResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_wisdom.types.headers
    import capo_wisdom.types.upload_id
    import capo_wisdom.types.url


class StartContentUploadResponse(TypedDict, closed=True):
    upload_id: "capo_wisdom.types.upload_id.UploadId"
    """<p>The identifier of the upload.</p>"""
    url: "capo_wisdom.types.url.Url"
    """<p>The URL of the upload.</p>"""
    url_expiry: "datetime.datetime"
    """<p>The expiration time of the URL as an epoch timestamp.</p>"""
    headers_to_include: "capo_wisdom.types.headers.Headers"
    """<p>The headers to include in the upload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartContentUploadResponse) -> dict:
    out: dict = {}
    out["uploadId"] = value["upload_id"]
    out["url"] = value["url"]
    out["urlExpiry"] = value["url_expiry"].timestamp()
    import capo_wisdom.types.headers

    out["headersToInclude"] = capo_wisdom.types.headers.serialize_json(
        value["headers_to_include"]
    )
    return out


def deserialize_json(data: dict) -> StartContentUploadResponse:
    out: StartContentUploadResponse = {}  # type: ignore[typeddict-item]
    if data.get("uploadId") is not None:
        out["upload_id"] = data["uploadId"]
    else:
        out["upload_id"] = ""
    if data.get("url") is not None:
        out["url"] = data["url"]
    else:
        out["url"] = ""
    if data.get("urlExpiry") is not None:
        import datetime

        out["url_expiry"] = datetime.datetime.fromtimestamp(
            float(data["urlExpiry"]), tz=datetime.timezone.utc
        )
    else:
        import datetime

        out["url_expiry"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("headersToInclude") is not None:
        import capo_wisdom.types.headers

        out["headers_to_include"] = capo_wisdom.types.headers.deserialize_json(
            data["headersToInclude"]
        )
    else:
        out["headers_to_include"] = {}
    return out


def redact_sensitive(value: StartContentUploadResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "url" in value:
        out["url"] = "*** Sensitive Data Redacted ***"
    return out
