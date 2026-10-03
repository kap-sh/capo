"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#GetDashManifestConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediapackagev2.types.dash_audio_timeline_pattern
    import capo_mediapackagev2.types.dash_availability_start_time_configuration
    import capo_mediapackagev2.types.dash_base_urls
    import capo_mediapackagev2.types.dash_compactness
    import capo_mediapackagev2.types.dash_drm_signaling
    import capo_mediapackagev2.types.dash_dvb_settings
    import capo_mediapackagev2.types.dash_period_triggers
    import capo_mediapackagev2.types.dash_profiles
    import capo_mediapackagev2.types.dash_program_information
    import capo_mediapackagev2.types.dash_segment_template_format
    import capo_mediapackagev2.types.dash_subtitle_configuration
    import capo_mediapackagev2.types.dash_utc_timing
    import capo_mediapackagev2.types.filter_configuration
    import capo_mediapackagev2.types.resource_name
    import capo_mediapackagev2.types.scte_dash
    import capo_mediapackagev2.types.uri_path_type


class GetDashManifestConfiguration(TypedDict, closed=True):
    manifest_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>A short string that's appended to the endpoint URL. The manifest name creates a unique path to this endpoint. If you don't enter a value, MediaPackage uses the default manifest name, index. </p>"""
    url: "str"
    """<p>The egress domain URL for stream delivery from MediaPackage.</p>"""
    manifest_window_seconds: NotRequired["int"]
    """<p>The total duration (in seconds) of the manifest's content.</p>"""
    filter_configuration: NotRequired[
        "capo_mediapackagev2.types.filter_configuration.FilterConfiguration"
    ]
    min_update_period_seconds: NotRequired["int"]
    """<p>Minimum amount of time (in seconds) that the player should wait before requesting updates to the manifest.</p>"""
    min_buffer_time_seconds: NotRequired["int"]
    """<p>Minimum amount of content (in seconds) that a player must keep available in the buffer.</p>"""
    suggested_presentation_delay_seconds: NotRequired["int"]
    """<p>The amount of time (in seconds) that the player should be from the end of the manifest.</p>"""
    segment_template_format: NotRequired[
        "capo_mediapackagev2.types.dash_segment_template_format.DashSegmentTemplateFormat"
    ]
    """<p>Determines the type of variable used in the <code>media</code> URL of the <code>SegmentTemplate</code> tag in the manifest. Also specifies if segment timeline information is included in <code>SegmentTimeline</code> or <code>SegmentTemplate</code>.</p> <p>Value description:</p> <ul> <li> <p> <code>NUMBER_WITH_TIMELINE</code> - The <code>$Number$</code> variable is used in the <code>media</code> URL. The value of this variable is the sequential number of the segment. A full <code>SegmentTimeline</code> object is presented in each <code>SegmentTemplate</code>.</p> </li> </ul>"""
    period_triggers: NotRequired[
        "capo_mediapackagev2.types.dash_period_triggers.DashPeriodTriggers"
    ]
    """<p>A list of triggers that controls when AWS Elemental MediaPackage separates the MPEG-DASH manifest into multiple periods. Leave this value empty to indicate that the manifest is contained all in one period. For more information about periods in the DASH manifest, see <a href="https://docs.aws.amazon.com/mediapackage/latest/userguide/multi-period.html">Multi-period DASH in AWS Elemental MediaPackage</a>.</p>"""
    scte_dash: NotRequired["capo_mediapackagev2.types.scte_dash.ScteDash"]
    """<p>The SCTE configuration.</p>"""
    drm_signaling: NotRequired[
        "capo_mediapackagev2.types.dash_drm_signaling.DashDrmSignaling"
    ]
    """<p>Determines how the DASH manifest signals the DRM content.</p>"""
    utc_timing: NotRequired["capo_mediapackagev2.types.dash_utc_timing.DashUtcTiming"]
    """<p>Determines the type of UTC timing included in the DASH Media Presentation Description (MPD).</p>"""
    profiles: NotRequired["capo_mediapackagev2.types.dash_profiles.DashProfiles"]
    """<p>The profile that the output is compliant with.</p>"""
    base_urls: NotRequired["capo_mediapackagev2.types.dash_base_urls.DashBaseUrls"]
    """<p>The base URL to use for retrieving segments.</p>"""
    program_information: NotRequired[
        "capo_mediapackagev2.types.dash_program_information.DashProgramInformation"
    ]
    """<p>Details about the content that you want MediaPackage to pass through in the manifest to the playback device.</p>"""
    dvb_settings: NotRequired[
        "capo_mediapackagev2.types.dash_dvb_settings.DashDvbSettings"
    ]
    """<p>For endpoints that use the DVB-DASH profile only. The font download and error reporting information that you want MediaPackage to pass through to the manifest.</p>"""
    compactness: NotRequired[
        "capo_mediapackagev2.types.dash_compactness.DashCompactness"
    ]
    """<p>The layout of the DASH manifest that MediaPackage produces. <code>STANDARD</code> indicates a default manifest, which is compacted. <code>NONE</code> indicates a full manifest.</p>"""
    audio_timeline_pattern: NotRequired[
        "capo_mediapackagev2.types.dash_audio_timeline_pattern.DashAudioTimelinePattern"
    ]
    """<p>How MediaPackage represents the audio timeline in the DASH manifest, using DASH Segment Duration Patternization for audio adaptation sets. <code>PATTERNED</code> indicates that MediaPackage uses a pattern-based segment template for audio, reducing manifest size. <code>NONE</code> indicates that the manifest contains an explicit timeline for each audio segment.</p>"""
    subtitle_configuration: NotRequired[
        "capo_mediapackagev2.types.dash_subtitle_configuration.DashSubtitleConfiguration"
    ]
    """<p>The configuration for DASH subtitles.</p>"""
    uri_path_type: NotRequired["capo_mediapackagev2.types.uri_path_type.UriPathType"]
    """<p>The type of path used in manifest URIs. <code>LEAF</code> indicates leaf-relative paths. <code>ROOT</code> indicates root-relative paths that include the full path from root.</p>"""
    availability_start_time_configuration: NotRequired[
        "capo_mediapackagev2.types.dash_availability_start_time_configuration.DashAvailabilityStartTimeConfiguration"
    ]
    """<p>The configuration for the DASH <code>availabilityStartTime</code> attribute of the Media Presentation Description (MPD).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDashManifestConfiguration) -> dict:
    out: dict = {}
    out["ManifestName"] = value["manifest_name"]
    out["Url"] = value["url"]
    if "manifest_window_seconds" in value:
        out["ManifestWindowSeconds"] = value["manifest_window_seconds"]
    if "filter_configuration" in value:
        import capo_mediapackagev2.types.filter_configuration

        out["FilterConfiguration"] = (
            capo_mediapackagev2.types.filter_configuration.serialize_json(
                value["filter_configuration"]
            )
        )
    if "min_update_period_seconds" in value:
        out["MinUpdatePeriodSeconds"] = value["min_update_period_seconds"]
    if "min_buffer_time_seconds" in value:
        out["MinBufferTimeSeconds"] = value["min_buffer_time_seconds"]
    if "suggested_presentation_delay_seconds" in value:
        out["SuggestedPresentationDelaySeconds"] = value[
            "suggested_presentation_delay_seconds"
        ]
    if "segment_template_format" in value:
        import capo_mediapackagev2.types.dash_segment_template_format

        out["SegmentTemplateFormat"] = (
            capo_mediapackagev2.types.dash_segment_template_format.serialize_json(
                value["segment_template_format"]
            )
        )
    if "period_triggers" in value:
        import capo_mediapackagev2.types.dash_period_triggers

        out["PeriodTriggers"] = (
            capo_mediapackagev2.types.dash_period_triggers.serialize_json(
                value["period_triggers"]
            )
        )
    if "scte_dash" in value:
        import capo_mediapackagev2.types.scte_dash

        out["ScteDash"] = capo_mediapackagev2.types.scte_dash.serialize_json(
            value["scte_dash"]
        )
    if "drm_signaling" in value:
        import capo_mediapackagev2.types.dash_drm_signaling

        out["DrmSignaling"] = (
            capo_mediapackagev2.types.dash_drm_signaling.serialize_json(
                value["drm_signaling"]
            )
        )
    if "utc_timing" in value:
        import capo_mediapackagev2.types.dash_utc_timing

        out["UtcTiming"] = capo_mediapackagev2.types.dash_utc_timing.serialize_json(
            value["utc_timing"]
        )
    if "profiles" in value:
        import capo_mediapackagev2.types.dash_profiles

        out["Profiles"] = capo_mediapackagev2.types.dash_profiles.serialize_json(
            value["profiles"]
        )
    if "base_urls" in value:
        import capo_mediapackagev2.types.dash_base_urls

        out["BaseUrls"] = capo_mediapackagev2.types.dash_base_urls.serialize_json(
            value["base_urls"]
        )
    if "program_information" in value:
        import capo_mediapackagev2.types.dash_program_information

        out["ProgramInformation"] = (
            capo_mediapackagev2.types.dash_program_information.serialize_json(
                value["program_information"]
            )
        )
    if "dvb_settings" in value:
        import capo_mediapackagev2.types.dash_dvb_settings

        out["DvbSettings"] = capo_mediapackagev2.types.dash_dvb_settings.serialize_json(
            value["dvb_settings"]
        )
    if "compactness" in value:
        import capo_mediapackagev2.types.dash_compactness

        out["Compactness"] = capo_mediapackagev2.types.dash_compactness.serialize_json(
            value["compactness"]
        )
    if "audio_timeline_pattern" in value:
        import capo_mediapackagev2.types.dash_audio_timeline_pattern

        out["AudioTimelinePattern"] = (
            capo_mediapackagev2.types.dash_audio_timeline_pattern.serialize_json(
                value["audio_timeline_pattern"]
            )
        )
    if "subtitle_configuration" in value:
        import capo_mediapackagev2.types.dash_subtitle_configuration

        out["SubtitleConfiguration"] = (
            capo_mediapackagev2.types.dash_subtitle_configuration.serialize_json(
                value["subtitle_configuration"]
            )
        )
    if "uri_path_type" in value:
        import capo_mediapackagev2.types.uri_path_type

        out["UriPathType"] = capo_mediapackagev2.types.uri_path_type.serialize_json(
            value["uri_path_type"]
        )
    if "availability_start_time_configuration" in value:
        import capo_mediapackagev2.types.dash_availability_start_time_configuration

        out["AvailabilityStartTimeConfiguration"] = (
            capo_mediapackagev2.types.dash_availability_start_time_configuration.serialize_json(
                value["availability_start_time_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDashManifestConfiguration:
    out: GetDashManifestConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ManifestName") is not None:
        out["manifest_name"] = data["ManifestName"]
    else:
        raise DeserializationError(
            "GetDashManifestConfiguration.manifest_name required"
        )
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    else:
        raise DeserializationError("GetDashManifestConfiguration.url required")
    if data.get("ManifestWindowSeconds") is not None:
        out["manifest_window_seconds"] = data["ManifestWindowSeconds"]
    if data.get("FilterConfiguration") is not None:
        import capo_mediapackagev2.types.filter_configuration

        out["filter_configuration"] = (
            capo_mediapackagev2.types.filter_configuration.deserialize_json(
                data["FilterConfiguration"]
            )
        )
    if data.get("MinUpdatePeriodSeconds") is not None:
        out["min_update_period_seconds"] = data["MinUpdatePeriodSeconds"]
    if data.get("MinBufferTimeSeconds") is not None:
        out["min_buffer_time_seconds"] = data["MinBufferTimeSeconds"]
    if data.get("SuggestedPresentationDelaySeconds") is not None:
        out["suggested_presentation_delay_seconds"] = data[
            "SuggestedPresentationDelaySeconds"
        ]
    if data.get("SegmentTemplateFormat") is not None:
        import capo_mediapackagev2.types.dash_segment_template_format

        out["segment_template_format"] = (
            capo_mediapackagev2.types.dash_segment_template_format.deserialize_json(
                data["SegmentTemplateFormat"]
            )
        )
    if data.get("PeriodTriggers") is not None:
        import capo_mediapackagev2.types.dash_period_triggers

        out["period_triggers"] = (
            capo_mediapackagev2.types.dash_period_triggers.deserialize_json(
                data["PeriodTriggers"]
            )
        )
    if data.get("ScteDash") is not None:
        import capo_mediapackagev2.types.scte_dash

        out["scte_dash"] = capo_mediapackagev2.types.scte_dash.deserialize_json(
            data["ScteDash"]
        )
    if data.get("DrmSignaling") is not None:
        import capo_mediapackagev2.types.dash_drm_signaling

        out["drm_signaling"] = (
            capo_mediapackagev2.types.dash_drm_signaling.deserialize_json(
                data["DrmSignaling"]
            )
        )
    if data.get("UtcTiming") is not None:
        import capo_mediapackagev2.types.dash_utc_timing

        out["utc_timing"] = capo_mediapackagev2.types.dash_utc_timing.deserialize_json(
            data["UtcTiming"]
        )
    if data.get("Profiles") is not None:
        import capo_mediapackagev2.types.dash_profiles

        out["profiles"] = capo_mediapackagev2.types.dash_profiles.deserialize_json(
            data["Profiles"]
        )
    if data.get("BaseUrls") is not None:
        import capo_mediapackagev2.types.dash_base_urls

        out["base_urls"] = capo_mediapackagev2.types.dash_base_urls.deserialize_json(
            data["BaseUrls"]
        )
    if data.get("ProgramInformation") is not None:
        import capo_mediapackagev2.types.dash_program_information

        out["program_information"] = (
            capo_mediapackagev2.types.dash_program_information.deserialize_json(
                data["ProgramInformation"]
            )
        )
    if data.get("DvbSettings") is not None:
        import capo_mediapackagev2.types.dash_dvb_settings

        out["dvb_settings"] = (
            capo_mediapackagev2.types.dash_dvb_settings.deserialize_json(
                data["DvbSettings"]
            )
        )
    if data.get("Compactness") is not None:
        import capo_mediapackagev2.types.dash_compactness

        out["compactness"] = (
            capo_mediapackagev2.types.dash_compactness.deserialize_json(
                data["Compactness"]
            )
        )
    if data.get("AudioTimelinePattern") is not None:
        import capo_mediapackagev2.types.dash_audio_timeline_pattern

        out["audio_timeline_pattern"] = (
            capo_mediapackagev2.types.dash_audio_timeline_pattern.deserialize_json(
                data["AudioTimelinePattern"]
            )
        )
    if data.get("SubtitleConfiguration") is not None:
        import capo_mediapackagev2.types.dash_subtitle_configuration

        out["subtitle_configuration"] = (
            capo_mediapackagev2.types.dash_subtitle_configuration.deserialize_json(
                data["SubtitleConfiguration"]
            )
        )
    if data.get("UriPathType") is not None:
        import capo_mediapackagev2.types.uri_path_type

        out["uri_path_type"] = capo_mediapackagev2.types.uri_path_type.deserialize_json(
            data["UriPathType"]
        )
    if data.get("AvailabilityStartTimeConfiguration") is not None:
        import capo_mediapackagev2.types.dash_availability_start_time_configuration

        out["availability_start_time_configuration"] = (
            capo_mediapackagev2.types.dash_availability_start_time_configuration.deserialize_json(
                data["AvailabilityStartTimeConfiguration"]
            )
        )
    return out
