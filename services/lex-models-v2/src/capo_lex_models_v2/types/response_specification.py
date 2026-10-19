"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ResponseSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boxed_boolean
    import capo_lex_models_v2.types.message_groups_list


class ResponseSpecification(TypedDict, closed=True):
    message_groups: "capo_lex_models_v2.types.message_groups_list.MessageGroupsList"
    """<p>A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.</p>"""
    allow_interrupt: NotRequired["capo_lex_models_v2.types.boxed_boolean.BoxedBoolean"]
    """<p>Indicates whether the user can interrupt a speech response from Amazon Lex.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResponseSpecification) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.message_groups_list

    out["messageGroups"] = capo_lex_models_v2.types.message_groups_list.serialize_json(
        value["message_groups"]
    )
    if "allow_interrupt" in value:
        out["allowInterrupt"] = value["allow_interrupt"]
    return out


def deserialize_json(data: dict) -> ResponseSpecification:
    out: ResponseSpecification = {}  # type: ignore[typeddict-item]
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
