"""Generated from Smithy shape ``com.amazonaws.mailmanager#UpdateRuleSetRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.rule_set_id
    import capo_mailmanager.types.rule_set_name
    import capo_mailmanager.types.rules


class UpdateRuleSetRequest(TypedDict, closed=True):
    rule_set_id: "capo_mailmanager.types.rule_set_id.RuleSetId"
    """<p>The identifier of a rule set you want to update.</p>"""
    rule_set_name: NotRequired["capo_mailmanager.types.rule_set_name.RuleSetName"]
    """<p>A user-friendly name for the rule set resource.</p>"""
    rules: NotRequired["capo_mailmanager.types.rules.Rules"]
    """<p>A new set of rules to replace the current rules of the rule set—these rules will override all the rules of the rule set.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateRuleSetRequest) -> dict:
    out: dict = {}
    out["RuleSetId"] = value["rule_set_id"]
    if "rule_set_name" in value:
        out["RuleSetName"] = value["rule_set_name"]
    if "rules" in value:
        import capo_mailmanager.types.rules

        out["Rules"] = capo_mailmanager.types.rules.serialize_aws_json_1_0(
            value["rules"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateRuleSetRequest:
    out: UpdateRuleSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("RuleSetId") is not None:
        out["rule_set_id"] = data["RuleSetId"]
    else:
        raise DeserializationError("UpdateRuleSetRequest.rule_set_id required")
    if data.get("RuleSetName") is not None:
        out["rule_set_name"] = data["RuleSetName"]
    if data.get("Rules") is not None:
        import capo_mailmanager.types.rules

        out["rules"] = capo_mailmanager.types.rules.deserialize_aws_json_1_0(
            data["Rules"]
        )
    return out


def redact_sensitive(value: UpdateRuleSetRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "rules" in value:
        import capo_mailmanager.types.rules

        out["rules"] = capo_mailmanager.types.rules.redact_sensitive(value["rules"])
    return out
