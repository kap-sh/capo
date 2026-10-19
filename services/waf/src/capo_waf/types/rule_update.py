"""Generated from Smithy shape ``com.amazonaws.waf#RuleUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf.types.change_action
    import capo_waf.types.predicate


class RuleUpdate(TypedDict, closed=True):
    action: "capo_waf.types.change_action.ChangeAction"
    """<p>Specify <code>INSERT</code> to add a <code>Predicate</code> to a <code>Rule</code>. Use <code>DELETE</code> to remove a <code>Predicate</code> from a <code>Rule</code>.</p>"""
    predicate: "capo_waf.types.predicate.Predicate"
    """<p>The ID of the <code>Predicate</code> (such as an <code>IPSet</code>) that you want to add to a <code>Rule</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleUpdate) -> dict:
    out: dict = {}
    import capo_waf.types.change_action

    out["Action"] = capo_waf.types.change_action.serialize_aws_json_1_1(value["action"])
    import capo_waf.types.predicate

    out["Predicate"] = capo_waf.types.predicate.serialize_aws_json_1_1(
        value["predicate"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleUpdate:
    out: RuleUpdate = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_waf.types.change_action

        out["action"] = capo_waf.types.change_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    else:
        import typing

        out["action"] = typing.cast("capo_waf.types.change_action.ChangeAction", "")
    if data.get("Predicate") is not None:
        import capo_waf.types.predicate

        out["predicate"] = capo_waf.types.predicate.deserialize_aws_json_1_1(
            data["Predicate"]
        )
    else:
        raise DeserializationError("RuleUpdate.predicate required")
    return out
