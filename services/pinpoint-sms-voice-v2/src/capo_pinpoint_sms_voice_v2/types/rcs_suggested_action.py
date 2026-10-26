"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RcsSuggestedAction``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError, SerializationError
from capo_pinpoint_sms_voice_v2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.rcs_create_calendar_event_action
    import capo_pinpoint_sms_voice_v2.types.rcs_dial_phone_action
    import capo_pinpoint_sms_voice_v2.types.rcs_open_url_action
    import capo_pinpoint_sms_voice_v2.types.rcs_reply_action
    import capo_pinpoint_sms_voice_v2.types.rcs_request_location_action
    import capo_pinpoint_sms_voice_v2.types.rcs_show_location_action


class _RcsSuggestedAction_Reply(TypedDict, closed=True):
    Reply: "capo_pinpoint_sms_voice_v2.types.rcs_reply_action.RcsReplyAction"


class _RcsSuggestedAction_OpenUrl(TypedDict, closed=True):
    OpenUrl: "capo_pinpoint_sms_voice_v2.types.rcs_open_url_action.RcsOpenUrlAction"


class _RcsSuggestedAction_DialPhone(TypedDict, closed=True):
    DialPhone: (
        "capo_pinpoint_sms_voice_v2.types.rcs_dial_phone_action.RcsDialPhoneAction"
    )


class _RcsSuggestedAction_ShowLocation(TypedDict, closed=True):
    ShowLocation: "capo_pinpoint_sms_voice_v2.types.rcs_show_location_action.RcsShowLocationAction"


class _RcsSuggestedAction_RequestLocation(TypedDict, closed=True):
    RequestLocation: "capo_pinpoint_sms_voice_v2.types.rcs_request_location_action.RcsRequestLocationAction"


class _RcsSuggestedAction_CreateCalendarEvent(TypedDict, closed=True):
    CreateCalendarEvent: "capo_pinpoint_sms_voice_v2.types.rcs_create_calendar_event_action.RcsCreateCalendarEventAction"


RcsSuggestedAction: TypeAlias = (
    _RcsSuggestedAction_Reply
    | _RcsSuggestedAction_OpenUrl
    | _RcsSuggestedAction_DialPhone
    | _RcsSuggestedAction_ShowLocation
    | _RcsSuggestedAction_RequestLocation
    | _RcsSuggestedAction_CreateCalendarEvent
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RcsSuggestedAction) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RcsSuggestedAction: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Reply" in value:
        import capo_pinpoint_sms_voice_v2.types.rcs_reply_action

        return {
            "Reply": capo_pinpoint_sms_voice_v2.types.rcs_reply_action.serialize_aws_json_1_0(
                value["Reply"]
            )
        }
    elif "OpenUrl" in value:
        import capo_pinpoint_sms_voice_v2.types.rcs_open_url_action

        return {
            "OpenUrl": capo_pinpoint_sms_voice_v2.types.rcs_open_url_action.serialize_aws_json_1_0(
                value["OpenUrl"]
            )
        }
    elif "DialPhone" in value:
        import capo_pinpoint_sms_voice_v2.types.rcs_dial_phone_action

        return {
            "DialPhone": capo_pinpoint_sms_voice_v2.types.rcs_dial_phone_action.serialize_aws_json_1_0(
                value["DialPhone"]
            )
        }
    elif "ShowLocation" in value:
        import capo_pinpoint_sms_voice_v2.types.rcs_show_location_action

        return {
            "ShowLocation": capo_pinpoint_sms_voice_v2.types.rcs_show_location_action.serialize_aws_json_1_0(
                value["ShowLocation"]
            )
        }
    elif "RequestLocation" in value:
        import capo_pinpoint_sms_voice_v2.types.rcs_request_location_action

        return {
            "RequestLocation": capo_pinpoint_sms_voice_v2.types.rcs_request_location_action.serialize_aws_json_1_0(
                value["RequestLocation"]
            )
        }
    elif "CreateCalendarEvent" in value:
        import capo_pinpoint_sms_voice_v2.types.rcs_create_calendar_event_action

        return {
            "CreateCalendarEvent": capo_pinpoint_sms_voice_v2.types.rcs_create_calendar_event_action.serialize_aws_json_1_0(
                value["CreateCalendarEvent"]
            )
        }
    else:
        raise SerializationError("RcsSuggestedAction: no variant present")


def deserialize_aws_json_1_0(data: dict) -> RcsSuggestedAction:
    if data.get("Reply") is not None:
        import capo_pinpoint_sms_voice_v2.types.rcs_reply_action

        return {
            "Reply": capo_pinpoint_sms_voice_v2.types.rcs_reply_action.deserialize_aws_json_1_0(
                data["Reply"]
            )
        }
    elif data.get("OpenUrl") is not None:
        import capo_pinpoint_sms_voice_v2.types.rcs_open_url_action

        return {
            "OpenUrl": capo_pinpoint_sms_voice_v2.types.rcs_open_url_action.deserialize_aws_json_1_0(
                data["OpenUrl"]
            )
        }
    elif data.get("DialPhone") is not None:
        import capo_pinpoint_sms_voice_v2.types.rcs_dial_phone_action

        return {
            "DialPhone": capo_pinpoint_sms_voice_v2.types.rcs_dial_phone_action.deserialize_aws_json_1_0(
                data["DialPhone"]
            )
        }
    elif data.get("ShowLocation") is not None:
        import capo_pinpoint_sms_voice_v2.types.rcs_show_location_action

        return {
            "ShowLocation": capo_pinpoint_sms_voice_v2.types.rcs_show_location_action.deserialize_aws_json_1_0(
                data["ShowLocation"]
            )
        }
    elif data.get("RequestLocation") is not None:
        import capo_pinpoint_sms_voice_v2.types.rcs_request_location_action

        return {
            "RequestLocation": capo_pinpoint_sms_voice_v2.types.rcs_request_location_action.deserialize_aws_json_1_0(
                data["RequestLocation"]
            )
        }
    elif data.get("CreateCalendarEvent") is not None:
        import capo_pinpoint_sms_voice_v2.types.rcs_create_calendar_event_action

        return {
            "CreateCalendarEvent": capo_pinpoint_sms_voice_v2.types.rcs_create_calendar_event_action.deserialize_aws_json_1_0(
                data["CreateCalendarEvent"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RcsSuggestedAction: no recognized variant key")
