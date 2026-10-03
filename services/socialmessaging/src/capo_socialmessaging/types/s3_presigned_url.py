"""Generated from Smithy shape ``com.amazonaws.socialmessaging#S3PresignedUrl``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_socialmessaging.types.headers


class S3PresignedUrl(TypedDict, closed=True):
    url: "str"
    """<p>The presign url to the object.</p>"""
    headers: "capo_socialmessaging.types.headers.Headers"
    """<p>A map of headers and their values. You must specify the <code>Content-Type</code> header when using <code>PostWhatsAppMessageMedia</code>. For a list of common headers, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/RESTCommonRequestHeaders.html">Common Request Headers</a> in the <i>Amazon S3 API Reference</i> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3PresignedUrl) -> dict:
    out: dict = {}
    out["url"] = value["url"]
    import capo_socialmessaging.types.headers

    out["headers"] = capo_socialmessaging.types.headers.serialize_json(value["headers"])
    return out


def deserialize_json(data: dict) -> S3PresignedUrl:
    out: S3PresignedUrl = {}  # type: ignore[typeddict-item]
    if data.get("url") is not None:
        out["url"] = data["url"]
    else:
        raise DeserializationError("S3PresignedUrl.url required")
    if data.get("headers") is not None:
        import capo_socialmessaging.types.headers

        out["headers"] = capo_socialmessaging.types.headers.deserialize_json(
            data["headers"]
        )
    else:
        raise DeserializationError("S3PresignedUrl.headers required")
    return out
