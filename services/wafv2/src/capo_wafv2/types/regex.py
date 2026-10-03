"""Generated from Smithy shape ``com.amazonaws.wafv2#Regex``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.regex_pattern_string


class Regex(TypedDict, closed=True):
    regex_string: NotRequired[
        "capo_wafv2.types.regex_pattern_string.RegexPatternString"
    ]
    """<p>The string representing the regular expression. WAF enforces a quota on the maximum number of characters in a regex pattern. For the current limit, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Regex) -> dict:
    out: dict = {}
    if "regex_string" in value:
        out["RegexString"] = value["regex_string"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Regex:
    out: Regex = {}  # type: ignore[typeddict-item]
    if data.get("RegexString") is not None:
        out["regex_string"] = data["RegexString"]
    return out
