"""Generated from Smithy shape ``com.amazonaws.kendra#MemberUser``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.user_id


class MemberUser(TypedDict, closed=True):
    user_id: "capo_kendra.types.user_id.UserId"
    """<p>The identifier of the user you want to map to a group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MemberUser) -> dict:
    out: dict = {}
    out["UserId"] = value["user_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MemberUser:
    out: MemberUser = {}  # type: ignore[typeddict-item]
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    else:
        out["user_id"] = ""
    return out
