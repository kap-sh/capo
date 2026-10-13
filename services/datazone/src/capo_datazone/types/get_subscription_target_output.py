"""Generated from Smithy shape ``com.amazonaws.datazone#GetSubscriptionTargetOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

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


class GetSubscriptionTargetOutput(TypedDict, closed=True):
    id: "capo_datazone.types.subscription_target_id.SubscriptionTargetId"
    """<p>The ID of the subscription target.</p>"""
    authorized_principals: "capo_datazone.types.authorized_principal_identifiers.AuthorizedPrincipalIdentifiers"
    """<p>The authorized principals of the subscription target.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the subscription target exists.</p>"""
    project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The ID of the project associated with the subscription target.</p>"""
    environment_id: "capo_datazone.types.environment_id.EnvironmentId"
    """<p>The ID of the environment associated with the subscription target.</p>"""
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
    """<p>The manage access role with which the subscription target was created.</p>"""
    applicable_asset_types: (
        "capo_datazone.types.applicable_asset_types.ApplicableAssetTypes"
    )
    """<p>The asset types associated with the subscription target.</p>"""
    subscription_target_config: (
        "capo_datazone.types.subscription_target_forms.SubscriptionTargetForms"
    )
    """<p>The configuration of teh subscription target.</p>"""
    provider: "str"
    """<p>The provider of the subscription target.</p>"""
    subscription_grant_creation_mode: NotRequired[
        "capo_datazone.types.subscription_grant_creation_mode.SubscriptionGrantCreationMode"
    ]
    """<p> Determines the subscription grant creation mode for this target, defining if grants are auto-created upon subscription approval or managed manually. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSubscriptionTargetOutput) -> dict:
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


def deserialize_json(data: dict) -> GetSubscriptionTargetOutput:
    out: GetSubscriptionTargetOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetSubscriptionTargetOutput.id required")
    if data.get("authorizedPrincipals") is not None:
        import capo_datazone.types.authorized_principal_identifiers

        out["authorized_principals"] = (
            capo_datazone.types.authorized_principal_identifiers.deserialize_json(
                data["authorizedPrincipals"]
            )
        )
    else:
        raise DeserializationError(
            "GetSubscriptionTargetOutput.authorized_principals required"
        )
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("GetSubscriptionTargetOutput.domain_id required")
    if data.get("projectId") is not None:
        out["project_id"] = data["projectId"]
    else:
        raise DeserializationError("GetSubscriptionTargetOutput.project_id required")
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError(
            "GetSubscriptionTargetOutput.environment_id required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetSubscriptionTargetOutput.name required")
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("GetSubscriptionTargetOutput.type required")
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("GetSubscriptionTargetOutput.created_by required")
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    if data.get("createdAt") is not None:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetSubscriptionTargetOutput.created_at required")
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
        raise DeserializationError(
            "GetSubscriptionTargetOutput.applicable_asset_types required"
        )
    if data.get("subscriptionTargetConfig") is not None:
        import capo_datazone.types.subscription_target_forms

        out["subscription_target_config"] = (
            capo_datazone.types.subscription_target_forms.deserialize_json(
                data["subscriptionTargetConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetSubscriptionTargetOutput.subscription_target_config required"
        )
    if data.get("provider") is not None:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("GetSubscriptionTargetOutput.provider required")
    if data.get("subscriptionGrantCreationMode") is not None:
        import capo_datazone.types.subscription_grant_creation_mode

        out["subscription_grant_creation_mode"] = (
            capo_datazone.types.subscription_grant_creation_mode.deserialize_json(
                data["subscriptionGrantCreationMode"]
            )
        )
    return out


def redact_sensitive(value: GetSubscriptionTargetOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
