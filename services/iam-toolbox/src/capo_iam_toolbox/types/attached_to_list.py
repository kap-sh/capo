"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#AttachedToList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iam_toolbox.types.attached_to

AttachedToList: TypeAlias = list["capo_iam_toolbox.types.attached_to.AttachedTo"]


# --- restJson1 ser/de ---
def serialize_json(value: AttachedToList) -> list:
    import capo_iam_toolbox.types.attached_to

    out: list = []
    for item in value:
        out.append(capo_iam_toolbox.types.attached_to.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttachedToList:
    import capo_iam_toolbox.types.attached_to

    out: AttachedToList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_iam_toolbox.types.attached_to.deserialize_json(item))
    return out
