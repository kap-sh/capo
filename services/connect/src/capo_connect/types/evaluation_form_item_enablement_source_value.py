"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementSourceValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_item_enablement_source_value_type
    import capo_connect.types.reference_id


class EvaluationFormItemEnablementSourceValue(TypedDict, closed=True):
    type: "capo_connect.types.evaluation_form_item_enablement_source_value_type.EvaluationFormItemEnablementSourceValueType"
    """<p>A type of source item value. </p>"""
    ref_id: NotRequired["capo_connect.types.reference_id.ReferenceId"]
    """<p>A referenceId of the source value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItemEnablementSourceValue) -> dict:
    out: dict = {}
    import capo_connect.types.evaluation_form_item_enablement_source_value_type

    out["Type"] = (
        capo_connect.types.evaluation_form_item_enablement_source_value_type.serialize_json(
            value["type"]
        )
    )
    if "ref_id" in value:
        out["RefId"] = value["ref_id"]
    return out


def deserialize_json(data: dict) -> EvaluationFormItemEnablementSourceValue:
    out: EvaluationFormItemEnablementSourceValue = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_connect.types.evaluation_form_item_enablement_source_value_type

        out["type"] = (
            capo_connect.types.evaluation_form_item_enablement_source_value_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_connect.types.evaluation_form_item_enablement_source_value_type.EvaluationFormItemEnablementSourceValueType",
            "",
        )
    if data.get("RefId") is not None:
        out["ref_id"] = data["RefId"]
    return out
