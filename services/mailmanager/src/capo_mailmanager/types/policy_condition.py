"""Generated from Smithy shape ``com.amazonaws.mailmanager#PolicyCondition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError
from capo_mailmanager.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mailmanager.types.ingress_boolean_expression
    import capo_mailmanager.types.ingress_ipv4_expression
    import capo_mailmanager.types.ingress_ipv6_expression
    import capo_mailmanager.types.ingress_string_expression
    import capo_mailmanager.types.ingress_tls_protocol_expression


class PolicyConditionStringExpressionMember(TypedDict, closed=True):
    StringExpression: (
        "capo_mailmanager.types.ingress_string_expression.IngressStringExpression"
    )


class PolicyConditionIpExpressionMember(TypedDict, closed=True):
    IpExpression: "capo_mailmanager.types.ingress_ipv4_expression.IngressIpv4Expression"


class PolicyConditionIpv6ExpressionMember(TypedDict, closed=True):
    Ipv6Expression: (
        "capo_mailmanager.types.ingress_ipv6_expression.IngressIpv6Expression"
    )


class PolicyConditionTlsExpressionMember(TypedDict, closed=True):
    TlsExpression: "capo_mailmanager.types.ingress_tls_protocol_expression.IngressTlsProtocolExpression"


class PolicyConditionBooleanExpressionMember(TypedDict, closed=True):
    BooleanExpression: (
        "capo_mailmanager.types.ingress_boolean_expression.IngressBooleanExpression"
    )


PolicyCondition: TypeAlias = (
    PolicyConditionStringExpressionMember
    | PolicyConditionIpExpressionMember
    | PolicyConditionIpv6ExpressionMember
    | PolicyConditionTlsExpressionMember
    | PolicyConditionBooleanExpressionMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyCondition) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PolicyCondition: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "StringExpression" in value:
        import capo_mailmanager.types.ingress_string_expression

        return {
            "StringExpression": capo_mailmanager.types.ingress_string_expression.serialize_aws_json_1_0(
                value["StringExpression"]
            )
        }
    elif "IpExpression" in value:
        import capo_mailmanager.types.ingress_ipv4_expression

        return {
            "IpExpression": capo_mailmanager.types.ingress_ipv4_expression.serialize_aws_json_1_0(
                value["IpExpression"]
            )
        }
    elif "Ipv6Expression" in value:
        import capo_mailmanager.types.ingress_ipv6_expression

        return {
            "Ipv6Expression": capo_mailmanager.types.ingress_ipv6_expression.serialize_aws_json_1_0(
                value["Ipv6Expression"]
            )
        }
    elif "TlsExpression" in value:
        import capo_mailmanager.types.ingress_tls_protocol_expression

        return {
            "TlsExpression": capo_mailmanager.types.ingress_tls_protocol_expression.serialize_aws_json_1_0(
                value["TlsExpression"]
            )
        }
    elif "BooleanExpression" in value:
        import capo_mailmanager.types.ingress_boolean_expression

        return {
            "BooleanExpression": capo_mailmanager.types.ingress_boolean_expression.serialize_aws_json_1_0(
                value["BooleanExpression"]
            )
        }
    else:
        raise SerializationError("PolicyCondition: no variant present")


def deserialize_aws_json_1_0(data: dict) -> PolicyCondition:
    if data.get("StringExpression") is not None:
        import capo_mailmanager.types.ingress_string_expression

        return {
            "StringExpression": capo_mailmanager.types.ingress_string_expression.deserialize_aws_json_1_0(
                data["StringExpression"]
            )
        }
    elif data.get("IpExpression") is not None:
        import capo_mailmanager.types.ingress_ipv4_expression

        return {
            "IpExpression": capo_mailmanager.types.ingress_ipv4_expression.deserialize_aws_json_1_0(
                data["IpExpression"]
            )
        }
    elif data.get("Ipv6Expression") is not None:
        import capo_mailmanager.types.ingress_ipv6_expression

        return {
            "Ipv6Expression": capo_mailmanager.types.ingress_ipv6_expression.deserialize_aws_json_1_0(
                data["Ipv6Expression"]
            )
        }
    elif data.get("TlsExpression") is not None:
        import capo_mailmanager.types.ingress_tls_protocol_expression

        return {
            "TlsExpression": capo_mailmanager.types.ingress_tls_protocol_expression.deserialize_aws_json_1_0(
                data["TlsExpression"]
            )
        }
    elif data.get("BooleanExpression") is not None:
        import capo_mailmanager.types.ingress_boolean_expression

        return {
            "BooleanExpression": capo_mailmanager.types.ingress_boolean_expression.deserialize_aws_json_1_0(
                data["BooleanExpression"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("PolicyCondition: no recognized variant key")
