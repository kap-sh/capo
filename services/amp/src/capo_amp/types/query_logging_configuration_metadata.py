"""Generated from Smithy shape ``com.amazonaws.amp#QueryLoggingConfigurationMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_amp.types.logging_destinations
    import capo_amp.types.query_logging_configuration_status
    import capo_amp.types.workspace_id


class QueryLoggingConfigurationMetadata(TypedDict, closed=True):
    status: "capo_amp.types.query_logging_configuration_status.QueryLoggingConfigurationStatus"
    """<p>The current status of the query logging configuration.</p>"""
    workspace: "capo_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace associated with this query logging configuration.</p>"""
    destinations: "capo_amp.types.logging_destinations.LoggingDestinations"
    """<p>The configured destinations for the query logging configuration.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time when the query logging configuration was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time when the query logging configuration was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryLoggingConfigurationMetadata) -> dict:
    out: dict = {}
    import capo_amp.types.query_logging_configuration_status

    out["status"] = capo_amp.types.query_logging_configuration_status.serialize_json(
        value["status"]
    )
    out["workspace"] = value["workspace"]
    import capo_amp.types.logging_destinations

    out["destinations"] = capo_amp.types.logging_destinations.serialize_json(
        value["destinations"]
    )
    import capo_amp.types._prelude.timestamp

    out["createdAt"] = capo_amp.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_amp.types._prelude.timestamp

    out["modifiedAt"] = capo_amp.types._prelude.timestamp.serialize_json(
        value["modified_at"]
    )
    return out


def deserialize_json(data: dict) -> QueryLoggingConfigurationMetadata:
    out: QueryLoggingConfigurationMetadata = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_amp.types.query_logging_configuration_status

        out["status"] = (
            capo_amp.types.query_logging_configuration_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("QueryLoggingConfigurationMetadata.status required")
    if data.get("workspace") is not None:
        out["workspace"] = data["workspace"]
    else:
        out["workspace"] = ""
    if data.get("destinations") is not None:
        import capo_amp.types.logging_destinations

        out["destinations"] = capo_amp.types.logging_destinations.deserialize_json(
            data["destinations"]
        )
    else:
        out["destinations"] = []
    if data.get("createdAt") is not None:
        import capo_amp.types._prelude.timestamp

        out["created_at"] = capo_amp.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("modifiedAt") is not None:
        import capo_amp.types._prelude.timestamp

        out["modified_at"] = capo_amp.types._prelude.timestamp.deserialize_json(
            data["modifiedAt"]
        )
    else:
        import datetime

        out["modified_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
