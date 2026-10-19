"""Generated from Smithy shape ``com.amazonaws.wafregional#RegexPatternSetUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.change_action
    import capo_waf_regional.types.regex_pattern_string


class RegexPatternSetUpdate(TypedDict, closed=True):
    action: "capo_waf_regional.types.change_action.ChangeAction"
    """<p>Specifies whether to insert or delete a <code>RegexPatternString</code>.</p>"""
    regex_pattern_string: (
        "capo_waf_regional.types.regex_pattern_string.RegexPatternString"
    )
    """<p>Specifies the regular expression (regex) pattern that you want AWS WAF to search for, such as <code>B[a@]dB[o0]t</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegexPatternSetUpdate) -> dict:
    out: dict = {}
    import capo_waf_regional.types.change_action

    out["Action"] = capo_waf_regional.types.change_action.serialize_aws_json_1_1(
        value["action"]
    )
    out["RegexPatternString"] = value["regex_pattern_string"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegexPatternSetUpdate:
    out: RegexPatternSetUpdate = {}  # type: ignore[typeddict-item]
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
    if data.get("RegexPatternString") is not None:
        out["regex_pattern_string"] = data["RegexPatternString"]
    else:
        out["regex_pattern_string"] = ""
    return out
