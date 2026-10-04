"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#FilterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mediapackagev2.types.multiview_filter_configuration


class FilterConfiguration(TypedDict, closed=True):
    manifest_filter: NotRequired["str"]
    """<p>Optionally specify one or more manifest filters for all of your manifest egress requests. When you include a manifest filter, note that you cannot use an identical manifest filter query parameter for this manifest's endpoint URL.</p>"""
    drm_settings: NotRequired["str"]
    """<p>Optionally specify one or more DRM settings for all of your manifest egress requests. When you include a DRM setting, note that you cannot use an identical DRM setting query parameter for this manifest's endpoint URL.</p>"""
    start: NotRequired["datetime.datetime"]
    """<p>Optionally specify the start time for all of your manifest egress requests. When you include start time, note that you cannot use start time query parameters for this manifest's endpoint URL.</p>"""
    end: NotRequired["datetime.datetime"]
    """<p>Optionally specify the end time for all of your manifest egress requests. When you include end time, note that you cannot use end time query parameters for this manifest's endpoint URL.</p>"""
    time_delay_seconds: NotRequired["int"]
    """<p>Optionally specify the time delay for all of your manifest egress requests. Enter a value that is smaller than your endpoint's startover window. When you include time delay, note that you cannot use time delay query parameters for this manifest's endpoint URL.</p>"""
    clip_start_time: NotRequired["datetime.datetime"]
    """<p>Optionally specify the clip start time for all of your manifest egress requests. When you include clip start time, note that you cannot use clip start time query parameters for this manifest's endpoint URL.</p>"""
    multiview: NotRequired[
        "capo_mediapackagev2.types.multiview_filter_configuration.MultiviewFilterConfiguration"
    ]
    """<p>Optionally pin this manifest to a single multiview combination, so that players request it without an <code>aws.multiview</code> query parameter. When you pin a combination, note that you cannot use the <code>aws.multiview</code> query parameter for this manifest's endpoint URL, even when that parameter requests the same combination.</p> <p>This setting is valid only on an origin endpoint whose channel has an <code>InputType</code> of <code>MULTIVIEW</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterConfiguration) -> dict:
    out: dict = {}
    if "manifest_filter" in value:
        out["ManifestFilter"] = value["manifest_filter"]
    if "drm_settings" in value:
        out["DrmSettings"] = value["drm_settings"]
    if "start" in value:
        import capo_mediapackagev2.types._prelude.timestamp

        out["Start"] = capo_mediapackagev2.types._prelude.timestamp.serialize_json(
            value["start"]
        )
    if "end" in value:
        import capo_mediapackagev2.types._prelude.timestamp

        out["End"] = capo_mediapackagev2.types._prelude.timestamp.serialize_json(
            value["end"]
        )
    if "time_delay_seconds" in value:
        out["TimeDelaySeconds"] = value["time_delay_seconds"]
    if "clip_start_time" in value:
        import capo_mediapackagev2.types._prelude.timestamp

        out["ClipStartTime"] = (
            capo_mediapackagev2.types._prelude.timestamp.serialize_json(
                value["clip_start_time"]
            )
        )
    if "multiview" in value:
        import capo_mediapackagev2.types.multiview_filter_configuration

        out["Multiview"] = (
            capo_mediapackagev2.types.multiview_filter_configuration.serialize_json(
                value["multiview"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterConfiguration:
    out: FilterConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ManifestFilter") is not None:
        out["manifest_filter"] = data["ManifestFilter"]
    if data.get("DrmSettings") is not None:
        out["drm_settings"] = data["DrmSettings"]
    if data.get("Start") is not None:
        import capo_mediapackagev2.types._prelude.timestamp

        out["start"] = capo_mediapackagev2.types._prelude.timestamp.deserialize_json(
            data["Start"]
        )
    if data.get("End") is not None:
        import capo_mediapackagev2.types._prelude.timestamp

        out["end"] = capo_mediapackagev2.types._prelude.timestamp.deserialize_json(
            data["End"]
        )
    if data.get("TimeDelaySeconds") is not None:
        out["time_delay_seconds"] = data["TimeDelaySeconds"]
    if data.get("ClipStartTime") is not None:
        import capo_mediapackagev2.types._prelude.timestamp

        out["clip_start_time"] = (
            capo_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["ClipStartTime"]
            )
        )
    if data.get("Multiview") is not None:
        import capo_mediapackagev2.types.multiview_filter_configuration

        out["multiview"] = (
            capo_mediapackagev2.types.multiview_filter_configuration.deserialize_json(
                data["Multiview"]
            )
        )
    return out
