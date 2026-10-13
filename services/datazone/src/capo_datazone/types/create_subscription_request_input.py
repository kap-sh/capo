"""Generated from Smithy shape ``com.amazonaws.datazone#CreateSubscriptionRequestInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.accepted_asset_scopes
    import capo_datazone.types.asset_permissions
    import capo_datazone.types.domain_id
    import capo_datazone.types.metadata_form_inputs
    import capo_datazone.types.request_reason
    import capo_datazone.types.subscribed_listing_inputs
    import capo_datazone.types.subscribed_principal_inputs


class CreateSubscriptionRequestInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the subscription request is created.</p>"""
    subscribed_principals: (
        "capo_datazone.types.subscribed_principal_inputs.SubscribedPrincipalInputs"
    )
    """<p>The Amazon DataZone principals for whom the subscription request is created.</p>"""
    subscribed_listings: (
        "capo_datazone.types.subscribed_listing_inputs.SubscribedListingInputs"
    )
    """<p>The published asset for which the subscription grant is to be created.</p>"""
    request_reason: "capo_datazone.types.request_reason.RequestReason"
    """<p>The reason for the subscription request.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""
    metadata_forms: NotRequired[
        "capo_datazone.types.metadata_form_inputs.MetadataFormInputs"
    ]
    """<p>The metadata form included in the subscription request.</p>"""
    asset_permissions: NotRequired[
        "capo_datazone.types.asset_permissions.AssetPermissions"
    ]
    """<p>The asset permissions of the subscription request.</p>"""
    asset_scopes: NotRequired[
        "capo_datazone.types.accepted_asset_scopes.AcceptedAssetScopes"
    ]
    """<p>The asset scopes of the subscription request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSubscriptionRequestInput) -> dict:
    out: dict = {}
    import capo_datazone.types.subscribed_principal_inputs

    out["subscribedPrincipals"] = (
        capo_datazone.types.subscribed_principal_inputs.serialize_json(
            value["subscribed_principals"]
        )
    )
    import capo_datazone.types.subscribed_listing_inputs

    out["subscribedListings"] = (
        capo_datazone.types.subscribed_listing_inputs.serialize_json(
            value["subscribed_listings"]
        )
    )
    out["requestReason"] = value["request_reason"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "metadata_forms" in value:
        import capo_datazone.types.metadata_form_inputs

        out["metadataForms"] = capo_datazone.types.metadata_form_inputs.serialize_json(
            value["metadata_forms"]
        )
    if "asset_permissions" in value:
        import capo_datazone.types.asset_permissions

        out["assetPermissions"] = capo_datazone.types.asset_permissions.serialize_json(
            value["asset_permissions"]
        )
    if "asset_scopes" in value:
        import capo_datazone.types.accepted_asset_scopes

        out["assetScopes"] = capo_datazone.types.accepted_asset_scopes.serialize_json(
            value["asset_scopes"]
        )
    return out


def deserialize_json(data: dict) -> CreateSubscriptionRequestInput:
    out: CreateSubscriptionRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("subscribedPrincipals") is not None:
        import capo_datazone.types.subscribed_principal_inputs

        out["subscribed_principals"] = (
            capo_datazone.types.subscribed_principal_inputs.deserialize_json(
                data["subscribedPrincipals"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSubscriptionRequestInput.subscribed_principals required"
        )
    if data.get("subscribedListings") is not None:
        import capo_datazone.types.subscribed_listing_inputs

        out["subscribed_listings"] = (
            capo_datazone.types.subscribed_listing_inputs.deserialize_json(
                data["subscribedListings"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSubscriptionRequestInput.subscribed_listings required"
        )
    if data.get("requestReason") is not None:
        out["request_reason"] = data["requestReason"]
    else:
        raise DeserializationError(
            "CreateSubscriptionRequestInput.request_reason required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("metadataForms") is not None:
        import capo_datazone.types.metadata_form_inputs

        out["metadata_forms"] = (
            capo_datazone.types.metadata_form_inputs.deserialize_json(
                data["metadataForms"]
            )
        )
    if data.get("assetPermissions") is not None:
        import capo_datazone.types.asset_permissions

        out["asset_permissions"] = (
            capo_datazone.types.asset_permissions.deserialize_json(
                data["assetPermissions"]
            )
        )
    if data.get("assetScopes") is not None:
        import capo_datazone.types.accepted_asset_scopes

        out["asset_scopes"] = (
            capo_datazone.types.accepted_asset_scopes.deserialize_json(
                data["assetScopes"]
            )
        )
    return out


def redact_sensitive(value: CreateSubscriptionRequestInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "request_reason" in value:
        out["request_reason"] = "*** Sensitive Data Redacted ***"
    if "metadata_forms" in value:
        import capo_datazone.types.metadata_form_inputs

        out["metadata_forms"] = (
            capo_datazone.types.metadata_form_inputs.redact_sensitive(
                value["metadata_forms"]
            )
        )
    return out
