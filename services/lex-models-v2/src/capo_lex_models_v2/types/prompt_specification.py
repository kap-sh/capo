"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#PromptSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boxed_boolean
    import capo_lex_models_v2.types.message_groups_list
    import capo_lex_models_v2.types.message_selection_strategy
    import capo_lex_models_v2.types.prompt_attempts_specification_map
    import capo_lex_models_v2.types.prompt_max_retries


class PromptSpecification(TypedDict, closed=True):
    message_groups: "capo_lex_models_v2.types.message_groups_list.MessageGroupsList"
    """<p>A collection of messages that Amazon Lex can send to the user. Amazon Lex chooses the actual message to send at runtime.</p>"""
    max_retries: "capo_lex_models_v2.types.prompt_max_retries.PromptMaxRetries"
    """<p>The maximum number of times the bot tries to elicit a response from the user using this prompt.</p>"""
    allow_interrupt: NotRequired["capo_lex_models_v2.types.boxed_boolean.BoxedBoolean"]
    """<p>Indicates whether the user can interrupt a speech prompt from the bot.</p>"""
    message_selection_strategy: NotRequired[
        "capo_lex_models_v2.types.message_selection_strategy.MessageSelectionStrategy"
    ]
    """<p>Indicates how a message is selected from a message group among retries.</p>"""
    prompt_attempts_specification: NotRequired[
        "capo_lex_models_v2.types.prompt_attempts_specification_map.PromptAttemptsSpecificationMap"
    ]
    """<p>Specifies the advanced settings on each attempt of the prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromptSpecification) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.message_groups_list

    out["messageGroups"] = capo_lex_models_v2.types.message_groups_list.serialize_json(
        value["message_groups"]
    )
    out["maxRetries"] = value["max_retries"]
    if "allow_interrupt" in value:
        out["allowInterrupt"] = value["allow_interrupt"]
    if "message_selection_strategy" in value:
        import capo_lex_models_v2.types.message_selection_strategy

        out["messageSelectionStrategy"] = (
            capo_lex_models_v2.types.message_selection_strategy.serialize_json(
                value["message_selection_strategy"]
            )
        )
    if "prompt_attempts_specification" in value:
        import capo_lex_models_v2.types.prompt_attempts_specification_map

        out["promptAttemptsSpecification"] = (
            capo_lex_models_v2.types.prompt_attempts_specification_map.serialize_json(
                value["prompt_attempts_specification"]
            )
        )
    return out


def deserialize_json(data: dict) -> PromptSpecification:
    out: PromptSpecification = {}  # type: ignore[typeddict-item]
    if data.get("messageGroups") is not None:
        import capo_lex_models_v2.types.message_groups_list

        out["message_groups"] = (
            capo_lex_models_v2.types.message_groups_list.deserialize_json(
                data["messageGroups"]
            )
        )
    else:
        out["message_groups"] = []
    if data.get("maxRetries") is not None:
        out["max_retries"] = data["maxRetries"]
    else:
        out["max_retries"] = 0
    if data.get("allowInterrupt") is not None:
        out["allow_interrupt"] = data["allowInterrupt"]
    if data.get("messageSelectionStrategy") is not None:
        import capo_lex_models_v2.types.message_selection_strategy

        out["message_selection_strategy"] = (
            capo_lex_models_v2.types.message_selection_strategy.deserialize_json(
                data["messageSelectionStrategy"]
            )
        )
    if data.get("promptAttemptsSpecification") is not None:
        import capo_lex_models_v2.types.prompt_attempts_specification_map

        out["prompt_attempts_specification"] = (
            capo_lex_models_v2.types.prompt_attempts_specification_map.deserialize_json(
                data["promptAttemptsSpecification"]
            )
        )
    return out
