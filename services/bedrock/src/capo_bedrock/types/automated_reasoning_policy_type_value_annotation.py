"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyTypeValueAnnotation``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_add_type_value
    import capo_bedrock.types.automated_reasoning_policy_delete_type_value
    import capo_bedrock.types.automated_reasoning_policy_update_type_value


class _AutomatedReasoningPolicyTypeValueAnnotation_addTypeValue(TypedDict, closed=True):
    addTypeValue: "capo_bedrock.types.automated_reasoning_policy_add_type_value.AutomatedReasoningPolicyAddTypeValue"


class _AutomatedReasoningPolicyTypeValueAnnotation_updateTypeValue(
    TypedDict, closed=True
):
    updateTypeValue: "capo_bedrock.types.automated_reasoning_policy_update_type_value.AutomatedReasoningPolicyUpdateTypeValue"


class _AutomatedReasoningPolicyTypeValueAnnotation_deleteTypeValue(
    TypedDict, closed=True
):
    deleteTypeValue: "capo_bedrock.types.automated_reasoning_policy_delete_type_value.AutomatedReasoningPolicyDeleteTypeValue"


AutomatedReasoningPolicyTypeValueAnnotation: TypeAlias = (
    _AutomatedReasoningPolicyTypeValueAnnotation_addTypeValue
    | _AutomatedReasoningPolicyTypeValueAnnotation_updateTypeValue
    | _AutomatedReasoningPolicyTypeValueAnnotation_deleteTypeValue
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyTypeValueAnnotation) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AutomatedReasoningPolicyTypeValueAnnotation: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "addTypeValue" in value:
        import capo_bedrock.types.automated_reasoning_policy_add_type_value

        return {
            "addTypeValue": capo_bedrock.types.automated_reasoning_policy_add_type_value.serialize_json(
                value["addTypeValue"]
            )
        }
    elif "updateTypeValue" in value:
        import capo_bedrock.types.automated_reasoning_policy_update_type_value

        return {
            "updateTypeValue": capo_bedrock.types.automated_reasoning_policy_update_type_value.serialize_json(
                value["updateTypeValue"]
            )
        }
    elif "deleteTypeValue" in value:
        import capo_bedrock.types.automated_reasoning_policy_delete_type_value

        return {
            "deleteTypeValue": capo_bedrock.types.automated_reasoning_policy_delete_type_value.serialize_json(
                value["deleteTypeValue"]
            )
        }
    else:
        raise SerializationError(
            "AutomatedReasoningPolicyTypeValueAnnotation: no variant present"
        )


def deserialize_json(data: dict) -> AutomatedReasoningPolicyTypeValueAnnotation:
    if data.get("addTypeValue") is not None:
        import capo_bedrock.types.automated_reasoning_policy_add_type_value

        return {
            "addTypeValue": capo_bedrock.types.automated_reasoning_policy_add_type_value.deserialize_json(
                data["addTypeValue"]
            )
        }
    elif data.get("updateTypeValue") is not None:
        import capo_bedrock.types.automated_reasoning_policy_update_type_value

        return {
            "updateTypeValue": capo_bedrock.types.automated_reasoning_policy_update_type_value.deserialize_json(
                data["updateTypeValue"]
            )
        }
    elif data.get("deleteTypeValue") is not None:
        import capo_bedrock.types.automated_reasoning_policy_delete_type_value

        return {
            "deleteTypeValue": capo_bedrock.types.automated_reasoning_policy_delete_type_value.deserialize_json(
                data["deleteTypeValue"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "AutomatedReasoningPolicyTypeValueAnnotation: no recognized variant key"
        )


def redact_sensitive(
    value: AutomatedReasoningPolicyTypeValueAnnotation,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "addTypeValue" in value:
        import capo_bedrock.types.automated_reasoning_policy_add_type_value

        out["addTypeValue"] = (
            capo_bedrock.types.automated_reasoning_policy_add_type_value.redact_sensitive(
                value["addTypeValue"]
            )
        )
    if "updateTypeValue" in value:
        import capo_bedrock.types.automated_reasoning_policy_update_type_value

        out["updateTypeValue"] = (
            capo_bedrock.types.automated_reasoning_policy_update_type_value.redact_sensitive(
                value["updateTypeValue"]
            )
        )
    return out
