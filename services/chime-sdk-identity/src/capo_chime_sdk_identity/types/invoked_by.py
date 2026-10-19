"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#InvokedBy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.standard_messages
    import capo_chime_sdk_identity.types.targeted_messages


class InvokedBy(TypedDict, closed=True):
    standard_messages: (
        "capo_chime_sdk_identity.types.standard_messages.StandardMessages"
    )
    """<p>Sets standard messages as the bot trigger. For standard messages:</p> <ul> <li> <p> <code>ALL</code>: The bot processes all standard messages.</p> </li> <li> <p> <code>AUTO</code>: The bot responds to ALL messages when the channel has one other non-hidden member, and responds to MENTIONS when the channel has more than one other non-hidden member.</p> </li> <li> <p> <code>MENTIONS</code>: The bot processes all standard messages that have a message attribute with <code>CHIME.mentions</code> and a value of the bot ARN.</p> </li> <li> <p> <code>NONE</code>: The bot processes no standard messages.</p> </li> </ul>"""
    targeted_messages: (
        "capo_chime_sdk_identity.types.targeted_messages.TargetedMessages"
    )
    """<p>Sets targeted messages as the bot trigger. For targeted messages:</p> <ul> <li> <p> <code>ALL</code>: The bot processes all <code>TargetedMessages</code> sent to it. The bot then responds with a targeted message back to the sender. </p> </li> <li> <p> <code>NONE</code>: The bot processes no targeted messages.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokedBy) -> dict:
    out: dict = {}
    import capo_chime_sdk_identity.types.standard_messages

    out["StandardMessages"] = (
        capo_chime_sdk_identity.types.standard_messages.serialize_json(
            value["standard_messages"]
        )
    )
    import capo_chime_sdk_identity.types.targeted_messages

    out["TargetedMessages"] = (
        capo_chime_sdk_identity.types.targeted_messages.serialize_json(
            value["targeted_messages"]
        )
    )
    return out


def deserialize_json(data: dict) -> InvokedBy:
    out: InvokedBy = {}  # type: ignore[typeddict-item]
    if data.get("StandardMessages") is not None:
        import capo_chime_sdk_identity.types.standard_messages

        out["standard_messages"] = (
            capo_chime_sdk_identity.types.standard_messages.deserialize_json(
                data["StandardMessages"]
            )
        )
    else:
        import typing

        out["standard_messages"] = typing.cast(
            "capo_chime_sdk_identity.types.standard_messages.StandardMessages", ""
        )
    if data.get("TargetedMessages") is not None:
        import capo_chime_sdk_identity.types.targeted_messages

        out["targeted_messages"] = (
            capo_chime_sdk_identity.types.targeted_messages.deserialize_json(
                data["TargetedMessages"]
            )
        )
    else:
        import typing

        out["targeted_messages"] = typing.cast(
            "capo_chime_sdk_identity.types.targeted_messages.TargetedMessages", ""
        )
    return out
