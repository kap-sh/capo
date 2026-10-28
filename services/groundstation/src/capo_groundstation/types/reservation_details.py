"""Generated from Smithy shape ``com.amazonaws.groundstation#ReservationDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError, SerializationError
from capo_groundstation.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_groundstation.types.contact_reservation_details
    import capo_groundstation.types.maintenance_reservation_details


class ReservationDetailsMaintenanceMember(TypedDict, closed=True):
    maintenance: "capo_groundstation.types.maintenance_reservation_details.MaintenanceReservationDetails"


class ReservationDetailsContactMember(TypedDict, closed=True):
    contact: (
        "capo_groundstation.types.contact_reservation_details.ContactReservationDetails"
    )


ReservationDetails: TypeAlias = (
    ReservationDetailsMaintenanceMember
    | ReservationDetailsContactMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ReservationDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ReservationDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "maintenance" in value:
        import capo_groundstation.types.maintenance_reservation_details

        return {
            "maintenance": capo_groundstation.types.maintenance_reservation_details.serialize_json(
                value["maintenance"]
            )
        }
    elif "contact" in value:
        import capo_groundstation.types.contact_reservation_details

        return {
            "contact": capo_groundstation.types.contact_reservation_details.serialize_json(
                value["contact"]
            )
        }
    else:
        raise SerializationError("ReservationDetails: no variant present")


def deserialize_json(data: dict) -> ReservationDetails:
    if data.get("maintenance") is not None:
        import capo_groundstation.types.maintenance_reservation_details

        return {
            "maintenance": capo_groundstation.types.maintenance_reservation_details.deserialize_json(
                data["maintenance"]
            )
        }
    elif data.get("contact") is not None:
        import capo_groundstation.types.contact_reservation_details

        return {
            "contact": capo_groundstation.types.contact_reservation_details.deserialize_json(
                data["contact"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ReservationDetails: no recognized variant key")
