"""Generated from Smithy shape ``com.amazonaws.emrserverless#Session``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_emr_serverless.types.application_id
    import capo_emr_serverless.types.date
    import capo_emr_serverless.types.duration
    import capo_emr_serverless.types.iam_role_arn
    import capo_emr_serverless.types.network_configuration
    import capo_emr_serverless.types.release_label
    import capo_emr_serverless.types.request_identity_user_arn
    import capo_emr_serverless.types.resource_utilization
    import capo_emr_serverless.types.session_arn
    import capo_emr_serverless.types.session_configuration_overrides
    import capo_emr_serverless.types.session_id
    import capo_emr_serverless.types.session_state
    import capo_emr_serverless.types.string256
    import capo_emr_serverless.types.string1024
    import capo_emr_serverless.types.tag_map
    import capo_emr_serverless.types.total_resource_utilization


class Session(TypedDict, closed=True):
    application_id: "capo_emr_serverless.types.application_id.ApplicationId"
    """<p>The ID of the application that the session belongs to.</p>"""
    session_id: "capo_emr_serverless.types.session_id.SessionId"
    """<p>The ID of the session.</p>"""
    arn: "capo_emr_serverless.types.session_arn.SessionArn"
    """<p>The Amazon Resource Name (ARN) of the session.</p>"""
    name: NotRequired["capo_emr_serverless.types.string256.String256"]
    """<p>The optional name of the session.</p>"""
    state: "capo_emr_serverless.types.session_state.SessionState"
    """<p>The state of the session.</p>"""
    state_details: "capo_emr_serverless.types.string1024.String1024"
    """<p>Additional details about the current state of the session.</p>"""
    release_label: "capo_emr_serverless.types.release_label.ReleaseLabel"
    """<p>The Amazon EMR release label associated with the session.</p>"""
    execution_role_arn: "capo_emr_serverless.types.iam_role_arn.IAMRoleArn"
    """<p>The Amazon Resource Name (ARN) of the execution role for the session.</p>"""
    created_by: (
        "capo_emr_serverless.types.request_identity_user_arn.RequestIdentityUserArn"
    )
    """<p>The IAM principal that created the session.</p>"""
    created_at: "capo_emr_serverless.types.date.Date"
    """<p>The date and time that the session was created.</p>"""
    updated_at: "capo_emr_serverless.types.date.Date"
    """<p>The date and time that the session was last updated.</p>"""
    started_at: NotRequired["capo_emr_serverless.types.date.Date"]
    """<p>The date and time that the session moved to a running state.</p>"""
    ended_at: NotRequired["capo_emr_serverless.types.date.Date"]
    """<p>The date and time that the session was terminated or failed.</p>"""
    idle_since: NotRequired["capo_emr_serverless.types.date.Date"]
    """<p>The date and time that the session became idle.</p>"""
    configuration_overrides: NotRequired[
        "capo_emr_serverless.types.session_configuration_overrides.SessionConfigurationOverrides"
    ]
    """<p>The configuration overrides for the session, including runtime configuration properties.</p>"""
    network_configuration: NotRequired[
        "capo_emr_serverless.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The network configuration for customer VPC connectivity for the session.</p>"""
    idle_timeout_minutes: NotRequired["capo_emr_serverless.types.duration.Duration"]
    """<p>The idle timeout in minutes for the session. After the session remains idle for this duration, it is automatically terminated.</p>"""
    tags: NotRequired["capo_emr_serverless.types.tag_map.TagMap"]
    """<p>The tags assigned to the session.</p>"""
    total_resource_utilization: NotRequired[
        "capo_emr_serverless.types.total_resource_utilization.TotalResourceUtilization"
    ]
    """<p>The aggregate vCPU, memory, and storage resources used from the time the session starts to execute, until the time the session terminates, rounded up to the nearest second.</p>"""
    billed_resource_utilization: NotRequired[
        "capo_emr_serverless.types.resource_utilization.ResourceUtilization"
    ]
    """<p>The aggregate vCPU, memory, and storage that Amazon Web Services has billed for the session. The billed resources include a 1-minute minimum usage for workers, plus additional storage over 20 GB per worker. Note that billed resources do not include usage for idle pre-initialized workers.</p>"""
    total_execution_duration_seconds: NotRequired["int"]
    """<p>The total execution duration of the session in seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Session) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    out["sessionId"] = value["session_id"]
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    out["state"] = value["state"]
    out["stateDetails"] = value["state_details"]
    out["releaseLabel"] = value["release_label"]
    out["executionRoleArn"] = value["execution_role_arn"]
    out["createdBy"] = value["created_by"]
    import capo_emr_serverless.types.date

    out["createdAt"] = capo_emr_serverless.types.date.serialize_json(
        value["created_at"]
    )
    import capo_emr_serverless.types.date

    out["updatedAt"] = capo_emr_serverless.types.date.serialize_json(
        value["updated_at"]
    )
    if "started_at" in value:
        import capo_emr_serverless.types.date

        out["startedAt"] = capo_emr_serverless.types.date.serialize_json(
            value["started_at"]
        )
    if "ended_at" in value:
        import capo_emr_serverless.types.date

        out["endedAt"] = capo_emr_serverless.types.date.serialize_json(
            value["ended_at"]
        )
    if "idle_since" in value:
        import capo_emr_serverless.types.date

        out["idleSince"] = capo_emr_serverless.types.date.serialize_json(
            value["idle_since"]
        )
    if "configuration_overrides" in value:
        import capo_emr_serverless.types.session_configuration_overrides

        out["configurationOverrides"] = (
            capo_emr_serverless.types.session_configuration_overrides.serialize_json(
                value["configuration_overrides"]
            )
        )
    if "network_configuration" in value:
        import capo_emr_serverless.types.network_configuration

        out["networkConfiguration"] = (
            capo_emr_serverless.types.network_configuration.serialize_json(
                value["network_configuration"]
            )
        )
    if "idle_timeout_minutes" in value:
        out["idleTimeoutMinutes"] = value["idle_timeout_minutes"]
    if "tags" in value:
        import capo_emr_serverless.types.tag_map

        out["tags"] = capo_emr_serverless.types.tag_map.serialize_json(value["tags"])
    if "total_resource_utilization" in value:
        import capo_emr_serverless.types.total_resource_utilization

        out["totalResourceUtilization"] = (
            capo_emr_serverless.types.total_resource_utilization.serialize_json(
                value["total_resource_utilization"]
            )
        )
    if "billed_resource_utilization" in value:
        import capo_emr_serverless.types.resource_utilization

        out["billedResourceUtilization"] = (
            capo_emr_serverless.types.resource_utilization.serialize_json(
                value["billed_resource_utilization"]
            )
        )
    if "total_execution_duration_seconds" in value:
        out["totalExecutionDurationSeconds"] = value["total_execution_duration_seconds"]
    return out


def deserialize_json(data: dict) -> Session:
    out: Session = {}  # type: ignore[typeddict-item]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("Session.application_id required")
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("Session.session_id required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Session.arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        raise DeserializationError("Session.state required")
    if data.get("stateDetails") is not None:
        out["state_details"] = data["stateDetails"]
    else:
        raise DeserializationError("Session.state_details required")
    if data.get("releaseLabel") is not None:
        out["release_label"] = data["releaseLabel"]
    else:
        raise DeserializationError("Session.release_label required")
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        raise DeserializationError("Session.execution_role_arn required")
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("Session.created_by required")
    if data.get("createdAt") is not None:
        import capo_emr_serverless.types.date

        out["created_at"] = capo_emr_serverless.types.date.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("Session.created_at required")
    if data.get("updatedAt") is not None:
        import capo_emr_serverless.types.date

        out["updated_at"] = capo_emr_serverless.types.date.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("Session.updated_at required")
    if data.get("startedAt") is not None:
        import capo_emr_serverless.types.date

        out["started_at"] = capo_emr_serverless.types.date.deserialize_json(
            data["startedAt"]
        )
    if data.get("endedAt") is not None:
        import capo_emr_serverless.types.date

        out["ended_at"] = capo_emr_serverless.types.date.deserialize_json(
            data["endedAt"]
        )
    if data.get("idleSince") is not None:
        import capo_emr_serverless.types.date

        out["idle_since"] = capo_emr_serverless.types.date.deserialize_json(
            data["idleSince"]
        )
    if data.get("configurationOverrides") is not None:
        import capo_emr_serverless.types.session_configuration_overrides

        out["configuration_overrides"] = (
            capo_emr_serverless.types.session_configuration_overrides.deserialize_json(
                data["configurationOverrides"]
            )
        )
    if data.get("networkConfiguration") is not None:
        import capo_emr_serverless.types.network_configuration

        out["network_configuration"] = (
            capo_emr_serverless.types.network_configuration.deserialize_json(
                data["networkConfiguration"]
            )
        )
    if data.get("idleTimeoutMinutes") is not None:
        out["idle_timeout_minutes"] = data["idleTimeoutMinutes"]
    if data.get("tags") is not None:
        import capo_emr_serverless.types.tag_map

        out["tags"] = capo_emr_serverless.types.tag_map.deserialize_json(data["tags"])
    if data.get("totalResourceUtilization") is not None:
        import capo_emr_serverless.types.total_resource_utilization

        out["total_resource_utilization"] = (
            capo_emr_serverless.types.total_resource_utilization.deserialize_json(
                data["totalResourceUtilization"]
            )
        )
    if data.get("billedResourceUtilization") is not None:
        import capo_emr_serverless.types.resource_utilization

        out["billed_resource_utilization"] = (
            capo_emr_serverless.types.resource_utilization.deserialize_json(
                data["billedResourceUtilization"]
            )
        )
    if data.get("totalExecutionDurationSeconds") is not None:
        out["total_execution_duration_seconds"] = data["totalExecutionDurationSeconds"]
    return out


def redact_sensitive(value: Session) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "configuration_overrides" in value:
        import capo_emr_serverless.types.session_configuration_overrides

        out["configuration_overrides"] = (
            capo_emr_serverless.types.session_configuration_overrides.redact_sensitive(
                value["configuration_overrides"]
            )
        )
    return out
