"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyDefinitionDetail``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.static_policy_definition_detail
    import capo_verifiedpermissions.types.template_linked_policy_definition_detail


class _PolicyDefinitionDetail_static(TypedDict, closed=True):
    static: "capo_verifiedpermissions.types.static_policy_definition_detail.StaticPolicyDefinitionDetail"


class _PolicyDefinitionDetail_templateLinked(TypedDict, closed=True):
    templateLinked: "capo_verifiedpermissions.types.template_linked_policy_definition_detail.TemplateLinkedPolicyDefinitionDetail"


PolicyDefinitionDetail: TypeAlias = (
    _PolicyDefinitionDetail_static | _PolicyDefinitionDetail_templateLinked
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyDefinitionDetail) -> dict:
    if "static" in value:
        import capo_verifiedpermissions.types.static_policy_definition_detail

        return {
            "static": capo_verifiedpermissions.types.static_policy_definition_detail.serialize_aws_json_1_0(
                value["static"]
            )
        }
    elif "templateLinked" in value:
        import capo_verifiedpermissions.types.template_linked_policy_definition_detail

        return {
            "templateLinked": capo_verifiedpermissions.types.template_linked_policy_definition_detail.serialize_aws_json_1_0(
                value["templateLinked"]
            )
        }
    else:
        raise SerializationError("PolicyDefinitionDetail: no variant present")


def deserialize_aws_json_1_0(data: dict) -> PolicyDefinitionDetail:
    if data.get("static") is not None:
        import capo_verifiedpermissions.types.static_policy_definition_detail

        return {
            "static": capo_verifiedpermissions.types.static_policy_definition_detail.deserialize_aws_json_1_0(
                data["static"]
            )
        }
    elif data.get("templateLinked") is not None:
        import capo_verifiedpermissions.types.template_linked_policy_definition_detail

        return {
            "templateLinked": capo_verifiedpermissions.types.template_linked_policy_definition_detail.deserialize_aws_json_1_0(
                data["templateLinked"]
            )
        }
    else:
        raise DeserializationError("PolicyDefinitionDetail: no recognized variant key")


def redact_sensitive(value: PolicyDefinitionDetail) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "static" in value:
        import capo_verifiedpermissions.types.static_policy_definition_detail

        out["static"] = (
            capo_verifiedpermissions.types.static_policy_definition_detail.redact_sensitive(
                value["static"]
            )
        )
    if "templateLinked" in value:
        import capo_verifiedpermissions.types.template_linked_policy_definition_detail

        out["templateLinked"] = (
            capo_verifiedpermissions.types.template_linked_policy_definition_detail.redact_sensitive(
                value["templateLinked"]
            )
        )
    return out
