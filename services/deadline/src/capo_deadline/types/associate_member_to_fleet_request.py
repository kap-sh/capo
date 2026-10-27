"""Generated from Smithy shape ``com.amazonaws.deadline#AssociateMemberToFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.deadline_principal_type
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.identity_center_principal_id
    import capo_deadline.types.identity_store_id
    import capo_deadline.types.membership_level
    import capo_deadline.types.region


class AssociateMemberToFleetRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the fleet to associate with the member."""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """The ID of the fleet to associate with a member."""
    principal_type: "capo_deadline.types.deadline_principal_type.DeadlinePrincipalType"
    """The member's principal type to associate with the fleet."""
    identity_store_id: "capo_deadline.types.identity_store_id.IdentityStoreId"
    """The member's identity store ID to associate with the fleet."""
    membership_level: "capo_deadline.types.membership_level.MembershipLevel"
    """The principal's membership level for the associated fleet."""
    principal_id: (
        "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
    )
    """The member's principal ID to associate with a fleet."""
    identity_center_region: NotRequired["capo_deadline.types.region.Region"]
    """The Region of the IAM Identity Center instance. If not provided, the service defaults to the Region of the farm."""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateMemberToFleetRequest) -> dict:
    out: dict = {}
    import capo_deadline.types.deadline_principal_type

    out["principalType"] = capo_deadline.types.deadline_principal_type.serialize_json(
        value["principal_type"]
    )
    out["identityStoreId"] = value["identity_store_id"]
    import capo_deadline.types.membership_level

    out["membershipLevel"] = capo_deadline.types.membership_level.serialize_json(
        value["membership_level"]
    )
    if "identity_center_region" in value:
        out["identityCenterRegion"] = value["identity_center_region"]
    return out


def deserialize_json(data: dict) -> AssociateMemberToFleetRequest:
    out: AssociateMemberToFleetRequest = {}  # type: ignore[typeddict-item]
    if data.get("principalType") is not None:
        import capo_deadline.types.deadline_principal_type

        out["principal_type"] = (
            capo_deadline.types.deadline_principal_type.deserialize_json(
                data["principalType"]
            )
        )
    else:
        import typing

        out["principal_type"] = typing.cast(
            "capo_deadline.types.deadline_principal_type.DeadlinePrincipalType", ""
        )
    if data.get("identityStoreId") is not None:
        out["identity_store_id"] = data["identityStoreId"]
    else:
        out["identity_store_id"] = ""
    if data.get("membershipLevel") is not None:
        import capo_deadline.types.membership_level

        out["membership_level"] = capo_deadline.types.membership_level.deserialize_json(
            data["membershipLevel"]
        )
    else:
        import typing

        out["membership_level"] = typing.cast(
            "capo_deadline.types.membership_level.MembershipLevel", ""
        )
    if data.get("identityCenterRegion") is not None:
        out["identity_center_region"] = data["identityCenterRegion"]
    return out
