"""Generated from Smithy shape ``com.amazonaws.emr#JobFlowDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.boolean
    import capo_emr.types.bootstrap_action_detail_list
    import capo_emr.types.job_flow_execution_status_detail
    import capo_emr.types.job_flow_instances_detail
    import capo_emr.types.scale_down_behavior
    import capo_emr.types.step_detail_list
    import capo_emr.types.supported_products_list
    import capo_emr.types.xml_string
    import capo_emr.types.xml_string_max_len256


class JobFlowDetail(TypedDict, closed=True):
    job_flow_id: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The job flow identifier.</p>"""
    name: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The name of the job flow.</p>"""
    log_uri: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The location in Amazon S3 where log files for the job are stored.</p>"""
    log_encryption_kms_key_id: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The KMS key used for encrypting log files. This attribute is only available with Amazon EMR 5.30.0 and later, excluding 6.0.0.</p>"""
    ami_version: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>Applies only to Amazon EMR AMI versions 3.x and 2.x. For Amazon EMR releases 4.0 and later, <code>ReleaseLabel</code> is used. To specify a custom AMI, use <code>CustomAmiID</code>.</p>"""
    execution_status_detail: NotRequired[
        "capo_emr.types.job_flow_execution_status_detail.JobFlowExecutionStatusDetail"
    ]
    """<p>Describes the execution status of the job flow.</p>"""
    instances: NotRequired[
        "capo_emr.types.job_flow_instances_detail.JobFlowInstancesDetail"
    ]
    """<p>Describes the Amazon EC2 instances of the job flow.</p>"""
    steps: NotRequired["capo_emr.types.step_detail_list.StepDetailList"]
    """<p>A list of steps run by the job flow.</p>"""
    bootstrap_actions: NotRequired[
        "capo_emr.types.bootstrap_action_detail_list.BootstrapActionDetailList"
    ]
    """<p>A list of the bootstrap actions run by the job flow.</p>"""
    supported_products: NotRequired[
        "capo_emr.types.supported_products_list.SupportedProductsList"
    ]
    """<p>A list of strings set by third-party software when the job flow is launched. If you are not using third-party software to manage the job flow, this value is empty.</p>"""
    visible_to_all_users: NotRequired["capo_emr.types.boolean.Boolean"]
    """<p>Indicates whether the cluster is visible to IAM principals in the Amazon Web Services account associated with the cluster. When <code>true</code>, IAM principals in the Amazon Web Services account can perform Amazon EMR cluster actions that their IAM policies allow. When <code>false</code>, only the IAM principal that created the cluster and the Amazon Web Services account root user can perform Amazon EMR actions, regardless of IAM permissions policies attached to other IAM principals.</p> <p>The default value is <code>true</code> if a value is not provided when creating a cluster using the Amazon EMR API <a>RunJobFlow</a> command, the CLI <a href="https://docs.aws.amazon.com/cli/latest/reference/emr/create-cluster.html">create-cluster</a> command, or the Amazon Web Services Management Console.</p>"""
    job_flow_role: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The IAM role that was specified when the job flow was launched. The Amazon EC2 instances of the job flow assume this role.</p>"""
    service_role: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The IAM role that is assumed by the Amazon EMR service to access Amazon Web Services resources on your behalf.</p>"""
    auto_scaling_role: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>An IAM role for automatic scaling policies. The default role is <code>EMR_AutoScaling_DefaultRole</code>. The IAM role provides a way for the automatic scaling feature to get the required permissions it needs to launch and terminate Amazon EC2 instances in an instance group.</p>"""
    scale_down_behavior: NotRequired[
        "capo_emr.types.scale_down_behavior.ScaleDownBehavior"
    ]
    """<p>The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an instance group is resized. <code>TERMINATE_AT_INSTANCE_HOUR</code> indicates that Amazon EMR terminates nodes at the instance-hour boundary, regardless of when the request to terminate the instance was submitted. This option is only available with Amazon EMR 5.1.0 and later and is the default for clusters created using that version. <code>TERMINATE_AT_TASK_COMPLETION</code> indicates that Amazon EMR adds nodes to a deny list and drains tasks from nodes before terminating the Amazon EC2 instances, regardless of the instance-hour boundary. With either behavior, Amazon EMR removes the least active nodes first and blocks instance termination if it could lead to HDFS corruption. <code>TERMINATE_AT_TASK_COMPLETION</code> available only in Amazon EMR releases 4.1.0 and later, and is the default for releases of Amazon EMR earlier than 5.1.0.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobFlowDetail) -> dict:
    out: dict = {}
    if "job_flow_id" in value:
        out["JobFlowId"] = value["job_flow_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "log_uri" in value:
        out["LogUri"] = value["log_uri"]
    if "log_encryption_kms_key_id" in value:
        out["LogEncryptionKmsKeyId"] = value["log_encryption_kms_key_id"]
    if "ami_version" in value:
        out["AmiVersion"] = value["ami_version"]
    if "execution_status_detail" in value:
        import capo_emr.types.job_flow_execution_status_detail

        out["ExecutionStatusDetail"] = (
            capo_emr.types.job_flow_execution_status_detail.serialize_aws_json_1_1(
                value["execution_status_detail"]
            )
        )
    if "instances" in value:
        import capo_emr.types.job_flow_instances_detail

        out["Instances"] = (
            capo_emr.types.job_flow_instances_detail.serialize_aws_json_1_1(
                value["instances"]
            )
        )
    if "steps" in value:
        import capo_emr.types.step_detail_list

        out["Steps"] = capo_emr.types.step_detail_list.serialize_aws_json_1_1(
            value["steps"]
        )
    if "bootstrap_actions" in value:
        import capo_emr.types.bootstrap_action_detail_list

        out["BootstrapActions"] = (
            capo_emr.types.bootstrap_action_detail_list.serialize_aws_json_1_1(
                value["bootstrap_actions"]
            )
        )
    if "supported_products" in value:
        import capo_emr.types.supported_products_list

        out["SupportedProducts"] = (
            capo_emr.types.supported_products_list.serialize_aws_json_1_1(
                value["supported_products"]
            )
        )
    if "visible_to_all_users" in value:
        out["VisibleToAllUsers"] = value["visible_to_all_users"]
    if "job_flow_role" in value:
        out["JobFlowRole"] = value["job_flow_role"]
    if "service_role" in value:
        out["ServiceRole"] = value["service_role"]
    if "auto_scaling_role" in value:
        out["AutoScalingRole"] = value["auto_scaling_role"]
    if "scale_down_behavior" in value:
        import capo_emr.types.scale_down_behavior

        out["ScaleDownBehavior"] = (
            capo_emr.types.scale_down_behavior.serialize_aws_json_1_1(
                value["scale_down_behavior"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> JobFlowDetail:
    out: JobFlowDetail = {}  # type: ignore[typeddict-item]
    if data.get("JobFlowId") is not None:
        out["job_flow_id"] = data["JobFlowId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("LogUri") is not None:
        out["log_uri"] = data["LogUri"]
    if data.get("LogEncryptionKmsKeyId") is not None:
        out["log_encryption_kms_key_id"] = data["LogEncryptionKmsKeyId"]
    if data.get("AmiVersion") is not None:
        out["ami_version"] = data["AmiVersion"]
    if data.get("ExecutionStatusDetail") is not None:
        import capo_emr.types.job_flow_execution_status_detail

        out["execution_status_detail"] = (
            capo_emr.types.job_flow_execution_status_detail.deserialize_aws_json_1_1(
                data["ExecutionStatusDetail"]
            )
        )
    if data.get("Instances") is not None:
        import capo_emr.types.job_flow_instances_detail

        out["instances"] = (
            capo_emr.types.job_flow_instances_detail.deserialize_aws_json_1_1(
                data["Instances"]
            )
        )
    if data.get("Steps") is not None:
        import capo_emr.types.step_detail_list

        out["steps"] = capo_emr.types.step_detail_list.deserialize_aws_json_1_1(
            data["Steps"]
        )
    if data.get("BootstrapActions") is not None:
        import capo_emr.types.bootstrap_action_detail_list

        out["bootstrap_actions"] = (
            capo_emr.types.bootstrap_action_detail_list.deserialize_aws_json_1_1(
                data["BootstrapActions"]
            )
        )
    if data.get("SupportedProducts") is not None:
        import capo_emr.types.supported_products_list

        out["supported_products"] = (
            capo_emr.types.supported_products_list.deserialize_aws_json_1_1(
                data["SupportedProducts"]
            )
        )
    if data.get("VisibleToAllUsers") is not None:
        out["visible_to_all_users"] = data["VisibleToAllUsers"]
    if data.get("JobFlowRole") is not None:
        out["job_flow_role"] = data["JobFlowRole"]
    if data.get("ServiceRole") is not None:
        out["service_role"] = data["ServiceRole"]
    if data.get("AutoScalingRole") is not None:
        out["auto_scaling_role"] = data["AutoScalingRole"]
    if data.get("ScaleDownBehavior") is not None:
        import capo_emr.types.scale_down_behavior

        out["scale_down_behavior"] = (
            capo_emr.types.scale_down_behavior.deserialize_aws_json_1_1(
                data["ScaleDownBehavior"]
            )
        )
    return out
