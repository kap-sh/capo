"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyUpdateTypeAnnotation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_type_description
    import capo_bedrock.types.automated_reasoning_policy_definition_type_name
    import capo_bedrock.types.automated_reasoning_policy_type_value_annotation_list


class AutomatedReasoningPolicyUpdateTypeAnnotation(TypedDict, closed=True):
    name: "capo_bedrock.types.automated_reasoning_policy_definition_type_name.AutomatedReasoningPolicyDefinitionTypeName"
    """<p>The current name of the custom type to update.</p>"""
    new_name: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_definition_type_name.AutomatedReasoningPolicyDefinitionTypeName"
    ]
    """<p>The new name for the custom type, if you want to rename it. If not provided, the name remains unchanged.</p>"""
    description: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_definition_type_description.AutomatedReasoningPolicyDefinitionTypeDescription"
    ]
    """<p>The new description for the custom type, replacing the previous description.</p>"""
    values: "capo_bedrock.types.automated_reasoning_policy_type_value_annotation_list.AutomatedReasoningPolicyTypeValueAnnotationList"
    """<p>The updated list of values for the custom type, which can include additions, modifications, or removals.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyUpdateTypeAnnotation) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "new_name" in value:
        out["newName"] = value["new_name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock.types.automated_reasoning_policy_type_value_annotation_list

    out["values"] = (
        capo_bedrock.types.automated_reasoning_policy_type_value_annotation_list.serialize_json(
            value["values"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyUpdateTypeAnnotation:
    out: AutomatedReasoningPolicyUpdateTypeAnnotation = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyUpdateTypeAnnotation.name required"
        )
    if data.get("newName") is not None:
        out["new_name"] = data["newName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("values") is not None:
        import capo_bedrock.types.automated_reasoning_policy_type_value_annotation_list

        out["values"] = (
            capo_bedrock.types.automated_reasoning_policy_type_value_annotation_list.deserialize_json(
                data["values"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyUpdateTypeAnnotation.values required"
        )
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyUpdateTypeAnnotation,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "new_name" in value:
        out["new_name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "values" in value:
        import capo_bedrock.types.automated_reasoning_policy_type_value_annotation_list

        out["values"] = (
            capo_bedrock.types.automated_reasoning_policy_type_value_annotation_list.redact_sensitive(
                value["values"]
            )
        )
    return out
