"""Generated from Smithy shape ``com.amazonaws.ssm#ParameterStringFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.parameter_string_filter_key
    import capo_ssm.types.parameter_string_filter_value_list
    import capo_ssm.types.parameter_string_query_option


class ParameterStringFilter(TypedDict, closed=True):
    key: "capo_ssm.types.parameter_string_filter_key.ParameterStringFilterKey"
    """<p>The name of the filter.</p> <p>The <code>ParameterStringFilter</code> object is used by the <a>DescribeParameters</a> and <a>GetParametersByPath</a> API operations. However, not all of the pattern values listed for <code>Key</code> can be used with both operations.</p> <p>For <code>DescribeParameters</code>, all of the listed patterns are valid except <code>Label</code>.</p> <p>For <code>GetParametersByPath</code>, the following patterns listed for <code>Key</code> aren't valid: <code>tag</code>, <code>DataType</code>, <code>Name</code>, <code>Path</code>, and <code>Tier</code>.</p> <p>For examples of Amazon Web Services CLI commands demonstrating valid parameter filter constructions, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-search.html">Searching for Systems Manager parameters</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    option: NotRequired[
        "capo_ssm.types.parameter_string_query_option.ParameterStringQueryOption"
    ]
    """<p>For all filters used with <a>DescribeParameters</a>, valid options include <code>Equals</code> and <code>BeginsWith</code>. The <code>Name</code> filter additionally supports the <code>Contains</code> option. (Exception: For filters using the key <code>Path</code>, valid options include <code>Recursive</code> and <code>OneLevel</code>.)</p> <p>For filters used with <a>GetParametersByPath</a>, valid options include <code>Equals</code> and <code>BeginsWith</code>. (Exception: For filters using <code>Label</code> as the Key name, the only valid option is <code>Equals</code>.)</p>"""
    values: NotRequired[
        "capo_ssm.types.parameter_string_filter_value_list.ParameterStringFilterValueList"
    ]
    """<p>The value you want to search for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterStringFilter) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    if "option" in value:
        out["Option"] = value["option"]
    if "values" in value:
        import capo_ssm.types.parameter_string_filter_value_list

        out["Values"] = (
            capo_ssm.types.parameter_string_filter_value_list.serialize_aws_json_1_1(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterStringFilter:
    out: ParameterStringFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("ParameterStringFilter.key required")
    if data.get("Option") is not None:
        out["option"] = data["Option"]
    if data.get("Values") is not None:
        import capo_ssm.types.parameter_string_filter_value_list

        out["values"] = (
            capo_ssm.types.parameter_string_filter_value_list.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    return out
