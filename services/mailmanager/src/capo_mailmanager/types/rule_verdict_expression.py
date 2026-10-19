"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleVerdictExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.rule_verdict_operator
    import capo_mailmanager.types.rule_verdict_to_evaluate
    import capo_mailmanager.types.rule_verdict_value_list


class RuleVerdictExpression(TypedDict, closed=True):
    evaluate: "capo_mailmanager.types.rule_verdict_to_evaluate.RuleVerdictToEvaluate"
    """<p>The verdict to evaluate in a verdict condition expression.</p>"""
    operator: "capo_mailmanager.types.rule_verdict_operator.RuleVerdictOperator"
    """<p>The matching operator for a verdict condition expression.</p>"""
    values: "capo_mailmanager.types.rule_verdict_value_list.RuleVerdictValueList"
    """<p>The values to match with the email's verdict using the given operator. For the EQUALS operator, if multiple values are given, the condition is deemed to match if any of the given verdicts match that of the email. For the NOT_EQUALS operator, if multiple values are given, the condition is deemed to match of none of the given verdicts match the verdict of the email.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleVerdictExpression) -> dict:
    out: dict = {}
    import capo_mailmanager.types.rule_verdict_to_evaluate

    out["Evaluate"] = (
        capo_mailmanager.types.rule_verdict_to_evaluate.serialize_aws_json_1_0(
            value["evaluate"]
        )
    )
    import capo_mailmanager.types.rule_verdict_operator

    out["Operator"] = (
        capo_mailmanager.types.rule_verdict_operator.serialize_aws_json_1_0(
            value["operator"]
        )
    )
    import capo_mailmanager.types.rule_verdict_value_list

    out["Values"] = (
        capo_mailmanager.types.rule_verdict_value_list.serialize_aws_json_1_0(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RuleVerdictExpression:
    out: RuleVerdictExpression = {}  # type: ignore[typeddict-item]
    if data.get("Evaluate") is not None:
        import capo_mailmanager.types.rule_verdict_to_evaluate

        out["evaluate"] = (
            capo_mailmanager.types.rule_verdict_to_evaluate.deserialize_aws_json_1_0(
                data["Evaluate"]
            )
        )
    else:
        import capo_mailmanager.types._unknown

        out["evaluate"] = capo_mailmanager.types._unknown.UnknownUnionMember("")
    if data.get("Operator") is not None:
        import capo_mailmanager.types.rule_verdict_operator

        out["operator"] = (
            capo_mailmanager.types.rule_verdict_operator.deserialize_aws_json_1_0(
                data["Operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_mailmanager.types.rule_verdict_operator.RuleVerdictOperator", ""
        )
    if data.get("Values") is not None:
        import capo_mailmanager.types.rule_verdict_value_list

        out["values"] = (
            capo_mailmanager.types.rule_verdict_value_list.deserialize_aws_json_1_0(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    return out
