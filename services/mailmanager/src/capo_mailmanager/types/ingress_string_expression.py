"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressStringExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.ingress_string_operator
    import capo_mailmanager.types.ingress_string_to_evaluate
    import capo_mailmanager.types.string_list


class IngressStringExpression(TypedDict, closed=True):
    evaluate: (
        "capo_mailmanager.types.ingress_string_to_evaluate.IngressStringToEvaluate"
    )
    """<p>The left hand side argument of a string condition expression.</p>"""
    operator: "capo_mailmanager.types.ingress_string_operator.IngressStringOperator"
    """<p>The matching operator for a string condition expression.</p>"""
    values: "capo_mailmanager.types.string_list.StringList"
    """<p>The right hand side argument of a string condition expression.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressStringExpression) -> dict:
    out: dict = {}
    import capo_mailmanager.types.ingress_string_to_evaluate

    out["Evaluate"] = (
        capo_mailmanager.types.ingress_string_to_evaluate.serialize_aws_json_1_0(
            value["evaluate"]
        )
    )
    import capo_mailmanager.types.ingress_string_operator

    out["Operator"] = (
        capo_mailmanager.types.ingress_string_operator.serialize_aws_json_1_0(
            value["operator"]
        )
    )
    import capo_mailmanager.types.string_list

    out["Values"] = capo_mailmanager.types.string_list.serialize_aws_json_1_0(
        value["values"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> IngressStringExpression:
    out: IngressStringExpression = {}  # type: ignore[typeddict-item]
    if data.get("Evaluate") is not None:
        import capo_mailmanager.types.ingress_string_to_evaluate

        out["evaluate"] = (
            capo_mailmanager.types.ingress_string_to_evaluate.deserialize_aws_json_1_0(
                data["Evaluate"]
            )
        )
    else:
        import capo_mailmanager.types._unknown

        out["evaluate"] = capo_mailmanager.types._unknown.UnknownUnionMember("")
    if data.get("Operator") is not None:
        import capo_mailmanager.types.ingress_string_operator

        out["operator"] = (
            capo_mailmanager.types.ingress_string_operator.deserialize_aws_json_1_0(
                data["Operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_mailmanager.types.ingress_string_operator.IngressStringOperator", ""
        )
    if data.get("Values") is not None:
        import capo_mailmanager.types.string_list

        out["values"] = capo_mailmanager.types.string_list.deserialize_aws_json_1_0(
            data["Values"]
        )
    else:
        out["values"] = []
    return out
