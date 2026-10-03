"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#Statement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_model_building_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.message_list
    import capo_lex_model_building_service.types.response_card


class Statement(TypedDict, closed=True):
    messages: "capo_lex_model_building_service.types.message_list.MessageList"
    """<p>A collection of message objects.</p>"""
    response_card: NotRequired[
        "capo_lex_model_building_service.types.response_card.ResponseCard"
    ]
    """<p> At runtime, if the client is using the <a href="http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html">PostText</a> API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Statement) -> dict:
    out: dict = {}
    import capo_lex_model_building_service.types.message_list

    out["messages"] = capo_lex_model_building_service.types.message_list.serialize_json(
        value["messages"]
    )
    if "response_card" in value:
        out["responseCard"] = value["response_card"]
    return out


def deserialize_json(data: dict) -> Statement:
    out: Statement = {}  # type: ignore[typeddict-item]
    if data.get("messages") is not None:
        import capo_lex_model_building_service.types.message_list

        out["messages"] = (
            capo_lex_model_building_service.types.message_list.deserialize_json(
                data["messages"]
            )
        )
    else:
        raise DeserializationError("Statement.messages required")
    if data.get("responseCard") is not None:
        out["response_card"] = data["responseCard"]
    return out
