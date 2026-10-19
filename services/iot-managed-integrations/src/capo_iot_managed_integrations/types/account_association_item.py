"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#AccountAssociationItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.account_association_arn
    import capo_iot_managed_integrations.types.account_association_description
    import capo_iot_managed_integrations.types.account_association_error_message
    import capo_iot_managed_integrations.types.account_association_id
    import capo_iot_managed_integrations.types.account_association_name
    import capo_iot_managed_integrations.types.association_state
    import capo_iot_managed_integrations.types.connector_destination_id


class AccountAssociationItem(TypedDict, closed=True):
    account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId"
    """<p>The unique identifier of the account association.</p>"""
    association_state: (
        "capo_iot_managed_integrations.types.association_state.AssociationState"
    )
    """<p>The current state of the account association, indicating its status in the association lifecycle.</p>"""
    error_message: NotRequired[
        "capo_iot_managed_integrations.types.account_association_error_message.AccountAssociationErrorMessage"
    ]
    """<p>The error message explaining any issues with the account association, if applicable.</p>"""
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
    """<p>A description of the account association.</p>"""
    arn: NotRequired[
        "capo_iot_managed_integrations.types.account_association_arn.AccountAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the account association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountAssociationItem) -> dict:
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
    return out


def deserialize_json(data: dict) -> AccountAssociationItem:
    out: AccountAssociationItem = {}  # type: ignore[typeddict-item]
    if data.get("AccountAssociationId") is not None:
        out["account_association_id"] = data["AccountAssociationId"]
    else:
        out["account_association_id"] = ""
    if data.get("AssociationState") is not None:
        import capo_iot_managed_integrations.types.association_state

        out["association_state"] = (
            capo_iot_managed_integrations.types.association_state.deserialize_json(
                data["AssociationState"]
            )
        )
    else:
        import typing

        out["association_state"] = typing.cast(
            "capo_iot_managed_integrations.types.association_state.AssociationState", ""
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
    return out
