"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateSubscriptionTargetInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.applicable_asset_types
    import capo_datazone.types.authorized_principal_identifiers
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_id
    import capo_datazone.types.iam_role_arn
    import capo_datazone.types.subscription_grant_creation_mode
    import capo_datazone.types.subscription_target_forms
    import capo_datazone.types.subscription_target_id
    import capo_datazone.types.subscription_target_name


class UpdateSubscriptionTargetInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which a subscription target is to be updated.</p>"""
    environment_identifier: "capo_datazone.types.environment_id.EnvironmentId"
    """<p>The identifier of the environment in which a subscription target is to be updated.</p>"""
    identifier: "capo_datazone.types.subscription_target_id.SubscriptionTargetId"
    """<p>Identifier of the subscription target that is to be updated.</p>"""
    name: NotRequired[
        "capo_datazone.types.subscription_target_name.SubscriptionTargetName"
    ]
    """<p>The name to be updated as part of the <code>UpdateSubscriptionTarget</code> action.</p>"""
    authorized_principals: NotRequired[
        "capo_datazone.types.authorized_principal_identifiers.AuthorizedPrincipalIdentifiers"
    ]
    """<p>The authorized principals to be updated as part of the <code>UpdateSubscriptionTarget</code> action.</p>"""
    applicable_asset_types: NotRequired[
        "capo_datazone.types.applicable_asset_types.ApplicableAssetTypes"
    ]
    """<p>The applicable asset types to be updated as part of the <code>UpdateSubscriptionTarget</code> action.</p>"""
    subscription_target_config: NotRequired[
        "capo_datazone.types.subscription_target_forms.SubscriptionTargetForms"
    ]
    """<p>The configuration to be updated as part of the <code>UpdateSubscriptionTarget</code> action.</p>"""
    manage_access_role: NotRequired["capo_datazone.types.iam_role_arn.IamRoleArn"]
    """<p>The manage access role to be updated as part of the <code>UpdateSubscriptionTarget</code> action.</p>"""
    provider: NotRequired["str"]
    """<p>The provider to be updated as part of the <code>UpdateSubscriptionTarget</code> action.</p>"""
    subscription_grant_creation_mode: NotRequired[
        "capo_datazone.types.subscription_grant_creation_mode.SubscriptionGrantCreationMode"
    ]
    """<p> Determines the subscription grant creation mode for this target, defining if grants are auto-created upon subscription approval or managed manually. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSubscriptionTargetInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "authorized_principals" in value:
        import capo_datazone.types.authorized_principal_identifiers

        out["authorizedPrincipals"] = (
            capo_datazone.types.authorized_principal_identifiers.serialize_json(
                value["authorized_principals"]
            )
        )
    if "applicable_asset_types" in value:
        import capo_datazone.types.applicable_asset_types

        out["applicableAssetTypes"] = (
            capo_datazone.types.applicable_asset_types.serialize_json(
                value["applicable_asset_types"]
            )
        )
    if "subscription_target_config" in value:
        import capo_datazone.types.subscription_target_forms

        out["subscriptionTargetConfig"] = (
            capo_datazone.types.subscription_target_forms.serialize_json(
                value["subscription_target_config"]
            )
        )
    if "manage_access_role" in value:
        out["manageAccessRole"] = value["manage_access_role"]
    if "provider" in value:
        out["provider"] = value["provider"]
    if "subscription_grant_creation_mode" in value:
        import capo_datazone.types.subscription_grant_creation_mode

        out["subscriptionGrantCreationMode"] = (
            capo_datazone.types.subscription_grant_creation_mode.serialize_json(
                value["subscription_grant_creation_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSubscriptionTargetInput:
    out: UpdateSubscriptionTargetInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("authorizedPrincipals") is not None:
        import capo_datazone.types.authorized_principal_identifiers

        out["authorized_principals"] = (
            capo_datazone.types.authorized_principal_identifiers.deserialize_json(
                data["authorizedPrincipals"]
            )
        )
    if data.get("applicableAssetTypes") is not None:
        import capo_datazone.types.applicable_asset_types

        out["applicable_asset_types"] = (
            capo_datazone.types.applicable_asset_types.deserialize_json(
                data["applicableAssetTypes"]
            )
        )
    if data.get("subscriptionTargetConfig") is not None:
        import capo_datazone.types.subscription_target_forms

        out["subscription_target_config"] = (
            capo_datazone.types.subscription_target_forms.deserialize_json(
                data["subscriptionTargetConfig"]
            )
        )
    if data.get("manageAccessRole") is not None:
        out["manage_access_role"] = data["manageAccessRole"]
    if data.get("provider") is not None:
        out["provider"] = data["provider"]
    if data.get("subscriptionGrantCreationMode") is not None:
        import capo_datazone.types.subscription_grant_creation_mode

        out["subscription_grant_creation_mode"] = (
            capo_datazone.types.subscription_grant_creation_mode.deserialize_json(
                data["subscriptionGrantCreationMode"]
            )
        )
    return out


def redact_sensitive(value: UpdateSubscriptionTargetInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
