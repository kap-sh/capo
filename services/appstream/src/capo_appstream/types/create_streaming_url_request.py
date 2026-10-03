"""Generated from Smithy shape ``com.amazonaws.appstream#CreateStreamingURLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.long
    import capo_appstream.types.streaming_url_user_id
    import capo_appstream.types.string


class CreateStreamingURLRequest(TypedDict, closed=True):
    stack_name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the stack.</p>"""
    fleet_name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the fleet.</p>"""
    user_id: NotRequired[
        "capo_appstream.types.streaming_url_user_id.StreamingUrlUserId"
    ]
    """<p>The identifier of the user.</p>"""
    application_id: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the application to launch after the session starts. This is the name that you specified as <b>Name</b> in the Image Assistant. If your fleet is enabled for the <b>Desktop</b> stream view, you can also choose to launch directly to the operating system desktop. To do so, specify <b>Desktop</b>.</p>"""
    validity: NotRequired["capo_appstream.types.long.Long"]
    """<p>The time that the streaming URL will be valid, in seconds. Specify a value between 1 and 604800 seconds. The default is 60 seconds.</p>"""
    session_context: NotRequired["capo_appstream.types.string.String"]
    """<p>The session context. For more information, see <a href="https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-stacks-fleets.html#managing-stacks-fleets-parameters">Session Context</a> in the <i>Amazon WorkSpaces Applications Administration Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateStreamingURLRequest) -> dict:
    out: dict = {}
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    if "fleet_name" in value:
        out["FleetName"] = value["fleet_name"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "validity" in value:
        out["Validity"] = value["validity"]
    if "session_context" in value:
        out["SessionContext"] = value["session_context"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateStreamingURLRequest:
    out: CreateStreamingURLRequest = {}  # type: ignore[typeddict-item]
    if data.get("StackName") is not None:
        out["stack_name"] = data["StackName"]
    if data.get("FleetName") is not None:
        out["fleet_name"] = data["FleetName"]
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    if data.get("Validity") is not None:
        out["validity"] = data["Validity"]
    if data.get("SessionContext") is not None:
        out["session_context"] = data["SessionContext"]
    return out
