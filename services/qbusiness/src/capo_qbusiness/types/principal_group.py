"""Generated from Smithy shape ``com.amazonaws.qbusiness#PrincipalGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.group_name
    import capo_qbusiness.types.membership_type
    import capo_qbusiness.types.read_access_type


class PrincipalGroup(TypedDict, closed=True):
    name: NotRequired["capo_qbusiness.types.group_name.GroupName"]
    """<p>The name of the group.</p>"""
    access: "capo_qbusiness.types.read_access_type.ReadAccessType"
    """<p>Provides information about whether to allow or deny access to the principal.</p>"""
    membership_type: NotRequired["capo_qbusiness.types.membership_type.MembershipType"]
    """<p>The type of group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalGroup) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
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


def deserialize_json(data: dict) -> PrincipalGroup:
    out: PrincipalGroup = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
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
