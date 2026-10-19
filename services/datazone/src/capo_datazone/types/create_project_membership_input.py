"""Generated from Smithy shape ``com.amazonaws.datazone#CreateProjectMembershipInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.member
    import capo_datazone.types.project_id
    import capo_datazone.types.user_designation


class CreateProjectMembershipInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which project membership is created.</p>"""
    project_identifier: "capo_datazone.types.project_id.ProjectId"
    """<p>The ID of the project for which this project membership was created.</p>"""
    member: "capo_datazone.types.member.Member"
    """<p>The project member whose project membership was created.</p>"""
    designation: "capo_datazone.types.user_designation.UserDesignation"
    """<p>The designation of the project membership.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProjectMembershipInput) -> dict:
    out: dict = {}
    import capo_datazone.types.member

    out["member"] = capo_datazone.types.member.serialize_json(value["member"])
    import capo_datazone.types.user_designation

    out["designation"] = capo_datazone.types.user_designation.serialize_json(
        value["designation"]
    )
    return out


def deserialize_json(data: dict) -> CreateProjectMembershipInput:
    out: CreateProjectMembershipInput = {}  # type: ignore[typeddict-item]
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
