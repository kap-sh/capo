"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRelationalDatabaseEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.integer
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.string


class GetRelationalDatabaseEventsRequest(TypedDict, closed=True):
    relational_database_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the database from which to get events.</p>"""
    duration_in_minutes: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The number of minutes in the past from which to retrieve events. For example, to get all events from the past 2 hours, enter 120.</p> <p>Default: <code>60</code> </p> <p>The minimum is 1 and the maximum is 14 days (20160 minutes).</p>"""
    page_token: NotRequired["capo_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetRelationalDatabaseEvents</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRelationalDatabaseEventsRequest) -> dict:
    out: dict = {}
    out["relationalDatabaseName"] = value["relational_database_name"]
    if "duration_in_minutes" in value:
        out["durationInMinutes"] = value["duration_in_minutes"]
    if "page_token" in value:
        out["pageToken"] = value["page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRelationalDatabaseEventsRequest:
    out: GetRelationalDatabaseEventsRequest = {}  # type: ignore[typeddict-item]
    if data.get("relationalDatabaseName") is not None:
        out["relational_database_name"] = data["relationalDatabaseName"]
    else:
        out["relational_database_name"] = ""
    if data.get("durationInMinutes") is not None:
        out["duration_in_minutes"] = data["durationInMinutes"]
    if data.get("pageToken") is not None:
        out["page_token"] = data["pageToken"]
    return out
