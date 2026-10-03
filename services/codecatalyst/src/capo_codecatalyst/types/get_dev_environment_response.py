"""Generated from Smithy shape ``com.amazonaws.codecatalyst#GetDevEnvironmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecatalyst.types.dev_environment_repository_summaries
    import capo_codecatalyst.types.dev_environment_status
    import capo_codecatalyst.types.ides
    import capo_codecatalyst.types.inactivity_timeout_minutes
    import capo_codecatalyst.types.instance_type
    import capo_codecatalyst.types.name_string
    import capo_codecatalyst.types.persistent_storage
    import capo_codecatalyst.types.status_reason
    import capo_codecatalyst.types.timestamp
    import capo_codecatalyst.types.uuid


class GetDevEnvironmentResponse(TypedDict, closed=True):
    space_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    id: "capo_codecatalyst.types.uuid.Uuid"
    """<p>The system-generated unique ID of the Dev Environment. </p>"""
    last_updated_time: "capo_codecatalyst.types.timestamp.Timestamp"
    """<p>The time when the Dev Environment was last updated, in coordinated universal time (UTC) timestamp format as specified in <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6">RFC 3339</a>.</p>"""
    creator_id: "str"
    """<p>The system-generated unique ID of the user who created the Dev Environment. </p>"""
    status: "capo_codecatalyst.types.dev_environment_status.DevEnvironmentStatus"
    """<p>The current status of the Dev Environment.</p>"""
    status_reason: NotRequired["capo_codecatalyst.types.status_reason.StatusReason"]
    """<p>The reason for the status.</p>"""
    repositories: "capo_codecatalyst.types.dev_environment_repository_summaries.DevEnvironmentRepositorySummaries"
    """<p>The source repository that contains the branch cloned into the Dev Environment. </p>"""
    alias: NotRequired["str"]
    """<p>The user-specified alias for the Dev Environment. </p>"""
    ides: NotRequired["capo_codecatalyst.types.ides.Ides"]
    """<p>Information about the integrated development environment (IDE) configured for the Dev Environment. </p>"""
    instance_type: "capo_codecatalyst.types.instance_type.InstanceType"
    """<p>The Amazon EC2 instace type to use for the Dev Environment. </p>"""
    inactivity_timeout_minutes: (
        "capo_codecatalyst.types.inactivity_timeout_minutes.InactivityTimeoutMinutes"
    )
    """<p>The amount of time the Dev Environment will run without any activity detected before stopping, in minutes.</p>"""
    persistent_storage: "capo_codecatalyst.types.persistent_storage.PersistentStorage"
    """<p>Information about the amount of storage allocated to the Dev Environment. By default, a Dev Environment is configured to have 16GB of persistent storage.</p>"""
    vpc_connection_name: NotRequired["capo_codecatalyst.types.name_string.NameString"]
    """<p>The name of the connection used to connect to Amazon VPC used when the Dev Environment was created, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDevEnvironmentResponse) -> dict:
    out: dict = {}
    out["spaceName"] = value["space_name"]
    out["projectName"] = value["project_name"]
    out["id"] = value["id"]
    import capo_codecatalyst._protocol.serialize

    out["lastUpdatedTime"] = capo_codecatalyst._protocol.serialize.fmt_date_time(
        value["last_updated_time"]
    )
    out["creatorId"] = value["creator_id"]
    out["status"] = value["status"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import capo_codecatalyst.types.dev_environment_repository_summaries

    out["repositories"] = (
        capo_codecatalyst.types.dev_environment_repository_summaries.serialize_json(
            value["repositories"]
        )
    )
    if "alias" in value:
        out["alias"] = value["alias"]
    if "ides" in value:
        import capo_codecatalyst.types.ides

        out["ides"] = capo_codecatalyst.types.ides.serialize_json(value["ides"])
    out["instanceType"] = value["instance_type"]
    out["inactivityTimeoutMinutes"] = value.get("inactivity_timeout_minutes", 0)
    import capo_codecatalyst.types.persistent_storage

    out["persistentStorage"] = (
        capo_codecatalyst.types.persistent_storage.serialize_json(
            value["persistent_storage"]
        )
    )
    if "vpc_connection_name" in value:
        out["vpcConnectionName"] = value["vpc_connection_name"]
    return out


def deserialize_json(data: dict) -> GetDevEnvironmentResponse:
    out: GetDevEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("spaceName") is not None:
        out["space_name"] = data["spaceName"]
    else:
        raise DeserializationError("GetDevEnvironmentResponse.space_name required")
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError("GetDevEnvironmentResponse.project_name required")
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetDevEnvironmentResponse.id required")
    if data.get("lastUpdatedTime") is not None:
        import datetime

        out["last_updated_time"] = datetime.datetime.fromisoformat(
            data["lastUpdatedTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError(
            "GetDevEnvironmentResponse.last_updated_time required"
        )
    if data.get("creatorId") is not None:
        out["creator_id"] = data["creatorId"]
    else:
        raise DeserializationError("GetDevEnvironmentResponse.creator_id required")
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetDevEnvironmentResponse.status required")
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("repositories") is not None:
        import capo_codecatalyst.types.dev_environment_repository_summaries

        out["repositories"] = (
            capo_codecatalyst.types.dev_environment_repository_summaries.deserialize_json(
                data["repositories"]
            )
        )
    else:
        raise DeserializationError("GetDevEnvironmentResponse.repositories required")
    if data.get("alias") is not None:
        out["alias"] = data["alias"]
    if data.get("ides") is not None:
        import capo_codecatalyst.types.ides

        out["ides"] = capo_codecatalyst.types.ides.deserialize_json(data["ides"])
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    else:
        raise DeserializationError("GetDevEnvironmentResponse.instance_type required")
    if data.get("inactivityTimeoutMinutes") is not None:
        out["inactivity_timeout_minutes"] = data["inactivityTimeoutMinutes"]
    else:
        out["inactivity_timeout_minutes"] = 0
    if data.get("persistentStorage") is not None:
        import capo_codecatalyst.types.persistent_storage

        out["persistent_storage"] = (
            capo_codecatalyst.types.persistent_storage.deserialize_json(
                data["persistentStorage"]
            )
        )
    else:
        raise DeserializationError(
            "GetDevEnvironmentResponse.persistent_storage required"
        )
    if data.get("vpcConnectionName") is not None:
        out["vpc_connection_name"] = data["vpcConnectionName"]
    return out
