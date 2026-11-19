"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ThirdPartyTelemetryEnrichmentSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.third_party_telemetry_enrichment_summary

ThirdPartyTelemetryEnrichmentSummaries: TypeAlias = list[
    "capo_observabilityadmin.types.third_party_telemetry_enrichment_summary.ThirdPartyTelemetryEnrichmentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThirdPartyTelemetryEnrichmentSummaries) -> list:
    import capo_observabilityadmin.types.third_party_telemetry_enrichment_summary

    out: list = []
    for item in value:
        out.append(
            capo_observabilityadmin.types.third_party_telemetry_enrichment_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ThirdPartyTelemetryEnrichmentSummaries:
    import capo_observabilityadmin.types.third_party_telemetry_enrichment_summary

    out: ThirdPartyTelemetryEnrichmentSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_observabilityadmin.types.third_party_telemetry_enrichment_summary.deserialize_json(
                item
            )
        )
    return out
