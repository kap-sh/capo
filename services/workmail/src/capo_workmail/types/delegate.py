"""Generated from Smithy shape ``com.amazonaws.workmail#Delegate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.member_type
    import capo_workmail.types.string


class Delegate(TypedDict, closed=True):
    id: "capo_workmail.types.string.String"
    """<p>The identifier for the user or group associated as the resource's delegate.</p>"""
    type: "capo_workmail.types.member_type.MemberType"
    """<p>The type of the delegate: user or group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Delegate) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import capo_workmail.types.member_type

    out["Type"] = capo_workmail.types.member_type.serialize_aws_json_1_1(value["type"])
    return out


def deserialize_aws_json_1_1(data: dict) -> Delegate:
    out: Delegate = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Type") is not None:
        import capo_workmail.types.member_type

        out["type"] = capo_workmail.types.member_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast("capo_workmail.types.member_type.MemberType", "")
    return out
