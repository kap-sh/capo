"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_item_enablement_source
    import capo_connect.types.evaluation_form_item_enablement_source_value_list
    import capo_connect.types.evaluation_form_item_source_values_comparator


class EvaluationFormItemEnablementExpression(TypedDict, closed=True):
    source: "capo_connect.types.evaluation_form_item_enablement_source.EvaluationFormItemEnablementSource"
    """<p>A source item of enablement expression.</p>"""
    values: "capo_connect.types.evaluation_form_item_enablement_source_value_list.EvaluationFormItemEnablementSourceValueList"
    """<p>A list of values from source item.</p>"""
    comparator: "capo_connect.types.evaluation_form_item_source_values_comparator.EvaluationFormItemSourceValuesComparator"
    """<p>A comparator to be used against list of values. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItemEnablementExpression) -> dict:
    out: dict = {}
    import capo_connect.types.evaluation_form_item_enablement_source

    out["Source"] = (
        capo_connect.types.evaluation_form_item_enablement_source.serialize_json(
            value["source"]
        )
    )
    import capo_connect.types.evaluation_form_item_enablement_source_value_list

    out["Values"] = (
        capo_connect.types.evaluation_form_item_enablement_source_value_list.serialize_json(
            value["values"]
        )
    )
    import capo_connect.types.evaluation_form_item_source_values_comparator

    out["Comparator"] = (
        capo_connect.types.evaluation_form_item_source_values_comparator.serialize_json(
            value["comparator"]
        )
    )
    return out


def deserialize_json(data: dict) -> EvaluationFormItemEnablementExpression:
    out: EvaluationFormItemEnablementExpression = {}  # type: ignore[typeddict-item]
    if data.get("Source") is not None:
        import capo_connect.types.evaluation_form_item_enablement_source

        out["source"] = (
            capo_connect.types.evaluation_form_item_enablement_source.deserialize_json(
                data["Source"]
            )
        )
    else:
        raise DeserializationError(
            "EvaluationFormItemEnablementExpression.source required"
        )
    if data.get("Values") is not None:
        import capo_connect.types.evaluation_form_item_enablement_source_value_list

        out["values"] = (
            capo_connect.types.evaluation_form_item_enablement_source_value_list.deserialize_json(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    if data.get("Comparator") is not None:
        import capo_connect.types.evaluation_form_item_source_values_comparator

        out["comparator"] = (
            capo_connect.types.evaluation_form_item_source_values_comparator.deserialize_json(
                data["Comparator"]
            )
        )
    else:
        import typing

        out["comparator"] = typing.cast(
            "capo_connect.types.evaluation_form_item_source_values_comparator.EvaluationFormItemSourceValuesComparator",
            "",
        )
    return out
