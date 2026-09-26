"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#Evaluations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iam_toolbox.types.evaluation

Evaluations: TypeAlias = list["capo_iam_toolbox.types.evaluation.Evaluation"]


# --- restJson1 ser/de ---
def serialize_json(value: Evaluations) -> list:
    import capo_iam_toolbox.types.evaluation

    out: list = []
    for item in value:
        out.append(capo_iam_toolbox.types.evaluation.serialize_json(item))
    return out


def deserialize_json(data: list) -> Evaluations:
    import capo_iam_toolbox.types.evaluation

    out: Evaluations = []
    for item in data:
        if item is None:
            continue
        out.append(capo_iam_toolbox.types.evaluation.deserialize_json(item))
    return out
