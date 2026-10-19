"""Generated from Smithy shape ``com.amazonaws.ssm#GetParametersByPathRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.boolean
    import capo_ssm.types.get_parameters_by_path_max_results
    import capo_ssm.types.next_token
    import capo_ssm.types.parameter_string_filter_list
    import capo_ssm.types.ps_parameter_name


class GetParametersByPathRequest(TypedDict, closed=True):
    path: "capo_ssm.types.ps_parameter_name.PSParameterName"
    """<p>The hierarchy for the parameter. Hierarchies start with a forward slash (/). The hierarchy is the parameter name except the last part of the parameter. For the API call to succeed, the last part of the parameter name can't be in the path. A parameter name hierarchy can have a maximum of 15 levels. Here is an example of a hierarchy: <code>/Finance/Prod/IAD/WinServ2016/license33 </code> </p>"""
    recursive: NotRequired["capo_ssm.types.boolean.Boolean"]
    """<p>Retrieve all parameters within a hierarchy.</p> <important> <p>If a user has access to a path, then the user can access all levels of that path. For example, if a user has permission to access path <code>/a</code>, then the user can also access <code>/a/b</code>. Even if a user has explicitly been denied access in IAM for parameter <code>/a/b</code>, they can still call the GetParametersByPath API operation recursively for <code>/a</code> and view <code>/a/b</code>.</p> </important>"""
    parameter_filters: NotRequired[
        "capo_ssm.types.parameter_string_filter_list.ParameterStringFilterList"
    ]
    """<p>Filters to limit the request results.</p> <note> <p>The following <code>Key</code> values are supported for <code>GetParametersByPath</code>: <code>Type</code>, <code>KeyId</code>, and <code>Label</code>.</p> <p>The following <code>Key</code> values aren't supported for <code>GetParametersByPath</code>: <code>tag</code>, <code>DataType</code>, <code>Name</code>, <code>Path</code>, and <code>Tier</code>.</p> </note>"""
    with_decryption: NotRequired["capo_ssm.types.boolean.Boolean"]
    """<p>Retrieve all parameters in a hierarchy with their value decrypted.</p>"""
    max_results: NotRequired[
        "capo_ssm.types.get_parameters_by_path_max_results.GetParametersByPathMaxResults"
    ]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>A token to start the list. Use this token to get the next set of results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetParametersByPathRequest) -> dict:
    out: dict = {}
    out["Path"] = value["path"]
    if "recursive" in value:
        out["Recursive"] = value["recursive"]
    if "parameter_filters" in value:
        import capo_ssm.types.parameter_string_filter_list

        out["ParameterFilters"] = (
            capo_ssm.types.parameter_string_filter_list.serialize_aws_json_1_1(
                value["parameter_filters"]
            )
        )
    if "with_decryption" in value:
        out["WithDecryption"] = value["with_decryption"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetParametersByPathRequest:
    out: GetParametersByPathRequest = {}  # type: ignore[typeddict-item]
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    else:
        out["path"] = ""
    if data.get("Recursive") is not None:
        out["recursive"] = data["Recursive"]
    if data.get("ParameterFilters") is not None:
        import capo_ssm.types.parameter_string_filter_list

        out["parameter_filters"] = (
            capo_ssm.types.parameter_string_filter_list.deserialize_aws_json_1_1(
                data["ParameterFilters"]
            )
        )
    if data.get("WithDecryption") is not None:
        out["with_decryption"] = data["WithDecryption"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
