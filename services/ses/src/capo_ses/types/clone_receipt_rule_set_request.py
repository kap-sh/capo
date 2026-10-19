"""Generated from Smithy shape ``com.amazonaws.ses#CloneReceiptRuleSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.receipt_rule_set_name


class CloneReceiptRuleSetRequest(TypedDict, closed=True):
    rule_set_name: "capo_ses.types.receipt_rule_set_name.ReceiptRuleSetName"
    """<p>The name of the rule set to create. The name must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).</p> </li> <li> <p>Start and end with a letter or number.</p> </li> <li> <p>Contain 64 characters or fewer.</p> </li> </ul>"""
    original_rule_set_name: "capo_ses.types.receipt_rule_set_name.ReceiptRuleSetName"
    """<p>The name of the rule set to clone.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CloneReceiptRuleSetRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}RuleSetName", str(value["rule_set_name"])))
    pairs.append(
        (f"{key_prefix}OriginalRuleSetName", str(value["original_rule_set_name"]))
    )


def deserialize_query(el: Element) -> CloneReceiptRuleSetRequest:
    out: CloneReceiptRuleSetRequest = {}  # type: ignore[typeddict-item]
    child_rule_set_name = el.find("RuleSetName")
    if child_rule_set_name is not None:
        out["rule_set_name"] = str(child_rule_set_name.text or "")
    else:
        out["rule_set_name"] = ""
    child_original_rule_set_name = el.find("OriginalRuleSetName")
    if child_original_rule_set_name is not None:
        out["original_rule_set_name"] = str(child_original_rule_set_name.text or "")
    else:
        out["original_rule_set_name"] = ""
    return out
