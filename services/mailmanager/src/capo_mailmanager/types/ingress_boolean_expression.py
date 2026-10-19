"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressBooleanExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.ingress_boolean_operator
    import capo_mailmanager.types.ingress_boolean_to_evaluate


class IngressBooleanExpression(TypedDict, closed=True):
    evaluate: (
        "capo_mailmanager.types.ingress_boolean_to_evaluate.IngressBooleanToEvaluate"
    )
    """<p>The operand on which to perform a boolean condition operation.</p>"""
    operator: "capo_mailmanager.types.ingress_boolean_operator.IngressBooleanOperator"
    """<p>The matching operator for a boolean condition expression.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressBooleanExpression) -> dict:
    out: dict = {}
    import capo_mailmanager.types.ingress_boolean_to_evaluate

    out["Evaluate"] = (
        capo_mailmanager.types.ingress_boolean_to_evaluate.serialize_aws_json_1_0(
            value["evaluate"]
        )
    )
    import capo_mailmanager.types.ingress_boolean_operator

    out["Operator"] = (
        capo_mailmanager.types.ingress_boolean_operator.serialize_aws_json_1_0(
            value["operator"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> IngressBooleanExpression:
    out: IngressBooleanExpression = {}  # type: ignore[typeddict-item]
    if data.get("Evaluate") is not None:
        import capo_mailmanager.types.ingress_boolean_to_evaluate

        out["evaluate"] = (
            capo_mailmanager.types.ingress_boolean_to_evaluate.deserialize_aws_json_1_0(
                data["Evaluate"]
            )
        )
    else:
        import capo_mailmanager.types._unknown

        out["evaluate"] = capo_mailmanager.types._unknown.UnknownUnionMember("")
    if data.get("Operator") is not None:
        import capo_mailmanager.types.ingress_boolean_operator

        out["operator"] = (
            capo_mailmanager.types.ingress_boolean_operator.deserialize_aws_json_1_0(
                data["Operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_mailmanager.types.ingress_boolean_operator.IngressBooleanOperator", ""
        )
    return out
