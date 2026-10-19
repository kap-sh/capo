"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#TemplateVariableMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.template_variable_source
    import capo_pinpoint_sms_voice_v2.types.template_variable_type


class TemplateVariableMetadata(TypedDict, closed=True):
    type: "capo_pinpoint_sms_voice_v2.types.template_variable_type.TemplateVariableType"
    """<p>The type of the variable.</p>"""
    required: "bool"
    """<p>Whether the variable is required.</p>"""
    description: NotRequired["str"]
    """<p>A description of the variable.</p>"""
    max_length: NotRequired["int"]
    """<p>The maximum length for string variables.</p>"""
    min_value: NotRequired["int"]
    """<p>The minimum value for numeric variables.</p>"""
    max_value: NotRequired["int"]
    """<p>The maximum value for numeric variables.</p>"""
    default_value: NotRequired["str"]
    """<p>The default value for the variable.</p>"""
    pattern: NotRequired["str"]
    """<p>The regex pattern the variable value must match.</p>"""
    sample: NotRequired["str"]
    """<p>A sample value for the variable.</p>"""
    source: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.template_variable_source.TemplateVariableSource"
    ]
    """<p>The source of the variable, either <code>CUSTOMER</code> or <code>SYSTEM</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TemplateVariableMetadata) -> dict:
    out: dict = {}
    out["Type"] = value["type"]
    out["Required"] = value.get("required", False)
    if "description" in value:
        out["Description"] = value["description"]
    if "max_length" in value:
        out["MaxLength"] = value["max_length"]
    if "min_value" in value:
        out["MinValue"] = value["min_value"]
    if "max_value" in value:
        out["MaxValue"] = value["max_value"]
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    if "pattern" in value:
        out["Pattern"] = value["pattern"]
    if "sample" in value:
        out["Sample"] = value["sample"]
    if "source" in value:
        out["Source"] = value["source"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TemplateVariableMetadata:
    out: TemplateVariableMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    else:
        out["type"] = ""
    if data.get("Required") is not None:
        out["required"] = data["Required"]
    else:
        out["required"] = False
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("MaxLength") is not None:
        out["max_length"] = data["MaxLength"]
    if data.get("MinValue") is not None:
        out["min_value"] = data["MinValue"]
    if data.get("MaxValue") is not None:
        out["max_value"] = data["MaxValue"]
    if data.get("DefaultValue") is not None:
        out["default_value"] = data["DefaultValue"]
    if data.get("Pattern") is not None:
        out["pattern"] = data["Pattern"]
    if data.get("Sample") is not None:
        out["sample"] = data["Sample"]
    if data.get("Source") is not None:
        out["source"] = data["Source"]
    return out
