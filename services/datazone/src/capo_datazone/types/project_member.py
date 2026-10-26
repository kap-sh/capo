"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectMember``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.designation_id
    import capo_datazone.types.member_details
    import capo_datazone.types.user_designation


class ProjectMember(TypedDict, closed=True):
    member_details: "capo_datazone.types.member_details.MemberDetails"
    """<p>The membership details of a project member.</p>"""
    designation: "capo_datazone.types.user_designation.UserDesignation"
    """<p>The designated role of a project member.</p>"""
    user_created_designation_id: NotRequired[
        "capo_datazone.types.designation_id.DesignationId"
    ]
    """<p>The ID of the user-created designation held by the project member when <code>designation</code> is <code>USER_CREATED_DESIGNATION</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProjectMember) -> dict:
    out: dict = {}
    import capo_datazone.types.member_details

    out["memberDetails"] = capo_datazone.types.member_details.serialize_json(
        value["member_details"]
    )
    import capo_datazone.types.user_designation

    out["designation"] = capo_datazone.types.user_designation.serialize_json(
        value["designation"]
    )
    if "user_created_designation_id" in value:
        out["userCreatedDesignationId"] = value["user_created_designation_id"]
    return out


def deserialize_json(data: dict) -> ProjectMember:
    out: ProjectMember = {}  # type: ignore[typeddict-item]
    if data.get("memberDetails") is not None:
        import capo_datazone.types.member_details

        out["member_details"] = capo_datazone.types.member_details.deserialize_json(
            data["memberDetails"]
        )
    else:
        out["member_details"] = {"$unknown": {"name": ""}}
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
    if data.get("userCreatedDesignationId") is not None:
        out["user_created_designation_id"] = data["userCreatedDesignationId"]
    return out
