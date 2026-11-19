"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationResolvedSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.evaluation_resolved_source

EvaluationResolvedSourceList: TypeAlias = list[
    "capo_connect.types.evaluation_resolved_source.EvaluationResolvedSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationResolvedSourceList) -> list:
    import capo_connect.types.evaluation_resolved_source

    out: list = []
    for item in value:
        out.append(capo_connect.types.evaluation_resolved_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> EvaluationResolvedSourceList:
    import capo_connect.types.evaluation_resolved_source

    out: EvaluationResolvedSourceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.evaluation_resolved_source.deserialize_json(item))
    return out
