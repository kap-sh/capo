"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ThirdPartyTelemetryEnrichmentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.third_party_telemetry_enrichment_name
    import capo_observabilityadmin.types.third_party_telemetry_enrichment_status
    import capo_observabilityadmin.types.third_party_telemetry_source


class ThirdPartyTelemetryEnrichmentSummary(TypedDict, closed=True):
    name: NotRequired[
        "capo_observabilityadmin.types.third_party_telemetry_enrichment_name.ThirdPartyTelemetryEnrichmentName"
    ]
    """<p>The name of the enrichment.</p>"""
    telemetry_source: NotRequired[
        "capo_observabilityadmin.types.third_party_telemetry_source.ThirdPartyTelemetrySource"
    ]
    """<p>The third-party telemetry source of the enrichment.</p>"""
    status: NotRequired[
        "capo_observabilityadmin.types.third_party_telemetry_enrichment_status.ThirdPartyTelemetryEnrichmentStatus"
    ]
    """<p>The current status of the enrichment. Valid values:</p> <ul> <li> <p> <code>Initializing</code> - CloudWatch is setting up the enrichment. Some telemetry can be enriched before setup completes.</p> </li> <li> <p> <code>Running</code> - The enrichment is active.</p> </li> <li> <p> <code>Stopped</code> - The enrichment is stopped.</p> </li> <li> <p> <code>Impaired</code> - The enrichment has a problem. <code>StatusReason</code> describes the problem.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThirdPartyTelemetryEnrichmentSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "telemetry_source" in value:
        import capo_observabilityadmin.types.third_party_telemetry_source

        out["TelemetrySource"] = (
            capo_observabilityadmin.types.third_party_telemetry_source.serialize_json(
                value["telemetry_source"]
            )
        )
    if "status" in value:
        import capo_observabilityadmin.types.third_party_telemetry_enrichment_status

        out["Status"] = (
            capo_observabilityadmin.types.third_party_telemetry_enrichment_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> ThirdPartyTelemetryEnrichmentSummary:
    out: ThirdPartyTelemetryEnrichmentSummary = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("TelemetrySource") is not None:
        import capo_observabilityadmin.types.third_party_telemetry_source

        out["telemetry_source"] = (
            capo_observabilityadmin.types.third_party_telemetry_source.deserialize_json(
                data["TelemetrySource"]
            )
        )
    if data.get("Status") is not None:
        import capo_observabilityadmin.types.third_party_telemetry_enrichment_status

        out["status"] = (
            capo_observabilityadmin.types.third_party_telemetry_enrichment_status.deserialize_json(
                data["Status"]
            )
        )
    return out
