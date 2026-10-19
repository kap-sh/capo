"""Generated from Smithy shape ``com.amazonaws.ses#SetReceiptRulePositionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.receipt_rule_name
    import capo_ses.types.receipt_rule_set_name


class SetReceiptRulePositionRequest(TypedDict, closed=True):
    rule_set_name: "capo_ses.types.receipt_rule_set_name.ReceiptRuleSetName"
    """<p>The name of the receipt rule set that contains the receipt rule to reposition.</p>"""
    rule_name: "capo_ses.types.receipt_rule_name.ReceiptRuleName"
    """<p>The name of the receipt rule to reposition.</p>"""
    after: NotRequired["capo_ses.types.receipt_rule_name.ReceiptRuleName"]
    """<p>The name of the receipt rule after which to place the specified receipt rule.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetReceiptRulePositionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}RuleSetName", str(value["rule_set_name"])))
    pairs.append((f"{key_prefix}RuleName", str(value["rule_name"])))
    if "after" in value:
        pairs.append((f"{key_prefix}After", str(value["after"])))


def deserialize_query(el: Element) -> SetReceiptRulePositionRequest:
    out: SetReceiptRulePositionRequest = {}  # type: ignore[typeddict-item]
    child_rule_set_name = el.find("RuleSetName")
    if child_rule_set_name is not None:
        out["rule_set_name"] = str(child_rule_set_name.text or "")
    else:
        out["rule_set_name"] = ""
    child_rule_name = el.find("RuleName")
    if child_rule_name is not None:
        out["rule_name"] = str(child_rule_name.text or "")
    else:
        out["rule_name"] = ""
    child_after = el.find("After")
    if child_after is not None:
        out["after"] = str(child_after.text or "")
    return out
