"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#CreateIngestConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.ingest_configuration
    import capo_ivs_realtime.types.string


class CreateIngestConfigurationResponse(TypedDict, closed=True):
    access_control_allow_origin: NotRequired["capo_ivs_realtime.types.string.String"]
    """<p>See <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin">Access-Control-Allow-Origin</a> in the MDN Web Docs.</p>"""
    access_control_expose_headers: NotRequired["capo_ivs_realtime.types.string.String"]
    """<p>See <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Expose-Headers">Access-Control-Expose-Headers</a> in the MDN Web Docs.</p>"""
    cache_control: NotRequired["capo_ivs_realtime.types.string.String"]
    """<p>See <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control">Cache-Control</a> in the MDN Web Docs.</p>"""
    content_security_policy: NotRequired["capo_ivs_realtime.types.string.String"]
    """<p>See <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy">Content-Security-Policy</a> in the MDN Web Docs.</p>"""
    strict_transport_security: NotRequired["capo_ivs_realtime.types.string.String"]
    """<p>See <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security">Strict-Transport-Security</a> in the MDN Web Docs.</p>"""
    x_content_type_options: NotRequired["capo_ivs_realtime.types.string.String"]
    """<p>See <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Content-Type-Options">X-Content-Type-Options</a> in the MDN Web Docs.</p>"""
    x_frame_options: NotRequired["capo_ivs_realtime.types.string.String"]
    """<p>See <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options">X-Frame-Options</a> in the MDN Web Docs.</p>"""
    ingest_configuration: NotRequired[
        "capo_ivs_realtime.types.ingest_configuration.IngestConfiguration"
    ]
    """<p>The IngestConfiguration that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIngestConfigurationResponse) -> dict:
    out: dict = {}
    if "ingest_configuration" in value:
        import capo_ivs_realtime.types.ingest_configuration

        out["ingestConfiguration"] = (
            capo_ivs_realtime.types.ingest_configuration.serialize_json(
                value["ingest_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateIngestConfigurationResponse:
    out: CreateIngestConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("ingestConfiguration") is not None:
        import capo_ivs_realtime.types.ingest_configuration

        out["ingest_configuration"] = (
            capo_ivs_realtime.types.ingest_configuration.deserialize_json(
                data["ingestConfiguration"]
            )
        )
    return out
