"""Generated from Smithy shape ``com.amazonaws.emrserverless#StartSessionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_emr_serverless.types.application_id
    import capo_emr_serverless.types.client_token
    import capo_emr_serverless.types.duration
    import capo_emr_serverless.types.iam_role_arn
    import capo_emr_serverless.types.session_configuration_overrides
    import capo_emr_serverless.types.string256
    import capo_emr_serverless.types.tag_map


class StartSessionRequest(TypedDict, closed=True):
    application_id: "capo_emr_serverless.types.application_id.ApplicationId"
    """<p>The ID of the application on which to start the session.</p>"""
    client_token: "capo_emr_serverless.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token, the server returns the successful response without performing the operation again.</p>"""
    execution_role_arn: "capo_emr_serverless.types.iam_role_arn.IAMRoleArn"
    """<p>The execution role ARN for the session. Amazon EMR Serverless uses this role to access Amazon Web Services resources on your behalf during session execution.</p>"""
    configuration_overrides: NotRequired[
        "capo_emr_serverless.types.session_configuration_overrides.SessionConfigurationOverrides"
    ]
    """<p>The configuration overrides for the session. Only runtime configuration overrides are supported.</p>"""
    tags: NotRequired["capo_emr_serverless.types.tag_map.TagMap"]
    """<p>The tags to assign to the session.</p>"""
    idle_timeout_minutes: NotRequired["capo_emr_serverless.types.duration.Duration"]
    """<p>The idle timeout in minutes for the session. After the session remains idle for this duration, Amazon EMR Serverless automatically terminates it.</p>"""
    name: NotRequired["capo_emr_serverless.types.string256.String256"]
    """<p>The optional name for the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSessionRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    out["executionRoleArn"] = value["execution_role_arn"]
    if "configuration_overrides" in value:
        import capo_emr_serverless.types.session_configuration_overrides

        out["configurationOverrides"] = (
            capo_emr_serverless.types.session_configuration_overrides.serialize_json(
                value["configuration_overrides"]
            )
        )
    if "tags" in value:
        import capo_emr_serverless.types.tag_map

        out["tags"] = capo_emr_serverless.types.tag_map.serialize_json(value["tags"])
    if "idle_timeout_minutes" in value:
        out["idleTimeoutMinutes"] = value["idle_timeout_minutes"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> StartSessionRequest:
    out: StartSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("StartSessionRequest.client_token required")
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        raise DeserializationError("StartSessionRequest.execution_role_arn required")
    if data.get("configurationOverrides") is not None:
        import capo_emr_serverless.types.session_configuration_overrides

        out["configuration_overrides"] = (
            capo_emr_serverless.types.session_configuration_overrides.deserialize_json(
                data["configurationOverrides"]
            )
        )
    if data.get("tags") is not None:
        import capo_emr_serverless.types.tag_map

        out["tags"] = capo_emr_serverless.types.tag_map.deserialize_json(data["tags"])
    if data.get("idleTimeoutMinutes") is not None:
        out["idle_timeout_minutes"] = data["idleTimeoutMinutes"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out


def redact_sensitive(value: StartSessionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "configuration_overrides" in value:
        import capo_emr_serverless.types.session_configuration_overrides

        out["configuration_overrides"] = (
            capo_emr_serverless.types.session_configuration_overrides.redact_sensitive(
                value["configuration_overrides"]
            )
        )
    return out
