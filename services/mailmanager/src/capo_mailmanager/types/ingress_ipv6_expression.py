"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressIpv6Expression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.ingress_ip_operator
    import capo_mailmanager.types.ingress_ipv6_to_evaluate
    import capo_mailmanager.types.ipv6_cidrs


class IngressIpv6Expression(TypedDict, closed=True):
    evaluate: "capo_mailmanager.types.ingress_ipv6_to_evaluate.IngressIpv6ToEvaluate"
    """<p>The left hand side argument of an IPv6 condition expression.</p>"""
    operator: "capo_mailmanager.types.ingress_ip_operator.IngressIpOperator"
    """<p>The matching operator for an IPv6 condition expression.</p>"""
    values: "capo_mailmanager.types.ipv6_cidrs.Ipv6Cidrs"
    """<p>The right hand side argument of an IPv6 condition expression.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressIpv6Expression) -> dict:
    out: dict = {}
    import capo_mailmanager.types.ingress_ipv6_to_evaluate

    out["Evaluate"] = (
        capo_mailmanager.types.ingress_ipv6_to_evaluate.serialize_aws_json_1_0(
            value["evaluate"]
        )
    )
    import capo_mailmanager.types.ingress_ip_operator

    out["Operator"] = capo_mailmanager.types.ingress_ip_operator.serialize_aws_json_1_0(
        value["operator"]
    )
    import capo_mailmanager.types.ipv6_cidrs

    out["Values"] = capo_mailmanager.types.ipv6_cidrs.serialize_aws_json_1_0(
        value["values"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> IngressIpv6Expression:
    out: IngressIpv6Expression = {}  # type: ignore[typeddict-item]
    if data.get("Evaluate") is not None:
        import capo_mailmanager.types.ingress_ipv6_to_evaluate

        out["evaluate"] = (
            capo_mailmanager.types.ingress_ipv6_to_evaluate.deserialize_aws_json_1_0(
                data["Evaluate"]
            )
        )
    else:
        out["evaluate"] = {"$unknown": {"name": ""}}
    if data.get("Operator") is not None:
        import capo_mailmanager.types.ingress_ip_operator

        out["operator"] = (
            capo_mailmanager.types.ingress_ip_operator.deserialize_aws_json_1_0(
                data["Operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_mailmanager.types.ingress_ip_operator.IngressIpOperator", ""
        )
    if data.get("Values") is not None:
        import capo_mailmanager.types.ipv6_cidrs

        out["values"] = capo_mailmanager.types.ipv6_cidrs.deserialize_aws_json_1_0(
            data["Values"]
        )
    else:
        out["values"] = []
    return out
