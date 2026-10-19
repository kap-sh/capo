"""Generated from Smithy shape ``com.amazonaws.ses#ReorderReceiptRuleSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.receipt_rule_names_list
    import capo_ses.types.receipt_rule_set_name


class ReorderReceiptRuleSetRequest(TypedDict, closed=True):
    rule_set_name: "capo_ses.types.receipt_rule_set_name.ReceiptRuleSetName"
    """<p>The name of the receipt rule set to reorder.</p>"""
    rule_names: "capo_ses.types.receipt_rule_names_list.ReceiptRuleNamesList"
    """<p>The specified receipt rule set's receipt rules, in order.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReorderReceiptRuleSetRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}RuleSetName", str(value["rule_set_name"])))
    import capo_ses.types.receipt_rule_names_list

    capo_ses.types.receipt_rule_names_list.serialize_query(
        value["rule_names"], pairs, f"{key_prefix}RuleNames"
    )


def deserialize_query(el: Element) -> ReorderReceiptRuleSetRequest:
    out: ReorderReceiptRuleSetRequest = {}  # type: ignore[typeddict-item]
    child_rule_set_name = el.find("RuleSetName")
    if child_rule_set_name is not None:
        out["rule_set_name"] = str(child_rule_set_name.text or "")
    else:
        out["rule_set_name"] = ""
    child_rule_names = el.find("RuleNames")
    if child_rule_names is not None:
        import capo_ses.types.receipt_rule_names_list

        out["rule_names"] = capo_ses.types.receipt_rule_names_list.deserialize_query(
            child_rule_names
        )
    else:
        out["rule_names"] = []
    return out
