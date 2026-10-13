"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#GetIngestConfigurationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.ingest_configuration


class GetIngestConfigurationResponse(TypedDict, closed=True):
    ingest_configuration: NotRequired[
        "capo_ivs_realtime.types.ingest_configuration.IngestConfiguration"
    ]
    """<p>The IngestConfiguration that was returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIngestConfigurationResponse) -> dict:
    out: dict = {}
    if "ingest_configuration" in value:
        import capo_ivs_realtime.types.ingest_configuration

        out["ingestConfiguration"] = (
            capo_ivs_realtime.types.ingest_configuration.serialize_json(
                value["ingest_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetIngestConfigurationResponse:
    out: GetIngestConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("ingestConfiguration") is not None:
        import capo_ivs_realtime.types.ingest_configuration

        out["ingest_configuration"] = (
            capo_ivs_realtime.types.ingest_configuration.deserialize_json(
                data["ingestConfiguration"]
            )
        )
    return out


def redact_sensitive(value: GetIngestConfigurationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ingest_configuration" in value:
        import capo_ivs_realtime.types.ingest_configuration

        out["ingest_configuration"] = (
            capo_ivs_realtime.types.ingest_configuration.redact_sensitive(
                value["ingest_configuration"]
            )
        )
    return out
