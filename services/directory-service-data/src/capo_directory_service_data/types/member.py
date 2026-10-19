"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#Member``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_directory_service_data.types.member_name
    import capo_directory_service_data.types.member_type
    import capo_directory_service_data.types.sid


class Member(TypedDict, closed=True):
    sid: "capo_directory_service_data.types.sid.SID"
    """<p> The unique security identifier (SID) of the group member. </p>"""
    sam_account_name: "capo_directory_service_data.types.member_name.MemberName"
    """<p> The name of the group member. </p>"""
    member_type: "capo_directory_service_data.types.member_type.MemberType"
    """<p> The AD type of the member object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Member) -> dict:
    out: dict = {}
    out["SID"] = value["sid"]
    out["SAMAccountName"] = value["sam_account_name"]
    import capo_directory_service_data.types.member_type

    out["MemberType"] = capo_directory_service_data.types.member_type.serialize_json(
        value["member_type"]
    )
    return out


def deserialize_json(data: dict) -> Member:
    out: Member = {}  # type: ignore[typeddict-item]
    if data.get("SID") is not None:
        out["sid"] = data["SID"]
    else:
        out["sid"] = ""
    if data.get("SAMAccountName") is not None:
        out["sam_account_name"] = data["SAMAccountName"]
    else:
        out["sam_account_name"] = ""
    if data.get("MemberType") is not None:
        import capo_directory_service_data.types.member_type

        out["member_type"] = (
            capo_directory_service_data.types.member_type.deserialize_json(
                data["MemberType"]
            )
        )
    else:
        import typing

        out["member_type"] = typing.cast(
            "capo_directory_service_data.types.member_type.MemberType", ""
        )
    return out
