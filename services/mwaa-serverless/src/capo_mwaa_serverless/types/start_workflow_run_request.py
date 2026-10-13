"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#StartWorkflowRunRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_mwaa_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.idempotency_token_string
    import capo_mwaa_serverless.types.object_map
    import capo_mwaa_serverless.types.version_id
    import capo_mwaa_serverless.types.workflow_arn


class StartWorkflowRunRequest(TypedDict, closed=True):
    workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn"
    """<p>The Amazon Resource Name (ARN) of the workflow you want to run.</p>"""
    client_token: NotRequired[
        "capo_mwaa_serverless.types.idempotency_token_string.IdempotencyTokenString"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token prevents duplicate workflow run requests.</p>"""
    override_parameters: NotRequired["capo_mwaa_serverless.types.object_map.ObjectMap"]
    """<p>Optional parameters to override default workflow parameters for this specific run. These parameters are passed to the workflow during execution and can be used to customize behavior without modifying the workflow definition. Parameters are made available as environment variables to tasks and you can reference them within the YAML workflow definition using standard parameter substitution syntax.</p>"""
    workflow_version: NotRequired["capo_mwaa_serverless.types.version_id.VersionId"]
    """<p>Optional. The specific version of the workflow to execute. If not specified, the latest version is used.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartWorkflowRunRequest) -> dict:
    out: dict = {}
    out["WorkflowArn"] = value["workflow_arn"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "override_parameters" in value:
        import capo_mwaa_serverless.types.object_map

        out["OverrideParameters"] = (
            capo_mwaa_serverless.types.object_map.serialize_aws_json_1_0(
                value["override_parameters"]
            )
        )
    if "workflow_version" in value:
        out["WorkflowVersion"] = value["workflow_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartWorkflowRunRequest:
    out: StartWorkflowRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkflowArn") is not None:
        out["workflow_arn"] = data["WorkflowArn"]
    else:
        raise DeserializationError("StartWorkflowRunRequest.workflow_arn required")
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("OverrideParameters") is not None:
        import capo_mwaa_serverless.types.object_map

        out["override_parameters"] = (
            capo_mwaa_serverless.types.object_map.deserialize_aws_json_1_0(
                data["OverrideParameters"]
            )
        )
    if data.get("WorkflowVersion") is not None:
        out["workflow_version"] = data["WorkflowVersion"]
    return out


def redact_sensitive(value: StartWorkflowRunRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "override_parameters" in value:
        out["override_parameters"] = "*** Sensitive Data Redacted ***"
    return out
