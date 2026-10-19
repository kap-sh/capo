"""Generated from Smithy shape ``com.amazonaws.qbusiness#PrincipalUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.membership_type
    import capo_qbusiness.types.read_access_type
    import capo_qbusiness.types.user_id


class PrincipalUser(TypedDict, closed=True):
    id: NotRequired["capo_qbusiness.types.user_id.UserId"]
    """<p> The identifier of the user. </p>"""
    access: "capo_qbusiness.types.read_access_type.ReadAccessType"
    """<p>Provides information about whether to allow or deny access to the principal.</p>"""
    membership_type: NotRequired["capo_qbusiness.types.membership_type.MembershipType"]
    """<p>The type of group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalUser) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    import capo_qbusiness.types.read_access_type

    out["access"] = capo_qbusiness.types.read_access_type.serialize_json(
        value["access"]
    )
    if "membership_type" in value:
        import capo_qbusiness.types.membership_type

        out["membershipType"] = capo_qbusiness.types.membership_type.serialize_json(
            value["membership_type"]
        )
    return out


def deserialize_json(data: dict) -> PrincipalUser:
    out: PrincipalUser = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("access") is not None:
        import capo_qbusiness.types.read_access_type

        out["access"] = capo_qbusiness.types.read_access_type.deserialize_json(
            data["access"]
        )
    else:
        import typing

        out["access"] = typing.cast(
            "capo_qbusiness.types.read_access_type.ReadAccessType", ""
        )
    if data.get("membershipType") is not None:
        import capo_qbusiness.types.membership_type

        out["membership_type"] = capo_qbusiness.types.membership_type.deserialize_json(
            data["membershipType"]
        )
    return out
