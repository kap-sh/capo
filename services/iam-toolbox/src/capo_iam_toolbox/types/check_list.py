"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#CheckList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iam_toolbox.types.check

CheckList: TypeAlias = list["capo_iam_toolbox.types.check.Check"]


# --- restJson1 ser/de ---
def serialize_json(value: CheckList) -> list:
    import capo_iam_toolbox.types.check

    out: list = []
    for item in value:
        out.append(capo_iam_toolbox.types.check.serialize_json(item))
    return out


def deserialize_json(data: list) -> CheckList:
    import capo_iam_toolbox.types.check

    out: CheckList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_iam_toolbox.types.check.deserialize_json(item))
    return out
