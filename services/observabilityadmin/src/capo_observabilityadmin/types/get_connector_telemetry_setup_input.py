"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#GetConnectorTelemetrySetupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.connector_identifier
    import capo_observabilityadmin.types.setup_format


class GetConnectorTelemetrySetupInput(TypedDict, closed=True):
    connector_identifier: (
        "capo_observabilityadmin.types.connector_identifier.ConnectorIdentifier"
    )
    """<p>The connector whose telemetry manifest you want to generate the setup from. Specify one of the following:</p> <ul> <li> <p>The Amazon Resource Name (ARN) of the connector</p> </li> <li> <p>The ID of the connector</p> </li> </ul>"""
    format: NotRequired["capo_observabilityadmin.types.setup_format.SetupFormat"]
    """<p>The format of the setup artifacts. If you omit this value, the service uses the default format for the connector's provider (<code>BICEP</code> for an Azure connector). If the provider doesn't support the format, the service returns a <code>ValidationException</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectorTelemetrySetupInput) -> dict:
    out: dict = {}
    out["ConnectorIdentifier"] = value["connector_identifier"]
    if "format" in value:
        import capo_observabilityadmin.types.setup_format

        out["Format"] = capo_observabilityadmin.types.setup_format.serialize_json(
            value["format"]
        )
    return out


def deserialize_json(data: dict) -> GetConnectorTelemetrySetupInput:
    out: GetConnectorTelemetrySetupInput = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorIdentifier") is not None:
        out["connector_identifier"] = data["ConnectorIdentifier"]
    else:
        out["connector_identifier"] = ""
    if data.get("Format") is not None:
        import capo_observabilityadmin.types.setup_format

        out["format"] = capo_observabilityadmin.types.setup_format.deserialize_json(
            data["Format"]
        )
    return out
