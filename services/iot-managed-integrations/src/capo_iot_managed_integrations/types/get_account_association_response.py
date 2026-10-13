"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetAccountAssociationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.account_association_arn
    import capo_iot_managed_integrations.types.account_association_description
    import capo_iot_managed_integrations.types.account_association_error_message
    import capo_iot_managed_integrations.types.account_association_id
    import capo_iot_managed_integrations.types.account_association_name
    import capo_iot_managed_integrations.types.association_state
    import capo_iot_managed_integrations.types.connector_destination_id
    import capo_iot_managed_integrations.types.general_authorization_name
    import capo_iot_managed_integrations.types.o_auth_authorization_url_output
    import capo_iot_managed_integrations.types.tags_map


class GetAccountAssociationResponse(TypedDict, closed=True):
    account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId"
    """<p>The unique identifier of the retrieved account association.</p>"""
    association_state: (
        "capo_iot_managed_integrations.types.association_state.AssociationState"
    )
    """<p>The current status state for the account association.</p>"""
    error_message: NotRequired[
        "capo_iot_managed_integrations.types.account_association_error_message.AccountAssociationErrorMessage"
    ]
    """<p>The error message explaining the current account association error.</p>"""
    connector_destination_id: NotRequired[
        "capo_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
    ]
    """<p>The identifier of the connector destination associated with this account association.</p>"""
    name: NotRequired[
        "capo_iot_managed_integrations.types.account_association_name.AccountAssociationName"
    ]
    """<p>The name of the account association.</p>"""
    description: NotRequired[
        "capo_iot_managed_integrations.types.account_association_description.AccountAssociationDescription"
    ]
    """<p>The description of the account association.</p>"""
    arn: NotRequired[
        "capo_iot_managed_integrations.types.account_association_arn.AccountAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the account association.</p>"""
    o_auth_authorization_url: "capo_iot_managed_integrations.types.o_auth_authorization_url_output.OAuthAuthorizationUrlOutput"
    """<p>Third party IoT platform OAuth authorization server URL backed with all the required parameters to perform end-user authentication. This field will be empty when using General Authorization flows that do not require OAuth.</p>"""
    tags: NotRequired["capo_iot_managed_integrations.types.tags_map.TagsMap"]
    """<p>A set of key/value pairs that are used to manage the account association.</p>"""
    general_authorization: NotRequired[
        "capo_iot_managed_integrations.types.general_authorization_name.GeneralAuthorizationName"
    ]
    """<p>The General Authorization reference by authorization material name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountAssociationResponse) -> dict:
    out: dict = {}
    out["AccountAssociationId"] = value["account_association_id"]
    import capo_iot_managed_integrations.types.association_state

    out["AssociationState"] = (
        capo_iot_managed_integrations.types.association_state.serialize_json(
            value["association_state"]
        )
    )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "connector_destination_id" in value:
        out["ConnectorDestinationId"] = value["connector_destination_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    out["OAuthAuthorizationUrl"] = value.get("o_auth_authorization_url", "")
    if "tags" in value:
        import capo_iot_managed_integrations.types.tags_map

        out["Tags"] = capo_iot_managed_integrations.types.tags_map.serialize_json(
            value["tags"]
        )
    if "general_authorization" in value:
        import capo_iot_managed_integrations.types.general_authorization_name

        out["GeneralAuthorization"] = (
            capo_iot_managed_integrations.types.general_authorization_name.serialize_json(
                value["general_authorization"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetAccountAssociationResponse:
    out: GetAccountAssociationResponse = {}  # type: ignore[typeddict-item]
    if data.get("AccountAssociationId") is not None:
        out["account_association_id"] = data["AccountAssociationId"]
    else:
        raise DeserializationError(
            "GetAccountAssociationResponse.account_association_id required"
        )
    if data.get("AssociationState") is not None:
        import capo_iot_managed_integrations.types.association_state

        out["association_state"] = (
            capo_iot_managed_integrations.types.association_state.deserialize_json(
                data["AssociationState"]
            )
        )
    else:
        raise DeserializationError(
            "GetAccountAssociationResponse.association_state required"
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("ConnectorDestinationId") is not None:
        out["connector_destination_id"] = data["ConnectorDestinationId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("OAuthAuthorizationUrl") is not None:
        out["o_auth_authorization_url"] = data["OAuthAuthorizationUrl"]
    else:
        out["o_auth_authorization_url"] = ""
    if data.get("Tags") is not None:
        import capo_iot_managed_integrations.types.tags_map

        out["tags"] = capo_iot_managed_integrations.types.tags_map.deserialize_json(
            data["Tags"]
        )
    if data.get("GeneralAuthorization") is not None:
        import capo_iot_managed_integrations.types.general_authorization_name

        out["general_authorization"] = (
            capo_iot_managed_integrations.types.general_authorization_name.deserialize_json(
                data["GeneralAuthorization"]
            )
        )
    return out


def redact_sensitive(value: GetAccountAssociationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "o_auth_authorization_url" in value:
        out["o_auth_authorization_url"] = "*** Sensitive Data Redacted ***"
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
