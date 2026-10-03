"""Generated from Smithy shape ``com.amazonaws.ivs#BatchGetStreamKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.batch_errors
    import capo_ivs.types.stream_keys
    import capo_ivs.types.string


class BatchGetStreamKeyResponse(TypedDict, closed=True):
    access_control_allow_origin: NotRequired["capo_ivs.types.string.String"]
    """<p>See <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin">Access-Control-Allow-Origin</a> in the MDN Web Docs.</p>"""
    access_control_expose_headers: NotRequired["capo_ivs.types.string.String"]
    """<p>See <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Expose-Headers">Access-Control-Expose-Headers</a> in the MDN Web Docs.</p>"""
    cache_control: NotRequired["capo_ivs.types.string.String"]
    """<p>See <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control">Cache-Control</a> in the MDN Web Docs.</p>"""
    content_security_policy: NotRequired["capo_ivs.types.string.String"]
    """<p>See <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy">Content-Security-Policy</a> in the MDN Web Docs.</p>"""
    strict_transport_security: NotRequired["capo_ivs.types.string.String"]
    """<p>See <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security">Strict-Transport-Security</a> in the MDN Web Docs.</p>"""
    x_content_type_options: NotRequired["capo_ivs.types.string.String"]
    """<p>See <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Content-Type-Options">X-Content-Type-Options</a> in the MDN Web Docs.</p>"""
    x_frame_options: NotRequired["capo_ivs.types.string.String"]
    """<p>See <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options">X-Frame-Options</a> in the MDN Web Docs.</p>"""
    stream_keys: NotRequired["capo_ivs.types.stream_keys.StreamKeys"]
    """<p/>"""
    errors: NotRequired["capo_ivs.types.batch_errors.BatchErrors"]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetStreamKeyResponse) -> dict:
    out: dict = {}
    if "stream_keys" in value:
        import capo_ivs.types.stream_keys

        out["streamKeys"] = capo_ivs.types.stream_keys.serialize_json(
            value["stream_keys"]
        )
    if "errors" in value:
        import capo_ivs.types.batch_errors

        out["errors"] = capo_ivs.types.batch_errors.serialize_json(value["errors"])
    return out


def deserialize_json(data: dict) -> BatchGetStreamKeyResponse:
    out: BatchGetStreamKeyResponse = {}  # type: ignore[typeddict-item]
    if data.get("streamKeys") is not None:
        import capo_ivs.types.stream_keys

        out["stream_keys"] = capo_ivs.types.stream_keys.deserialize_json(
            data["streamKeys"]
        )
    if data.get("errors") is not None:
        import capo_ivs.types.batch_errors

        out["errors"] = capo_ivs.types.batch_errors.deserialize_json(data["errors"])
    return out
