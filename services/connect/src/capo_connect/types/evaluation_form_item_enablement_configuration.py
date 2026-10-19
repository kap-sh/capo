"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_item_enablement_action
    import capo_connect.types.evaluation_form_item_enablement_condition


class EvaluationFormItemEnablementConfiguration(TypedDict, closed=True):
    condition: "capo_connect.types.evaluation_form_item_enablement_condition.EvaluationFormItemEnablementCondition"
    """<p>A condition for item enablement configuration.</p>"""
    action: "capo_connect.types.evaluation_form_item_enablement_action.EvaluationFormItemEnablementAction"
    """<p>An enablement action that if condition is satisfied. </p>"""
    default_action: NotRequired[
        "capo_connect.types.evaluation_form_item_enablement_action.EvaluationFormItemEnablementAction"
    ]
    """<p>An enablement action that if condition is not satisfied. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItemEnablementConfiguration) -> dict:
    out: dict = {}
    import capo_connect.types.evaluation_form_item_enablement_condition

    out["Condition"] = (
        capo_connect.types.evaluation_form_item_enablement_condition.serialize_json(
            value["condition"]
        )
    )
    import capo_connect.types.evaluation_form_item_enablement_action

    out["Action"] = (
        capo_connect.types.evaluation_form_item_enablement_action.serialize_json(
            value["action"]
        )
    )
    if "default_action" in value:
        import capo_connect.types.evaluation_form_item_enablement_action

        out["DefaultAction"] = (
            capo_connect.types.evaluation_form_item_enablement_action.serialize_json(
                value["default_action"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormItemEnablementConfiguration:
    out: EvaluationFormItemEnablementConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Condition") is not None:
        import capo_connect.types.evaluation_form_item_enablement_condition

        out["condition"] = (
            capo_connect.types.evaluation_form_item_enablement_condition.deserialize_json(
                data["Condition"]
            )
        )
    else:
        raise DeserializationError(
            "EvaluationFormItemEnablementConfiguration.condition required"
        )
    if data.get("Action") is not None:
        import capo_connect.types.evaluation_form_item_enablement_action

        out["action"] = (
            capo_connect.types.evaluation_form_item_enablement_action.deserialize_json(
                data["Action"]
            )
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_connect.types.evaluation_form_item_enablement_action.EvaluationFormItemEnablementAction",
            "",
        )
    if data.get("DefaultAction") is not None:
        import capo_connect.types.evaluation_form_item_enablement_action

        out["default_action"] = (
            capo_connect.types.evaluation_form_item_enablement_action.deserialize_json(
                data["DefaultAction"]
            )
        )
    return out
