"""Generated from Smithy shape ``com.amazonaws.waf#ByteMatchSetUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf.types.byte_match_tuple
    import capo_waf.types.change_action


class ByteMatchSetUpdate(TypedDict, closed=True):
    action: "capo_waf.types.change_action.ChangeAction"
    """<p>Specifies whether to insert or delete a <a>ByteMatchTuple</a>.</p>"""
    byte_match_tuple: "capo_waf.types.byte_match_tuple.ByteMatchTuple"
    """<p>Information about the part of a web request that you want AWS WAF to inspect and the value that you want AWS WAF to search for. If you specify <code>DELETE</code> for the value of <code>Action</code>, the <code>ByteMatchTuple</code> values must exactly match the values in the <code>ByteMatchTuple</code> that you want to delete from the <code>ByteMatchSet</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ByteMatchSetUpdate) -> dict:
    out: dict = {}
    import capo_waf.types.change_action

    out["Action"] = capo_waf.types.change_action.serialize_aws_json_1_1(value["action"])
    import capo_waf.types.byte_match_tuple

    out["ByteMatchTuple"] = capo_waf.types.byte_match_tuple.serialize_aws_json_1_1(
        value["byte_match_tuple"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ByteMatchSetUpdate:
    out: ByteMatchSetUpdate = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_waf.types.change_action

        out["action"] = capo_waf.types.change_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    else:
        import typing

        out["action"] = typing.cast("capo_waf.types.change_action.ChangeAction", "")
    if data.get("ByteMatchTuple") is not None:
        import capo_waf.types.byte_match_tuple

        out["byte_match_tuple"] = (
            capo_waf.types.byte_match_tuple.deserialize_aws_json_1_1(
                data["ByteMatchTuple"]
            )
        )
    else:
        raise DeserializationError("ByteMatchSetUpdate.byte_match_tuple required")
    return out
