"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#DashPackage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage_vod.types.__boolean
    import capo_mediapackage_vod.types.__integer
    import capo_mediapackage_vod.types.__list_of__period_triggers_element
    import capo_mediapackage_vod.types.__list_of_dash_manifest
    import capo_mediapackage_vod.types.dash_encryption
    import capo_mediapackage_vod.types.segment_template_format


class DashPackage(TypedDict, closed=True):
    dash_manifests: NotRequired[
        "capo_mediapackage_vod.types.__list_of_dash_manifest.__listOfDashManifest"
    ]
    """A list of DASH manifest configurations."""
    encryption: NotRequired[
        "capo_mediapackage_vod.types.dash_encryption.DashEncryption"
    ]
    include_encoder_configuration_in_segments: NotRequired[
        "capo_mediapackage_vod.types.__boolean.__boolean"
    ]
    """When includeEncoderConfigurationInSegments is set to true, MediaPackage places your encoder's Sequence Parameter Set (SPS), Picture Parameter Set (PPS), and Video Parameter Set (VPS) metadata in every video segment instead of in the init fragment. This lets you use different SPS/PPS/VPS settings for your assets during content playback."""
    include_iframe_only_stream: NotRequired[
        "capo_mediapackage_vod.types.__boolean.__boolean"
    ]
    """When enabled, an I-Frame only stream will be included in the output."""
    period_triggers: NotRequired[
        "capo_mediapackage_vod.types.__list_of__period_triggers_element.__listOf__PeriodTriggersElement"
    ]
    """A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains "ADS", new periods will be created where the Asset contains SCTE-35 ad markers."""
    segment_duration_seconds: NotRequired[
        "capo_mediapackage_vod.types.__integer.__integer"
    ]
    """Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration."""
    segment_template_format: NotRequired[
        "capo_mediapackage_vod.types.segment_template_format.SegmentTemplateFormat"
    ]
    """Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs."""


# --- restJson1 ser/de ---
def serialize_json(value: DashPackage) -> dict:
    out: dict = {}
    if "dash_manifests" in value:
        import capo_mediapackage_vod.types.__list_of_dash_manifest

        out["dashManifests"] = (
            capo_mediapackage_vod.types.__list_of_dash_manifest.serialize_json(
                value["dash_manifests"]
            )
        )
    if "encryption" in value:
        import capo_mediapackage_vod.types.dash_encryption

        out["encryption"] = capo_mediapackage_vod.types.dash_encryption.serialize_json(
            value["encryption"]
        )
    if "include_encoder_configuration_in_segments" in value:
        out["includeEncoderConfigurationInSegments"] = value[
            "include_encoder_configuration_in_segments"
        ]
    if "include_iframe_only_stream" in value:
        out["includeIframeOnlyStream"] = value["include_iframe_only_stream"]
    if "period_triggers" in value:
        import capo_mediapackage_vod.types.__list_of__period_triggers_element

        out["periodTriggers"] = (
            capo_mediapackage_vod.types.__list_of__period_triggers_element.serialize_json(
                value["period_triggers"]
            )
        )
    if "segment_duration_seconds" in value:
        out["segmentDurationSeconds"] = value["segment_duration_seconds"]
    if "segment_template_format" in value:
        import capo_mediapackage_vod.types.segment_template_format

        out["segmentTemplateFormat"] = (
            capo_mediapackage_vod.types.segment_template_format.serialize_json(
                value["segment_template_format"]
            )
        )
    return out


def deserialize_json(data: dict) -> DashPackage:
    out: DashPackage = {}  # type: ignore[typeddict-item]
    if data.get("dashManifests") is not None:
        import capo_mediapackage_vod.types.__list_of_dash_manifest

        out["dash_manifests"] = (
            capo_mediapackage_vod.types.__list_of_dash_manifest.deserialize_json(
                data["dashManifests"]
            )
        )
    if data.get("encryption") is not None:
        import capo_mediapackage_vod.types.dash_encryption

        out["encryption"] = (
            capo_mediapackage_vod.types.dash_encryption.deserialize_json(
                data["encryption"]
            )
        )
    if data.get("includeEncoderConfigurationInSegments") is not None:
        out["include_encoder_configuration_in_segments"] = data[
            "includeEncoderConfigurationInSegments"
        ]
    if data.get("includeIframeOnlyStream") is not None:
        out["include_iframe_only_stream"] = data["includeIframeOnlyStream"]
    if data.get("periodTriggers") is not None:
        import capo_mediapackage_vod.types.__list_of__period_triggers_element

        out["period_triggers"] = (
            capo_mediapackage_vod.types.__list_of__period_triggers_element.deserialize_json(
                data["periodTriggers"]
            )
        )
    if data.get("segmentDurationSeconds") is not None:
        out["segment_duration_seconds"] = data["segmentDurationSeconds"]
    if data.get("segmentTemplateFormat") is not None:
        import capo_mediapackage_vod.types.segment_template_format

        out["segment_template_format"] = (
            capo_mediapackage_vod.types.segment_template_format.deserialize_json(
                data["segmentTemplateFormat"]
            )
        )
    return out
