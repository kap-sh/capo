"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#Source``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcampaignsv2.errors import DeserializationError, SerializationError
from capo_connectcampaignsv2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.arn
    import capo_connectcampaignsv2.types.event_trigger


class SourceCustomerProfilesSegmentArnMember(TypedDict, closed=True):
    customerProfilesSegmentArn: "capo_connectcampaignsv2.types.arn.Arn"


class SourceEventTriggerMember(TypedDict, closed=True):
    eventTrigger: "capo_connectcampaignsv2.types.event_trigger.EventTrigger"


Source: TypeAlias = (
    SourceCustomerProfilesSegmentArnMember
    | SourceEventTriggerMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Source) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Source: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "customerProfilesSegmentArn" in value:
        return {"customerProfilesSegmentArn": value["customerProfilesSegmentArn"]}
    elif "eventTrigger" in value:
        import capo_connectcampaignsv2.types.event_trigger

        return {
            "eventTrigger": capo_connectcampaignsv2.types.event_trigger.serialize_json(
                value["eventTrigger"]
            )
        }
    else:
        raise SerializationError("Source: no variant present")


def deserialize_json(data: dict) -> Source:
    if data.get("customerProfilesSegmentArn") is not None:
        return {"customerProfilesSegmentArn": data["customerProfilesSegmentArn"]}
    elif data.get("eventTrigger") is not None:
        import capo_connectcampaignsv2.types.event_trigger

        return {
            "eventTrigger": capo_connectcampaignsv2.types.event_trigger.deserialize_json(
                data["eventTrigger"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Source: no recognized variant key")
