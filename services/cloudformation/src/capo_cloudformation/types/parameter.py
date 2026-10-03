"""Generated from Smithy shape ``com.amazonaws.cloudformation#Parameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.parameter_key
    import capo_cloudformation.types.parameter_value
    import capo_cloudformation.types.use_previous_value


class Parameter(TypedDict, closed=True):
    parameter_key: NotRequired["capo_cloudformation.types.parameter_key.ParameterKey"]
    """<p>The key associated with the parameter. If you don't specify a key and value for a particular parameter, CloudFormation uses the default value that's specified in your template.</p>"""
    parameter_value: NotRequired[
        "capo_cloudformation.types.parameter_value.ParameterValue"
    ]
    """<p>The input value associated with the parameter.</p>"""
    use_previous_value: NotRequired[
        "capo_cloudformation.types.use_previous_value.UsePreviousValue"
    ]
    """<p>During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify <code>true</code>, do not specify a parameter value.</p>"""
    resolved_value: NotRequired[
        "capo_cloudformation.types.parameter_value.ParameterValue"
    ]
    """<p>Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for Systems Manager parameter types in the template. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-supplied-parameter-types.html">Specify existing resources at runtime with CloudFormation-supplied parameter types</a> in the <i>CloudFormation User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: Parameter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "parameter_key" in value:
        pairs.append((f"{key_prefix}ParameterKey", str(value["parameter_key"])))
    if "parameter_value" in value:
        pairs.append((f"{key_prefix}ParameterValue", str(value["parameter_value"])))
    if "use_previous_value" in value:
        pairs.append(
            (
                f"{key_prefix}UsePreviousValue",
                "true" if value["use_previous_value"] else "false",
            )
        )
    if "resolved_value" in value:
        pairs.append((f"{key_prefix}ResolvedValue", str(value["resolved_value"])))


def deserialize_query(el: Element) -> Parameter:
    out: Parameter = {}  # type: ignore[typeddict-item]
    child_parameter_key = el.find("ParameterKey")
    if child_parameter_key is not None:
        out["parameter_key"] = str(child_parameter_key.text or "")
    child_parameter_value = el.find("ParameterValue")
    if child_parameter_value is not None:
        out["parameter_value"] = str(child_parameter_value.text or "")
    child_use_previous_value = el.find("UsePreviousValue")
    if child_use_previous_value is not None:
        out["use_previous_value"] = (
            child_use_previous_value.text or ""
        ).lower() == "true"
    child_resolved_value = el.find("ResolvedValue")
    if child_resolved_value is not None:
        out["resolved_value"] = str(child_resolved_value.text or "")
    return out
