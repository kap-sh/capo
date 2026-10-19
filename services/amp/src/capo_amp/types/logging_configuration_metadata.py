"""Generated from Smithy shape ``com.amazonaws.amp#LoggingConfigurationMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_amp.types.log_group_arn
    import capo_amp.types.logging_configuration_status
    import capo_amp.types.workspace_id


class LoggingConfigurationMetadata(TypedDict, closed=True):
    status: "capo_amp.types.logging_configuration_status.LoggingConfigurationStatus"
    """<p>The current status of the logging configuration.</p>"""
    workspace: "capo_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace the logging configuration is for.</p>"""
    log_group_arn: "capo_amp.types.log_group_arn.LogGroupArn"
    """<p>The ARN of the CloudWatch log group to which the vended log data will be published.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time that the logging configuration was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time that the logging configuration was most recently changed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoggingConfigurationMetadata) -> dict:
    out: dict = {}
    import capo_amp.types.logging_configuration_status

    out["status"] = capo_amp.types.logging_configuration_status.serialize_json(
        value["status"]
    )
    out["workspace"] = value["workspace"]
    out["logGroupArn"] = value["log_group_arn"]
    import capo_amp.types._prelude.timestamp

    out["createdAt"] = capo_amp.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_amp.types._prelude.timestamp

    out["modifiedAt"] = capo_amp.types._prelude.timestamp.serialize_json(
        value["modified_at"]
    )
    return out


def deserialize_json(data: dict) -> LoggingConfigurationMetadata:
    out: LoggingConfigurationMetadata = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_amp.types.logging_configuration_status

        out["status"] = capo_amp.types.logging_configuration_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("LoggingConfigurationMetadata.status required")
    if data.get("workspace") is not None:
        out["workspace"] = data["workspace"]
    else:
        out["workspace"] = ""
    if data.get("logGroupArn") is not None:
        out["log_group_arn"] = data["logGroupArn"]
    else:
        out["log_group_arn"] = ""
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
