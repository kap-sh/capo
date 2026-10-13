"""Generated from Smithy shape ``com.amazonaws.guardduty#Members``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.member

Members: TypeAlias = list["capo_guardduty.types.member.Member"]


# --- restJson1 ser/de ---
def serialize_json(value: Members) -> list:
    import capo_guardduty.types.member

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.member.serialize_json(item))
    return out


def deserialize_json(data: list) -> Members:
    import capo_guardduty.types.member

    out: Members = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.member.deserialize_json(item))
    return out


def redact_sensitive(value: Members) -> list[Any]:
    import capo_guardduty.types.member

    return [capo_guardduty.types.member.redact_sensitive(item) for item in value]
