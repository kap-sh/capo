"""Generated from Smithy shape ``com.amazonaws.ssm#ListCommandInvocationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.boolean
    import capo_ssm.types.command_filter_list
    import capo_ssm.types.command_id
    import capo_ssm.types.command_max_results
    import capo_ssm.types.instance_id
    import capo_ssm.types.next_token


class ListCommandInvocationsRequest(TypedDict, closed=True):
    command_id: NotRequired["capo_ssm.types.command_id.CommandId"]
    """<p>(Optional) The invocations for a specific command ID.</p>"""
    instance_id: NotRequired["capo_ssm.types.instance_id.InstanceId"]
    """<p>(Optional) The command execution details for a specific managed node ID.</p>"""
    max_results: NotRequired["capo_ssm.types.command_max_results.CommandMaxResults"]
    """<p>(Optional) The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>(Optional) The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    filters: NotRequired["capo_ssm.types.command_filter_list.CommandFilterList"]
    """<p>(Optional) One or more filters. Use a filter to return a more specific list of results.</p>"""
    details: NotRequired["capo_ssm.types.boolean.Boolean"]
    """<p>(Optional) If set this returns the response of the command executions and any command output. The default value is <code>false</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCommandInvocationsRequest) -> dict:
    out: dict = {}
    if "command_id" in value:
        out["CommandId"] = value["command_id"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import capo_ssm.types.command_filter_list

        out["Filters"] = capo_ssm.types.command_filter_list.serialize_aws_json_1_1(
            value["filters"]
        )
    if "details" in value:
        out["Details"] = value["details"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCommandInvocationsRequest:
    out: ListCommandInvocationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("CommandId") is not None:
        out["command_id"] = data["CommandId"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Filters") is not None:
        import capo_ssm.types.command_filter_list

        out["filters"] = capo_ssm.types.command_filter_list.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if data.get("Details") is not None:
        out["details"] = data["Details"]
    return out
