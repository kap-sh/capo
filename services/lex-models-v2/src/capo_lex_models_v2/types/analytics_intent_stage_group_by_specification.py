"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentStageGroupBySpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_intent_stage_field


class AnalyticsIntentStageGroupBySpecification(TypedDict, closed=True):
    name: "capo_lex_models_v2.types.analytics_intent_stage_field.AnalyticsIntentStageField"
    """<p>Specifies whether to group the intent stages by their name or the intent to which the session was switched.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentStageGroupBySpecification) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.analytics_intent_stage_field

    out["name"] = capo_lex_models_v2.types.analytics_intent_stage_field.serialize_json(
        value["name"]
    )
    return out


def deserialize_json(data: dict) -> AnalyticsIntentStageGroupBySpecification:
    out: AnalyticsIntentStageGroupBySpecification = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_lex_models_v2.types.analytics_intent_stage_field

        out["name"] = (
            capo_lex_models_v2.types.analytics_intent_stage_field.deserialize_json(
                data["name"]
            )
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_lex_models_v2.types.analytics_intent_stage_field.AnalyticsIntentStageField",
            "",
        )
    return out
