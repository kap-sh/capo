"""Generated from Smithy shape ``com.amazonaws.workdocs#OrganizationUserList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.user

OrganizationUserList: TypeAlias = list["capo_workdocs.types.user.User"]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationUserList) -> list:
    import capo_workdocs.types.user

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.user.serialize_json(item))
    return out


def deserialize_json(data: list) -> OrganizationUserList:
    import capo_workdocs.types.user

    out: OrganizationUserList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workdocs.types.user.deserialize_json(item))
    return out


def redact_sensitive(value: OrganizationUserList) -> list[Any]:
    import capo_workdocs.types.user

    return [capo_workdocs.types.user.redact_sensitive(item) for item in value]
