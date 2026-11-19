"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ListThirdPartyTelemetryEnrichmentsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.next_token
    import capo_observabilityadmin.types.third_party_telemetry_enrichment_summaries


class ListThirdPartyTelemetryEnrichmentsOutput(TypedDict, closed=True):
    telemetry_enrichments: NotRequired[
        "capo_observabilityadmin.types.third_party_telemetry_enrichment_summaries.ThirdPartyTelemetryEnrichmentSummaries"
    ]
    """<p>The enrichments in your account and Region.</p>"""
    next_token: NotRequired["capo_observabilityadmin.types.next_token.NextToken"]
    """<p>A token to resume pagination of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThirdPartyTelemetryEnrichmentsOutput) -> dict:
    out: dict = {}
    if "telemetry_enrichments" in value:
        import capo_observabilityadmin.types.third_party_telemetry_enrichment_summaries

        out["TelemetryEnrichments"] = (
            capo_observabilityadmin.types.third_party_telemetry_enrichment_summaries.serialize_json(
                value["telemetry_enrichments"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListThirdPartyTelemetryEnrichmentsOutput:
    out: ListThirdPartyTelemetryEnrichmentsOutput = {}  # type: ignore[typeddict-item]
    if data.get("TelemetryEnrichments") is not None:
        import capo_observabilityadmin.types.third_party_telemetry_enrichment_summaries

        out["telemetry_enrichments"] = (
            capo_observabilityadmin.types.third_party_telemetry_enrichment_summaries.deserialize_json(
                data["TelemetryEnrichments"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
