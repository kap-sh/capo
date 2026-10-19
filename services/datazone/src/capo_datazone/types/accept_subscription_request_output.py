"""Generated from Smithy shape ``com.amazonaws.datazone#AcceptSubscriptionRequestOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.decision_comment
    import capo_datazone.types.domain_id
    import capo_datazone.types.metadata_forms
    import capo_datazone.types.request_reason
    import capo_datazone.types.subscribed_listings
    import capo_datazone.types.subscribed_principals
    import capo_datazone.types.subscription_id
    import capo_datazone.types.subscription_request_id
    import capo_datazone.types.subscription_request_status
    import capo_datazone.types.updated_at
    import capo_datazone.types.updated_by


class AcceptSubscriptionRequestOutput(TypedDict, closed=True):
    id: "capo_datazone.types.subscription_request_id.SubscriptionRequestId"
    """<p>The identifier of the subscription request.</p>"""
    created_by: "capo_datazone.types.created_by.CreatedBy"
    """<p>Specifies the Amazon DataZone user that accepted the specified subscription request.</p>"""
    updated_by: NotRequired["capo_datazone.types.updated_by.UpdatedBy"]
    """<p>Specifies the Amazon DataZone user who updated the subscription request.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The unique identifier of the Amazon DataZone domain where the specified subscription request was accepted.</p>"""
    status: "capo_datazone.types.subscription_request_status.SubscriptionRequestStatus"
    """<p>Specifies the status of the subscription request.</p>"""
    created_at: "capo_datazone.types.created_at.CreatedAt"
    """<p>The timestamp that specifies when the subscription request was accepted.</p>"""
    updated_at: "capo_datazone.types.updated_at.UpdatedAt"
    """<p>Specifies the timestamp when subscription request was updated.</p>"""
    request_reason: "capo_datazone.types.request_reason.RequestReason"
    """<p>Specifies the reason for requesting a subscription to the asset.</p>"""
    subscribed_principals: (
        "capo_datazone.types.subscribed_principals.SubscribedPrincipals"
    )
    """<p>Specifies the Amazon DataZone users who are subscribed to the asset specified in the subscription request.</p>"""
    subscribed_listings: "capo_datazone.types.subscribed_listings.SubscribedListings"
    """<p>Specifies the asset for which the subscription request was created.</p>"""
    reviewer_id: NotRequired["str"]
    """<p>Specifes the ID of the Amazon DataZone user who reviewed the subscription request.</p>"""
    decision_comment: NotRequired[
        "capo_datazone.types.decision_comment.DecisionComment"
    ]
    """<p>Specifies the reason for accepting the subscription request.</p>"""
    existing_subscription_id: NotRequired[
        "capo_datazone.types.subscription_id.SubscriptionId"
    ]
    """<p>The ID of the existing subscription.</p>"""
    metadata_forms: NotRequired["capo_datazone.types.metadata_forms.MetadataForms"]
    """<p>The metadata form in the subscription request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptSubscriptionRequestOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["createdBy"] = value["created_by"]
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    out["domainId"] = value["domain_id"]
    import capo_datazone.types.subscription_request_status

    out["status"] = capo_datazone.types.subscription_request_status.serialize_json(
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
    out["requestReason"] = value["request_reason"]
    import capo_datazone.types.subscribed_principals

    out["subscribedPrincipals"] = (
        capo_datazone.types.subscribed_principals.serialize_json(
            value["subscribed_principals"]
        )
    )
    import capo_datazone.types.subscribed_listings

    out["subscribedListings"] = capo_datazone.types.subscribed_listings.serialize_json(
        value["subscribed_listings"]
    )
    if "reviewer_id" in value:
        out["reviewerId"] = value["reviewer_id"]
    if "decision_comment" in value:
        out["decisionComment"] = value["decision_comment"]
    if "existing_subscription_id" in value:
        out["existingSubscriptionId"] = value["existing_subscription_id"]
    if "metadata_forms" in value:
        import capo_datazone.types.metadata_forms

        out["metadataForms"] = capo_datazone.types.metadata_forms.serialize_json(
            value["metadata_forms"]
        )
    return out


def deserialize_json(data: dict) -> AcceptSubscriptionRequestOutput:
    out: AcceptSubscriptionRequestOutput = {}  # type: ignore[typeddict-item]
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
        import capo_datazone.types.subscription_request_status

        out["status"] = (
            capo_datazone.types.subscription_request_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_datazone.types.subscription_request_status.SubscriptionRequestStatus",
            "",
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
    if data.get("requestReason") is not None:
        out["request_reason"] = data["requestReason"]
    else:
        out["request_reason"] = ""
    if data.get("subscribedPrincipals") is not None:
        import capo_datazone.types.subscribed_principals

        out["subscribed_principals"] = (
            capo_datazone.types.subscribed_principals.deserialize_json(
                data["subscribedPrincipals"]
            )
        )
    else:
        out["subscribed_principals"] = []
    if data.get("subscribedListings") is not None:
        import capo_datazone.types.subscribed_listings

        out["subscribed_listings"] = (
            capo_datazone.types.subscribed_listings.deserialize_json(
                data["subscribedListings"]
            )
        )
    else:
        out["subscribed_listings"] = []
    if data.get("reviewerId") is not None:
        out["reviewer_id"] = data["reviewerId"]
    if data.get("decisionComment") is not None:
        out["decision_comment"] = data["decisionComment"]
    if data.get("existingSubscriptionId") is not None:
        out["existing_subscription_id"] = data["existingSubscriptionId"]
    if data.get("metadataForms") is not None:
        import capo_datazone.types.metadata_forms

        out["metadata_forms"] = capo_datazone.types.metadata_forms.deserialize_json(
            data["metadataForms"]
        )
    return out


def redact_sensitive(value: AcceptSubscriptionRequestOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "request_reason" in value:
        out["request_reason"] = "*** Sensitive Data Redacted ***"
    if "subscribed_principals" in value:
        import capo_datazone.types.subscribed_principals

        out["subscribed_principals"] = (
            capo_datazone.types.subscribed_principals.redact_sensitive(
                value["subscribed_principals"]
            )
        )
    if "subscribed_listings" in value:
        import capo_datazone.types.subscribed_listings

        out["subscribed_listings"] = (
            capo_datazone.types.subscribed_listings.redact_sensitive(
                value["subscribed_listings"]
            )
        )
    if "decision_comment" in value:
        out["decision_comment"] = "*** Sensitive Data Redacted ***"
    if "metadata_forms" in value:
        import capo_datazone.types.metadata_forms

        out["metadata_forms"] = capo_datazone.types.metadata_forms.redact_sensitive(
            value["metadata_forms"]
        )
    return out
