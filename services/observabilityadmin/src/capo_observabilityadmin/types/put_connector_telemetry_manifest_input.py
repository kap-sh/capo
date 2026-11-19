"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#PutConnectorTelemetryManifestInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_observabilityadmin.types.client_token
    import capo_observabilityadmin.types.connector_identifier
    import capo_observabilityadmin.types.telemetry_manifest


class PutConnectorTelemetryManifestInput(TypedDict, closed=True):
    connector_identifier: (
        "capo_observabilityadmin.types.connector_identifier.ConnectorIdentifier"
    )
    """<p>The connector. Specify one of the following:</p> <ul> <li> <p>The Amazon Resource Name (ARN) of the connector</p> </li> <li> <p>The ID of the connector</p> </li> </ul>"""
    manifest: "capo_observabilityadmin.types.telemetry_manifest.TelemetryManifest"
    """<p>The telemetry manifest.</p>"""
    expected_version: NotRequired["int"]
    """<p>The version of the telemetry manifest that you expect to replace, as returned by <code>GetConnectorTelemetryManifest</code>. Omit this value when you create the first telemetry manifest. If the value doesn't match the current version, the request fails with a <code>ConflictException</code>.</p>"""
    client_token: NotRequired["capo_observabilityadmin.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the operation completes no more than one time. If you use an Amazon Web Services SDK, the SDK generates this value and reuses it on retries. If this token matches a previous request with the same telemetry manifest, the service returns the stored version without an error. If you use the same token with a different telemetry manifest, the service returns a <code>ValidationException</code>. This operation is idempotent when you use the same token and parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutConnectorTelemetryManifestInput) -> dict:
    out: dict = {}
    out["ConnectorIdentifier"] = value["connector_identifier"]
    import capo_observabilityadmin.types.telemetry_manifest

    out["Manifest"] = capo_observabilityadmin.types.telemetry_manifest.serialize_json(
        value["manifest"]
    )
    if "expected_version" in value:
        out["ExpectedVersion"] = value["expected_version"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> PutConnectorTelemetryManifestInput:
    out: PutConnectorTelemetryManifestInput = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorIdentifier") is not None:
        out["connector_identifier"] = data["ConnectorIdentifier"]
    else:
        out["connector_identifier"] = ""
    if data.get("Manifest") is not None:
        import capo_observabilityadmin.types.telemetry_manifest

        out["manifest"] = (
            capo_observabilityadmin.types.telemetry_manifest.deserialize_json(
                data["Manifest"]
            )
        )
    else:
        raise DeserializationError(
            "PutConnectorTelemetryManifestInput.manifest required"
        )
    if data.get("ExpectedVersion") is not None:
        out["expected_version"] = data["ExpectedVersion"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out


def redact_sensitive(value: PutConnectorTelemetryManifestInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_token" in value:
        out["client_token"] = "*** Sensitive Data Redacted ***"
    return out
