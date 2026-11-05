"""Generated from Smithy shape ``com.amazonaws.emr#Step``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.action_on_failure
    import capo_emr.types.hadoop_step_config
    import capo_emr.types.optional_arn_type
    import capo_emr.types.step_additional_info
    import capo_emr.types.step_id
    import capo_emr.types.step_status
    import capo_emr.types.string


class Step(TypedDict, closed=True):
    id: NotRequired["capo_emr.types.step_id.StepId"]
    """<p>The identifier of the cluster step.</p>"""
    name: NotRequired["capo_emr.types.string.String"]
    """<p>The name of the cluster step.</p>"""
    config: NotRequired["capo_emr.types.hadoop_step_config.HadoopStepConfig"]
    """<p>The Hadoop job configuration of the cluster step.</p>"""
    action_on_failure: NotRequired["capo_emr.types.action_on_failure.ActionOnFailure"]
    """<p>The action to take when the cluster step fails. Possible values are <code>TERMINATE_CLUSTER</code>, <code>CANCEL_AND_WAIT</code>, and <code>CONTINUE</code>. <code>TERMINATE_JOB_FLOW</code> is provided for backward compatibility. We recommend using <code>TERMINATE_CLUSTER</code> instead.</p> <p>If a cluster's <code>StepConcurrencyLevel</code> is greater than <code>1</code>, do not use <code>AddJobFlowSteps</code> to submit a step with this parameter set to <code>CANCEL_AND_WAIT</code> or <code>TERMINATE_CLUSTER</code>. The step is not submitted and the action fails with a message that the <code>ActionOnFailure</code> setting is not valid.</p> <p>If you change a cluster's <code>StepConcurrencyLevel</code> to be greater than 1 while a step is running, the <code>ActionOnFailure</code> parameter may not behave as you expect. In this case, for a step that fails with this parameter set to <code>CANCEL_AND_WAIT</code>, pending steps and the running step are not canceled; for a step that fails with this parameter set to <code>TERMINATE_CLUSTER</code>, the cluster does not terminate.</p>"""
    status: NotRequired["capo_emr.types.step_status.StepStatus"]
    """<p>The current execution status details of the cluster step.</p>"""
    execution_role_arn: NotRequired["capo_emr.types.optional_arn_type.OptionalArnType"]
    """<p>The Amazon Resource Name (ARN) of the runtime role for a step on the cluster. The runtime role can be a cross-account IAM role. The runtime role ARN is a combination of account ID, role name, and role type using the following format: <code>arn:partition:service:region:account:resource</code>. </p> <p>For example, <code>arn:aws:IAM::1234567890:role/ReadOnly</code> is a correctly formatted runtime role ARN.</p>"""
    log_uri: NotRequired["capo_emr.types.string.String"]
    """<p>The Amazon S3 destination URI for log publishing.</p>"""
    encryption_key_arn: NotRequired["capo_emr.types.string.String"]
    """<p>The KMS key ARN to encrypt the logs published to the given Amazon S3 destination.</p>"""
    additional_info: NotRequired[
        "capo_emr.types.step_additional_info.StepAdditionalInfo"
    ]
    """<p>Additional information about the step, including the YARN application IDs associated with the step and the resource manager that processed it.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Step) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "config" in value:
        import capo_emr.types.hadoop_step_config

        out["Config"] = capo_emr.types.hadoop_step_config.serialize_aws_json_1_1(
            value["config"]
        )
    if "action_on_failure" in value:
        import capo_emr.types.action_on_failure

        out["ActionOnFailure"] = (
            capo_emr.types.action_on_failure.serialize_aws_json_1_1(
                value["action_on_failure"]
            )
        )
    if "status" in value:
        import capo_emr.types.step_status

        out["Status"] = capo_emr.types.step_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "log_uri" in value:
        out["LogUri"] = value["log_uri"]
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    if "additional_info" in value:
        import capo_emr.types.step_additional_info

        out["AdditionalInfo"] = (
            capo_emr.types.step_additional_info.serialize_aws_json_1_1(
                value["additional_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Step:
    out: Step = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Config") is not None:
        import capo_emr.types.hadoop_step_config

        out["config"] = capo_emr.types.hadoop_step_config.deserialize_aws_json_1_1(
            data["Config"]
        )
    if data.get("ActionOnFailure") is not None:
        import capo_emr.types.action_on_failure

        out["action_on_failure"] = (
            capo_emr.types.action_on_failure.deserialize_aws_json_1_1(
                data["ActionOnFailure"]
            )
        )
    if data.get("Status") is not None:
        import capo_emr.types.step_status

        out["status"] = capo_emr.types.step_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("ExecutionRoleArn") is not None:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    if data.get("LogUri") is not None:
        out["log_uri"] = data["LogUri"]
    if data.get("EncryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    if data.get("AdditionalInfo") is not None:
        import capo_emr.types.step_additional_info

        out["additional_info"] = (
            capo_emr.types.step_additional_info.deserialize_aws_json_1_1(
                data["AdditionalInfo"]
            )
        )
    return out
