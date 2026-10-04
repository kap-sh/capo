"""Generated from Smithy shape ``com.amazonaws.endusermessaging#RegistrationAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_endusermessaging.types.registration_id
    import capo_endusermessaging.types.registration_type


class RegistrationAssociationSummary(TypedDict, closed=True):
    registration_id: "capo_endusermessaging.types.registration_id.RegistrationId"
    """<p>The identifier of the registration.</p>"""
    registration_type: "capo_endusermessaging.types.registration_type.RegistrationType"
    """<p>The type of the registration, for example US_TOLL_FREE_REGISTRATION or SENDER_ID.</p>"""
    created_at: "datetime.datetime"
    """<p>The time when the resource was created, in Unix epoch time.</p>"""
    smart_match_used: "bool"
    """<p>Specifies whether smart matching was used to create the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegistrationAssociationSummary) -> dict:
    out: dict = {}
    out["registrationId"] = value["registration_id"]
    out["registrationType"] = value["registration_type"]
    import capo_endusermessaging.types._prelude.timestamp

    out["createdAt"] = capo_endusermessaging.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    out["smartMatchUsed"] = value["smart_match_used"]
    return out


def deserialize_json(data: dict) -> RegistrationAssociationSummary:
    out: RegistrationAssociationSummary = {}  # type: ignore[typeddict-item]
    if data.get("registrationId") is not None:
        out["registration_id"] = data["registrationId"]
    else:
        raise DeserializationError(
            "RegistrationAssociationSummary.registration_id required"
        )
    if data.get("registrationType") is not None:
        out["registration_type"] = data["registrationType"]
    else:
        raise DeserializationError(
            "RegistrationAssociationSummary.registration_type required"
        )
    if data.get("createdAt") is not None:
        import capo_endusermessaging.types._prelude.timestamp

        out["created_at"] = (
            capo_endusermessaging.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("RegistrationAssociationSummary.created_at required")
    if data.get("smartMatchUsed") is not None:
        out["smart_match_used"] = data["smartMatchUsed"]
    else:
        raise DeserializationError(
            "RegistrationAssociationSummary.smart_match_used required"
        )
    return out
