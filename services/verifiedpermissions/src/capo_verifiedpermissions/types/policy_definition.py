"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyDefinition``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError
from capo_verifiedpermissions.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.static_policy_definition
    import capo_verifiedpermissions.types.template_linked_policy_definition


class _PolicyDefinition_static(TypedDict, closed=True):
    static: (
        "capo_verifiedpermissions.types.static_policy_definition.StaticPolicyDefinition"
    )


class _PolicyDefinition_templateLinked(TypedDict, closed=True):
    templateLinked: "capo_verifiedpermissions.types.template_linked_policy_definition.TemplateLinkedPolicyDefinition"


PolicyDefinition: TypeAlias = (
    _PolicyDefinition_static | _PolicyDefinition_templateLinked | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyDefinition) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"PolicyDefinition: cannot serialize unknown variant {value.name!r}"
        )
    elif "static" in value:
        import capo_verifiedpermissions.types.static_policy_definition

        return {
            "static": capo_verifiedpermissions.types.static_policy_definition.serialize_aws_json_1_0(
                value["static"]
            )
        }
    elif "templateLinked" in value:
        import capo_verifiedpermissions.types.template_linked_policy_definition

        return {
            "templateLinked": capo_verifiedpermissions.types.template_linked_policy_definition.serialize_aws_json_1_0(
                value["templateLinked"]
            )
        }
    else:
        raise SerializationError("PolicyDefinition: no variant present")


def deserialize_aws_json_1_0(data: dict) -> PolicyDefinition:
    if data.get("static") is not None:
        import capo_verifiedpermissions.types.static_policy_definition

        return {
            "static": capo_verifiedpermissions.types.static_policy_definition.deserialize_aws_json_1_0(
                data["static"]
            )
        }
    elif data.get("templateLinked") is not None:
        import capo_verifiedpermissions.types.template_linked_policy_definition

        return {
            "templateLinked": capo_verifiedpermissions.types.template_linked_policy_definition.deserialize_aws_json_1_0(
                data["templateLinked"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("PolicyDefinition: no recognized variant key")


def redact_sensitive(value: PolicyDefinition) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "static" in value:
        import capo_verifiedpermissions.types.static_policy_definition

        out["static"] = (
            capo_verifiedpermissions.types.static_policy_definition.redact_sensitive(
                value["static"]
            )
        )
    if "templateLinked" in value:
        import capo_verifiedpermissions.types.template_linked_policy_definition

        out["templateLinked"] = (
            capo_verifiedpermissions.types.template_linked_policy_definition.redact_sensitive(
                value["templateLinked"]
            )
        )
    return out
