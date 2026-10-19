"""Generated from Smithy shape ``com.amazonaws.wafregional#RegexMatchSetUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf_regional.types.change_action
    import capo_waf_regional.types.regex_match_tuple


class RegexMatchSetUpdate(TypedDict, closed=True):
    action: "capo_waf_regional.types.change_action.ChangeAction"
    """<p>Specifies whether to insert or delete a <a>RegexMatchTuple</a>.</p>"""
    regex_match_tuple: "capo_waf_regional.types.regex_match_tuple.RegexMatchTuple"
    """<p>Information about the part of a web request that you want AWS WAF to inspect and the identifier of the regular expression (regex) pattern that you want AWS WAF to search for. If you specify <code>DELETE</code> for the value of <code>Action</code>, the <code>RegexMatchTuple</code> values must exactly match the values in the <code>RegexMatchTuple</code> that you want to delete from the <code>RegexMatchSet</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegexMatchSetUpdate) -> dict:
    out: dict = {}
    import capo_waf_regional.types.change_action

    out["Action"] = capo_waf_regional.types.change_action.serialize_aws_json_1_1(
        value["action"]
    )
    import capo_waf_regional.types.regex_match_tuple

    out["RegexMatchTuple"] = (
        capo_waf_regional.types.regex_match_tuple.serialize_aws_json_1_1(
            value["regex_match_tuple"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegexMatchSetUpdate:
    out: RegexMatchSetUpdate = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_waf_regional.types.change_action

        out["action"] = capo_waf_regional.types.change_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_waf_regional.types.change_action.ChangeAction", ""
        )
    if data.get("RegexMatchTuple") is not None:
        import capo_waf_regional.types.regex_match_tuple

        out["regex_match_tuple"] = (
            capo_waf_regional.types.regex_match_tuple.deserialize_aws_json_1_1(
                data["RegexMatchTuple"]
            )
        )
    else:
        raise DeserializationError("RegexMatchSetUpdate.regex_match_tuple required")
    return out
