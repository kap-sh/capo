"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationResolvedSourceValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_item_enablement_source_value

EvaluationResolvedSourceValueList: TypeAlias = list[
    "capo_connect.types.evaluation_form_item_enablement_source_value.EvaluationFormItemEnablementSourceValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationResolvedSourceValueList) -> list:
    import capo_connect.types.evaluation_form_item_enablement_source_value

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.evaluation_form_item_enablement_source_value.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EvaluationResolvedSourceValueList:
    import capo_connect.types.evaluation_form_item_enablement_source_value

    out: EvaluationResolvedSourceValueList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connect.types.evaluation_form_item_enablement_source_value.deserialize_json(
                item
            )
        )
    return out
