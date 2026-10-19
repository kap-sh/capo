"""Generated from Smithy shape ``com.amazonaws.datazone#CreateSubscriptionGrantInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.asset_target_names
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_id
    import capo_datazone.types.granted_entity_input
    import capo_datazone.types.subscription_target_id


class CreateSubscriptionGrantInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the subscription grant is created.</p>"""
    environment_identifier: "capo_datazone.types.environment_id.EnvironmentId"
    """<p>The ID of the environment in which the subscription grant is created.</p>"""
    subscription_target_identifier: NotRequired[
        "capo_datazone.types.subscription_target_id.SubscriptionTargetId"
    ]
    """<p>The ID of the subscription target for which the subscription grant is created.</p>"""
    granted_entity: "capo_datazone.types.granted_entity_input.GrantedEntityInput"
    """<p>The entity to which the subscription is to be granted.</p>"""
    asset_target_names: NotRequired[
        "capo_datazone.types.asset_target_names.AssetTargetNames"
    ]
    """<p>The names of the assets for which the subscription grant is created.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSubscriptionGrantInput) -> dict:
    out: dict = {}
    out["environmentIdentifier"] = value["environment_identifier"]
    if "subscription_target_identifier" in value:
        out["subscriptionTargetIdentifier"] = value["subscription_target_identifier"]
    import capo_datazone.types.granted_entity_input

    out["grantedEntity"] = capo_datazone.types.granted_entity_input.serialize_json(
        value["granted_entity"]
    )
    if "asset_target_names" in value:
        import capo_datazone.types.asset_target_names

        out["assetTargetNames"] = capo_datazone.types.asset_target_names.serialize_json(
            value["asset_target_names"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateSubscriptionGrantInput:
    out: CreateSubscriptionGrantInput = {}  # type: ignore[typeddict-item]
    if data.get("environmentIdentifier") is not None:
        out["environment_identifier"] = data["environmentIdentifier"]
    else:
        out["environment_identifier"] = ""
    if data.get("subscriptionTargetIdentifier") is not None:
        out["subscription_target_identifier"] = data["subscriptionTargetIdentifier"]
    if data.get("grantedEntity") is not None:
        import capo_datazone.types.granted_entity_input

        out["granted_entity"] = (
            capo_datazone.types.granted_entity_input.deserialize_json(
                data["grantedEntity"]
            )
        )
    else:
        import capo_datazone.types._unknown

        out["granted_entity"] = capo_datazone.types._unknown.UnknownUnionMember("")
    if data.get("assetTargetNames") is not None:
        import capo_datazone.types.asset_target_names

        out["asset_target_names"] = (
            capo_datazone.types.asset_target_names.deserialize_json(
                data["assetTargetNames"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
