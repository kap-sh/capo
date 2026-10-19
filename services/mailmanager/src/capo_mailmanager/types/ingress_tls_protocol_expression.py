"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressTlsProtocolExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.ingress_tls_protocol_attribute
    import capo_mailmanager.types.ingress_tls_protocol_operator
    import capo_mailmanager.types.ingress_tls_protocol_to_evaluate


class IngressTlsProtocolExpression(TypedDict, closed=True):
    evaluate: "capo_mailmanager.types.ingress_tls_protocol_to_evaluate.IngressTlsProtocolToEvaluate"
    """<p>The left hand side argument of a TLS condition expression.</p>"""
    operator: "capo_mailmanager.types.ingress_tls_protocol_operator.IngressTlsProtocolOperator"
    """<p>The matching operator for a TLS condition expression.</p>"""
    value: "capo_mailmanager.types.ingress_tls_protocol_attribute.IngressTlsProtocolAttribute"
    """<p>The right hand side argument of a TLS condition expression.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressTlsProtocolExpression) -> dict:
    out: dict = {}
    import capo_mailmanager.types.ingress_tls_protocol_to_evaluate

    out["Evaluate"] = (
        capo_mailmanager.types.ingress_tls_protocol_to_evaluate.serialize_aws_json_1_0(
            value["evaluate"]
        )
    )
    import capo_mailmanager.types.ingress_tls_protocol_operator

    out["Operator"] = (
        capo_mailmanager.types.ingress_tls_protocol_operator.serialize_aws_json_1_0(
            value["operator"]
        )
    )
    import capo_mailmanager.types.ingress_tls_protocol_attribute

    out["Value"] = (
        capo_mailmanager.types.ingress_tls_protocol_attribute.serialize_aws_json_1_0(
            value["value"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> IngressTlsProtocolExpression:
    out: IngressTlsProtocolExpression = {}  # type: ignore[typeddict-item]
    if data.get("Evaluate") is not None:
        import capo_mailmanager.types.ingress_tls_protocol_to_evaluate

        out["evaluate"] = (
            capo_mailmanager.types.ingress_tls_protocol_to_evaluate.deserialize_aws_json_1_0(
                data["Evaluate"]
            )
        )
    else:
        import capo_mailmanager.types._unknown

        out["evaluate"] = capo_mailmanager.types._unknown.UnknownUnionMember("")
    if data.get("Operator") is not None:
        import capo_mailmanager.types.ingress_tls_protocol_operator

        out["operator"] = (
            capo_mailmanager.types.ingress_tls_protocol_operator.deserialize_aws_json_1_0(
                data["Operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_mailmanager.types.ingress_tls_protocol_operator.IngressTlsProtocolOperator",
            "",
        )
    if data.get("Value") is not None:
        import capo_mailmanager.types.ingress_tls_protocol_attribute

        out["value"] = (
            capo_mailmanager.types.ingress_tls_protocol_attribute.deserialize_aws_json_1_0(
                data["Value"]
            )
        )
    else:
        import typing

        out["value"] = typing.cast(
            "capo_mailmanager.types.ingress_tls_protocol_attribute.IngressTlsProtocolAttribute",
            "",
        )
    return out
