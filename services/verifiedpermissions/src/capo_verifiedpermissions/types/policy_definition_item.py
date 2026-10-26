"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyDefinitionItem``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError
from capo_verifiedpermissions.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.static_policy_definition_item
    import capo_verifiedpermissions.types.template_linked_policy_definition_item


class _PolicyDefinitionItem_static(TypedDict, closed=True):
    static: "capo_verifiedpermissions.types.static_policy_definition_item.StaticPolicyDefinitionItem"


class _PolicyDefinitionItem_templateLinked(TypedDict, closed=True):
    templateLinked: "capo_verifiedpermissions.types.template_linked_policy_definition_item.TemplateLinkedPolicyDefinitionItem"


PolicyDefinitionItem: TypeAlias = (
    _PolicyDefinitionItem_static
    | _PolicyDefinitionItem_templateLinked
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyDefinitionItem) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PolicyDefinitionItem: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "static" in value:
        import capo_verifiedpermissions.types.static_policy_definition_item

        return {
            "static": capo_verifiedpermissions.types.static_policy_definition_item.serialize_aws_json_1_0(
                value["static"]
            )
        }
    elif "templateLinked" in value:
        import capo_verifiedpermissions.types.template_linked_policy_definition_item

        return {
            "templateLinked": capo_verifiedpermissions.types.template_linked_policy_definition_item.serialize_aws_json_1_0(
                value["templateLinked"]
            )
        }
    else:
        raise SerializationError("PolicyDefinitionItem: no variant present")


def deserialize_aws_json_1_0(data: dict) -> PolicyDefinitionItem:
    if data.get("static") is not None:
        import capo_verifiedpermissions.types.static_policy_definition_item

        return {
            "static": capo_verifiedpermissions.types.static_policy_definition_item.deserialize_aws_json_1_0(
                data["static"]
            )
        }
    elif data.get("templateLinked") is not None:
        import capo_verifiedpermissions.types.template_linked_policy_definition_item

        return {
            "templateLinked": capo_verifiedpermissions.types.template_linked_policy_definition_item.deserialize_aws_json_1_0(
                data["templateLinked"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("PolicyDefinitionItem: no recognized variant key")


def redact_sensitive(value: PolicyDefinitionItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "static" in value:
        import capo_verifiedpermissions.types.static_policy_definition_item

        out["static"] = (
            capo_verifiedpermissions.types.static_policy_definition_item.redact_sensitive(
                value["static"]
            )
        )
    if "templateLinked" in value:
        import capo_verifiedpermissions.types.template_linked_policy_definition_item

        out["templateLinked"] = (
            capo_verifiedpermissions.types.template_linked_policy_definition_item.redact_sensitive(
                value["templateLinked"]
            )
        )
    return out
