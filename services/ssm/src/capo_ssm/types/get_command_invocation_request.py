"""Generated from Smithy shape ``com.amazonaws.ssm#GetCommandInvocationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.command_id
    import capo_ssm.types.command_plugin_name
    import capo_ssm.types.instance_id


class GetCommandInvocationRequest(TypedDict, closed=True):
    command_id: "capo_ssm.types.command_id.CommandId"
    """<p>(Required) The parent command ID of the invocation plugin.</p>"""
    instance_id: "capo_ssm.types.instance_id.InstanceId"
    """<p>(Required) The ID of the managed node targeted by the command. A <i>managed node</i> can be an Amazon Elastic Compute Cloud (Amazon EC2) instance, edge device, and on-premises server or VM in your hybrid environment that is configured for Amazon Web Services Systems Manager.</p>"""
    plugin_name: NotRequired["capo_ssm.types.command_plugin_name.CommandPluginName"]
    """<p>The name of the step for which you want detailed results. If the document contains only one step, you can omit the name and details for that step. If the document contains more than one step, you must specify the name of the step for which you want to view details. Be sure to specify the name of the step, not the name of a plugin like <code>aws:RunShellScript</code>.</p> <p>To find the <code>PluginName</code>, check the document content and find the name of the step you want details for. Alternatively, use <a>ListCommandInvocations</a> with the <code>CommandId</code> and <code>Details</code> parameters. The <code>PluginName</code> is the <code>Name</code> attribute of the <code>CommandPlugin</code> object in the <code>CommandPlugins</code> list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCommandInvocationRequest) -> dict:
    out: dict = {}
    out["CommandId"] = value["command_id"]
    out["InstanceId"] = value["instance_id"]
    if "plugin_name" in value:
        out["PluginName"] = value["plugin_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCommandInvocationRequest:
    out: GetCommandInvocationRequest = {}  # type: ignore[typeddict-item]
    if data.get("CommandId") is not None:
        out["command_id"] = data["CommandId"]
    else:
        out["command_id"] = ""
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        out["instance_id"] = ""
    if data.get("PluginName") is not None:
        out["plugin_name"] = data["PluginName"]
    return out
