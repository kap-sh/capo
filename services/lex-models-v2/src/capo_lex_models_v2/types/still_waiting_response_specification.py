"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#StillWaitingResponseSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boxed_boolean
    import capo_lex_models_v2.types.message_groups_list
    import capo_lex_models_v2.types.still_waiting_response_frequency
    import capo_lex_models_v2.types.still_waiting_response_timeout


class StillWaitingResponseSpecification(TypedDict, closed=True):
    message_groups: "capo_lex_models_v2.types.message_groups_list.MessageGroupsList"
    """<p>One or more message groups, each containing one or more messages, that define the prompts that Amazon Lex sends to the user.</p>"""
    frequency_in_seconds: "capo_lex_models_v2.types.still_waiting_response_frequency.StillWaitingResponseFrequency"
    """<p>How often a message should be sent to the user. Minimum of 1 second, maximum of 5 minutes.</p>"""
    timeout_in_seconds: "capo_lex_models_v2.types.still_waiting_response_timeout.StillWaitingResponseTimeout"
    """<p>If Amazon Lex waits longer than this length of time for a response, it will stop sending messages.</p>"""
    allow_interrupt: NotRequired["capo_lex_models_v2.types.boxed_boolean.BoxedBoolean"]
    """<p>Indicates that the user can interrupt the response by speaking while the message is being played.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StillWaitingResponseSpecification) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.message_groups_list

    out["messageGroups"] = capo_lex_models_v2.types.message_groups_list.serialize_json(
        value["message_groups"]
    )
    out["frequencyInSeconds"] = value["frequency_in_seconds"]
    out["timeoutInSeconds"] = value["timeout_in_seconds"]
    if "allow_interrupt" in value:
        out["allowInterrupt"] = value["allow_interrupt"]
    return out


def deserialize_json(data: dict) -> StillWaitingResponseSpecification:
    out: StillWaitingResponseSpecification = {}  # type: ignore[typeddict-item]
    if data.get("messageGroups") is not None:
        import capo_lex_models_v2.types.message_groups_list

        out["message_groups"] = (
            capo_lex_models_v2.types.message_groups_list.deserialize_json(
                data["messageGroups"]
            )
        )
    else:
        out["message_groups"] = []
    if data.get("frequencyInSeconds") is not None:
        out["frequency_in_seconds"] = data["frequencyInSeconds"]
    else:
        out["frequency_in_seconds"] = 0
    if data.get("timeoutInSeconds") is not None:
        out["timeout_in_seconds"] = data["timeoutInSeconds"]
    else:
        out["timeout_in_seconds"] = 0
    if data.get("allowInterrupt") is not None:
        out["allow_interrupt"] = data["allowInterrupt"]
    return out
