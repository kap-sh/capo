"""Generated from Smithy shape ``com.amazonaws.detective#MemberDetailList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_detective.types.member_detail

MemberDetailList: TypeAlias = list["capo_detective.types.member_detail.MemberDetail"]


# --- restJson1 ser/de ---
def serialize_json(value: MemberDetailList) -> list:
    import capo_detective.types.member_detail

    out: list = []
    for item in value:
        out.append(capo_detective.types.member_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> MemberDetailList:
    import capo_detective.types.member_detail

    out: MemberDetailList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_detective.types.member_detail.deserialize_json(item))
    return out


def redact_sensitive(value: MemberDetailList) -> list[Any]:
    import capo_detective.types.member_detail

    return [capo_detective.types.member_detail.redact_sensitive(item) for item in value]
