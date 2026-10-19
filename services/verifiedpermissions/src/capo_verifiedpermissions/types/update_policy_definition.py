"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#UpdatePolicyDefinition``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError
from capo_verifiedpermissions.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.update_static_policy_definition


class _UpdatePolicyDefinition_static(TypedDict, closed=True):
    static: "capo_verifiedpermissions.types.update_static_policy_definition.UpdateStaticPolicyDefinition"


UpdatePolicyDefinition: TypeAlias = _UpdatePolicyDefinition_static | UnknownUnionMember


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdatePolicyDefinition) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"UpdatePolicyDefinition: cannot serialize unknown variant {value.name!r}"
        )
    elif "static" in value:
        import capo_verifiedpermissions.types.update_static_policy_definition

        return {
            "static": capo_verifiedpermissions.types.update_static_policy_definition.serialize_aws_json_1_0(
                value["static"]
            )
        }
    else:
        raise SerializationError("UpdatePolicyDefinition: no variant present")


def deserialize_aws_json_1_0(data: dict) -> UpdatePolicyDefinition:
    if data.get("static") is not None:
        import capo_verifiedpermissions.types.update_static_policy_definition

        return {
            "static": capo_verifiedpermissions.types.update_static_policy_definition.deserialize_aws_json_1_0(
                data["static"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("UpdatePolicyDefinition: no recognized variant key")


def redact_sensitive(
    value: UpdatePolicyDefinition,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "static" in value:
        import capo_verifiedpermissions.types.update_static_policy_definition

        out["static"] = (
            capo_verifiedpermissions.types.update_static_policy_definition.redact_sensitive(
                value["static"]
            )
        )
    return out
