"""Generated from Smithy shape ``com.amazonaws.ses#DescribeReceiptRuleSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.receipt_rule_set_name


class DescribeReceiptRuleSetRequest(TypedDict, closed=True):
    rule_set_name: "capo_ses.types.receipt_rule_set_name.ReceiptRuleSetName"
    """<p>The name of the receipt rule set to describe.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeReceiptRuleSetRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}RuleSetName", str(value["rule_set_name"])))


def deserialize_query(el: Element) -> DescribeReceiptRuleSetRequest:
    out: DescribeReceiptRuleSetRequest = {}  # type: ignore[typeddict-item]
    child_rule_set_name = el.find("RuleSetName")
    if child_rule_set_name is not None:
        out["rule_set_name"] = str(child_rule_set_name.text or "")
    else:
        out["rule_set_name"] = ""
    return out
