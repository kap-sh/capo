"""Generated from Smithy shape ``com.amazonaws.pinpoint#JourneyExecutionActivityMetricsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.map_of__string


class JourneyExecutionActivityMetricsResponse(TypedDict, closed=True):
    activity_type: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The type of activity that the metric applies to. Possible values are:</p> <ul><li><p>CONDITIONAL_SPLIT – For a yes/no split activity, which is an activity that sends participants down one of two paths in a journey.</p></li> <li><p>HOLDOUT – For a holdout activity, which is an activity that stops a journey for a specified percentage of participants.</p></li> <li><p>MESSAGE – For an email activity, which is an activity that sends an email message to participants.</p></li> <li><p>MULTI_CONDITIONAL_SPLIT – For a multivariate split activity, which is an activity that sends participants down one of as many as five paths in a journey.</p></li> <li><p>RANDOM_SPLIT – For a random split activity, which is an activity that sends specified percentages of participants down one of as many as five paths in a journey.</p></li> <li><p>WAIT – For a wait activity, which is an activity that waits for a certain amount of time or until a specific date and time before moving participants to the next activity in a journey.</p></li></ul>"""
    application_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the application that the metric applies to.</p>"""
    journey_activity_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the activity that the metric applies to.</p>"""
    journey_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the journey that the metric applies to.</p>"""
    last_evaluated_time: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date and time, in ISO 8601 format, when Amazon Pinpoint last evaluated the execution status of the activity and updated the data for the metric.</p>"""
    metrics: NotRequired["capo_pinpoint.types.map_of__string.MapOf__string"]
    """<p>A JSON object that contains the results of the query. The results vary depending on the type of activity (ActivityType). For information about the structure and contents of the results, see the <a href="https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html">Amazon Pinpoint Developer Guide</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JourneyExecutionActivityMetricsResponse) -> dict:
    out: dict = {}
    if "activity_type" in value:
        out["ActivityType"] = value["activity_type"]
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "journey_activity_id" in value:
        out["JourneyActivityId"] = value["journey_activity_id"]
    if "journey_id" in value:
        out["JourneyId"] = value["journey_id"]
    if "last_evaluated_time" in value:
        out["LastEvaluatedTime"] = value["last_evaluated_time"]
    if "metrics" in value:
        import capo_pinpoint.types.map_of__string

        out["Metrics"] = capo_pinpoint.types.map_of__string.serialize_json(
            value["metrics"]
        )
    return out


def deserialize_json(data: dict) -> JourneyExecutionActivityMetricsResponse:
    out: JourneyExecutionActivityMetricsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ActivityType") is not None:
        out["activity_type"] = data["ActivityType"]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    if data.get("JourneyActivityId") is not None:
        out["journey_activity_id"] = data["JourneyActivityId"]
    if data.get("JourneyId") is not None:
        out["journey_id"] = data["JourneyId"]
    if data.get("LastEvaluatedTime") is not None:
        out["last_evaluated_time"] = data["LastEvaluatedTime"]
    if data.get("Metrics") is not None:
        import capo_pinpoint.types.map_of__string

        out["metrics"] = capo_pinpoint.types.map_of__string.deserialize_json(
            data["Metrics"]
        )
    return out
