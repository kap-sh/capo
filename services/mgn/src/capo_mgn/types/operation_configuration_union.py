"""Generated from Smithy shape ``com.amazonaws.mgn#OperationConfigurationUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mgn.errors import DeserializationError, SerializationError
from capo_mgn.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mgn.types.security_group_configuration
    import capo_mgn.types.security_group_rule_configuration


class OperationConfigurationUnionSecurityGroupMember(TypedDict, closed=True):
    securityGroup: (
        "capo_mgn.types.security_group_configuration.SecurityGroupConfiguration"
    )


class OperationConfigurationUnionSecurityGroupRuleMember(TypedDict, closed=True):
    securityGroupRule: "capo_mgn.types.security_group_rule_configuration.SecurityGroupRuleConfiguration"


OperationConfigurationUnion: TypeAlias = (
    OperationConfigurationUnionSecurityGroupMember
    | OperationConfigurationUnionSecurityGroupRuleMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: OperationConfigurationUnion) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"OperationConfigurationUnion: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "securityGroup" in value:
        import capo_mgn.types.security_group_configuration

        return {
            "securityGroup": capo_mgn.types.security_group_configuration.serialize_json(
                value["securityGroup"]
            )
        }
    elif "securityGroupRule" in value:
        import capo_mgn.types.security_group_rule_configuration

        return {
            "securityGroupRule": capo_mgn.types.security_group_rule_configuration.serialize_json(
                value["securityGroupRule"]
            )
        }
    else:
        raise SerializationError("OperationConfigurationUnion: no variant present")


def deserialize_json(data: dict) -> OperationConfigurationUnion:
    if data.get("securityGroup") is not None:
        import capo_mgn.types.security_group_configuration

        return {
            "securityGroup": capo_mgn.types.security_group_configuration.deserialize_json(
                data["securityGroup"]
            )
        }
    elif data.get("securityGroupRule") is not None:
        import capo_mgn.types.security_group_rule_configuration

        return {
            "securityGroupRule": capo_mgn.types.security_group_rule_configuration.deserialize_json(
                data["securityGroupRule"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "OperationConfigurationUnion: no recognized variant key"
        )
