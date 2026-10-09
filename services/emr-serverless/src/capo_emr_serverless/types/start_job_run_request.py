"""Generated from Smithy shape ``com.amazonaws.emrserverless#StartJobRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_emr_serverless.types.application_id
    import capo_emr_serverless.types.client_token
    import capo_emr_serverless.types.configuration_overrides
    import capo_emr_serverless.types.duration
    import capo_emr_serverless.types.iam_role_arn
    import capo_emr_serverless.types.job_driver
    import capo_emr_serverless.types.job_run_execution_iam_policy
    import capo_emr_serverless.types.job_run_mode
    import capo_emr_serverless.types.retry_policy
    import capo_emr_serverless.types.string256
    import capo_emr_serverless.types.tag_map


class StartJobRunRequest(TypedDict, closed=True):
    application_id: "capo_emr_serverless.types.application_id.ApplicationId"
    """<p>The ID of the application on which to run the job.</p>"""
    client_token: "capo_emr_serverless.types.client_token.ClientToken"
    """<p>The client idempotency token of the job run to start. Its value must be unique for each request.</p>"""
    execution_role_arn: "capo_emr_serverless.types.iam_role_arn.IAMRoleArn"
    """<p>The execution role ARN for the job run.</p>"""
    execution_iam_policy: NotRequired[
        "capo_emr_serverless.types.job_run_execution_iam_policy.JobRunExecutionIamPolicy"
    ]
    """<p>You can pass an optional IAM policy. The resulting job IAM role permissions will be an intersection of this policy and the policy associated with your job execution role.</p>"""
    job_driver: NotRequired["capo_emr_serverless.types.job_driver.JobDriver"]
    """<p>The job driver for the job run.</p>"""
    configuration_overrides: NotRequired[
        "capo_emr_serverless.types.configuration_overrides.ConfigurationOverrides"
    ]
    """<p>The configuration overrides for the job run.</p>"""
    tags: NotRequired["capo_emr_serverless.types.tag_map.TagMap"]
    """<p>The tags assigned to the job run.</p>"""
    execution_timeout_minutes: NotRequired[
        "capo_emr_serverless.types.duration.Duration"
    ]
    """<p>The maximum duration, in minutes, for the job run. If the job run exceeds this duration, Amazon EMR Serverless cancels it automatically.</p> <p>For BATCH mode job runs, the maximum value is 10080 minutes (7 days) starting with Amazon EMR release 7.11. Setting a value of 0 to disable the timeout is no longer supported for BATCH mode job runs.</p>"""
    name: NotRequired["capo_emr_serverless.types.string256.String256"]
    """<p>The optional job run name. This doesn't have to be unique.</p>"""
    mode: NotRequired["capo_emr_serverless.types.job_run_mode.JobRunMode"]
    """<p>The mode of the job run when it starts.</p>"""
    retry_policy: NotRequired["capo_emr_serverless.types.retry_policy.RetryPolicy"]
    """<p>The retry policy when job run starts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartJobRunRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    out["executionRoleArn"] = value["execution_role_arn"]
    if "execution_iam_policy" in value:
        import capo_emr_serverless.types.job_run_execution_iam_policy

        out["executionIamPolicy"] = (
            capo_emr_serverless.types.job_run_execution_iam_policy.serialize_json(
                value["execution_iam_policy"]
            )
        )
    if "job_driver" in value:
        import capo_emr_serverless.types.job_driver

        out["jobDriver"] = capo_emr_serverless.types.job_driver.serialize_json(
            value["job_driver"]
        )
    if "configuration_overrides" in value:
        import capo_emr_serverless.types.configuration_overrides

        out["configurationOverrides"] = (
            capo_emr_serverless.types.configuration_overrides.serialize_json(
                value["configuration_overrides"]
            )
        )
    if "tags" in value:
        import capo_emr_serverless.types.tag_map

        out["tags"] = capo_emr_serverless.types.tag_map.serialize_json(value["tags"])
    if "execution_timeout_minutes" in value:
        out["executionTimeoutMinutes"] = value["execution_timeout_minutes"]
    if "name" in value:
        out["name"] = value["name"]
    if "mode" in value:
        out["mode"] = value["mode"]
    if "retry_policy" in value:
        import capo_emr_serverless.types.retry_policy

        out["retryPolicy"] = capo_emr_serverless.types.retry_policy.serialize_json(
            value["retry_policy"]
        )
    return out


def deserialize_json(data: dict) -> StartJobRunRequest:
    out: StartJobRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("StartJobRunRequest.client_token required")
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        raise DeserializationError("StartJobRunRequest.execution_role_arn required")
    if data.get("executionIamPolicy") is not None:
        import capo_emr_serverless.types.job_run_execution_iam_policy

        out["execution_iam_policy"] = (
            capo_emr_serverless.types.job_run_execution_iam_policy.deserialize_json(
                data["executionIamPolicy"]
            )
        )
    if data.get("jobDriver") is not None:
        import capo_emr_serverless.types.job_driver

        out["job_driver"] = capo_emr_serverless.types.job_driver.deserialize_json(
            data["jobDriver"]
        )
    if data.get("configurationOverrides") is not None:
        import capo_emr_serverless.types.configuration_overrides

        out["configuration_overrides"] = (
            capo_emr_serverless.types.configuration_overrides.deserialize_json(
                data["configurationOverrides"]
            )
        )
    if data.get("tags") is not None:
        import capo_emr_serverless.types.tag_map

        out["tags"] = capo_emr_serverless.types.tag_map.deserialize_json(data["tags"])
    if data.get("executionTimeoutMinutes") is not None:
        out["execution_timeout_minutes"] = data["executionTimeoutMinutes"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("mode") is not None:
        out["mode"] = data["mode"]
    if data.get("retryPolicy") is not None:
        import capo_emr_serverless.types.retry_policy

        out["retry_policy"] = capo_emr_serverless.types.retry_policy.deserialize_json(
            data["retryPolicy"]
        )
    return out
