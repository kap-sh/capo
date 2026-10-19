"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_item_enablement_source_type
    import capo_connect.types.reference_id


class EvaluationFormItemEnablementSource(TypedDict, closed=True):
    type: "capo_connect.types.evaluation_form_item_enablement_source_type.EvaluationFormItemEnablementSourceType"
    """<p>A type of source item. </p>"""
    ref_id: NotRequired["capo_connect.types.reference_id.ReferenceId"]
    """<p>A referenceId of the source item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItemEnablementSource) -> dict:
    out: dict = {}
    import capo_connect.types.evaluation_form_item_enablement_source_type

    out["Type"] = (
        capo_connect.types.evaluation_form_item_enablement_source_type.serialize_json(
            value["type"]
        )
    )
    if "ref_id" in value:
        out["RefId"] = value["ref_id"]
    return out


def deserialize_json(data: dict) -> EvaluationFormItemEnablementSource:
    out: EvaluationFormItemEnablementSource = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_connect.types.evaluation_form_item_enablement_source_type

        out["type"] = (
            capo_connect.types.evaluation_form_item_enablement_source_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_connect.types.evaluation_form_item_enablement_source_type.EvaluationFormItemEnablementSourceType",
            "",
        )
    if data.get("RefId") is not None:
        out["ref_id"] = data["RefId"]
    return out
