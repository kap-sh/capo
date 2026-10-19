"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceGroupBySpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_utterance_field


class AnalyticsUtteranceGroupBySpecification(TypedDict, closed=True):
    name: "capo_lex_models_v2.types.analytics_utterance_field.AnalyticsUtteranceField"
    """<p>Specifies whether to group the utterances by their text or their state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceGroupBySpecification) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.analytics_utterance_field

    out["name"] = capo_lex_models_v2.types.analytics_utterance_field.serialize_json(
        value["name"]
    )
    return out


def deserialize_json(data: dict) -> AnalyticsUtteranceGroupBySpecification:
    out: AnalyticsUtteranceGroupBySpecification = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_lex_models_v2.types.analytics_utterance_field

        out["name"] = (
            capo_lex_models_v2.types.analytics_utterance_field.deserialize_json(
                data["name"]
            )
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_lex_models_v2.types.analytics_utterance_field.AnalyticsUtteranceField",
            "",
        )
    return out
