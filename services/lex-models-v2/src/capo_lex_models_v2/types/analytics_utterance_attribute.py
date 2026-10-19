"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_utterance_attribute_name


class AnalyticsUtteranceAttribute(TypedDict, closed=True):
    name: "capo_lex_models_v2.types.analytics_utterance_attribute_name.AnalyticsUtteranceAttributeName"
    """<p>An attribute to return. The only available attribute is the intent that the bot mapped the utterance to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceAttribute) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.analytics_utterance_attribute_name

    out["name"] = (
        capo_lex_models_v2.types.analytics_utterance_attribute_name.serialize_json(
            value["name"]
        )
    )
    return out


def deserialize_json(data: dict) -> AnalyticsUtteranceAttribute:
    out: AnalyticsUtteranceAttribute = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_lex_models_v2.types.analytics_utterance_attribute_name

        out["name"] = (
            capo_lex_models_v2.types.analytics_utterance_attribute_name.deserialize_json(
                data["name"]
            )
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_lex_models_v2.types.analytics_utterance_attribute_name.AnalyticsUtteranceAttributeName",
            "",
        )
    return out
