"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleConfigurationProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.boolean
    import capo_codepipeline.types.description
    import capo_codepipeline.types.rule_configuration_key
    import capo_codepipeline.types.rule_configuration_property_type


class RuleConfigurationProperty(TypedDict, closed=True):
    name: "capo_codepipeline.types.rule_configuration_key.RuleConfigurationKey"
    """<p>The name of the rule configuration property.</p>"""
    required: "capo_codepipeline.types.boolean.Boolean"
    """<p>Whether the configuration property is a required value.</p>"""
    key: "capo_codepipeline.types.boolean.Boolean"
    """<p>Whether the configuration property is a key.</p>"""
    secret: "capo_codepipeline.types.boolean.Boolean"
    """<p>Whether the configuration property is secret.</p> <p>When updating a pipeline, passing * * * * * without changing any other values of the action preserves the previous value of the secret.</p>"""
    queryable: "capo_codepipeline.types.boolean.Boolean"
    """<p>Indicates whether the property can be queried.</p> <p>If you create a pipeline with a condition and rule, and that rule contains a queryable property, the value for that configuration property is subject to other restrictions. The value must be less than or equal to twenty (20) characters. The value can contain only alphanumeric characters, underscores, and hyphens.</p>"""
    description: NotRequired["capo_codepipeline.types.description.Description"]
    """<p>The description of the action configuration property that is displayed to users.</p>"""
    type: NotRequired[
        "capo_codepipeline.types.rule_configuration_property_type.RuleConfigurationPropertyType"
    ]
    """<p>The type of the configuration property.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleConfigurationProperty) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["required"] = value.get("required", False)
    out["key"] = value.get("key", False)
    out["secret"] = value.get("secret", False)
    out["queryable"] = value.get("queryable", False)
    if "description" in value:
        out["description"] = value["description"]
    if "type" in value:
        import capo_codepipeline.types.rule_configuration_property_type

        out["type"] = (
            capo_codepipeline.types.rule_configuration_property_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleConfigurationProperty:
    out: RuleConfigurationProperty = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("required") is not None:
        out["required"] = data["required"]
    else:
        out["required"] = False
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = False
    if data.get("secret") is not None:
        out["secret"] = data["secret"]
    else:
        out["secret"] = False
    if data.get("queryable") is not None:
        out["queryable"] = data["queryable"]
    else:
        out["queryable"] = False
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("type") is not None:
        import capo_codepipeline.types.rule_configuration_property_type

        out["type"] = (
            capo_codepipeline.types.rule_configuration_property_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    return out
