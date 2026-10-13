"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleStringExpression``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.rule_string_list
    import capo_mailmanager.types.rule_string_operator
    import capo_mailmanager.types.rule_string_to_evaluate


class RuleStringExpression(TypedDict, closed=True):
    evaluate: "capo_mailmanager.types.rule_string_to_evaluate.RuleStringToEvaluate"
    """<p>The string to evaluate in a string condition expression.</p>"""
    operator: "capo_mailmanager.types.rule_string_operator.RuleStringOperator"
    """<p>The matching operator for a string condition expression.</p>"""
    values: "capo_mailmanager.types.rule_string_list.RuleStringList"
    """<p>The string(s) to be evaluated in a string condition expression. For all operators, except for NOT_EQUALS, if multiple values are given, the values are processed as an OR. That is, if any of the values match the email's string using the given operator, the condition is deemed to match. However, for NOT_EQUALS, the condition is only deemed to match if none of the given strings match the email's string.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleStringExpression) -> dict:
    out: dict = {}
    import capo_mailmanager.types.rule_string_to_evaluate

    out["Evaluate"] = (
        capo_mailmanager.types.rule_string_to_evaluate.serialize_aws_json_1_0(
            value["evaluate"]
        )
    )
    import capo_mailmanager.types.rule_string_operator

    out["Operator"] = (
        capo_mailmanager.types.rule_string_operator.serialize_aws_json_1_0(
            value["operator"]
        )
    )
    import capo_mailmanager.types.rule_string_list

    out["Values"] = capo_mailmanager.types.rule_string_list.serialize_aws_json_1_0(
        value["values"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RuleStringExpression:
    out: RuleStringExpression = {}  # type: ignore[typeddict-item]
    if data.get("Evaluate") is not None:
        import capo_mailmanager.types.rule_string_to_evaluate

        out["evaluate"] = (
            capo_mailmanager.types.rule_string_to_evaluate.deserialize_aws_json_1_0(
                data["Evaluate"]
            )
        )
    else:
        raise DeserializationError("RuleStringExpression.evaluate required")
    if data.get("Operator") is not None:
        import capo_mailmanager.types.rule_string_operator

        out["operator"] = (
            capo_mailmanager.types.rule_string_operator.deserialize_aws_json_1_0(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("RuleStringExpression.operator required")
    if data.get("Values") is not None:
        import capo_mailmanager.types.rule_string_list

        out["values"] = (
            capo_mailmanager.types.rule_string_list.deserialize_aws_json_1_0(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("RuleStringExpression.values required")
    return out


def redact_sensitive(value: RuleStringExpression) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "values" in value:
        import capo_mailmanager.types.rule_string_list

        out["values"] = capo_mailmanager.types.rule_string_list.redact_sensitive(
            value["values"]
        )
    return out
