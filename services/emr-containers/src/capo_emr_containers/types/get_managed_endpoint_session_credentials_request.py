"""Generated from Smithy shape ``com.amazonaws.emrcontainers#GetManagedEndpointSessionCredentialsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.client_token
    import capo_emr_containers.types.credential_type
    import capo_emr_containers.types.iam_role_arn
    import capo_emr_containers.types.java_integer
    import capo_emr_containers.types.log_context
    import capo_emr_containers.types.string2048


class GetManagedEndpointSessionCredentialsRequest(TypedDict, closed=True):
    endpoint_identifier: "capo_emr_containers.types.string2048.String2048"
    """<p>The ARN of the managed endpoint for which the request is submitted. </p>"""
    virtual_cluster_identifier: "capo_emr_containers.types.string2048.String2048"
    """<p>The ARN of the Virtual Cluster which the Managed Endpoint belongs to. </p>"""
    execution_role_arn: "capo_emr_containers.types.iam_role_arn.IAMRoleArn"
    """<p>The IAM Execution Role ARN that will be used by the job run. </p>"""
    credential_type: "capo_emr_containers.types.credential_type.CredentialType"
    """<p>Type of the token requested. Currently supported and default value of this field is “TOKEN.”</p>"""
    duration_in_seconds: NotRequired[
        "capo_emr_containers.types.java_integer.JavaInteger"
    ]
    """<p>Duration in seconds for which the session token is valid. The default duration is 15 minutes and the maximum is 12 hours.</p>"""
    log_context: NotRequired["capo_emr_containers.types.log_context.LogContext"]
    """<p>String identifier used to separate sections of the execution logs uploaded to S3.</p>"""
    client_token: NotRequired["capo_emr_containers.types.client_token.ClientToken"]
    """<p>The client idempotency token of the job run request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedEndpointSessionCredentialsRequest) -> dict:
    out: dict = {}
    out["executionRoleArn"] = value["execution_role_arn"]
    out["credentialType"] = value["credential_type"]
    if "duration_in_seconds" in value:
        out["durationInSeconds"] = value["duration_in_seconds"]
    if "log_context" in value:
        out["logContext"] = value["log_context"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> GetManagedEndpointSessionCredentialsRequest:
    out: GetManagedEndpointSessionCredentialsRequest = {}  # type: ignore[typeddict-item]
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        out["execution_role_arn"] = ""
    if data.get("credentialType") is not None:
        out["credential_type"] = data["credentialType"]
    else:
        out["credential_type"] = ""
    if data.get("durationInSeconds") is not None:
        out["duration_in_seconds"] = data["durationInSeconds"]
    if data.get("logContext") is not None:
        out["log_context"] = data["logContext"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
