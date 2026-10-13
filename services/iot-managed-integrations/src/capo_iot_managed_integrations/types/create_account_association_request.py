"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateAccountAssociationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.account_association_description
    import capo_iot_managed_integrations.types.account_association_name
    import capo_iot_managed_integrations.types.client_token
    import capo_iot_managed_integrations.types.connector_destination_id
    import capo_iot_managed_integrations.types.general_authorization_name
    import capo_iot_managed_integrations.types.tags_map


class CreateAccountAssociationRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_iot_managed_integrations.types.client_token.ClientToken"
    ]
    """<p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>"""
    connector_destination_id: "capo_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
    """<p>The identifier of the connector destination.</p>"""
    name: NotRequired[
        "capo_iot_managed_integrations.types.account_association_name.AccountAssociationName"
    ]
    """<p>The name of the destination for the new account association.</p>"""
    description: NotRequired[
        "capo_iot_managed_integrations.types.account_association_description.AccountAssociationDescription"
    ]
    """<p>A description of the account association request.</p>"""
    tags: NotRequired["capo_iot_managed_integrations.types.tags_map.TagsMap"]
    """<p>A set of key/value pairs that are used to manage the account association.</p>"""
    general_authorization: NotRequired[
        "capo_iot_managed_integrations.types.general_authorization_name.GeneralAuthorizationName"
    ]
    """<p>The General Authorization reference by authorization material name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccountAssociationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["ConnectorDestinationId"] = value["connector_destination_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
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


def deserialize_json(data: dict) -> CreateAccountAssociationRequest:
    out: CreateAccountAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("ConnectorDestinationId") is not None:
        out["connector_destination_id"] = data["ConnectorDestinationId"]
    else:
        raise DeserializationError(
            "CreateAccountAssociationRequest.connector_destination_id required"
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
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


def redact_sensitive(value: CreateAccountAssociationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
