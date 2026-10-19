"""Generated from Smithy shape ``com.amazonaws.ses#CreateReceiptRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.receipt_rule
    import capo_ses.types.receipt_rule_name
    import capo_ses.types.receipt_rule_set_name


class CreateReceiptRuleRequest(TypedDict, closed=True):
    rule_set_name: "capo_ses.types.receipt_rule_set_name.ReceiptRuleSetName"
    """<p>The name of the rule set where the receipt rule is added.</p>"""
    after: NotRequired["capo_ses.types.receipt_rule_name.ReceiptRuleName"]
    """<p>The name of an existing rule after which the new rule is placed. If this parameter is null, the new rule is inserted at the beginning of the rule list.</p>"""
    rule: "capo_ses.types.receipt_rule.ReceiptRule"
    """<p>A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateReceiptRuleRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}RuleSetName", str(value["rule_set_name"])))
    if "after" in value:
        pairs.append((f"{key_prefix}After", str(value["after"])))
    import capo_ses.types.receipt_rule

    capo_ses.types.receipt_rule.serialize_query(
        value["rule"], pairs, f"{key_prefix}Rule"
    )


def deserialize_query(el: Element) -> CreateReceiptRuleRequest:
    out: CreateReceiptRuleRequest = {}  # type: ignore[typeddict-item]
    child_rule_set_name = el.find("RuleSetName")
    if child_rule_set_name is not None:
        out["rule_set_name"] = str(child_rule_set_name.text or "")
    else:
        out["rule_set_name"] = ""
    child_after = el.find("After")
    if child_after is not None:
        out["after"] = str(child_after.text or "")
    child_rule = el.find("Rule")
    if child_rule is not None:
        import capo_ses.types.receipt_rule

        out["rule"] = capo_ses.types.receipt_rule.deserialize_query(child_rule)
    else:
        raise DeserializationError("CreateReceiptRuleRequest.rule required")
    return out
