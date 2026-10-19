"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#FulfillmentStartResponseSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boxed_boolean
    import capo_lex_models_v2.types.fulfillment_start_response_delay
    import capo_lex_models_v2.types.message_groups_list


class FulfillmentStartResponseSpecification(TypedDict, closed=True):
    delay_in_seconds: "capo_lex_models_v2.types.fulfillment_start_response_delay.FulfillmentStartResponseDelay"
    """<p>The delay between when the Lambda fulfillment function starts running and the start message is played. If the Lambda function returns before the delay is over, the start message isn't played.</p>"""
    message_groups: "capo_lex_models_v2.types.message_groups_list.MessageGroupsList"
    """<p>1 - 5 message groups that contain start messages. Amazon Lex chooses one of the messages to play to the user.</p>"""
    allow_interrupt: NotRequired["capo_lex_models_v2.types.boxed_boolean.BoxedBoolean"]
    """<p>Determines whether the user can interrupt the start message while it is playing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FulfillmentStartResponseSpecification) -> dict:
    out: dict = {}
    out["delayInSeconds"] = value["delay_in_seconds"]
    import capo_lex_models_v2.types.message_groups_list

    out["messageGroups"] = capo_lex_models_v2.types.message_groups_list.serialize_json(
        value["message_groups"]
    )
    if "allow_interrupt" in value:
        out["allowInterrupt"] = value["allow_interrupt"]
    return out


def deserialize_json(data: dict) -> FulfillmentStartResponseSpecification:
    out: FulfillmentStartResponseSpecification = {}  # type: ignore[typeddict-item]
    if data.get("delayInSeconds") is not None:
        out["delay_in_seconds"] = data["delayInSeconds"]
    else:
        out["delay_in_seconds"] = 0
    if data.get("messageGroups") is not None:
        import capo_lex_models_v2.types.message_groups_list

        out["message_groups"] = (
            capo_lex_models_v2.types.message_groups_list.deserialize_json(
                data["messageGroups"]
            )
        )
    else:
        out["message_groups"] = []
    if data.get("allowInterrupt") is not None:
        out["allow_interrupt"] = data["allowInterrupt"]
    return out
