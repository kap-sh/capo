"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentGroupBySpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_intent_field


class AnalyticsIntentGroupBySpecification(TypedDict, closed=True):
    name: "capo_lex_models_v2.types.analytics_intent_field.AnalyticsIntentField"
    """<p>Specifies whether to group the intent stages by their name or their end state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentGroupBySpecification) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.analytics_intent_field

    out["name"] = capo_lex_models_v2.types.analytics_intent_field.serialize_json(
        value["name"]
    )
    return out


def deserialize_json(data: dict) -> AnalyticsIntentGroupBySpecification:
    out: AnalyticsIntentGroupBySpecification = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_lex_models_v2.types.analytics_intent_field

        out["name"] = capo_lex_models_v2.types.analytics_intent_field.deserialize_json(
            data["name"]
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_lex_models_v2.types.analytics_intent_field.AnalyticsIntentField", ""
        )
    return out
