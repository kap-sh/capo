"""Generated from Smithy shape ``com.amazonaws.lightsail#GetContainerLogRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.container_service_name
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.string


class GetContainerLogRequest(TypedDict, closed=True):
    service_name: "capo_lightsail.types.container_service_name.ContainerServiceName"
    """<p>The name of the container service for which to get a container log.</p>"""
    container_name: "capo_lightsail.types.string.string"
    """<p>The name of the container that is either running or previously ran on the container service for which to return a log.</p>"""
    start_time: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The start of the time interval for which to get log data.</p> <p>Constraints:</p> <ul> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you wish to use a start time of October 1, 2018, at 8 PM UTC, specify <code>1538424000</code> as the start time.</p> </li> </ul> <p>You can convert a human-friendly time to Unix time format using a converter like <a href="https://www.epochconverter.com/">Epoch converter</a>.</p>"""
    end_time: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The end of the time interval for which to get log data.</p> <p>Constraints:</p> <ul> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you wish to use an end time of October 1, 2018, at 9 PM UTC, specify <code>1538427600</code> as the end time.</p> </li> </ul> <p>You can convert a human-friendly time to Unix time format using a converter like <a href="https://www.epochconverter.com/">Epoch converter</a>.</p>"""
    filter_pattern: NotRequired["capo_lightsail.types.string.string"]
    """<p>The pattern to use to filter the returned log events to a specific term.</p> <p>The following are a few examples of filter patterns that you can specify:</p> <ul> <li> <p>To return all log events, specify a filter pattern of <code>""</code>.</p> </li> <li> <p>To exclude log events that contain the <code>ERROR</code> term, and return all other log events, specify a filter pattern of <code>"-ERROR"</code>.</p> </li> <li> <p>To return log events that contain the <code>ERROR</code> term, specify a filter pattern of <code>"ERROR"</code>.</p> </li> <li> <p>To return log events that contain both the <code>ERROR</code> and <code>Exception</code> terms, specify a filter pattern of <code>"ERROR Exception"</code>.</p> </li> <li> <p>To return log events that contain the <code>ERROR</code> <i>or</i> the <code>Exception</code> term, specify a filter pattern of <code>"?ERROR ?Exception"</code>.</p> </li> </ul>"""
    page_token: NotRequired["capo_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetContainerLog</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContainerLogRequest) -> dict:
    out: dict = {}
    out["serviceName"] = value["service_name"]
    out["containerName"] = value["container_name"]
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
    if "filter_pattern" in value:
        out["filterPattern"] = value["filter_pattern"]
    if "page_token" in value:
        out["pageToken"] = value["page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContainerLogRequest:
    out: GetContainerLogRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    else:
        raise DeserializationError("GetContainerLogRequest.service_name required")
    if data.get("containerName") is not None:
        out["container_name"] = data["containerName"]
    else:
        raise DeserializationError("GetContainerLogRequest.container_name required")
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
    if data.get("filterPattern") is not None:
        out["filter_pattern"] = data["filterPattern"]
    if data.get("pageToken") is not None:
        out["page_token"] = data["pageToken"]
    return out
