"""Generated from Smithy shape ``com.amazonaws.deadline#DisassociateMemberFromFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.identity_center_principal_id


class DisassociateMemberFromFleetRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the fleet to disassociate a member from."""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """The fleet ID of the fleet to from which to disassociate a member."""
    principal_id: (
        "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
    )
    """A member's principal ID to disassociate from a fleet."""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateMemberFromFleetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateMemberFromFleetRequest:
    out: DisassociateMemberFromFleetRequest = {}  # type: ignore[typeddict-item]
    return out
