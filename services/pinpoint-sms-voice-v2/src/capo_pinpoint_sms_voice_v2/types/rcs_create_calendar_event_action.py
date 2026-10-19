"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RcsCreateCalendarEventAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.rcs_calendar_event_description
    import capo_pinpoint_sms_voice_v2.types.rcs_calendar_event_title
    import capo_pinpoint_sms_voice_v2.types.rcs_postback_data
    import capo_pinpoint_sms_voice_v2.types.rcs_suggested_action_text


class RcsCreateCalendarEventAction(TypedDict, closed=True):
    text: "capo_pinpoint_sms_voice_v2.types.rcs_suggested_action_text.RcsSuggestedActionText"
    """<p>The display text of the action. Maximum 25 characters.</p>"""
    postback_data: "capo_pinpoint_sms_voice_v2.types.rcs_postback_data.RcsPostbackData"
    """<p>The postback data sent to your webhook when the user taps this action. Maximum 2048 characters.</p>"""
    title: "capo_pinpoint_sms_voice_v2.types.rcs_calendar_event_title.RcsCalendarEventTitle"
    """<p>The title of the calendar event. Maximum 100 characters.</p>"""
    start_time: "datetime.datetime"
    """<p>The start time of the calendar event in ISO 8601 format.</p>"""
    end_time: "datetime.datetime"
    """<p>The end time of the calendar event in ISO 8601 format.</p>"""
    description: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.rcs_calendar_event_description.RcsCalendarEventDescription"
    ]
    """<p>An optional description for the calendar event. Maximum 500 characters.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RcsCreateCalendarEventAction) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    out["PostbackData"] = value["postback_data"]
    out["Title"] = value["title"]
    import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["StartTime"] = (
        capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["start_time"]
        )
    )
    import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["EndTime"] = (
        capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["end_time"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RcsCreateCalendarEventAction:
    out: RcsCreateCalendarEventAction = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    else:
        out["text"] = ""
    if data.get("PostbackData") is not None:
        out["postback_data"] = data["PostbackData"]
    else:
        out["postback_data"] = ""
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    else:
        out["title"] = ""
    if data.get("StartTime") is not None:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["start_time"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["StartTime"]
            )
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndTime") is not None:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["end_time"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["EndTime"]
            )
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
