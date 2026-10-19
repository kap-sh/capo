"""Generated from Smithy shape ``com.amazonaws.mediatailor#YieldOptimizationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.aps_publisher_id
    import capo_mediatailor.types.aps_region
    import capo_mediatailor.types.minimum_unfilled_duration_seconds
    import capo_mediatailor.types.open_rtb_template_string


class YieldOptimizationConfiguration(TypedDict, closed=True):
    minimum_unfilled_duration: "capo_mediatailor.types.minimum_unfilled_duration_seconds.MinimumUnfilledDurationSeconds"
    """<p>The minimum unfilled duration, in seconds, that must remain in an ad break before MediaTailor requests additional ads from Amazon Publisher Services (APS). For example, if set to 6 seconds, yield optimization triggers only when at least 6 seconds of unfilled time remains after the primary ad server response.</p>"""
    publisher_id: "capo_mediatailor.types.aps_publisher_id.ApsPublisherId"
    """<p>Publisher ID for an existing Amazon Publisher Services configuration. This ID must be obtained by registering with APS prior to using the Yield Optimization feature. The Publisher ID identifies your account in the APS system and is required for all bid requests.</p>"""
    region: "capo_mediatailor.types.aps_region.ApsRegion"
    """<p>The Amazon Publisher Services (APS) region that MediaTailor sends bid requests to. Choose the region closest to your primary audience, because the selection affects both latency and the ad inventory available to you. This setting applies to the entire playback configuration, not to individual viewers. If you serve traffic across multiple regions, create a separate playback configuration for each APS region.</p>"""
    open_rtb_template: (
        "capo_mediatailor.types.open_rtb_template_string.OpenRtbTemplateString"
    )
    """<p>The OpenRTB bid request template, in JSON, that MediaTailor sends to Amazon Publisher Services (APS). The template must include an <code>imp</code> array with one impression specifying <code>bidfloor</code>, an <code>app</code> object specifying <code>bundle</code> and <code>storeurl</code>, and a <code>device</code> object specifying <code>ua</code> and <code>ip</code>. Use double curly braces (for example, <code>{{player_params.user_agent}}</code>) to insert session variables and player parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: YieldOptimizationConfiguration) -> dict:
    out: dict = {}
    out["MinimumUnfilledDuration"] = value["minimum_unfilled_duration"]
    out["PublisherId"] = value["publisher_id"]
    import capo_mediatailor.types.aps_region

    out["Region"] = capo_mediatailor.types.aps_region.serialize_json(value["region"])
    out["OpenRtbTemplate"] = value["open_rtb_template"]
    return out


def deserialize_json(data: dict) -> YieldOptimizationConfiguration:
    out: YieldOptimizationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("MinimumUnfilledDuration") is not None:
        out["minimum_unfilled_duration"] = data["MinimumUnfilledDuration"]
    else:
        out["minimum_unfilled_duration"] = 0
    if data.get("PublisherId") is not None:
        out["publisher_id"] = data["PublisherId"]
    else:
        out["publisher_id"] = ""
    if data.get("Region") is not None:
        import capo_mediatailor.types.aps_region

        out["region"] = capo_mediatailor.types.aps_region.deserialize_json(
            data["Region"]
        )
    else:
        import typing

        out["region"] = typing.cast("capo_mediatailor.types.aps_region.ApsRegion", "")
    if data.get("OpenRtbTemplate") is not None:
        out["open_rtb_template"] = data["OpenRtbTemplate"]
    else:
        out["open_rtb_template"] = ""
    return out
