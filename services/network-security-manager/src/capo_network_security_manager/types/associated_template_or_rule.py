"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AssociatedTemplateOrRule``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_network_security_manager.errors import (
    DeserializationError,
    SerializationError,
)
from capo_network_security_manager.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_network_security_manager.types.rule_arn
    import capo_network_security_manager.types.template_arn


class AssociatedTemplateOrRuleTemplateArnMember(TypedDict, closed=True):
    templateArn: "capo_network_security_manager.types.template_arn.TemplateArn"


class AssociatedTemplateOrRuleRuleArnMember(TypedDict, closed=True):
    ruleArn: "capo_network_security_manager.types.rule_arn.RuleArn"


AssociatedTemplateOrRule: TypeAlias = (
    AssociatedTemplateOrRuleTemplateArnMember
    | AssociatedTemplateOrRuleRuleArnMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedTemplateOrRule) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AssociatedTemplateOrRule: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "templateArn" in value:
        return {"templateArn": value["templateArn"]}
    elif "ruleArn" in value:
        return {"ruleArn": value["ruleArn"]}
    else:
        raise SerializationError("AssociatedTemplateOrRule: no variant present")


def deserialize_json(data: dict) -> AssociatedTemplateOrRule:
    if data.get("templateArn") is not None:
        return {"templateArn": data["templateArn"]}
    elif data.get("ruleArn") is not None:
        return {"ruleArn": data["ruleArn"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "AssociatedTemplateOrRule: no recognized variant key"
        )
