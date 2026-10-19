"""Generated from Smithy shape ``com.amazonaws.datazone#SubscriptionTargetSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.applicable_asset_types
    import capo_datazone.types.authorized_principal_identifiers
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_id
    import capo_datazone.types.iam_role_arn
    import capo_datazone.types.project_id
    import capo_datazone.types.subscription_grant_creation_mode
    import capo_datazone.types.subscription_target_forms
    import capo_datazone.types.subscription_target_id
    import capo_datazone.types.subscription_target_name
    import capo_datazone.types.updated_at
    import capo_datazone.types.updated_by


class SubscriptionTargetSummary(TypedDict, closed=True):
    id: "capo_datazone.types.subscription_target_id.SubscriptionTargetId"
    """<p>The identifier of the subscription target.</p>"""
    authorized_principals: "capo_datazone.types.authorized_principal_identifiers.AuthorizedPrincipalIdentifiers"
    """<p>The authorized principals included in the subscription target.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which the subscription target exists.</p>"""
    project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project specified in the subscription target.</p>"""
    environment_id: "capo_datazone.types.environment_id.EnvironmentId"
    """<p>The identifier of the environment of the subscription target.</p>"""
    name: "capo_datazone.types.subscription_target_name.SubscriptionTargetName"
    """<p>The name of the subscription target.</p>"""
    type: "str"
    """<p>The type of the subscription target.</p>"""
    created_by: "capo_datazone.types.created_by.CreatedBy"
    """<p>The Amazon DataZone user who created the subscription target.</p>"""
    updated_by: NotRequired["capo_datazone.types.updated_by.UpdatedBy"]
    """<p>The Amazon DataZone user who updated the subscription target.</p>"""
    created_at: "capo_datazone.types.created_at.CreatedAt"
    """<p>The timestamp of when the subscription target was created.</p>"""
    updated_at: NotRequired["capo_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp of when the subscription target was updated.</p>"""
    manage_access_role: NotRequired["capo_datazone.types.iam_role_arn.IamRoleArn"]
    """<p>The manage access role specified in the subscription target.</p>"""
    applicable_asset_types: (
        "capo_datazone.types.applicable_asset_types.ApplicableAssetTypes"
    )
    """<p>The asset types included in the subscription target.</p>"""
    subscription_target_config: (
        "capo_datazone.types.subscription_target_forms.SubscriptionTargetForms"
    )
    """<p>The configuration of the subscription target.</p>"""
    provider: "str"
    """<p>The provider of the subscription target.</p>"""
    subscription_grant_creation_mode: NotRequired[
        "capo_datazone.types.subscription_grant_creation_mode.SubscriptionGrantCreationMode"
    ]
    """<p> Determines the subscription grant creation mode for this target, defining if grants are auto-created upon subscription approval or managed manually. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionTargetSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_datazone.types.authorized_principal_identifiers

    out["authorizedPrincipals"] = (
        capo_datazone.types.authorized_principal_identifiers.serialize_json(
            value["authorized_principals"]
        )
    )
    out["domainId"] = value["domain_id"]
    out["projectId"] = value["project_id"]
    out["environmentId"] = value["environment_id"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    out["createdBy"] = value["created_by"]
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    import capo_datazone.types.created_at

    out["createdAt"] = capo_datazone.types.created_at.serialize_json(
        value["created_at"]
    )
    if "updated_at" in value:
        import capo_datazone.types.updated_at

        out["updatedAt"] = capo_datazone.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "manage_access_role" in value:
        out["manageAccessRole"] = value["manage_access_role"]
    import capo_datazone.types.applicable_asset_types

    out["applicableAssetTypes"] = (
        capo_datazone.types.applicable_asset_types.serialize_json(
            value["applicable_asset_types"]
        )
    )
    import capo_datazone.types.subscription_target_forms

    out["subscriptionTargetConfig"] = (
        capo_datazone.types.subscription_target_forms.serialize_json(
            value["subscription_target_config"]
        )
    )
    out["provider"] = value["provider"]
    if "subscription_grant_creation_mode" in value:
        import capo_datazone.types.subscription_grant_creation_mode

        out["subscriptionGrantCreationMode"] = (
            capo_datazone.types.subscription_grant_creation_mode.serialize_json(
                value["subscription_grant_creation_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> SubscriptionTargetSummary:
    out: SubscriptionTargetSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("authorizedPrincipals") is not None:
        import capo_datazone.types.authorized_principal_identifiers

        out["authorized_principals"] = (
            capo_datazone.types.authorized_principal_identifiers.deserialize_json(
                data["authorizedPrincipals"]
            )
        )
    else:
        out["authorized_principals"] = []
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("projectId") is not None:
        out["project_id"] = data["projectId"]
    else:
        out["project_id"] = ""
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
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
    if data.get("manageAccessRole") is not None:
        out["manage_access_role"] = data["manageAccessRole"]
    if data.get("applicableAssetTypes") is not None:
        import capo_datazone.types.applicable_asset_types

        out["applicable_asset_types"] = (
            capo_datazone.types.applicable_asset_types.deserialize_json(
                data["applicableAssetTypes"]
            )
        )
    else:
        out["applicable_asset_types"] = []
    if data.get("subscriptionTargetConfig") is not None:
        import capo_datazone.types.subscription_target_forms

        out["subscription_target_config"] = (
            capo_datazone.types.subscription_target_forms.deserialize_json(
                data["subscriptionTargetConfig"]
            )
        )
    else:
        out["subscription_target_config"] = []
    if data.get("provider") is not None:
        out["provider"] = data["provider"]
    else:
        out["provider"] = ""
    if data.get("subscriptionGrantCreationMode") is not None:
        import capo_datazone.types.subscription_grant_creation_mode

        out["subscription_grant_creation_mode"] = (
            capo_datazone.types.subscription_grant_creation_mode.deserialize_json(
                data["subscriptionGrantCreationMode"]
            )
        )
    return out


def redact_sensitive(value: SubscriptionTargetSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
