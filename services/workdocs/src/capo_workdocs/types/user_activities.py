"""Generated from Smithy shape ``com.amazonaws.workdocs#UserActivities``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.activity

UserActivities: TypeAlias = list["capo_workdocs.types.activity.Activity"]


# --- restJson1 ser/de ---
def serialize_json(value: UserActivities) -> list:
    import capo_workdocs.types.activity

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.activity.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserActivities:
    import capo_workdocs.types.activity

    out: UserActivities = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workdocs.types.activity.deserialize_json(item))
    return out


def redact_sensitive(value: UserActivities) -> list[Any]:
    import capo_workdocs.types.activity

    return [capo_workdocs.types.activity.redact_sensitive(item) for item in value]
