"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#DialRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaigns.types.attributes
    import capo_connectcampaigns.types.client_token
    import capo_connectcampaigns.types.destination_phone_number
    import capo_connectcampaigns.types.time_stamp


class DialRequest(TypedDict, closed=True):
    client_token: "capo_connectcampaigns.types.client_token.ClientToken"
    phone_number: (
        "capo_connectcampaigns.types.destination_phone_number.DestinationPhoneNumber"
    )
    expiration_time: "capo_connectcampaigns.types.time_stamp.TimeStamp"
    attributes: "capo_connectcampaigns.types.attributes.Attributes"


# --- restJson1 ser/de ---
def serialize_json(value: DialRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    out["phoneNumber"] = value["phone_number"]
    import capo_connectcampaigns.types.time_stamp

    out["expirationTime"] = capo_connectcampaigns.types.time_stamp.serialize_json(
        value["expiration_time"]
    )
    import capo_connectcampaigns.types.attributes

    out["attributes"] = capo_connectcampaigns.types.attributes.serialize_json(
        value["attributes"]
    )
    return out


def deserialize_json(data: dict) -> DialRequest:
    out: DialRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    if data.get("phoneNumber") is not None:
        out["phone_number"] = data["phoneNumber"]
    else:
        out["phone_number"] = ""
    if data.get("expirationTime") is not None:
        import capo_connectcampaigns.types.time_stamp

        out["expiration_time"] = (
            capo_connectcampaigns.types.time_stamp.deserialize_json(
                data["expirationTime"]
            )
        )
    else:
        import datetime

        out["expiration_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("attributes") is not None:
        import capo_connectcampaigns.types.attributes

        out["attributes"] = capo_connectcampaigns.types.attributes.deserialize_json(
            data["attributes"]
        )
    else:
        out["attributes"] = {}
    return out


def redact_sensitive(value: DialRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "phone_number" in value:
        out["phone_number"] = "*** Sensitive Data Redacted ***"
    if "attributes" in value:
        out["attributes"] = "*** Sensitive Data Redacted ***"
    return out
