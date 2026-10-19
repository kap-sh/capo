"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConditionalSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boxed_boolean
    import capo_lex_models_v2.types.conditional_branches
    import capo_lex_models_v2.types.default_conditional_branch


class ConditionalSpecification(TypedDict, closed=True):
    active: "capo_lex_models_v2.types.boxed_boolean.BoxedBoolean"
    """<p>Determines whether a conditional branch is active. When <code>active</code> is false, the conditions are not evaluated.</p>"""
    conditional_branches: (
        "capo_lex_models_v2.types.conditional_branches.ConditionalBranches"
    )
    """<p>A list of conditional branches. A conditional branch is made up of a condition, a response and a next step. The response and next step are executed when the condition is true.</p>"""
    default_branch: (
        "capo_lex_models_v2.types.default_conditional_branch.DefaultConditionalBranch"
    )
    """<p>The conditional branch that should be followed when the conditions for other branches are not satisfied. A conditional branch is made up of a condition, a response and a next step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConditionalSpecification) -> dict:
    out: dict = {}
    out["active"] = value["active"]
    import capo_lex_models_v2.types.conditional_branches

    out["conditionalBranches"] = (
        capo_lex_models_v2.types.conditional_branches.serialize_json(
            value["conditional_branches"]
        )
    )
    import capo_lex_models_v2.types.default_conditional_branch

    out["defaultBranch"] = (
        capo_lex_models_v2.types.default_conditional_branch.serialize_json(
            value["default_branch"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConditionalSpecification:
    out: ConditionalSpecification = {}  # type: ignore[typeddict-item]
    if data.get("active") is not None:
        out["active"] = data["active"]
    else:
        out["active"] = False
    if data.get("conditionalBranches") is not None:
        import capo_lex_models_v2.types.conditional_branches

        out["conditional_branches"] = (
            capo_lex_models_v2.types.conditional_branches.deserialize_json(
                data["conditionalBranches"]
            )
        )
    else:
        out["conditional_branches"] = []
    if data.get("defaultBranch") is not None:
        import capo_lex_models_v2.types.default_conditional_branch

        out["default_branch"] = (
            capo_lex_models_v2.types.default_conditional_branch.deserialize_json(
                data["defaultBranch"]
            )
        )
    else:
        raise DeserializationError("ConditionalSpecification.default_branch required")
    return out
