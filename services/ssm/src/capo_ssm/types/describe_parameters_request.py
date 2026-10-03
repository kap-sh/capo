"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeParametersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.boolean
    import capo_ssm.types.max_results
    import capo_ssm.types.next_token
    import capo_ssm.types.parameter_string_filter_list
    import capo_ssm.types.parameters_filter_list


class DescribeParametersRequest(TypedDict, closed=True):
    filters: NotRequired["capo_ssm.types.parameters_filter_list.ParametersFilterList"]
    """<p>This data type is deprecated. Instead, use <code>ParameterFilters</code>.</p>"""
    parameter_filters: NotRequired[
        "capo_ssm.types.parameter_string_filter_list.ParameterStringFilterList"
    ]
    """<p>Filters to limit the request results.</p>"""
    max_results: NotRequired["capo_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    shared: NotRequired["capo_ssm.types.boolean.Boolean"]
    """<p>Lists parameters that are shared with you.</p> <note> <p>By default when using this option, the command returns parameters that have been shared using a standard Resource Access Manager Resource Share. In order for a parameter that was shared using the <a>PutResourcePolicy</a> command to be returned, the associated <code>RAM Resource Share Created From Policy</code> must have been promoted to a standard Resource Share using the RAM <a href="https://docs.aws.amazon.com/ram/latest/APIReference/API_PromoteResourceShareCreatedFromPolicy.html">PromoteResourceShareCreatedFromPolicy</a> API operation.</p> <p>For more information about sharing parameters, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-shared-parameters.html">Working with shared parameters</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeParametersRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_ssm.types.parameters_filter_list

        out["Filters"] = capo_ssm.types.parameters_filter_list.serialize_aws_json_1_1(
            value["filters"]
        )
    if "parameter_filters" in value:
        import capo_ssm.types.parameter_string_filter_list

        out["ParameterFilters"] = (
            capo_ssm.types.parameter_string_filter_list.serialize_aws_json_1_1(
                value["parameter_filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "shared" in value:
        out["Shared"] = value["shared"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeParametersRequest:
    out: DescribeParametersRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_ssm.types.parameters_filter_list

        out["filters"] = capo_ssm.types.parameters_filter_list.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if data.get("ParameterFilters") is not None:
        import capo_ssm.types.parameter_string_filter_list

        out["parameter_filters"] = (
            capo_ssm.types.parameter_string_filter_list.deserialize_aws_json_1_1(
                data["ParameterFilters"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Shared") is not None:
        out["shared"] = data["Shared"]
    return out
