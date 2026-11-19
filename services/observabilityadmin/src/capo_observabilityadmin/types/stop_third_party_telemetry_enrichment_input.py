"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#StopThirdPartyTelemetryEnrichmentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.third_party_telemetry_enrichment_identifier


class StopThirdPartyTelemetryEnrichmentInput(TypedDict, closed=True):
    telemetry_enrichment_identifier: "capo_observabilityadmin.types.third_party_telemetry_enrichment_identifier.ThirdPartyTelemetryEnrichmentIdentifier"
    """<p>The identifier of the enrichment to stop. You can specify one of the following:</p> <ul> <li> <p>The name of the enrichment.</p> </li> <li> <p>The Amazon Resource Name (ARN) of the enrichment.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopThirdPartyTelemetryEnrichmentInput) -> dict:
    out: dict = {}
    out["TelemetryEnrichmentIdentifier"] = value["telemetry_enrichment_identifier"]
    return out


def deserialize_json(data: dict) -> StopThirdPartyTelemetryEnrichmentInput:
    out: StopThirdPartyTelemetryEnrichmentInput = {}  # type: ignore[typeddict-item]
    if data.get("TelemetryEnrichmentIdentifier") is not None:
        out["telemetry_enrichment_identifier"] = data["TelemetryEnrichmentIdentifier"]
    else:
        out["telemetry_enrichment_identifier"] = ""
    return out
