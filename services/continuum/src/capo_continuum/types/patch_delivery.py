"""Generated from Smithy shape ``com.amazonaws.continuum#PatchDelivery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_continuum.types.delivery_status
    import capo_continuum.types.destination_target


class PatchDelivery(TypedDict, closed=True):
    status: "capo_continuum.types.delivery_status.DeliveryStatus"
    """How far delivery to the destination has progressed."""
    target: NotRequired["capo_continuum.types.destination_target.DestinationTarget"]
    """Where the patch was or will be delivered. Absent while the destination is still being resolved, or when delivery was skipped before a destination was known."""
    updated_at: "datetime.datetime"
    """When the delivery status last changed."""


# --- restJson1 ser/de ---
def serialize_json(value: PatchDelivery) -> dict:
    out: dict = {}
    import capo_continuum.types.delivery_status

    out["status"] = capo_continuum.types.delivery_status.serialize_json(value["status"])
    if "target" in value:
        import capo_continuum.types.destination_target

        out["target"] = capo_continuum.types.destination_target.serialize_json(
            value["target"]
        )
    import capo_continuum._protocol.serialize

    out["updatedAt"] = capo_continuum._protocol.serialize.fmt_date_time(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> PatchDelivery:
    out: PatchDelivery = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_continuum.types.delivery_status

        out["status"] = capo_continuum.types.delivery_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_continuum.types.delivery_status.DeliveryStatus", ""
        )
    if data.get("target") is not None:
        import capo_continuum.types.destination_target

        out["target"] = capo_continuum.types.destination_target.deserialize_json(
            data["target"]
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
