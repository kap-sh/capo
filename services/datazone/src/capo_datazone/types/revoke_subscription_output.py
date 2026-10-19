"""Generated from Smithy shape ``com.amazonaws.datazone#RevokeSubscriptionOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.domain_id
    import capo_datazone.types.subscribed_listing
    import capo_datazone.types.subscribed_principal
    import capo_datazone.types.subscription_id
    import capo_datazone.types.subscription_request_id
    import capo_datazone.types.subscription_status
    import capo_datazone.types.updated_at
    import capo_datazone.types.updated_by


class RevokeSubscriptionOutput(TypedDict, closed=True):
    id: "capo_datazone.types.subscription_id.SubscriptionId"
    """<p>The identifier of the revoked subscription.</p>"""
    created_by: "capo_datazone.types.created_by.CreatedBy"
    """<p>The identifier of the user who revoked the subscription.</p>"""
    updated_by: NotRequired["capo_datazone.types.updated_by.UpdatedBy"]
    """<p>The Amazon DataZone user who revoked the subscription.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain where you want to revoke a subscription.</p>"""
    status: "capo_datazone.types.subscription_status.SubscriptionStatus"
    """<p>The status of the revoked subscription.</p>"""
    created_at: "capo_datazone.types.created_at.CreatedAt"
    """<p>The timestamp of when the subscription was revoked.</p>"""
    updated_at: "capo_datazone.types.updated_at.UpdatedAt"
    """<p>The timestamp of when the subscription was revoked.</p>"""
    subscribed_principal: "capo_datazone.types.subscribed_principal.SubscribedPrincipal"
    """<p>The subscribed principal of the revoked subscription.</p>"""
    subscribed_listing: "capo_datazone.types.subscribed_listing.SubscribedListing"
    """<p>The subscribed listing of the revoked subscription.</p>"""
    subscription_request_id: NotRequired[
        "capo_datazone.types.subscription_request_id.SubscriptionRequestId"
    ]
    """<p>The identifier of the subscription request for the revoked subscription.</p>"""
    retain_permissions: NotRequired["bool"]
    """<p>Specifies whether permissions are retained when the subscription is revoked.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevokeSubscriptionOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["createdBy"] = value["created_by"]
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    out["domainId"] = value["domain_id"]
    import capo_datazone.types.subscription_status

    out["status"] = capo_datazone.types.subscription_status.serialize_json(
        value["status"]
    )
    import capo_datazone.types.created_at

    out["createdAt"] = capo_datazone.types.created_at.serialize_json(
        value["created_at"]
    )
    import capo_datazone.types.updated_at

    out["updatedAt"] = capo_datazone.types.updated_at.serialize_json(
        value["updated_at"]
    )
    import capo_datazone.types.subscribed_principal

    out["subscribedPrincipal"] = (
        capo_datazone.types.subscribed_principal.serialize_json(
            value["subscribed_principal"]
        )
    )
    import capo_datazone.types.subscribed_listing

    out["subscribedListing"] = capo_datazone.types.subscribed_listing.serialize_json(
        value["subscribed_listing"]
    )
    if "subscription_request_id" in value:
        out["subscriptionRequestId"] = value["subscription_request_id"]
    if "retain_permissions" in value:
        out["retainPermissions"] = value["retain_permissions"]
    return out


def deserialize_json(data: dict) -> RevokeSubscriptionOutput:
    out: RevokeSubscriptionOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("status") is not None:
        import capo_datazone.types.subscription_status

        out["status"] = capo_datazone.types.subscription_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_datazone.types.subscription_status.SubscriptionStatus", ""
        )
    if data.get("createdAt") is not None:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_datazone.types.updated_at

        out["updated_at"] = capo_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("subscribedPrincipal") is not None:
        import capo_datazone.types.subscribed_principal

        out["subscribed_principal"] = (
            capo_datazone.types.subscribed_principal.deserialize_json(
                data["subscribedPrincipal"]
            )
        )
    else:
        import capo_datazone.types._unknown

        out["subscribed_principal"] = capo_datazone.types._unknown.UnknownUnionMember(
            ""
        )
    if data.get("subscribedListing") is not None:
        import capo_datazone.types.subscribed_listing

        out["subscribed_listing"] = (
            capo_datazone.types.subscribed_listing.deserialize_json(
                data["subscribedListing"]
            )
        )
    else:
        raise DeserializationError(
            "RevokeSubscriptionOutput.subscribed_listing required"
        )
    if data.get("subscriptionRequestId") is not None:
        out["subscription_request_id"] = data["subscriptionRequestId"]
    if data.get("retainPermissions") is not None:
        out["retain_permissions"] = data["retainPermissions"]
    return out


def redact_sensitive(value: RevokeSubscriptionOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "subscribed_principal" in value:
        import capo_datazone.types.subscribed_principal

        out["subscribed_principal"] = (
            capo_datazone.types.subscribed_principal.redact_sensitive(
                value["subscribed_principal"]
            )
        )
    if "subscribed_listing" in value:
        import capo_datazone.types.subscribed_listing

        out["subscribed_listing"] = (
            capo_datazone.types.subscribed_listing.redact_sensitive(
                value["subscribed_listing"]
            )
        )
    return out
