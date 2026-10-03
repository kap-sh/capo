"""Generated from Smithy shape ``com.amazonaws.pinpoint#WriteApplicationSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__boolean
    import capo_pinpoint.types.application_settings_journey_limits
    import capo_pinpoint.types.campaign_hook
    import capo_pinpoint.types.campaign_limits
    import capo_pinpoint.types.quiet_time


class WriteApplicationSettingsRequest(TypedDict, closed=True):
    campaign_hook: NotRequired["capo_pinpoint.types.campaign_hook.CampaignHook"]
    """<p>The settings for the AWS Lambda function to invoke by default as a code hook for campaigns in the application. You can use this hook to customize segments that are used by campaigns in the application.</p> <p>To override these settings and define custom settings for a specific campaign, use the CampaignHook object of the <link linkend="apps-application-id-campaigns-campaign-id">Campaign</link> resource.</p>"""
    cloud_watch_metrics_enabled: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether to enable application-related alarms in Amazon CloudWatch.</p>"""
    event_tagging_enabled: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    limits: NotRequired["capo_pinpoint.types.campaign_limits.CampaignLimits"]
    """<p>The default sending limits for campaigns in the application. To override these limits and define custom limits for a specific campaign or journey, use the <link linkend="apps-application-id-campaigns-campaign-id">Campaign</link> resource or the <link linkend="apps-application-id-journeys-journey-id">Journey</link> resource, respectively.</p>"""
    quiet_time: NotRequired["capo_pinpoint.types.quiet_time.QuietTime"]
    """<p>The default quiet time for campaigns in the application. Quiet time is a specific time range when messages aren't sent to endpoints, if all the following conditions are met:</p> <ul><li><p>The EndpointDemographic.Timezone property of the endpoint is set to a valid value.</p></li> <li><p>The current time in the endpoint's time zone is later than or equal to the time specified by the QuietTime.Start property for the application (or a campaign or journey that has custom quiet time settings).</p></li> <li><p>The current time in the endpoint's time zone is earlier than or equal to the time specified by the QuietTime.End property for the application (or a campaign or journey that has custom quiet time settings).</p></li></ul> <p>If any of the preceding conditions isn't met, the endpoint will receive messages from a campaign or journey, even if quiet time is enabled.</p> <p>To override the default quiet time settings for a specific campaign or journey, use the <link linkend="apps-application-id-campaigns-campaign-id">Campaign</link> resource or the <link linkend="apps-application-id-journeys-journey-id">Journey</link> resource to define a custom quiet time for the campaign or journey.</p>"""
    journey_limits: NotRequired[
        "capo_pinpoint.types.application_settings_journey_limits.ApplicationSettingsJourneyLimits"
    ]
    """<p>The default sending limits for journeys in the application. These limits apply to each journey for the application but can be overridden, on a per journey basis, with the JourneyLimits resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WriteApplicationSettingsRequest) -> dict:
    out: dict = {}
    if "campaign_hook" in value:
        import capo_pinpoint.types.campaign_hook

        out["CampaignHook"] = capo_pinpoint.types.campaign_hook.serialize_json(
            value["campaign_hook"]
        )
    if "cloud_watch_metrics_enabled" in value:
        out["CloudWatchMetricsEnabled"] = value["cloud_watch_metrics_enabled"]
    if "event_tagging_enabled" in value:
        out["EventTaggingEnabled"] = value["event_tagging_enabled"]
    if "limits" in value:
        import capo_pinpoint.types.campaign_limits

        out["Limits"] = capo_pinpoint.types.campaign_limits.serialize_json(
            value["limits"]
        )
    if "quiet_time" in value:
        import capo_pinpoint.types.quiet_time

        out["QuietTime"] = capo_pinpoint.types.quiet_time.serialize_json(
            value["quiet_time"]
        )
    if "journey_limits" in value:
        import capo_pinpoint.types.application_settings_journey_limits

        out["JourneyLimits"] = (
            capo_pinpoint.types.application_settings_journey_limits.serialize_json(
                value["journey_limits"]
            )
        )
    return out


def deserialize_json(data: dict) -> WriteApplicationSettingsRequest:
    out: WriteApplicationSettingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("CampaignHook") is not None:
        import capo_pinpoint.types.campaign_hook

        out["campaign_hook"] = capo_pinpoint.types.campaign_hook.deserialize_json(
            data["CampaignHook"]
        )
    if data.get("CloudWatchMetricsEnabled") is not None:
        out["cloud_watch_metrics_enabled"] = data["CloudWatchMetricsEnabled"]
    if data.get("EventTaggingEnabled") is not None:
        out["event_tagging_enabled"] = data["EventTaggingEnabled"]
    if data.get("Limits") is not None:
        import capo_pinpoint.types.campaign_limits

        out["limits"] = capo_pinpoint.types.campaign_limits.deserialize_json(
            data["Limits"]
        )
    if data.get("QuietTime") is not None:
        import capo_pinpoint.types.quiet_time

        out["quiet_time"] = capo_pinpoint.types.quiet_time.deserialize_json(
            data["QuietTime"]
        )
    if data.get("JourneyLimits") is not None:
        import capo_pinpoint.types.application_settings_journey_limits

        out["journey_limits"] = (
            capo_pinpoint.types.application_settings_journey_limits.deserialize_json(
                data["JourneyLimits"]
            )
        )
    return out
