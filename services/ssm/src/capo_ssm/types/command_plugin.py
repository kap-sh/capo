"""Generated from Smithy shape ``com.amazonaws.ssm#CommandPlugin``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.command_plugin_name
    import capo_ssm.types.command_plugin_output
    import capo_ssm.types.command_plugin_status
    import capo_ssm.types.date_time
    import capo_ssm.types.response_code
    import capo_ssm.types.s3_bucket_name
    import capo_ssm.types.s3_key_prefix
    import capo_ssm.types.s3_region
    import capo_ssm.types.status_details
    import capo_ssm.types.url


class CommandPlugin(TypedDict, closed=True):
    name: NotRequired["capo_ssm.types.command_plugin_name.CommandPluginName"]
    """<p>The name of the plugin. Must be one of the following: <code>aws:updateAgent</code>, <code>aws:domainjoin</code>, <code>aws:applications</code>, <code>aws:runPowerShellScript</code>, <code>aws:psmodule</code>, <code>aws:cloudWatch</code>, <code>aws:runShellScript</code>, or <code>aws:updateSSMAgent</code>. </p>"""
    status: NotRequired["capo_ssm.types.command_plugin_status.CommandPluginStatus"]
    """<p>The status of this plugin. You can run a document with multiple plugins.</p>"""
    status_details: NotRequired["capo_ssm.types.status_details.StatusDetails"]
    """<p>A detailed status of the plugin execution. <code>StatusDetails</code> includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html">Understanding command statuses</a> in the <i>Amazon Web Services Systems Manager User Guide</i>. StatusDetails can be one of the following values:</p> <ul> <li> <p>Pending: The command hasn't been sent to the managed node.</p> </li> <li> <p>In Progress: The command has been sent to the managed node but hasn't reached a terminal state.</p> </li> <li> <p>Success: The execution of the command or plugin was successfully completed. This is a terminal state.</p> </li> <li> <p>Delivery Timed Out: The command wasn't delivered to the managed node before the delivery timeout expired. Delivery timeouts don't count against the parent command's <code>MaxErrors</code> limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state.</p> </li> <li> <p>Execution Timed Out: Command execution started on the managed node, but the execution wasn't complete before the execution timeout expired. Execution timeouts count against the <code>MaxErrors</code> limit of the parent command. This is a terminal state.</p> </li> <li> <p>Failed: The command wasn't successful on the managed node. For a plugin, this indicates that the result code wasn't zero. For a command invocation, this indicates that the result code for one or more plugins wasn't zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state.</p> </li> <li> <p>Cancelled: The command was terminated before it was completed. This is a terminal state.</p> </li> <li> <p>Undeliverable: The command can't be delivered to the managed node. The managed node might not exist, or it might not be responding. Undeliverable invocations don't count against the parent command's MaxErrors limit, and they don't contribute to whether the parent command status is Success or Incomplete. This is a terminal state.</p> </li> <li> <p>Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state.</p> </li> </ul>"""
    response_code: "capo_ssm.types.response_code.ResponseCode"
    """<p>A numeric response code generated after running the plugin. </p>"""
    response_start_date_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time the plugin started running. </p>"""
    response_finish_date_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time the plugin stopped running. Could stop prematurely if, for example, a cancel command was sent. </p>"""
    output: NotRequired["capo_ssm.types.command_plugin_output.CommandPluginOutput"]
    """<p>Output of the plugin execution.</p>"""
    standard_output_url: NotRequired["capo_ssm.types.url.Url"]
    """<p>The URL for the complete text written by the plugin to stdout in Amazon S3. If the S3 bucket for the command wasn't specified, then this string is empty.</p>"""
    standard_error_url: NotRequired["capo_ssm.types.url.Url"]
    """<p>The URL for the complete text written by the plugin to stderr. If execution isn't yet complete, then this string is empty.</p>"""
    output_s3_region: NotRequired["capo_ssm.types.s3_region.S3Region"]
    """<p>(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Amazon Web Services Systems Manager automatically determines the S3 bucket region.</p>"""
    output_s3_bucket_name: NotRequired["capo_ssm.types.s3_bucket_name.S3BucketName"]
    """<p>The S3 bucket where the responses to the command executions should be stored. This was requested when issuing the command. For example, in the following response:</p> <p> <code>amzn-s3-demo-bucket/my-prefix/i-02573cafcfEXAMPLE/awsrunShellScript</code> </p> <p> <code>amzn-s3-demo-bucket</code> is the name of the S3 bucket;</p> <p> <code>my-prefix</code> is the name of the S3 prefix;</p> <p> <code>i-02573cafcfEXAMPLE</code> is the managed node ID;</p> <p> <code>awsrunShellScript</code> is the name of the plugin.</p>"""
    output_s3_key_prefix: NotRequired["capo_ssm.types.s3_key_prefix.S3KeyPrefix"]
    """<p>The S3 directory path inside the bucket where the responses to the command executions should be stored. This was requested when issuing the command. For example, in the following response:</p> <p> <code>amzn-s3-demo-bucket/my-prefix/i-02573cafcfEXAMPLE/awsrunShellScript</code> </p> <p> <code>amzn-s3-demo-bucket</code> is the name of the S3 bucket;</p> <p> <code>my-prefix</code> is the name of the S3 prefix;</p> <p> <code>i-02573cafcfEXAMPLE</code> is the managed node ID;</p> <p> <code>awsrunShellScript</code> is the name of the plugin.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommandPlugin) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_ssm.types.command_plugin_status

        out["Status"] = capo_ssm.types.command_plugin_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_details" in value:
        out["StatusDetails"] = value["status_details"]
    out["ResponseCode"] = value.get("response_code", 0)
    if "response_start_date_time" in value:
        import capo_ssm.types.date_time

        out["ResponseStartDateTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["response_start_date_time"]
        )
    if "response_finish_date_time" in value:
        import capo_ssm.types.date_time

        out["ResponseFinishDateTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["response_finish_date_time"]
        )
    if "output" in value:
        out["Output"] = value["output"]
    if "standard_output_url" in value:
        out["StandardOutputUrl"] = value["standard_output_url"]
    if "standard_error_url" in value:
        out["StandardErrorUrl"] = value["standard_error_url"]
    if "output_s3_region" in value:
        out["OutputS3Region"] = value["output_s3_region"]
    if "output_s3_bucket_name" in value:
        out["OutputS3BucketName"] = value["output_s3_bucket_name"]
    if "output_s3_key_prefix" in value:
        out["OutputS3KeyPrefix"] = value["output_s3_key_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CommandPlugin:
    out: CommandPlugin = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        import capo_ssm.types.command_plugin_status

        out["status"] = capo_ssm.types.command_plugin_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("StatusDetails") is not None:
        out["status_details"] = data["StatusDetails"]
    if data.get("ResponseCode") is not None:
        out["response_code"] = data["ResponseCode"]
    else:
        out["response_code"] = 0
    if data.get("ResponseStartDateTime") is not None:
        import capo_ssm.types.date_time

        out["response_start_date_time"] = (
            capo_ssm.types.date_time.deserialize_aws_json_1_1(
                data["ResponseStartDateTime"]
            )
        )
    if data.get("ResponseFinishDateTime") is not None:
        import capo_ssm.types.date_time

        out["response_finish_date_time"] = (
            capo_ssm.types.date_time.deserialize_aws_json_1_1(
                data["ResponseFinishDateTime"]
            )
        )
    if data.get("Output") is not None:
        out["output"] = data["Output"]
    if data.get("StandardOutputUrl") is not None:
        out["standard_output_url"] = data["StandardOutputUrl"]
    if data.get("StandardErrorUrl") is not None:
        out["standard_error_url"] = data["StandardErrorUrl"]
    if data.get("OutputS3Region") is not None:
        out["output_s3_region"] = data["OutputS3Region"]
    if data.get("OutputS3BucketName") is not None:
        out["output_s3_bucket_name"] = data["OutputS3BucketName"]
    if data.get("OutputS3KeyPrefix") is not None:
        out["output_s3_key_prefix"] = data["OutputS3KeyPrefix"]
    return out
