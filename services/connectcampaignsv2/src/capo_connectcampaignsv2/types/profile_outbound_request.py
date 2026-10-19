"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#ProfileOutboundRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.client_token
    import capo_connectcampaignsv2.types.event_trigger_context
    import capo_connectcampaignsv2.types.profile_id
    import capo_connectcampaignsv2.types.time_stamp


class ProfileOutboundRequest(TypedDict, closed=True):
    client_token: "capo_connectcampaignsv2.types.client_token.ClientToken"
    profile_id: "capo_connectcampaignsv2.types.profile_id.ProfileId"
    expiration_time: NotRequired["capo_connectcampaignsv2.types.time_stamp.TimeStamp"]
    event_trigger_context: NotRequired[
        "capo_connectcampaignsv2.types.event_trigger_context.EventTriggerContext"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileOutboundRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    out["profileId"] = value["profile_id"]
    if "expiration_time" in value:
        import capo_connectcampaignsv2.types.time_stamp

        out["expirationTime"] = capo_connectcampaignsv2.types.time_stamp.serialize_json(
            value["expiration_time"]
        )
    if "event_trigger_context" in value:
        import capo_connectcampaignsv2.types.event_trigger_context

        out["eventTriggerContext"] = (
            capo_connectcampaignsv2.types.event_trigger_context.serialize_json(
                value["event_trigger_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProfileOutboundRequest:
    out: ProfileOutboundRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    else:
        out["profile_id"] = ""
    if data.get("expirationTime") is not None:
        import capo_connectcampaignsv2.types.time_stamp

        out["expiration_time"] = (
            capo_connectcampaignsv2.types.time_stamp.deserialize_json(
                data["expirationTime"]
            )
        )
    if data.get("eventTriggerContext") is not None:
        import capo_connectcampaignsv2.types.event_trigger_context

        out["event_trigger_context"] = (
            capo_connectcampaignsv2.types.event_trigger_context.deserialize_json(
                data["eventTriggerContext"]
            )
        )
    return out
