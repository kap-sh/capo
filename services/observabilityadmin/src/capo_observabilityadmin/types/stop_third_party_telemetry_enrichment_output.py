"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#StopThirdPartyTelemetryEnrichmentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.status_reason
    import capo_observabilityadmin.types.third_party_telemetry_enrichment_name
    import capo_observabilityadmin.types.third_party_telemetry_enrichment_status
    import capo_observabilityadmin.types.third_party_telemetry_source


class StopThirdPartyTelemetryEnrichmentOutput(TypedDict, closed=True):
    name: "capo_observabilityadmin.types.third_party_telemetry_enrichment_name.ThirdPartyTelemetryEnrichmentName"
    """<p>The name of the enrichment.</p>"""
    telemetry_source: "capo_observabilityadmin.types.third_party_telemetry_source.ThirdPartyTelemetrySource"
    """<p>The third-party telemetry source of the enrichment.</p>"""
    status: "capo_observabilityadmin.types.third_party_telemetry_enrichment_status.ThirdPartyTelemetryEnrichmentStatus"
    """<p>The status of the enrichment after the stop operation. Valid values:</p> <ul> <li> <p> <code>Initializing</code> - CloudWatch is setting up the enrichment. Some telemetry can be enriched before setup completes.</p> </li> <li> <p> <code>Running</code> - The enrichment is active.</p> </li> <li> <p> <code>Stopped</code> - The enrichment is stopped.</p> </li> <li> <p> <code>Impaired</code> - The enrichment has a problem. <code>StatusReason</code> describes the problem.</p> </li> </ul>"""
    status_reason: NotRequired[
        "capo_observabilityadmin.types.status_reason.StatusReason"
    ]
    """<p>The reason for the current status. This field is present when the status is <code>Impaired</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopThirdPartyTelemetryEnrichmentOutput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_observabilityadmin.types.third_party_telemetry_source

    out["TelemetrySource"] = (
        capo_observabilityadmin.types.third_party_telemetry_source.serialize_json(
            value["telemetry_source"]
        )
    )
    import capo_observabilityadmin.types.third_party_telemetry_enrichment_status

    out["Status"] = (
        capo_observabilityadmin.types.third_party_telemetry_enrichment_status.serialize_json(
            value["status"]
        )
    )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> StopThirdPartyTelemetryEnrichmentOutput:
    out: StopThirdPartyTelemetryEnrichmentOutput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("TelemetrySource") is not None:
        import capo_observabilityadmin.types.third_party_telemetry_source

        out["telemetry_source"] = (
            capo_observabilityadmin.types.third_party_telemetry_source.deserialize_json(
                data["TelemetrySource"]
            )
        )
    else:
        import typing

        out["telemetry_source"] = typing.cast(
            "capo_observabilityadmin.types.third_party_telemetry_source.ThirdPartyTelemetrySource",
            "",
        )
    if data.get("Status") is not None:
        import capo_observabilityadmin.types.third_party_telemetry_enrichment_status

        out["status"] = (
            capo_observabilityadmin.types.third_party_telemetry_enrichment_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_observabilityadmin.types.third_party_telemetry_enrichment_status.ThirdPartyTelemetryEnrichmentStatus",
            "",
        )
    if data.get("StatusReason") is not None:
        out["status_reason"] = data["StatusReason"]
    return out
