"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConditionalBranch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.condition
    import capo_lex_models_v2.types.dialog_state
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.response_specification


class ConditionalBranch(TypedDict, closed=True):
    name: "capo_lex_models_v2.types.name.Name"
    """<p>The name of the branch. </p>"""
    condition: "capo_lex_models_v2.types.condition.Condition"
    """<p>Contains the expression to evaluate. If the condition is true, the branch's actions are taken.</p>"""
    next_step: "capo_lex_models_v2.types.dialog_state.DialogState"
    """<p>The next step in the conversation.</p>"""
    response: NotRequired[
        "capo_lex_models_v2.types.response_specification.ResponseSpecification"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ConditionalBranch) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_lex_models_v2.types.condition

    out["condition"] = capo_lex_models_v2.types.condition.serialize_json(
        value["condition"]
    )
    import capo_lex_models_v2.types.dialog_state

    out["nextStep"] = capo_lex_models_v2.types.dialog_state.serialize_json(
        value["next_step"]
    )
    if "response" in value:
        import capo_lex_models_v2.types.response_specification

        out["response"] = (
            capo_lex_models_v2.types.response_specification.serialize_json(
                value["response"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConditionalBranch:
    out: ConditionalBranch = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("condition") is not None:
        import capo_lex_models_v2.types.condition

        out["condition"] = capo_lex_models_v2.types.condition.deserialize_json(
            data["condition"]
        )
    else:
        raise DeserializationError("ConditionalBranch.condition required")
    if data.get("nextStep") is not None:
        import capo_lex_models_v2.types.dialog_state

        out["next_step"] = capo_lex_models_v2.types.dialog_state.deserialize_json(
            data["nextStep"]
        )
    else:
        raise DeserializationError("ConditionalBranch.next_step required")
    if data.get("response") is not None:
        import capo_lex_models_v2.types.response_specification

        out["response"] = (
            capo_lex_models_v2.types.response_specification.deserialize_json(
                data["response"]
            )
        )
    return out
