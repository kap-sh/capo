"""Generated from Smithy shape ``com.amazonaws.iot#Job``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.abort_config
    import capo_iot.types.boolean_wrapper_object
    import capo_iot.types.comment
    import capo_iot.types.date_type
    import capo_iot.types.destination_package_versions
    import capo_iot.types.forced
    import capo_iot.types.job_arn
    import capo_iot.types.job_description
    import capo_iot.types.job_executions_retry_config
    import capo_iot.types.job_executions_rollout_config
    import capo_iot.types.job_id
    import capo_iot.types.job_process_details
    import capo_iot.types.job_status
    import capo_iot.types.job_targets
    import capo_iot.types.job_template_arn
    import capo_iot.types.namespace_id
    import capo_iot.types.parameter_map
    import capo_iot.types.presigned_url_config
    import capo_iot.types.reason_code
    import capo_iot.types.scheduled_job_rollout_list
    import capo_iot.types.scheduling_config
    import capo_iot.types.target_selection
    import capo_iot.types.timeout_config


class Job(TypedDict, closed=True):
    job_arn: NotRequired["capo_iot.types.job_arn.JobArn"]
    """<p>An ARN identifying the job with format "arn:aws:iot:region:account:job/jobId".</p>"""
    job_id: NotRequired["capo_iot.types.job_id.JobId"]
    """<p>The unique identifier you assigned to this job when it was created.</p>"""
    target_selection: NotRequired["capo_iot.types.target_selection.TargetSelection"]
    """<p>Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a device when the thing representing the device is added to a target group, even after the job was completed by all things originally in the group. </p> <note> <p>We recommend that you use continuous jobs instead of snapshot jobs for dynamic thing group targets. By using continuous jobs, devices that join the group receive the job execution even after the job has been created.</p> </note>"""
    status: NotRequired["capo_iot.types.job_status.JobStatus"]
    """<p>The status of the job, one of <code>IN_PROGRESS</code>, <code>CANCELED</code>, <code>DELETION_IN_PROGRESS</code> or <code>COMPLETED</code>. </p>"""
    force_canceled: NotRequired["capo_iot.types.forced.Forced"]
    """<p>Will be <code>true</code> if the job was canceled with the optional <code>force</code> parameter set to <code>true</code>.</p>"""
    reason_code: NotRequired["capo_iot.types.reason_code.ReasonCode"]
    """<p>If the job was updated, provides the reason code for the update.</p>"""
    comment: NotRequired["capo_iot.types.comment.Comment"]
    """<p>If the job was updated, describes the reason for the update.</p>"""
    targets: NotRequired["capo_iot.types.job_targets.JobTargets"]
    """<p>A list of IoT things and thing groups to which the job should be sent.</p>"""
    description: NotRequired["capo_iot.types.job_description.JobDescription"]
    """<p>A short text description of the job.</p>"""
    presigned_url_config: NotRequired[
        "capo_iot.types.presigned_url_config.PresignedUrlConfig"
    ]
    """<p>Configuration for pre-signed S3 URLs.</p>"""
    job_executions_rollout_config: NotRequired[
        "capo_iot.types.job_executions_rollout_config.JobExecutionsRolloutConfig"
    ]
    """<p>Allows you to create a staged rollout of a job.</p>"""
    abort_config: NotRequired["capo_iot.types.abort_config.AbortConfig"]
    """<p>Configuration for criteria to abort the job.</p>"""
    created_at: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The time, in seconds since the epoch, when the job was created.</p>"""
    last_updated_at: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The time, in seconds since the epoch, when the job was last updated.</p>"""
    completed_at: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The time, in seconds since the epoch, when the job was completed.</p>"""
    job_process_details: NotRequired[
        "capo_iot.types.job_process_details.JobProcessDetails"
    ]
    """<p>Details about the job process.</p>"""
    timeout_config: NotRequired["capo_iot.types.timeout_config.TimeoutConfig"]
    """<p>Specifies the amount of time each device has to finish its execution of the job. A timer is started when the job execution status is set to <code>IN_PROGRESS</code>. If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to <code>TIMED_OUT</code>.</p>"""
    namespace_id: NotRequired["capo_iot.types.namespace_id.NamespaceId"]
    """<p>The namespace used to indicate that a job is a customer-managed job.</p> <p>When you specify a value for this parameter, Amazon Web Services IoT Core sends jobs notifications to MQTT topics that contain the value in the following format.</p> <p> <code>$aws/things/<i>THING_NAME</i>/jobs/<i>JOB_ID</i>/notify-namespace-<i>NAMESPACE_ID</i>/</code> </p> <note> <p>The <code>namespaceId</code> feature is only supported by IoT Greengrass at this time. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/setting-up.html">Setting up IoT Greengrass core devices.</a> </p> </note>"""
    job_template_arn: NotRequired["capo_iot.types.job_template_arn.JobTemplateArn"]
    """<p>The ARN of the job template used to create the job.</p>"""
    job_executions_retry_config: NotRequired[
        "capo_iot.types.job_executions_retry_config.JobExecutionsRetryConfig"
    ]
    """<p>The configuration for the criteria to retry the job.</p>"""
    document_parameters: NotRequired["capo_iot.types.parameter_map.ParameterMap"]
    """<p>A key-value map that pairs the patterns that need to be replaced in a managed template job document schema. You can use the description of each key as a guidance to specify the inputs during runtime when creating a job.</p> <note> <p> <code>documentParameters</code> can only be used when creating jobs from Amazon Web Services managed templates. This parameter can't be used with custom job templates or to create jobs from them.</p> </note>"""
    is_concurrent: NotRequired[
        "capo_iot.types.boolean_wrapper_object.BooleanWrapperObject"
    ]
    """<p>Indicates whether a job is concurrent. Will be true when a job is rolling out new job executions or canceling previously created executions, otherwise false.</p>"""
    scheduling_config: NotRequired["capo_iot.types.scheduling_config.SchedulingConfig"]
    """<p>The configuration that allows you to schedule a job for a future date and time in addition to specifying the end behavior for each job execution.</p>"""
    scheduled_job_rollouts: NotRequired[
        "capo_iot.types.scheduled_job_rollout_list.ScheduledJobRolloutList"
    ]
    """<p>Displays the next seven maintenance window occurrences and their start times.</p>"""
    destination_package_versions: NotRequired[
        "capo_iot.types.destination_package_versions.DestinationPackageVersions"
    ]
    """<p>The package version Amazon Resource Names (ARNs) that are installed on the device when the job successfully completes. The package version must be in either the Published or Deprecated state when the job deploys. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle">Package version lifecycle</a>.The package version must be in either the Published or Deprecated state when the job deploys. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle">Package version lifecycle</a>.</p> <p> <b>Note:</b>The following Length Constraints relates to a single ARN. Up to 25 package version ARNs are allowed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Job) -> dict:
    out: dict = {}
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "target_selection" in value:
        import capo_iot.types.target_selection

        out["targetSelection"] = capo_iot.types.target_selection.serialize_json(
            value["target_selection"]
        )
    if "status" in value:
        import capo_iot.types.job_status

        out["status"] = capo_iot.types.job_status.serialize_json(value["status"])
    if "force_canceled" in value:
        out["forceCanceled"] = value["force_canceled"]
    if "reason_code" in value:
        out["reasonCode"] = value["reason_code"]
    if "comment" in value:
        out["comment"] = value["comment"]
    if "targets" in value:
        import capo_iot.types.job_targets

        out["targets"] = capo_iot.types.job_targets.serialize_json(value["targets"])
    if "description" in value:
        out["description"] = value["description"]
    if "presigned_url_config" in value:
        import capo_iot.types.presigned_url_config

        out["presignedUrlConfig"] = capo_iot.types.presigned_url_config.serialize_json(
            value["presigned_url_config"]
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
    if "created_at" in value:
        import capo_iot.types.date_type

        out["createdAt"] = capo_iot.types.date_type.serialize_json(value["created_at"])
    if "last_updated_at" in value:
        import capo_iot.types.date_type

        out["lastUpdatedAt"] = capo_iot.types.date_type.serialize_json(
            value["last_updated_at"]
        )
    if "completed_at" in value:
        import capo_iot.types.date_type

        out["completedAt"] = capo_iot.types.date_type.serialize_json(
            value["completed_at"]
        )
    if "job_process_details" in value:
        import capo_iot.types.job_process_details

        out["jobProcessDetails"] = capo_iot.types.job_process_details.serialize_json(
            value["job_process_details"]
        )
    if "timeout_config" in value:
        import capo_iot.types.timeout_config

        out["timeoutConfig"] = capo_iot.types.timeout_config.serialize_json(
            value["timeout_config"]
        )
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
    if "is_concurrent" in value:
        out["isConcurrent"] = value["is_concurrent"]
    if "scheduling_config" in value:
        import capo_iot.types.scheduling_config

        out["schedulingConfig"] = capo_iot.types.scheduling_config.serialize_json(
            value["scheduling_config"]
        )
    if "scheduled_job_rollouts" in value:
        import capo_iot.types.scheduled_job_rollout_list

        out["scheduledJobRollouts"] = (
            capo_iot.types.scheduled_job_rollout_list.serialize_json(
                value["scheduled_job_rollouts"]
            )
        )
    if "destination_package_versions" in value:
        import capo_iot.types.destination_package_versions

        out["destinationPackageVersions"] = (
            capo_iot.types.destination_package_versions.serialize_json(
                value["destination_package_versions"]
            )
        )
    return out


def deserialize_json(data: dict) -> Job:
    out: Job = {}  # type: ignore[typeddict-item]
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    if data.get("targetSelection") is not None:
        import capo_iot.types.target_selection

        out["target_selection"] = capo_iot.types.target_selection.deserialize_json(
            data["targetSelection"]
        )
    if data.get("status") is not None:
        import capo_iot.types.job_status

        out["status"] = capo_iot.types.job_status.deserialize_json(data["status"])
    if data.get("forceCanceled") is not None:
        out["force_canceled"] = data["forceCanceled"]
    if data.get("reasonCode") is not None:
        out["reason_code"] = data["reasonCode"]
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    if data.get("targets") is not None:
        import capo_iot.types.job_targets

        out["targets"] = capo_iot.types.job_targets.deserialize_json(data["targets"])
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("presignedUrlConfig") is not None:
        import capo_iot.types.presigned_url_config

        out["presigned_url_config"] = (
            capo_iot.types.presigned_url_config.deserialize_json(
                data["presignedUrlConfig"]
            )
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
    if data.get("createdAt") is not None:
        import capo_iot.types.date_type

        out["created_at"] = capo_iot.types.date_type.deserialize_json(data["createdAt"])
    if data.get("lastUpdatedAt") is not None:
        import capo_iot.types.date_type

        out["last_updated_at"] = capo_iot.types.date_type.deserialize_json(
            data["lastUpdatedAt"]
        )
    if data.get("completedAt") is not None:
        import capo_iot.types.date_type

        out["completed_at"] = capo_iot.types.date_type.deserialize_json(
            data["completedAt"]
        )
    if data.get("jobProcessDetails") is not None:
        import capo_iot.types.job_process_details

        out["job_process_details"] = (
            capo_iot.types.job_process_details.deserialize_json(
                data["jobProcessDetails"]
            )
        )
    if data.get("timeoutConfig") is not None:
        import capo_iot.types.timeout_config

        out["timeout_config"] = capo_iot.types.timeout_config.deserialize_json(
            data["timeoutConfig"]
        )
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
    if data.get("isConcurrent") is not None:
        out["is_concurrent"] = data["isConcurrent"]
    if data.get("schedulingConfig") is not None:
        import capo_iot.types.scheduling_config

        out["scheduling_config"] = capo_iot.types.scheduling_config.deserialize_json(
            data["schedulingConfig"]
        )
    if data.get("scheduledJobRollouts") is not None:
        import capo_iot.types.scheduled_job_rollout_list

        out["scheduled_job_rollouts"] = (
            capo_iot.types.scheduled_job_rollout_list.deserialize_json(
                data["scheduledJobRollouts"]
            )
        )
    if data.get("destinationPackageVersions") is not None:
        import capo_iot.types.destination_package_versions

        out["destination_package_versions"] = (
            capo_iot.types.destination_package_versions.deserialize_json(
                data["destinationPackageVersions"]
            )
        )
    return out
