"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetRuleSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.rule_set_id


class GetRuleSetRequest(TypedDict, closed=True):
    rule_set_id: "capo_mailmanager.types.rule_set_id.RuleSetId"
    """<p>The identifier of an existing rule set to be retrieved.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRuleSetRequest) -> dict:
    out: dict = {}
    out["RuleSetId"] = value["rule_set_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRuleSetRequest:
    out: GetRuleSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("RuleSetId") is not None:
        out["rule_set_id"] = data["RuleSetId"]
    else:
        out["rule_set_id"] = ""
    return out
