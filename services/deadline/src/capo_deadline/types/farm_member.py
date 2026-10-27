"""Generated from Smithy shape ``com.amazonaws.deadline#FarmMember``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.deadline_principal_type
    import capo_deadline.types.farm_id
    import capo_deadline.types.identity_center_principal_id
    import capo_deadline.types.identity_store_id
    import capo_deadline.types.membership_level


class FarmMember(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the farm member."""
    principal_id: (
        "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
    )
    """The principal ID of the farm member."""
    principal_type: "capo_deadline.types.deadline_principal_type.DeadlinePrincipalType"
    """The principal type of the farm member."""
    identity_store_id: "capo_deadline.types.identity_store_id.IdentityStoreId"
    """The identity store ID of the farm member."""
    membership_level: "capo_deadline.types.membership_level.MembershipLevel"
    """The farm member's membership level."""


# --- restJson1 ser/de ---
def serialize_json(value: FarmMember) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["principalId"] = value["principal_id"]
    import capo_deadline.types.deadline_principal_type

    out["principalType"] = capo_deadline.types.deadline_principal_type.serialize_json(
        value["principal_type"]
    )
    out["identityStoreId"] = value["identity_store_id"]
    import capo_deadline.types.membership_level

    out["membershipLevel"] = capo_deadline.types.membership_level.serialize_json(
        value["membership_level"]
    )
    return out


def deserialize_json(data: dict) -> FarmMember:
    out: FarmMember = {}  # type: ignore[typeddict-item]
    if data.get("farmId") is not None:
        out["farm_id"] = data["farmId"]
    else:
        out["farm_id"] = ""
    if data.get("principalId") is not None:
        out["principal_id"] = data["principalId"]
    else:
        out["principal_id"] = ""
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
    return out
