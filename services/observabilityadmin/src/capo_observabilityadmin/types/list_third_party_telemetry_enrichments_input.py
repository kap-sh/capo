"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ListThirdPartyTelemetryEnrichmentsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.list_third_party_telemetry_enrichments_max_results
    import capo_observabilityadmin.types.next_token
    import capo_observabilityadmin.types.third_party_telemetry_enrichment_status
    import capo_observabilityadmin.types.third_party_telemetry_source


class ListThirdPartyTelemetryEnrichmentsInput(TypedDict, closed=True):
    status: NotRequired[
        "capo_observabilityadmin.types.third_party_telemetry_enrichment_status.ThirdPartyTelemetryEnrichmentStatus"
    ]
    """<p>Returns only the enrichments that have this status. Valid values:</p> <ul> <li> <p> <code>Initializing</code> - CloudWatch is setting up the enrichment. Some telemetry can be enriched before setup completes.</p> </li> <li> <p> <code>Running</code> - The enrichment is active.</p> </li> <li> <p> <code>Stopped</code> - The enrichment is stopped.</p> </li> <li> <p> <code>Impaired</code> - The enrichment has a problem. <code>StatusReason</code> describes the problem.</p> </li> </ul>"""
    telemetry_source: NotRequired[
        "capo_observabilityadmin.types.third_party_telemetry_source.ThirdPartyTelemetrySource"
    ]
    """<p>Returns only the enrichments for this third-party telemetry source.</p>"""
    max_results: NotRequired[
        "capo_observabilityadmin.types.list_third_party_telemetry_enrichments_max_results.ListThirdPartyTelemetryEnrichmentsMaxResults"
    ]
    """<p>The maximum number of results to return in a single call. If you omit this parameter, the operation returns up to 100 results.</p>"""
    next_token: NotRequired["capo_observabilityadmin.types.next_token.NextToken"]
    """<p>The token for the next set of results. A previous call generates this token. If you omit this parameter, the operation returns the first page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThirdPartyTelemetryEnrichmentsInput) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_observabilityadmin.types.third_party_telemetry_enrichment_status

        out["Status"] = (
            capo_observabilityadmin.types.third_party_telemetry_enrichment_status.serialize_json(
                value["status"]
            )
        )
    if "telemetry_source" in value:
        import capo_observabilityadmin.types.third_party_telemetry_source

        out["TelemetrySource"] = (
            capo_observabilityadmin.types.third_party_telemetry_source.serialize_json(
                value["telemetry_source"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListThirdPartyTelemetryEnrichmentsInput:
    out: ListThirdPartyTelemetryEnrichmentsInput = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_observabilityadmin.types.third_party_telemetry_enrichment_status

        out["status"] = (
            capo_observabilityadmin.types.third_party_telemetry_enrichment_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("TelemetrySource") is not None:
        import capo_observabilityadmin.types.third_party_telemetry_source

        out["telemetry_source"] = (
            capo_observabilityadmin.types.third_party_telemetry_source.deserialize_json(
                data["TelemetrySource"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
