"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryManifest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.telemetry_manifest_infrastructure
    import capo_observabilityadmin.types.telemetry_manifest_source


class TelemetryManifest(TypedDict, closed=True):
    source: "capo_observabilityadmin.types.telemetry_manifest_source.TelemetryManifestSource"
    """<p>The resources to collect telemetry from and the telemetry types to collect.</p>"""
    infrastructure: NotRequired[
        "capo_observabilityadmin.types.telemetry_manifest_infrastructure.TelemetryManifestInfrastructure"
    ]
    """<p>The choices for the infrastructure that the setup creates in your cloud provider, such as the subscription that contains the Event Hubs and their size. If you omit this value, the setup uses default settings. If an <code>AzureScopeItem</code> collects <code>ResourceLogs</code>, you must specify at least the Azure <code>SubscriptionId</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryManifest) -> dict:
    out: dict = {}
    import capo_observabilityadmin.types.telemetry_manifest_source

    out["Source"] = (
        capo_observabilityadmin.types.telemetry_manifest_source.serialize_json(
            value["source"]
        )
    )
    if "infrastructure" in value:
        import capo_observabilityadmin.types.telemetry_manifest_infrastructure

        out["Infrastructure"] = (
            capo_observabilityadmin.types.telemetry_manifest_infrastructure.serialize_json(
                value["infrastructure"]
            )
        )
    return out


def deserialize_json(data: dict) -> TelemetryManifest:
    out: TelemetryManifest = {}  # type: ignore[typeddict-item]
    if data.get("Source") is not None:
        import capo_observabilityadmin.types.telemetry_manifest_source

        out["source"] = (
            capo_observabilityadmin.types.telemetry_manifest_source.deserialize_json(
                data["Source"]
            )
        )
    else:
        out["source"] = {"$unknown": {"name": ""}}
    if data.get("Infrastructure") is not None:
        import capo_observabilityadmin.types.telemetry_manifest_infrastructure

        out["infrastructure"] = (
            capo_observabilityadmin.types.telemetry_manifest_infrastructure.deserialize_json(
                data["Infrastructure"]
            )
        )
    return out
