"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAddTypeAnnotation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_type_description
    import capo_bedrock.types.automated_reasoning_policy_definition_type_name
    import capo_bedrock.types.automated_reasoning_policy_definition_type_value_list


class AutomatedReasoningPolicyAddTypeAnnotation(TypedDict, closed=True):
    name: "capo_bedrock.types.automated_reasoning_policy_definition_type_name.AutomatedReasoningPolicyDefinitionTypeName"
    """<p>The name of the new custom type. This name will be used to reference the type in variable definitions and rules.</p>"""
    description: "capo_bedrock.types.automated_reasoning_policy_definition_type_description.AutomatedReasoningPolicyDefinitionTypeDescription"
    """<p>A description of what the custom type represents and how it should be used in the policy.</p>"""
    values: "capo_bedrock.types.automated_reasoning_policy_definition_type_value_list.AutomatedReasoningPolicyDefinitionTypeValueList"
    """<p>The list of possible values that variables of this type can take, each with its own description and identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAddTypeAnnotation) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["description"] = value["description"]
    import capo_bedrock.types.automated_reasoning_policy_definition_type_value_list

    out["values"] = (
        capo_bedrock.types.automated_reasoning_policy_definition_type_value_list.serialize_json(
            value["values"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyAddTypeAnnotation:
    out: AutomatedReasoningPolicyAddTypeAnnotation = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("values") is not None:
        import capo_bedrock.types.automated_reasoning_policy_definition_type_value_list

        out["values"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_type_value_list.deserialize_json(
                data["values"]
            )
        )
    else:
        out["values"] = []
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyAddTypeAnnotation,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "values" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_type_value_list

        out["values"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_type_value_list.redact_sensitive(
                value["values"]
            )
        )
    return out
