"""Generated from Smithy shape ``com.amazonaws.quicksight#ActionConnector``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_quicksight.types.action_connector_description
    import capo_quicksight.types.action_connector_error
    import capo_quicksight.types.action_connector_name
    import capo_quicksight.types.action_connector_type
    import capo_quicksight.types.action_id_list
    import capo_quicksight.types.arn
    import capo_quicksight.types.read_auth_config
    import capo_quicksight.types.resource_status
    import capo_quicksight.types.short_restrictive_resource_id


class ActionConnector(TypedDict, closed=True):
    arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the action connector.</p>"""
    action_connector_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The unique identifier of the action connector.</p>"""
    type: "capo_quicksight.types.action_connector_type.ActionConnectorType"
    """<p>The type of action connector.</p>"""
    name: "capo_quicksight.types.action_connector_name.ActionConnectorName"
    """<p>The name of the action connector.</p>"""
    created_time: NotRequired["datetime.datetime"]
    """<p>The timestamp when the action connector was created.</p>"""
    last_updated_time: "datetime.datetime"
    """<p>The date and time when the action connector was last updated.</p>"""
    status: NotRequired["capo_quicksight.types.resource_status.ResourceStatus"]
    """<p>The current status of the action connector.</p>"""
    error: NotRequired[
        "capo_quicksight.types.action_connector_error.ActionConnectorError"
    ]
    """<p>Error information if the action connector is in an error state.</p>"""
    description: NotRequired[
        "capo_quicksight.types.action_connector_description.ActionConnectorDescription"
    ]
    """<p>The description of the action connector.</p>"""
    authentication_config: NotRequired[
        "capo_quicksight.types.read_auth_config.ReadAuthConfig"
    ]
    """<p>The authentication configuration used to connect to the external service.</p>"""
    enabled_actions: NotRequired["capo_quicksight.types.action_id_list.ActionIdList"]
    """<p>The list of actions that are enabled for this connector.</p>"""
    vpc_connection_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The ARN of the VPC connection used for secure connectivity to the external service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionConnector) -> dict:
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
    if "description" in value:
        out["Description"] = value["description"]
    if "authentication_config" in value:
        import capo_quicksight.types.read_auth_config

        out["AuthenticationConfig"] = (
            capo_quicksight.types.read_auth_config.serialize_json(
                value["authentication_config"]
            )
        )
    if "enabled_actions" in value:
        import capo_quicksight.types.action_id_list

        out["EnabledActions"] = capo_quicksight.types.action_id_list.serialize_json(
            value["enabled_actions"]
        )
    if "vpc_connection_arn" in value:
        out["VpcConnectionArn"] = value["vpc_connection_arn"]
    return out


def deserialize_json(data: dict) -> ActionConnector:
    out: ActionConnector = {}  # type: ignore[typeddict-item]
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
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("AuthenticationConfig") is not None:
        import capo_quicksight.types.read_auth_config

        out["authentication_config"] = (
            capo_quicksight.types.read_auth_config.deserialize_json(
                data["AuthenticationConfig"]
            )
        )
    if data.get("EnabledActions") is not None:
        import capo_quicksight.types.action_id_list

        out["enabled_actions"] = capo_quicksight.types.action_id_list.deserialize_json(
            data["EnabledActions"]
        )
    if data.get("VpcConnectionArn") is not None:
        out["vpc_connection_arn"] = data["VpcConnectionArn"]
    return out


def redact_sensitive(value: ActionConnector) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "authentication_config" in value:
        import capo_quicksight.types.read_auth_config

        out["authentication_config"] = (
            capo_quicksight.types.read_auth_config.redact_sensitive(
                value["authentication_config"]
            )
        )
    return out
