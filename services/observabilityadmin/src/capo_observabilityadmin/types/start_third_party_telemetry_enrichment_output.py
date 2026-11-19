"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#StartThirdPartyTelemetryEnrichmentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.status_reason
    import capo_observabilityadmin.types.tag_map_output
    import capo_observabilityadmin.types.telemetry_source_configuration_output
    import capo_observabilityadmin.types.third_party_telemetry_enrichment_arn
    import capo_observabilityadmin.types.third_party_telemetry_enrichment_name
    import capo_observabilityadmin.types.third_party_telemetry_enrichment_status


class StartThirdPartyTelemetryEnrichmentOutput(TypedDict, closed=True):
    arn: "capo_observabilityadmin.types.third_party_telemetry_enrichment_arn.ThirdPartyTelemetryEnrichmentArn"
    """<p>The Amazon Resource Name (ARN) of the enrichment.</p>"""
    name: "capo_observabilityadmin.types.third_party_telemetry_enrichment_name.ThirdPartyTelemetryEnrichmentName"
    """<p>The name of the enrichment.</p>"""
    status: "capo_observabilityadmin.types.third_party_telemetry_enrichment_status.ThirdPartyTelemetryEnrichmentStatus"
    """<p>The status of the enrichment after the start operation. Valid values:</p> <ul> <li> <p> <code>Initializing</code> - CloudWatch is setting up the enrichment. Some telemetry can be enriched before setup completes.</p> </li> <li> <p> <code>Running</code> - The enrichment is active.</p> </li> <li> <p> <code>Stopped</code> - The enrichment is stopped.</p> </li> <li> <p> <code>Impaired</code> - The enrichment has a problem. <code>StatusReason</code> describes the problem.</p> </li> </ul>"""
    status_reason: NotRequired[
        "capo_observabilityadmin.types.status_reason.StatusReason"
    ]
    """<p>The reason for the current status. This field is present when the status is <code>Impaired</code>.</p>"""
    telemetry_source_configuration: "capo_observabilityadmin.types.telemetry_source_configuration_output.TelemetrySourceConfigurationOutput"
    """<p>The source configuration of the enrichment.</p>"""
    tags: NotRequired["capo_observabilityadmin.types.tag_map_output.TagMapOutput"]
    """<p>The tags associated with the enrichment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartThirdPartyTelemetryEnrichmentOutput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    import capo_observabilityadmin.types.third_party_telemetry_enrichment_status

    out["Status"] = (
        capo_observabilityadmin.types.third_party_telemetry_enrichment_status.serialize_json(
            value["status"]
        )
    )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    import capo_observabilityadmin.types.telemetry_source_configuration_output

    out["TelemetrySourceConfiguration"] = (
        capo_observabilityadmin.types.telemetry_source_configuration_output.serialize_json(
            value["telemetry_source_configuration"]
        )
    )
    if "tags" in value:
        import capo_observabilityadmin.types.tag_map_output

        out["Tags"] = capo_observabilityadmin.types.tag_map_output.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> StartThirdPartyTelemetryEnrichmentOutput:
    out: StartThirdPartyTelemetryEnrichmentOutput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
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
    if data.get("TelemetrySourceConfiguration") is not None:
        import capo_observabilityadmin.types.telemetry_source_configuration_output

        out["telemetry_source_configuration"] = (
            capo_observabilityadmin.types.telemetry_source_configuration_output.deserialize_json(
                data["TelemetrySourceConfiguration"]
            )
        )
    else:
        out["telemetry_source_configuration"] = {"$unknown": {"name": ""}}
    if data.get("Tags") is not None:
        import capo_observabilityadmin.types.tag_map_output

        out["tags"] = capo_observabilityadmin.types.tag_map_output.deserialize_json(
            data["Tags"]
        )
    return out
