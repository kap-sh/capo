"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteSubscriptionGrantOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_id
    import capo_datazone.types.granted_entity
    import capo_datazone.types.subscribed_assets
    import capo_datazone.types.subscription_grant_id
    import capo_datazone.types.subscription_grant_overall_status
    import capo_datazone.types.subscription_id
    import capo_datazone.types.subscription_target_id
    import capo_datazone.types.updated_at
    import capo_datazone.types.updated_by


class DeleteSubscriptionGrantOutput(TypedDict, closed=True):
    id: "capo_datazone.types.subscription_grant_id.SubscriptionGrantId"
    """<p>The ID of the subscription grant that is deleted.</p>"""
    created_by: "capo_datazone.types.created_by.CreatedBy"
    """<p>The Amazon DataZone user who created the subscription grant that is deleted.</p>"""
    updated_by: NotRequired["capo_datazone.types.updated_by.UpdatedBy"]
    """<p>The Amazon DataZone user who updated the subscription grant that is deleted.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the subscription grant is deleted.</p>"""
    created_at: "capo_datazone.types.created_at.CreatedAt"
    """<p>The timestamp of when the subscription grant that is deleted was created.</p>"""
    updated_at: "capo_datazone.types.updated_at.UpdatedAt"
    """<p>The timestamp of when the subscription grant that is deleted was updated.</p>"""
    environment_id: NotRequired["capo_datazone.types.environment_id.EnvironmentId"]
    """<p>The ID of the environment in which the subscription grant is deleted.</p>"""
    subscription_target_id: (
        "capo_datazone.types.subscription_target_id.SubscriptionTargetId"
    )
    """<p>The ID of the subscription target associated with the subscription grant that is deleted.</p>"""
    granted_entity: "capo_datazone.types.granted_entity.GrantedEntity"
    """<p>The entity to which the subscription is deleted.</p>"""
    status: "capo_datazone.types.subscription_grant_overall_status.SubscriptionGrantOverallStatus"
    """<p>The status of the subscription grant that is deleted.</p>"""
    assets: NotRequired["capo_datazone.types.subscribed_assets.SubscribedAssets"]
    """<p>The assets for which the subsctiption grant that is deleted gave access.</p>"""
    subscription_id: NotRequired["capo_datazone.types.subscription_id.SubscriptionId"]
    """<p>The identifier of the subsctiption whose subscription grant is to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSubscriptionGrantOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["createdBy"] = value["created_by"]
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    out["domainId"] = value["domain_id"]
    import capo_datazone.types.created_at

    out["createdAt"] = capo_datazone.types.created_at.serialize_json(
        value["created_at"]
    )
    import capo_datazone.types.updated_at

    out["updatedAt"] = capo_datazone.types.updated_at.serialize_json(
        value["updated_at"]
    )
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    out["subscriptionTargetId"] = value["subscription_target_id"]
    import capo_datazone.types.granted_entity

    out["grantedEntity"] = capo_datazone.types.granted_entity.serialize_json(
        value["granted_entity"]
    )
    import capo_datazone.types.subscription_grant_overall_status

    out["status"] = (
        capo_datazone.types.subscription_grant_overall_status.serialize_json(
            value["status"]
        )
    )
    if "assets" in value:
        import capo_datazone.types.subscribed_assets

        out["assets"] = capo_datazone.types.subscribed_assets.serialize_json(
            value["assets"]
        )
    if "subscription_id" in value:
        out["subscriptionId"] = value["subscription_id"]
    return out


def deserialize_json(data: dict) -> DeleteSubscriptionGrantOutput:
    out: DeleteSubscriptionGrantOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    if data.get("subscriptionTargetId") is not None:
        out["subscription_target_id"] = data["subscriptionTargetId"]
    else:
        out["subscription_target_id"] = ""
    if data.get("grantedEntity") is not None:
        import capo_datazone.types.granted_entity

        out["granted_entity"] = capo_datazone.types.granted_entity.deserialize_json(
            data["grantedEntity"]
        )
    else:
        out["granted_entity"] = {"$unknown": {"name": ""}}
    if data.get("status") is not None:
        import capo_datazone.types.subscription_grant_overall_status

        out["status"] = (
            capo_datazone.types.subscription_grant_overall_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_datazone.types.subscription_grant_overall_status.SubscriptionGrantOverallStatus",
            "",
        )
    if data.get("assets") is not None:
        import capo_datazone.types.subscribed_assets

        out["assets"] = capo_datazone.types.subscribed_assets.deserialize_json(
            data["assets"]
        )
    if data.get("subscriptionId") is not None:
        out["subscription_id"] = data["subscriptionId"]
    return out
