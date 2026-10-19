"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateActionConnectorRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.action_connector_description
    import capo_quicksight.types.action_connector_name
    import capo_quicksight.types.action_connector_type
    import capo_quicksight.types.arn
    import capo_quicksight.types.auth_config
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.resource_permission_list
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.tag_list


class CreateActionConnectorRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID associated with the action connector.</p>"""
    action_connector_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>A unique identifier for the action connector. This ID must be unique within the Amazon Web Services account. The <code>ActionConnectorId</code> must not start with the prefix <code>quicksuite-</code> </p>"""
    name: "capo_quicksight.types.action_connector_name.ActionConnectorName"
    """<p>A descriptive name for the action connector.</p>"""
    type: "capo_quicksight.types.action_connector_type.ActionConnectorType"
    """<p>The type of action connector.</p>"""
    authentication_config: "capo_quicksight.types.auth_config.AuthConfig"
    """<p>The authentication configuration for connecting to the external service. This includes the authentication type, base URL, and authentication metadata such as client credentials or API keys.</p>"""
    description: NotRequired[
        "capo_quicksight.types.action_connector_description.ActionConnectorDescription"
    ]
    """<p>An optional description of the action connector.</p>"""
    permissions: NotRequired[
        "capo_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>The permissions configuration that defines which users, groups, or namespaces can access this action connector and what operations they can perform.</p>"""
    vpc_connection_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The ARN of the VPC connection to use for secure connectivity to the external service.</p>"""
    tags: NotRequired["capo_quicksight.types.tag_list.TagList"]
    """<p>A list of tags to apply to the action connector for resource management and organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateActionConnectorRequest) -> dict:
    out: dict = {}
    out["ActionConnectorId"] = value["action_connector_id"]
    out["Name"] = value["name"]
    import capo_quicksight.types.action_connector_type

    out["Type"] = capo_quicksight.types.action_connector_type.serialize_json(
        value["type"]
    )
    import capo_quicksight.types.auth_config

    out["AuthenticationConfig"] = capo_quicksight.types.auth_config.serialize_json(
        value["authentication_config"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "permissions" in value:
        import capo_quicksight.types.resource_permission_list

        out["Permissions"] = (
            capo_quicksight.types.resource_permission_list.serialize_json(
                value["permissions"]
            )
        )
    if "vpc_connection_arn" in value:
        out["VpcConnectionArn"] = value["vpc_connection_arn"]
    if "tags" in value:
        import capo_quicksight.types.tag_list

        out["Tags"] = capo_quicksight.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateActionConnectorRequest:
    out: CreateActionConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("ActionConnectorId") is not None:
        out["action_connector_id"] = data["ActionConnectorId"]
    else:
        out["action_connector_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
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
    if data.get("AuthenticationConfig") is not None:
        import capo_quicksight.types.auth_config

        out["authentication_config"] = (
            capo_quicksight.types.auth_config.deserialize_json(
                data["AuthenticationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateActionConnectorRequest.authentication_config required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Permissions") is not None:
        import capo_quicksight.types.resource_permission_list

        out["permissions"] = (
            capo_quicksight.types.resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    if data.get("VpcConnectionArn") is not None:
        out["vpc_connection_arn"] = data["VpcConnectionArn"]
    if data.get("Tags") is not None:
        import capo_quicksight.types.tag_list

        out["tags"] = capo_quicksight.types.tag_list.deserialize_json(data["Tags"])
    return out


def redact_sensitive(value: CreateActionConnectorRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "authentication_config" in value:
        import capo_quicksight.types.auth_config

        out["authentication_config"] = (
            capo_quicksight.types.auth_config.redact_sensitive(
                value["authentication_config"]
            )
        )
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
