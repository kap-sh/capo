"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#GetConnectorTelemetryManifestOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_observabilityadmin.types.telemetry_manifest


class GetConnectorTelemetryManifestOutput(TypedDict, closed=True):
    manifest: "capo_observabilityadmin.types.telemetry_manifest.TelemetryManifest"
    """<p>The telemetry manifest.</p>"""
    version: "int"
    """<p>The current version of the telemetry manifest. Pass this value as <code>ExpectedVersion</code> when you next call <code>PutConnectorTelemetryManifest</code>.</p>"""
    last_update_time_stamp: NotRequired["int"]
    """<p>The time when the telemetry manifest was last updated, in milliseconds since the Unix epoch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectorTelemetryManifestOutput) -> dict:
    out: dict = {}
    import capo_observabilityadmin.types.telemetry_manifest

    out["Manifest"] = capo_observabilityadmin.types.telemetry_manifest.serialize_json(
        value["manifest"]
    )
    out["Version"] = value["version"]
    if "last_update_time_stamp" in value:
        out["LastUpdateTimeStamp"] = value["last_update_time_stamp"]
    return out


def deserialize_json(data: dict) -> GetConnectorTelemetryManifestOutput:
    out: GetConnectorTelemetryManifestOutput = {}  # type: ignore[typeddict-item]
    if data.get("Manifest") is not None:
        import capo_observabilityadmin.types.telemetry_manifest

        out["manifest"] = (
            capo_observabilityadmin.types.telemetry_manifest.deserialize_json(
                data["Manifest"]
            )
        )
    else:
        raise DeserializationError(
            "GetConnectorTelemetryManifestOutput.manifest required"
        )
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    else:
        out["version"] = 0
    if data.get("LastUpdateTimeStamp") is not None:
        out["last_update_time_stamp"] = data["LastUpdateTimeStamp"]
    return out
