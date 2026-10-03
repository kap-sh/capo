"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleIpExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.rule_ip_operator
    import capo_mailmanager.types.rule_ip_to_evaluate
    import capo_mailmanager.types.rule_ip_value_list


class RuleIpExpression(TypedDict, closed=True):
    evaluate: "capo_mailmanager.types.rule_ip_to_evaluate.RuleIpToEvaluate"
    """<p>The IP address to evaluate in this condition.</p>"""
    operator: "capo_mailmanager.types.rule_ip_operator.RuleIpOperator"
    """<p>The operator to evaluate the IP address.</p>"""
    values: "capo_mailmanager.types.rule_ip_value_list.RuleIpValueList"
    """<p>The IP CIDR blocks in format "x.y.z.w/n" (eg 10.0.0.0/8) to match with the email's IP address. For the operator CIDR_MATCHES, if multiple values are given, they are evaluated as an OR. That is, if the IP address is contained within any of the given CIDR ranges, the condition is deemed to match. For NOT_CIDR_MATCHES, if multiple CIDR ranges are given, the condition is deemed to match if the IP address is not contained in any of the given CIDR ranges.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleIpExpression) -> dict:
    out: dict = {}
    import capo_mailmanager.types.rule_ip_to_evaluate

    out["Evaluate"] = capo_mailmanager.types.rule_ip_to_evaluate.serialize_aws_json_1_0(
        value["evaluate"]
    )
    import capo_mailmanager.types.rule_ip_operator

    out["Operator"] = capo_mailmanager.types.rule_ip_operator.serialize_aws_json_1_0(
        value["operator"]
    )
    import capo_mailmanager.types.rule_ip_value_list

    out["Values"] = capo_mailmanager.types.rule_ip_value_list.serialize_aws_json_1_0(
        value["values"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RuleIpExpression:
    out: RuleIpExpression = {}  # type: ignore[typeddict-item]
    if data.get("Evaluate") is not None:
        import capo_mailmanager.types.rule_ip_to_evaluate

        out["evaluate"] = (
            capo_mailmanager.types.rule_ip_to_evaluate.deserialize_aws_json_1_0(
                data["Evaluate"]
            )
        )
    else:
        raise DeserializationError("RuleIpExpression.evaluate required")
    if data.get("Operator") is not None:
        import capo_mailmanager.types.rule_ip_operator

        out["operator"] = (
            capo_mailmanager.types.rule_ip_operator.deserialize_aws_json_1_0(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("RuleIpExpression.operator required")
    if data.get("Values") is not None:
        import capo_mailmanager.types.rule_ip_value_list

        out["values"] = (
            capo_mailmanager.types.rule_ip_value_list.deserialize_aws_json_1_0(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("RuleIpExpression.values required")
    return out
