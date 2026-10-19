"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRelationalDatabaseLogEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.string


class GetRelationalDatabaseLogEventsRequest(TypedDict, closed=True):
    relational_database_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of your database for which to get log events.</p>"""
    log_stream_name: "capo_lightsail.types.string.string"
    """<p>The name of the log stream.</p> <p>Use the <code>get relational database log streams</code> operation to get a list of available log streams.</p>"""
    start_time: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The start of the time interval from which to get log events.</p> <p>Constraints:</p> <ul> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you wish to use a start time of October 1, 2018, at 8 PM UTC, then you input <code>1538424000</code> as the start time.</p> </li> </ul>"""
    end_time: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The end of the time interval from which to get log events.</p> <p>Constraints:</p> <ul> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you wish to use an end time of October 1, 2018, at 8 PM UTC, then you input <code>1538424000</code> as the end time.</p> </li> </ul>"""
    start_from_head: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>Parameter to specify if the log should start from head or tail. If <code>true</code> is specified, the log event starts from the head of the log. If <code>false</code> is specified, the log event starts from the tail of the log.</p> <note> <p>For PostgreSQL, the default value of <code>false</code> is the only option available.</p> </note>"""
    page_token: NotRequired["capo_lightsail.types.string.string"]
    """<p>The token to advance to the next or previous page of results from your request.</p> <p>To get a page token, perform an initial <code>GetRelationalDatabaseLogEvents</code> request. If your results are paginated, the response will return a next forward token and/or next backward token that you can specify as the page token in a subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRelationalDatabaseLogEventsRequest) -> dict:
    out: dict = {}
    out["relationalDatabaseName"] = value["relational_database_name"]
    out["logStreamName"] = value["log_stream_name"]
    if "start_time" in value:
        import capo_lightsail.types.iso_date

        out["startTime"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_lightsail.types.iso_date

        out["endTime"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "start_from_head" in value:
        out["startFromHead"] = value["start_from_head"]
    if "page_token" in value:
        out["pageToken"] = value["page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRelationalDatabaseLogEventsRequest:
    out: GetRelationalDatabaseLogEventsRequest = {}  # type: ignore[typeddict-item]
    if data.get("relationalDatabaseName") is not None:
        out["relational_database_name"] = data["relationalDatabaseName"]
    else:
        out["relational_database_name"] = ""
    if data.get("logStreamName") is not None:
        out["log_stream_name"] = data["logStreamName"]
    else:
        out["log_stream_name"] = ""
    if data.get("startTime") is not None:
        import capo_lightsail.types.iso_date

        out["start_time"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_lightsail.types.iso_date

        out["end_time"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["endTime"]
        )
    if data.get("startFromHead") is not None:
        out["start_from_head"] = data["startFromHead"]
    if data.get("pageToken") is not None:
        out["page_token"] = data["pageToken"]
    return out
