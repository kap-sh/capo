"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressIpv6ToEvaluate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError
from capo_mailmanager.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mailmanager.types.ingress_ipv6_attribute


class IngressIpv6ToEvaluateAttributeMember(TypedDict, closed=True):
    Attribute: "capo_mailmanager.types.ingress_ipv6_attribute.IngressIpv6Attribute"


IngressIpv6ToEvaluate: TypeAlias = (
    IngressIpv6ToEvaluateAttributeMember | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressIpv6ToEvaluate) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"IngressIpv6ToEvaluate: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Attribute" in value:
        import capo_mailmanager.types.ingress_ipv6_attribute

        return {
            "Attribute": capo_mailmanager.types.ingress_ipv6_attribute.serialize_aws_json_1_0(
                value["Attribute"]
            )
        }
    else:
        raise SerializationError("IngressIpv6ToEvaluate: no variant present")


def deserialize_aws_json_1_0(data: dict) -> IngressIpv6ToEvaluate:
    if data.get("Attribute") is not None:
        import capo_mailmanager.types.ingress_ipv6_attribute

        return {
            "Attribute": capo_mailmanager.types.ingress_ipv6_attribute.deserialize_aws_json_1_0(
                data["Attribute"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("IngressIpv6ToEvaluate: no recognized variant key")
