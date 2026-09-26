"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AssociatedTemplateOrRule``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_network_security_manager.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_network_security_manager.types.rule_arn
    import capo_network_security_manager.types.template_arn


class _AssociatedTemplateOrRule_templateArn(TypedDict, closed=True):
    templateArn: "capo_network_security_manager.types.template_arn.TemplateArn"


class _AssociatedTemplateOrRule_ruleArn(TypedDict, closed=True):
    ruleArn: "capo_network_security_manager.types.rule_arn.RuleArn"


AssociatedTemplateOrRule: TypeAlias = (
    _AssociatedTemplateOrRule_templateArn | _AssociatedTemplateOrRule_ruleArn
)


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedTemplateOrRule) -> dict:
    if "templateArn" in value:
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
        raise DeserializationError(
            "AssociatedTemplateOrRule: no recognized variant key"
        )
