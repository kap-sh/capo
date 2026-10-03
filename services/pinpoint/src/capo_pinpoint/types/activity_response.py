"""Generated from Smithy shape ``com.amazonaws.pinpoint#ActivityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__integer
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.map_of__string


class ActivityResponse(TypedDict, closed=True):
    application_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the application that the campaign applies to.</p>"""
    campaign_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the campaign that the activity applies to.</p>"""
    end: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The actual time, in ISO 8601 format, when the activity was marked CANCELLED or COMPLETED.</p>"""
    id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the activity.</p>"""
    result: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>Specifies whether the activity succeeded. Possible values are SUCCESS and FAIL.</p>"""
    scheduled_start: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The scheduled start time, in ISO 8601 format, for the activity.</p>"""
    start: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The actual start time, in ISO 8601 format, of the activity.</p>"""
    state: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The current status of the activity. Possible values are: PENDING, INITIALIZING, RUNNING, PAUSED, CANCELLED, and COMPLETED.</p>"""
    successful_endpoint_count: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The total number of endpoints that the campaign successfully delivered messages to.</p>"""
    timezones_completed_count: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The total number of time zones that were completed.</p>"""
    timezones_total_count: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The total number of unique time zones that are in the segment for the campaign.</p>"""
    total_endpoint_count: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The total number of endpoints that the campaign attempted to deliver messages to.</p>"""
    treatment_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the campaign treatment that the activity applies to. A treatment is a variation of a campaign that's used for A/B testing of a campaign.</p>"""
    execution_metrics: NotRequired["capo_pinpoint.types.map_of__string.MapOf__string"]
    """<p>A JSON object that contains metrics relating to the campaign execution for this campaign activity. For information about the structure and contents of the results, see <a href="https://docs.aws.amazon.com//pinpoint/latest/developerguide/analytics-standard-metrics.html">Standard Amazon Pinpoint analytics metrics</a> in the <i>Amazon Pinpoint Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActivityResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "campaign_id" in value:
        out["CampaignId"] = value["campaign_id"]
    if "end" in value:
        out["End"] = value["end"]
    if "id" in value:
        out["Id"] = value["id"]
    if "result" in value:
        out["Result"] = value["result"]
    if "scheduled_start" in value:
        out["ScheduledStart"] = value["scheduled_start"]
    if "start" in value:
        out["Start"] = value["start"]
    if "state" in value:
        out["State"] = value["state"]
    if "successful_endpoint_count" in value:
        out["SuccessfulEndpointCount"] = value["successful_endpoint_count"]
    if "timezones_completed_count" in value:
        out["TimezonesCompletedCount"] = value["timezones_completed_count"]
    if "timezones_total_count" in value:
        out["TimezonesTotalCount"] = value["timezones_total_count"]
    if "total_endpoint_count" in value:
        out["TotalEndpointCount"] = value["total_endpoint_count"]
    if "treatment_id" in value:
        out["TreatmentId"] = value["treatment_id"]
    if "execution_metrics" in value:
        import capo_pinpoint.types.map_of__string

        out["ExecutionMetrics"] = capo_pinpoint.types.map_of__string.serialize_json(
            value["execution_metrics"]
        )
    return out


def deserialize_json(data: dict) -> ActivityResponse:
    out: ActivityResponse = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    if data.get("CampaignId") is not None:
        out["campaign_id"] = data["CampaignId"]
    if data.get("End") is not None:
        out["end"] = data["End"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Result") is not None:
        out["result"] = data["Result"]
    if data.get("ScheduledStart") is not None:
        out["scheduled_start"] = data["ScheduledStart"]
    if data.get("Start") is not None:
        out["start"] = data["Start"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("SuccessfulEndpointCount") is not None:
        out["successful_endpoint_count"] = data["SuccessfulEndpointCount"]
    if data.get("TimezonesCompletedCount") is not None:
        out["timezones_completed_count"] = data["TimezonesCompletedCount"]
    if data.get("TimezonesTotalCount") is not None:
        out["timezones_total_count"] = data["TimezonesTotalCount"]
    if data.get("TotalEndpointCount") is not None:
        out["total_endpoint_count"] = data["TotalEndpointCount"]
    if data.get("TreatmentId") is not None:
        out["treatment_id"] = data["TreatmentId"]
    if data.get("ExecutionMetrics") is not None:
        import capo_pinpoint.types.map_of__string

        out["execution_metrics"] = capo_pinpoint.types.map_of__string.deserialize_json(
            data["ExecutionMetrics"]
        )
    return out
