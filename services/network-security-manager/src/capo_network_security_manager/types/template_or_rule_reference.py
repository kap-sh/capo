"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#TemplateOrRuleReference``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_network_security_manager.errors import (
    DeserializationError,
    SerializationError,
)
from capo_network_security_manager.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_network_security_manager.types.rule_identifier
    import capo_network_security_manager.types.template_identifier


class _TemplateOrRuleReference_templateIdentifier(TypedDict, closed=True):
    templateIdentifier: (
        "capo_network_security_manager.types.template_identifier.TemplateIdentifier"
    )


class _TemplateOrRuleReference_ruleIdentifier(TypedDict, closed=True):
    ruleIdentifier: "capo_network_security_manager.types.rule_identifier.RuleIdentifier"


TemplateOrRuleReference: TypeAlias = (
    _TemplateOrRuleReference_templateIdentifier
    | _TemplateOrRuleReference_ruleIdentifier
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TemplateOrRuleReference) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"TemplateOrRuleReference: cannot serialize unknown variant {value.name!r}"
        )
    elif "templateIdentifier" in value:
        return {"templateIdentifier": value["templateIdentifier"]}
    elif "ruleIdentifier" in value:
        return {"ruleIdentifier": value["ruleIdentifier"]}
    else:
        raise SerializationError("TemplateOrRuleReference: no variant present")


def deserialize_json(data: dict) -> TemplateOrRuleReference:
    if data.get("templateIdentifier") is not None:
        return {"templateIdentifier": data["templateIdentifier"]}
    elif data.get("ruleIdentifier") is not None:
        return {"ruleIdentifier": data["ruleIdentifier"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("TemplateOrRuleReference: no recognized variant key")
