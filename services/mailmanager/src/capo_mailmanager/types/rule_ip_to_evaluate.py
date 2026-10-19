"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleIpToEvaluate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError
from capo_mailmanager.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mailmanager.types.rule_ip_email_attribute


class _RuleIpToEvaluate_Attribute(TypedDict, closed=True):
    Attribute: "capo_mailmanager.types.rule_ip_email_attribute.RuleIpEmailAttribute"


RuleIpToEvaluate: TypeAlias = _RuleIpToEvaluate_Attribute | UnknownUnionMember


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleIpToEvaluate) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"RuleIpToEvaluate: cannot serialize unknown variant {value.name!r}"
        )
    elif "Attribute" in value:
        import capo_mailmanager.types.rule_ip_email_attribute

        return {
            "Attribute": capo_mailmanager.types.rule_ip_email_attribute.serialize_aws_json_1_0(
                value["Attribute"]
            )
        }
    else:
        raise SerializationError("RuleIpToEvaluate: no variant present")


def deserialize_aws_json_1_0(data: dict) -> RuleIpToEvaluate:
    if data.get("Attribute") is not None:
        import capo_mailmanager.types.rule_ip_email_attribute

        return {
            "Attribute": capo_mailmanager.types.rule_ip_email_attribute.deserialize_aws_json_1_0(
                data["Attribute"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("RuleIpToEvaluate: no recognized variant key")
