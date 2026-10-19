"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectMembershipAssignment``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.member
    import capo_datazone.types.user_designation


class ProjectMembershipAssignment(TypedDict, closed=True):
    member: "capo_datazone.types.member.Member"
    """<p>The details about a project member.</p>"""
    designation: "capo_datazone.types.user_designation.UserDesignation"
    """<p>The designation of the project membership.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProjectMembershipAssignment) -> dict:
    out: dict = {}
    import capo_datazone.types.member

    out["member"] = capo_datazone.types.member.serialize_json(value["member"])
    import capo_datazone.types.user_designation

    out["designation"] = capo_datazone.types.user_designation.serialize_json(
        value["designation"]
    )
    return out


def deserialize_json(data: dict) -> ProjectMembershipAssignment:
    out: ProjectMembershipAssignment = {}  # type: ignore[typeddict-item]
    if data.get("member") is not None:
        import capo_datazone.types.member

        out["member"] = capo_datazone.types.member.deserialize_json(data["member"])
    else:
        import capo_datazone.types._unknown

        out["member"] = capo_datazone.types._unknown.UnknownUnionMember("")
    if data.get("designation") is not None:
        import capo_datazone.types.user_designation

        out["designation"] = capo_datazone.types.user_designation.deserialize_json(
            data["designation"]
        )
    else:
        import typing

        out["designation"] = typing.cast(
            "capo_datazone.types.user_designation.UserDesignation", ""
        )
    return out
