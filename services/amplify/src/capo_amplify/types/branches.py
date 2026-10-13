"""Generated from Smithy shape ``com.amazonaws.amplify#Branches``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_amplify.types.branch

Branches: TypeAlias = list["capo_amplify.types.branch.Branch"]


# --- restJson1 ser/de ---
def serialize_json(value: Branches) -> list:
    import capo_amplify.types.branch

    out: list = []
    for item in value:
        out.append(capo_amplify.types.branch.serialize_json(item))
    return out


def deserialize_json(data: list) -> Branches:
    import capo_amplify.types.branch

    out: Branches = []
    for item in data:
        if item is None:
            continue
        out.append(capo_amplify.types.branch.deserialize_json(item))
    return out


def redact_sensitive(value: Branches) -> list[Any]:
    import capo_amplify.types.branch

    return [capo_amplify.types.branch.redact_sensitive(item) for item in value]
