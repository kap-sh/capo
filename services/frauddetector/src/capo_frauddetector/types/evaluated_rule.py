"""Generated from Smithy shape ``com.amazonaws.frauddetector#EvaluatedRule``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.boolean
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.list_of_strings
    import capo_frauddetector.types.sensitive_string
    import capo_frauddetector.types.whole_number_version_string


class EvaluatedRule(TypedDict, closed=True):
    rule_id: NotRequired["capo_frauddetector.types.identifier.identifier"]
    """<p> The rule ID. </p>"""
    rule_version: NotRequired[
        "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    ]
    """<p> The rule version. </p>"""
    expression: NotRequired["capo_frauddetector.types.sensitive_string.sensitiveString"]
    """<p> The rule expression. </p>"""
    expression_with_values: NotRequired[
        "capo_frauddetector.types.sensitive_string.sensitiveString"
    ]
    """<p> The rule expression value. </p>"""
    outcomes: NotRequired["capo_frauddetector.types.list_of_strings.ListOfStrings"]
    """<p> The rule outcome. </p>"""
    evaluated: NotRequired["capo_frauddetector.types.boolean.Boolean"]
    """<p> Indicates whether the rule was evaluated. </p>"""
    matched: NotRequired["capo_frauddetector.types.boolean.Boolean"]
    """<p> Indicates whether the rule matched. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluatedRule) -> dict:
    out: dict = {}
    if "rule_id" in value:
        out["ruleId"] = value["rule_id"]
    if "rule_version" in value:
        out["ruleVersion"] = value["rule_version"]
    if "expression" in value:
        out["expression"] = value["expression"]
    if "expression_with_values" in value:
        out["expressionWithValues"] = value["expression_with_values"]
    if "outcomes" in value:
        import capo_frauddetector.types.list_of_strings

        out["outcomes"] = (
            capo_frauddetector.types.list_of_strings.serialize_aws_json_1_1(
                value["outcomes"]
            )
        )
    if "evaluated" in value:
        out["evaluated"] = value["evaluated"]
    if "matched" in value:
        out["matched"] = value["matched"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluatedRule:
    out: EvaluatedRule = {}  # type: ignore[typeddict-item]
    if data.get("ruleId") is not None:
        out["rule_id"] = data["ruleId"]
    if data.get("ruleVersion") is not None:
        out["rule_version"] = data["ruleVersion"]
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    if data.get("expressionWithValues") is not None:
        out["expression_with_values"] = data["expressionWithValues"]
    if data.get("outcomes") is not None:
        import capo_frauddetector.types.list_of_strings

        out["outcomes"] = (
            capo_frauddetector.types.list_of_strings.deserialize_aws_json_1_1(
                data["outcomes"]
            )
        )
    if data.get("evaluated") is not None:
        out["evaluated"] = data["evaluated"]
    if data.get("matched") is not None:
        out["matched"] = data["matched"]
    return out


def redact_sensitive(value: EvaluatedRule) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    if "expression_with_values" in value:
        out["expression_with_values"] = "*** Sensitive Data Redacted ***"
    return out
