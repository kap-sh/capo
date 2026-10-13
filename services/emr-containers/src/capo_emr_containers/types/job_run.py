"""Generated from Smithy shape ``com.amazonaws.emrcontainers#JobRun``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.client_token
    import capo_emr_containers.types.configuration_overrides
    import capo_emr_containers.types.date
    import capo_emr_containers.types.failure_reason
    import capo_emr_containers.types.iam_role_arn
    import capo_emr_containers.types.job_arn
    import capo_emr_containers.types.job_driver
    import capo_emr_containers.types.job_run_state
    import capo_emr_containers.types.release_label
    import capo_emr_containers.types.request_identity_user_arn
    import capo_emr_containers.types.resource_id_string
    import capo_emr_containers.types.resource_name_string
    import capo_emr_containers.types.retry_policy_configuration
    import capo_emr_containers.types.retry_policy_execution
    import capo_emr_containers.types.string256
    import capo_emr_containers.types.tag_map


class JobRun(TypedDict, closed=True):
    id: NotRequired["capo_emr_containers.types.resource_id_string.ResourceIdString"]
    """<p>The ID of the job run.</p>"""
    name: NotRequired[
        "capo_emr_containers.types.resource_name_string.ResourceNameString"
    ]
    """<p>The name of the job run.</p>"""
    virtual_cluster_id: NotRequired[
        "capo_emr_containers.types.resource_id_string.ResourceIdString"
    ]
    """<p>The ID of the job run's virtual cluster.</p>"""
    arn: NotRequired["capo_emr_containers.types.job_arn.JobArn"]
    """<p>The ARN of job run.</p>"""
    state: NotRequired["capo_emr_containers.types.job_run_state.JobRunState"]
    """<p>The state of the job run. </p>"""
    client_token: NotRequired["capo_emr_containers.types.client_token.ClientToken"]
    """<p>The client token used to start a job run.</p>"""
    execution_role_arn: NotRequired["capo_emr_containers.types.iam_role_arn.IAMRoleArn"]
    """<p>The execution role ARN of the job run.</p>"""
    release_label: NotRequired["capo_emr_containers.types.release_label.ReleaseLabel"]
    """<p>The release version of Amazon EMR.</p>"""
    configuration_overrides: NotRequired[
        "capo_emr_containers.types.configuration_overrides.ConfigurationOverrides"
    ]
    """<p>The configuration settings that are used to override default configuration.</p>"""
    job_driver: NotRequired["capo_emr_containers.types.job_driver.JobDriver"]
    """<p>Parameters of job driver for the job run.</p>"""
    created_at: NotRequired["capo_emr_containers.types.date.Date"]
    """<p>The date and time when the job run was created.</p>"""
    created_by: NotRequired[
        "capo_emr_containers.types.request_identity_user_arn.RequestIdentityUserArn"
    ]
    """<p>The user who created the job run.</p>"""
    finished_at: NotRequired["capo_emr_containers.types.date.Date"]
    """<p>The date and time when the job run has finished.</p>"""
    state_details: NotRequired["capo_emr_containers.types.string256.String256"]
    """<p>Additional details of the job run state.</p>"""
    failure_reason: NotRequired[
        "capo_emr_containers.types.failure_reason.FailureReason"
    ]
    """<p>The reasons why the job run has failed.</p>"""
    tags: NotRequired["capo_emr_containers.types.tag_map.TagMap"]
    """<p>The assigned tags of the job run.</p>"""
    retry_policy_configuration: NotRequired[
        "capo_emr_containers.types.retry_policy_configuration.RetryPolicyConfiguration"
    ]
    """<p>The configuration of the retry policy that the job runs on.</p>"""
    retry_policy_execution: NotRequired[
        "capo_emr_containers.types.retry_policy_execution.RetryPolicyExecution"
    ]
    """<p>The current status of the retry policy executed on the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobRun) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "virtual_cluster_id" in value:
        out["virtualClusterId"] = value["virtual_cluster_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "state" in value:
        import capo_emr_containers.types.job_run_state

        out["state"] = capo_emr_containers.types.job_run_state.serialize_json(
            value["state"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    if "release_label" in value:
        out["releaseLabel"] = value["release_label"]
    if "configuration_overrides" in value:
        import capo_emr_containers.types.configuration_overrides

        out["configurationOverrides"] = (
            capo_emr_containers.types.configuration_overrides.serialize_json(
                value["configuration_overrides"]
            )
        )
    if "job_driver" in value:
        import capo_emr_containers.types.job_driver

        out["jobDriver"] = capo_emr_containers.types.job_driver.serialize_json(
            value["job_driver"]
        )
    if "created_at" in value:
        import capo_emr_containers.types.date

        out["createdAt"] = capo_emr_containers.types.date.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "finished_at" in value:
        import capo_emr_containers.types.date

        out["finishedAt"] = capo_emr_containers.types.date.serialize_json(
            value["finished_at"]
        )
    if "state_details" in value:
        out["stateDetails"] = value["state_details"]
    if "failure_reason" in value:
        import capo_emr_containers.types.failure_reason

        out["failureReason"] = capo_emr_containers.types.failure_reason.serialize_json(
            value["failure_reason"]
        )
    if "tags" in value:
        import capo_emr_containers.types.tag_map

        out["tags"] = capo_emr_containers.types.tag_map.serialize_json(value["tags"])
    if "retry_policy_configuration" in value:
        import capo_emr_containers.types.retry_policy_configuration

        out["retryPolicyConfiguration"] = (
            capo_emr_containers.types.retry_policy_configuration.serialize_json(
                value["retry_policy_configuration"]
            )
        )
    if "retry_policy_execution" in value:
        import capo_emr_containers.types.retry_policy_execution

        out["retryPolicyExecution"] = (
            capo_emr_containers.types.retry_policy_execution.serialize_json(
                value["retry_policy_execution"]
            )
        )
    return out


def deserialize_json(data: dict) -> JobRun:
    out: JobRun = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("virtualClusterId") is not None:
        out["virtual_cluster_id"] = data["virtualClusterId"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("state") is not None:
        import capo_emr_containers.types.job_run_state

        out["state"] = capo_emr_containers.types.job_run_state.deserialize_json(
            data["state"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    if data.get("releaseLabel") is not None:
        out["release_label"] = data["releaseLabel"]
    if data.get("configurationOverrides") is not None:
        import capo_emr_containers.types.configuration_overrides

        out["configuration_overrides"] = (
            capo_emr_containers.types.configuration_overrides.deserialize_json(
                data["configurationOverrides"]
            )
        )
    if data.get("jobDriver") is not None:
        import capo_emr_containers.types.job_driver

        out["job_driver"] = capo_emr_containers.types.job_driver.deserialize_json(
            data["jobDriver"]
        )
    if data.get("createdAt") is not None:
        import capo_emr_containers.types.date

        out["created_at"] = capo_emr_containers.types.date.deserialize_json(
            data["createdAt"]
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    if data.get("finishedAt") is not None:
        import capo_emr_containers.types.date

        out["finished_at"] = capo_emr_containers.types.date.deserialize_json(
            data["finishedAt"]
        )
    if data.get("stateDetails") is not None:
        out["state_details"] = data["stateDetails"]
    if data.get("failureReason") is not None:
        import capo_emr_containers.types.failure_reason

        out["failure_reason"] = (
            capo_emr_containers.types.failure_reason.deserialize_json(
                data["failureReason"]
            )
        )
    if data.get("tags") is not None:
        import capo_emr_containers.types.tag_map

        out["tags"] = capo_emr_containers.types.tag_map.deserialize_json(data["tags"])
    if data.get("retryPolicyConfiguration") is not None:
        import capo_emr_containers.types.retry_policy_configuration

        out["retry_policy_configuration"] = (
            capo_emr_containers.types.retry_policy_configuration.deserialize_json(
                data["retryPolicyConfiguration"]
            )
        )
    if data.get("retryPolicyExecution") is not None:
        import capo_emr_containers.types.retry_policy_execution

        out["retry_policy_execution"] = (
            capo_emr_containers.types.retry_policy_execution.deserialize_json(
                data["retryPolicyExecution"]
            )
        )
    return out


def redact_sensitive(value: JobRun) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "configuration_overrides" in value:
        import capo_emr_containers.types.configuration_overrides

        out["configuration_overrides"] = (
            capo_emr_containers.types.configuration_overrides.redact_sensitive(
                value["configuration_overrides"]
            )
        )
    if "job_driver" in value:
        import capo_emr_containers.types.job_driver

        out["job_driver"] = capo_emr_containers.types.job_driver.redact_sensitive(
            value["job_driver"]
        )
    return out
