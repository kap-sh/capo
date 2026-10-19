"""Generated from Smithy shape ``com.amazonaws.quicksight#ActionConnectorSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_quicksight.types.action_connector_error
    import capo_quicksight.types.action_connector_name
    import capo_quicksight.types.action_connector_type
    import capo_quicksight.types.arn
    import capo_quicksight.types.resource_status
    import capo_quicksight.types.short_restrictive_resource_id


class ActionConnectorSummary(TypedDict, closed=True):
    arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the action connector.</p>"""
    action_connector_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The unique identifier of the action connector.</p>"""
    type: "capo_quicksight.types.action_connector_type.ActionConnectorType"
    """<p>The type of action connector (e.g., SALESFORCE, JIRA, CUSTOM, BEDROCK).</p>"""
    name: "capo_quicksight.types.action_connector_name.ActionConnectorName"
    """<p>The name of the action connector.</p>"""
    created_time: NotRequired["datetime.datetime"]
    """<p>The date and time when the action connector was created.</p>"""
    last_updated_time: "datetime.datetime"
    """<p>The date and time when the action connector was last updated.</p>"""
    status: NotRequired["capo_quicksight.types.resource_status.ResourceStatus"]
    """<p>The current status of the action connector.</p>"""
    error: NotRequired[
        "capo_quicksight.types.action_connector_error.ActionConnectorError"
    ]
    """<p>Error information if the action connector is in an error state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionConnectorSummary) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["ActionConnectorId"] = value["action_connector_id"]
    import capo_quicksight.types.action_connector_type

    out["Type"] = capo_quicksight.types.action_connector_type.serialize_json(
        value["type"]
    )
    out["Name"] = value["name"]
    if "created_time" in value:
        import capo_quicksight.types._prelude.timestamp

        out["CreatedTime"] = capo_quicksight.types._prelude.timestamp.serialize_json(
            value["created_time"]
        )
    import capo_quicksight.types._prelude.timestamp

    out["LastUpdatedTime"] = capo_quicksight.types._prelude.timestamp.serialize_json(
        value["last_updated_time"]
    )
    if "status" in value:
        import capo_quicksight.types.resource_status

        out["Status"] = capo_quicksight.types.resource_status.serialize_json(
            value["status"]
        )
    if "error" in value:
        import capo_quicksight.types.action_connector_error

        out["Error"] = capo_quicksight.types.action_connector_error.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> ActionConnectorSummary:
    out: ActionConnectorSummary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("ActionConnectorId") is not None:
        out["action_connector_id"] = data["ActionConnectorId"]
    else:
        out["action_connector_id"] = ""
    if data.get("Type") is not None:
        import capo_quicksight.types.action_connector_type

        out["type"] = capo_quicksight.types.action_connector_type.deserialize_json(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_quicksight.types.action_connector_type.ActionConnectorType", ""
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("CreatedTime") is not None:
        import capo_quicksight.types._prelude.timestamp

        out["created_time"] = capo_quicksight.types._prelude.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_quicksight.types._prelude.timestamp

        out["last_updated_time"] = (
            capo_quicksight.types._prelude.timestamp.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    else:
        import datetime

        out["last_updated_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("Status") is not None:
        import capo_quicksight.types.resource_status

        out["status"] = capo_quicksight.types.resource_status.deserialize_json(
            data["Status"]
        )
    if data.get("Error") is not None:
        import capo_quicksight.types.action_connector_error

        out["error"] = capo_quicksight.types.action_connector_error.deserialize_json(
            data["Error"]
        )
    return out


def redact_sensitive(value: ActionConnectorSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
