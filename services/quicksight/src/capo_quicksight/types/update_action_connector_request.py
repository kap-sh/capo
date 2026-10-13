"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateActionConnectorRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.action_connector_description
    import capo_quicksight.types.action_connector_name
    import capo_quicksight.types.arn
    import capo_quicksight.types.auth_config
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.short_restrictive_resource_id


class UpdateActionConnectorRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID that contains the action connector to update.</p>"""
    action_connector_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The unique identifier of the action connector to update.</p>"""
    name: "capo_quicksight.types.action_connector_name.ActionConnectorName"
    """<p>The new name for the action connector.</p>"""
    authentication_config: "capo_quicksight.types.auth_config.AuthConfig"
    """<p>The updated authentication configuration for connecting to the external service.</p>"""
    description: NotRequired[
        "capo_quicksight.types.action_connector_description.ActionConnectorDescription"
    ]
    """<p>The updated description of the action connector.</p>"""
    vpc_connection_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The updated ARN of the VPC connection to use for secure connectivity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateActionConnectorRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_quicksight.types.auth_config

    out["AuthenticationConfig"] = capo_quicksight.types.auth_config.serialize_json(
        value["authentication_config"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "vpc_connection_arn" in value:
        out["VpcConnectionArn"] = value["vpc_connection_arn"]
    return out


def deserialize_json(data: dict) -> UpdateActionConnectorRequest:
    out: UpdateActionConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateActionConnectorRequest.name required")
    if data.get("AuthenticationConfig") is not None:
        import capo_quicksight.types.auth_config

        out["authentication_config"] = (
            capo_quicksight.types.auth_config.deserialize_json(
                data["AuthenticationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateActionConnectorRequest.authentication_config required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("VpcConnectionArn") is not None:
        out["vpc_connection_arn"] = data["VpcConnectionArn"]
    return out


def redact_sensitive(value: UpdateActionConnectorRequest) -> dict[str, Any]:
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
