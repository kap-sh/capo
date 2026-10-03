"""Generated from Smithy shape ``com.amazonaws.iot#CreateJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.abort_config
    import capo_iot.types.destination_package_versions
    import capo_iot.types.job_description
    import capo_iot.types.job_document
    import capo_iot.types.job_document_source
    import capo_iot.types.job_executions_retry_config
    import capo_iot.types.job_executions_rollout_config
    import capo_iot.types.job_id
    import capo_iot.types.job_targets
    import capo_iot.types.job_template_arn
    import capo_iot.types.namespace_id
    import capo_iot.types.parameter_map
    import capo_iot.types.presigned_url_config
    import capo_iot.types.scheduling_config
    import capo_iot.types.tag_list
    import capo_iot.types.target_selection
    import capo_iot.types.timeout_config


class CreateJobRequest(TypedDict, closed=True):
    job_id: "capo_iot.types.job_id.JobId"
    """<p>A job identifier which must be unique for your account. We recommend using a UUID. Alpha-numeric characters, "-" and "_" are valid for use here.</p>"""
    targets: "capo_iot.types.job_targets.JobTargets"
    """<p>A list of things and thing groups to which the job should be sent.</p>"""
    document_source: NotRequired["capo_iot.types.job_document_source.JobDocumentSource"]
    """<p>An S3 link, or S3 object URL, to the job document. The link is an Amazon S3 object URL and is required if you don't specify a value for <code>document</code>.</p> <p>For example, <code>--document-source https://s3.<i>region-code</i>.amazonaws.com/example-firmware/device-firmware.1.0</code> </p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-bucket-intro.html">Methods for accessing a bucket</a>.</p>"""
    document: NotRequired["capo_iot.types.job_document.JobDocument"]
    """<p>The job document. Required if you don't specify a value for <code>documentSource</code>.</p>"""
    description: NotRequired["capo_iot.types.job_description.JobDescription"]
    """<p>A short text description of the job.</p>"""
    presigned_url_config: NotRequired[
        "capo_iot.types.presigned_url_config.PresignedUrlConfig"
    ]
    """<p>Configuration information for pre-signed S3 URLs.</p>"""
    target_selection: NotRequired["capo_iot.types.target_selection.TargetSelection"]
    """<p>Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a thing when the thing is added to a target group, even after the job was completed by all things originally in the group.</p> <note> <p>We recommend that you use continuous jobs instead of snapshot jobs for dynamic thing group targets. By using continuous jobs, devices that join the group receive the job execution even after the job has been created.</p> </note>"""
    job_executions_rollout_config: NotRequired[
        "capo_iot.types.job_executions_rollout_config.JobExecutionsRolloutConfig"
    ]
    """<p>Allows you to create a staged rollout of the job.</p>"""
    abort_config: NotRequired["capo_iot.types.abort_config.AbortConfig"]
    """<p>Allows you to create the criteria to abort a job.</p>"""
    timeout_config: NotRequired["capo_iot.types.timeout_config.TimeoutConfig"]
    """<p>Specifies the amount of time each device has to finish its execution of the job. The timer is started when the job execution status is set to <code>IN_PROGRESS</code>. If the job execution status is not set to another terminal state before the time expires, it will be automatically set to <code>TIMED_OUT</code>.</p>"""
    tags: NotRequired["capo_iot.types.tag_list.TagList"]
    """<p>Metadata which can be used to manage the job.</p>"""
    namespace_id: NotRequired["capo_iot.types.namespace_id.NamespaceId"]
    """<p>The namespace used to indicate that a job is a customer-managed job.</p> <p>When you specify a value for this parameter, Amazon Web Services IoT Core sends jobs notifications to MQTT topics that contain the value in the following format.</p> <p> <code>$aws/things/<i>THING_NAME</i>/jobs/<i>JOB_ID</i>/notify-namespace-<i>NAMESPACE_ID</i>/</code> </p> <note> <p>The <code>namespaceId</code> feature is only supported by IoT Greengrass at this time. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/setting-up.html">Setting up IoT Greengrass core devices.</a> </p> </note>"""
    job_template_arn: NotRequired["capo_iot.types.job_template_arn.JobTemplateArn"]
    """<p>The ARN of the job template used to create the job.</p>"""
    job_executions_retry_config: NotRequired[
        "capo_iot.types.job_executions_retry_config.JobExecutionsRetryConfig"
    ]
    """<p>Allows you to create the criteria to retry a job.</p>"""
    document_parameters: NotRequired["capo_iot.types.parameter_map.ParameterMap"]
    """<p>Parameters of an Amazon Web Services managed template that you can specify to create the job document.</p> <note> <p> <code>documentParameters</code> can only be used when creating jobs from Amazon Web Services managed templates. This parameter can't be used with custom job templates or to create jobs from them.</p> </note>"""
    scheduling_config: NotRequired["capo_iot.types.scheduling_config.SchedulingConfig"]
    """<p>The configuration that allows you to schedule a job for a future date and time in addition to specifying the end behavior for each job execution.</p>"""
    destination_package_versions: NotRequired[
        "capo_iot.types.destination_package_versions.DestinationPackageVersions"
    ]
    """<p>The package version Amazon Resource Names (ARNs) that are installed on the device when the job successfully completes. The package version must be in either the Published or Deprecated state when the job deploys. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle">Package version lifecycle</a>. </p> <p> <b>Note:</b>The following Length Constraints relates to a single ARN. Up to 25 package version ARNs are allowed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobRequest) -> dict:
    out: dict = {}
    import capo_iot.types.job_targets

    out["targets"] = capo_iot.types.job_targets.serialize_json(value["targets"])
    if "document_source" in value:
        out["documentSource"] = value["document_source"]
    if "document" in value:
        out["document"] = value["document"]
    if "description" in value:
        out["description"] = value["description"]
    if "presigned_url_config" in value:
        import capo_iot.types.presigned_url_config

        out["presignedUrlConfig"] = capo_iot.types.presigned_url_config.serialize_json(
            value["presigned_url_config"]
        )
    if "target_selection" in value:
        import capo_iot.types.target_selection

        out["targetSelection"] = capo_iot.types.target_selection.serialize_json(
            value["target_selection"]
        )
    if "job_executions_rollout_config" in value:
        import capo_iot.types.job_executions_rollout_config

        out["jobExecutionsRolloutConfig"] = (
            capo_iot.types.job_executions_rollout_config.serialize_json(
                value["job_executions_rollout_config"]
            )
        )
    if "abort_config" in value:
        import capo_iot.types.abort_config

        out["abortConfig"] = capo_iot.types.abort_config.serialize_json(
            value["abort_config"]
        )
    if "timeout_config" in value:
        import capo_iot.types.timeout_config

        out["timeoutConfig"] = capo_iot.types.timeout_config.serialize_json(
            value["timeout_config"]
        )
    if "tags" in value:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.serialize_json(value["tags"])
    if "namespace_id" in value:
        out["namespaceId"] = value["namespace_id"]
    if "job_template_arn" in value:
        out["jobTemplateArn"] = value["job_template_arn"]
    if "job_executions_retry_config" in value:
        import capo_iot.types.job_executions_retry_config

        out["jobExecutionsRetryConfig"] = (
            capo_iot.types.job_executions_retry_config.serialize_json(
                value["job_executions_retry_config"]
            )
        )
    if "document_parameters" in value:
        import capo_iot.types.parameter_map

        out["documentParameters"] = capo_iot.types.parameter_map.serialize_json(
            value["document_parameters"]
        )
    if "scheduling_config" in value:
        import capo_iot.types.scheduling_config

        out["schedulingConfig"] = capo_iot.types.scheduling_config.serialize_json(
            value["scheduling_config"]
        )
    if "destination_package_versions" in value:
        import capo_iot.types.destination_package_versions

        out["destinationPackageVersions"] = (
            capo_iot.types.destination_package_versions.serialize_json(
                value["destination_package_versions"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateJobRequest:
    out: CreateJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("targets") is not None:
        import capo_iot.types.job_targets

        out["targets"] = capo_iot.types.job_targets.deserialize_json(data["targets"])
    else:
        raise DeserializationError("CreateJobRequest.targets required")
    if data.get("documentSource") is not None:
        out["document_source"] = data["documentSource"]
    if data.get("document") is not None:
        out["document"] = data["document"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("presignedUrlConfig") is not None:
        import capo_iot.types.presigned_url_config

        out["presigned_url_config"] = (
            capo_iot.types.presigned_url_config.deserialize_json(
                data["presignedUrlConfig"]
            )
        )
    if data.get("targetSelection") is not None:
        import capo_iot.types.target_selection

        out["target_selection"] = capo_iot.types.target_selection.deserialize_json(
            data["targetSelection"]
        )
    if data.get("jobExecutionsRolloutConfig") is not None:
        import capo_iot.types.job_executions_rollout_config

        out["job_executions_rollout_config"] = (
            capo_iot.types.job_executions_rollout_config.deserialize_json(
                data["jobExecutionsRolloutConfig"]
            )
        )
    if data.get("abortConfig") is not None:
        import capo_iot.types.abort_config

        out["abort_config"] = capo_iot.types.abort_config.deserialize_json(
            data["abortConfig"]
        )
    if data.get("timeoutConfig") is not None:
        import capo_iot.types.timeout_config

        out["timeout_config"] = capo_iot.types.timeout_config.deserialize_json(
            data["timeoutConfig"]
        )
    if data.get("tags") is not None:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.deserialize_json(data["tags"])
    if data.get("namespaceId") is not None:
        out["namespace_id"] = data["namespaceId"]
    if data.get("jobTemplateArn") is not None:
        out["job_template_arn"] = data["jobTemplateArn"]
    if data.get("jobExecutionsRetryConfig") is not None:
        import capo_iot.types.job_executions_retry_config

        out["job_executions_retry_config"] = (
            capo_iot.types.job_executions_retry_config.deserialize_json(
                data["jobExecutionsRetryConfig"]
            )
        )
    if data.get("documentParameters") is not None:
        import capo_iot.types.parameter_map

        out["document_parameters"] = capo_iot.types.parameter_map.deserialize_json(
            data["documentParameters"]
        )
    if data.get("schedulingConfig") is not None:
        import capo_iot.types.scheduling_config

        out["scheduling_config"] = capo_iot.types.scheduling_config.deserialize_json(
            data["schedulingConfig"]
        )
    if data.get("destinationPackageVersions") is not None:
        import capo_iot.types.destination_package_versions

        out["destination_package_versions"] = (
            capo_iot.types.destination_package_versions.deserialize_json(
                data["destinationPackageVersions"]
            )
        )
    return out
