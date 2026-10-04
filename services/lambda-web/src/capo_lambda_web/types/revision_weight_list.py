"""Generated from Smithy shape ``com.amazonaws.lambdaweb#RevisionWeightList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_web.types.revision_weight

RevisionWeightList: TypeAlias = list[
    "capo_lambda_web.types.revision_weight.RevisionWeight"
]


# --- restJson1 ser/de ---
def serialize_json(value: RevisionWeightList) -> list:
    import capo_lambda_web.types.revision_weight

    out: list = []
    for item in value:
        out.append(capo_lambda_web.types.revision_weight.serialize_json(item))
    return out


def deserialize_json(data: list) -> RevisionWeightList:
    import capo_lambda_web.types.revision_weight

    out: RevisionWeightList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda_web.types.revision_weight.deserialize_json(item))
    return out
