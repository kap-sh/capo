"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#StartThirdPartyTelemetryEnrichmentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.tag_map_input
    import capo_observabilityadmin.types.telemetry_source_configuration_input
    import capo_observabilityadmin.types.third_party_telemetry_enrichment_name


class StartThirdPartyTelemetryEnrichmentInput(TypedDict, closed=True):
    name: "capo_observabilityadmin.types.third_party_telemetry_enrichment_name.ThirdPartyTelemetryEnrichmentName"
    """<p>A name for the enrichment. The name must be unique in your account and Region. You can use the name instead of the ARN to identify the enrichment in other operations.</p>"""
    telemetry_source_configuration: "capo_observabilityadmin.types.telemetry_source_configuration_input.TelemetrySourceConfigurationInput"
    """<p>The third-party telemetry source to collect resource metadata from. Specify exactly one telemetry source.</p>"""
    tags: NotRequired["capo_observabilityadmin.types.tag_map_input.TagMapInput"]
    """<p>The tags to associate with the enrichment resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartThirdPartyTelemetryEnrichmentInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_observabilityadmin.types.telemetry_source_configuration_input

    out["TelemetrySourceConfiguration"] = (
        capo_observabilityadmin.types.telemetry_source_configuration_input.serialize_json(
            value["telemetry_source_configuration"]
        )
    )
    if "tags" in value:
        import capo_observabilityadmin.types.tag_map_input

        out["Tags"] = capo_observabilityadmin.types.tag_map_input.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> StartThirdPartyTelemetryEnrichmentInput:
    out: StartThirdPartyTelemetryEnrichmentInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("TelemetrySourceConfiguration") is not None:
        import capo_observabilityadmin.types.telemetry_source_configuration_input

        out["telemetry_source_configuration"] = (
            capo_observabilityadmin.types.telemetry_source_configuration_input.deserialize_json(
                data["TelemetrySourceConfiguration"]
            )
        )
    else:
        out["telemetry_source_configuration"] = {"$unknown": {"name": ""}}
    if data.get("Tags") is not None:
        import capo_observabilityadmin.types.tag_map_input

        out["tags"] = capo_observabilityadmin.types.tag_map_input.deserialize_json(
            data["Tags"]
        )
    return out
