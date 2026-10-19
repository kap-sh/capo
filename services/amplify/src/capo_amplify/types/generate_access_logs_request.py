"""Generated from Smithy shape ``com.amazonaws.amplify#GenerateAccessLogsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.app_id
    import capo_amplify.types.domain_name
    import capo_amplify.types.end_time
    import capo_amplify.types.start_time


class GenerateAccessLogsRequest(TypedDict, closed=True):
    start_time: NotRequired["capo_amplify.types.start_time.StartTime"]
    """<p>The time at which the logs should start. The time range specified is inclusive of the start time. </p>"""
    end_time: NotRequired["capo_amplify.types.end_time.EndTime"]
    """<p>The time at which the logs should end. The time range specified is inclusive of the end time. </p>"""
    domain_name: "capo_amplify.types.domain_name.DomainName"
    """<p>The name of the domain. </p>"""
    app_id: "capo_amplify.types.app_id.AppId"
    """<p>The unique ID for an Amplify app. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateAccessLogsRequest) -> dict:
    out: dict = {}
    if "start_time" in value:
        import capo_amplify.types.start_time

        out["startTime"] = capo_amplify.types.start_time.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_amplify.types.end_time

        out["endTime"] = capo_amplify.types.end_time.serialize_json(value["end_time"])
    out["domainName"] = value["domain_name"]
    return out


def deserialize_json(data: dict) -> GenerateAccessLogsRequest:
    out: GenerateAccessLogsRequest = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        import capo_amplify.types.start_time

        out["start_time"] = capo_amplify.types.start_time.deserialize_json(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_amplify.types.end_time

        out["end_time"] = capo_amplify.types.end_time.deserialize_json(data["endTime"])
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    else:
        out["domain_name"] = ""
    return out
