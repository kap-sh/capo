"""Generated from Smithy shape ``com.amazonaws.iot#UpdateJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.abort_config
    import capo_iot.types.job_description
    import capo_iot.types.job_executions_retry_config
    import capo_iot.types.job_executions_rollout_config
    import capo_iot.types.job_id
    import capo_iot.types.namespace_id
    import capo_iot.types.presigned_url_config
    import capo_iot.types.timeout_config


class UpdateJobRequest(TypedDict, closed=True):
    job_id: "capo_iot.types.job_id.JobId"
    """<p>The ID of the job to be updated.</p>"""
    description: NotRequired["capo_iot.types.job_description.JobDescription"]
    """<p>A short text description of the job.</p>"""
    presigned_url_config: NotRequired[
        "capo_iot.types.presigned_url_config.PresignedUrlConfig"
    ]
    """<p>Configuration information for pre-signed S3 URLs.</p>"""
    job_executions_rollout_config: NotRequired[
        "capo_iot.types.job_executions_rollout_config.JobExecutionsRolloutConfig"
    ]
    """<p>Allows you to create a staged rollout of the job.</p>"""
    abort_config: NotRequired["capo_iot.types.abort_config.AbortConfig"]
    """<p>Allows you to create criteria to abort a job.</p>"""
    timeout_config: NotRequired["capo_iot.types.timeout_config.TimeoutConfig"]
    """<p>Specifies the amount of time each device has to finish its execution of the job. The timer is started when the job execution status is set to <code>IN_PROGRESS</code>. If the job execution status is not set to another terminal state before the time expires, it will be automatically set to <code>TIMED_OUT</code>. </p>"""
    namespace_id: NotRequired["capo_iot.types.namespace_id.NamespaceId"]
    """<p>The namespace used to indicate that a job is a customer-managed job.</p> <p>When you specify a value for this parameter, Amazon Web Services IoT Core sends jobs notifications to MQTT topics that contain the value in the following format.</p> <p> <code>$aws/things/<i>THING_NAME</i>/jobs/<i>JOB_ID</i>/notify-namespace-<i>NAMESPACE_ID</i>/</code> </p> <note> <p>The <code>namespaceId</code> feature is only supported by IoT Greengrass at this time. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/setting-up.html">Setting up IoT Greengrass core devices.</a> </p> </note>"""
    job_executions_retry_config: NotRequired[
        "capo_iot.types.job_executions_retry_config.JobExecutionsRetryConfig"
    ]
    """<p>Allows you to create the criteria to retry a job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateJobRequest) -> dict:
    out: dict = {}
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
    if "timeout_config" in value:
        import capo_iot.types.timeout_config

        out["timeoutConfig"] = capo_iot.types.timeout_config.serialize_json(
            value["timeout_config"]
        )
    if "job_executions_retry_config" in value:
        import capo_iot.types.job_executions_retry_config

        out["jobExecutionsRetryConfig"] = (
            capo_iot.types.job_executions_retry_config.serialize_json(
                value["job_executions_retry_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateJobRequest:
    out: UpdateJobRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("timeoutConfig") is not None:
        import capo_iot.types.timeout_config

        out["timeout_config"] = capo_iot.types.timeout_config.deserialize_json(
            data["timeoutConfig"]
        )
    if data.get("jobExecutionsRetryConfig") is not None:
        import capo_iot.types.job_executions_retry_config

        out["job_executions_retry_config"] = (
            capo_iot.types.job_executions_retry_config.deserialize_json(
                data["jobExecutionsRetryConfig"]
            )
        )
    return out
