"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleDmarcExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.rule_dmarc_operator
    import capo_mailmanager.types.rule_dmarc_value_list


class RuleDmarcExpression(TypedDict, closed=True):
    operator: "capo_mailmanager.types.rule_dmarc_operator.RuleDmarcOperator"
    """<p>The operator to apply to the DMARC policy of the incoming email.</p>"""
    values: "capo_mailmanager.types.rule_dmarc_value_list.RuleDmarcValueList"
    """<p>The values to use for the given DMARC policy operator. For the operator EQUALS, if multiple values are given, they are evaluated as an OR. That is, if any of the given values match, the condition is deemed to match. For the operator NOT_EQUALS, if multiple values are given, they are evaluated as an AND. That is, only if the email's DMARC policy is not equal to any of the given values, then the condition is deemed to match.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleDmarcExpression) -> dict:
    out: dict = {}
    import capo_mailmanager.types.rule_dmarc_operator

    out["Operator"] = capo_mailmanager.types.rule_dmarc_operator.serialize_aws_json_1_0(
        value["operator"]
    )
    import capo_mailmanager.types.rule_dmarc_value_list

    out["Values"] = capo_mailmanager.types.rule_dmarc_value_list.serialize_aws_json_1_0(
        value["values"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RuleDmarcExpression:
    out: RuleDmarcExpression = {}  # type: ignore[typeddict-item]
    if data.get("Operator") is not None:
        import capo_mailmanager.types.rule_dmarc_operator

        out["operator"] = (
            capo_mailmanager.types.rule_dmarc_operator.deserialize_aws_json_1_0(
                data["Operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_mailmanager.types.rule_dmarc_operator.RuleDmarcOperator", ""
        )
    if data.get("Values") is not None:
        import capo_mailmanager.types.rule_dmarc_value_list

        out["values"] = (
            capo_mailmanager.types.rule_dmarc_value_list.deserialize_aws_json_1_0(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    return out
