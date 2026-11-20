"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#UpdateCampaignRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_identifier
    import capo_partnercentral_marketing.types.campaign_name
    import capo_partnercentral_marketing.types.campaign_social_connections
    import capo_partnercentral_marketing.types.catalog
    import capo_partnercentral_marketing.types.client_token
    import capo_partnercentral_marketing.types.engagement_group_id_list
    import capo_partnercentral_marketing.types.file_ref
    import capo_partnercentral_marketing.types.monetary_value
    import capo_partnercentral_marketing.types.partner_address
    import capo_partnercentral_marketing.types.privacy_policy_url
    import capo_partnercentral_marketing.types.sender_email
    import capo_partnercentral_marketing.types.target_audience
    import capo_partnercentral_marketing.types.utc_date


class UpdateCampaignRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_marketing.types.catalog.Catalog"
    """The catalog (AWS or Sandbox)."""
    campaign_identifier: (
        "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier"
    )
    """The campaign identifier."""
    name: NotRequired["capo_partnercentral_marketing.types.campaign_name.CampaignName"]
    """The display name."""
    sender_email: NotRequired[
        "capo_partnercentral_marketing.types.sender_email.SenderEmail"
    ]
    """Sets or replaces the address the campaign's emails are sent from. Checked by the same three rules as on `CreateCampaign`, with the same codes, but only when it differs, ignoring case, from the stored sender: re-sending the stored one is not checked, and `StartCampaignAssetActivationTask` re-checks it before an email activates. <p>Replaces, never clears: like every member of this operation, an omitted value leaves the sender as it was, and there is no way to remove one once set."""
    privacy_policy_url: NotRequired[
        "capo_partnercentral_marketing.types.privacy_policy_url.PrivacyPolicyUrl"
    ]
    """Sets or replaces the URL of the partner's privacy policy. Replaces, never clears."""
    partner_address: NotRequired[
        "capo_partnercentral_marketing.types.partner_address.PartnerAddress"
    ]
    """Sets or replaces the partner's postal address. Replaces, never clears."""
    partner_badge: NotRequired["capo_partnercentral_marketing.types.file_ref.FileRef"]
    """Sets or replaces the partner's badge, checked exactly as on `CreateCampaign`. Replaces, never clears: upload the Standalone AWS Partner badge to show it again. The badge an asset already published keeps showing on it until that asset is activated again."""
    email_target: NotRequired["capo_partnercentral_marketing.types.file_ref.FileRef"]
    """Replaces the campaign's attached recipient list. <p>The referenced object is copied and pinned again on every call that supplies it, so the pinned copy always reflects the *last* `UpdateCampaign` that named one. Editing the source object in your own bucket without calling this operation again has no effect. <p>Replaces, never detaches: a partner can swap the list but cannot remove it."""
    email_target_engagement_group_ids: NotRequired[
        "capo_partnercentral_marketing.types.engagement_group_id_list.EngagementGroupIdList"
    ]
    """Engagement groups whose contacts the campaign's emails will also go to (see `CreateCampaign`). Replaces the stored list; never clears it. <p>As on `CreateCampaign`: each group once (`INVALID_VALUE` otherwise), not checked against your groups when saved, and resolved at Start where the stage can (`ENGAGEMENT_GROUPS_UNAVAILABLE` where it can't)."""
    social_connections: NotRequired[
        "capo_partnercentral_marketing.types.campaign_social_connections.CampaignSocialConnections"
    ]
    """Sets the account the campaign's social posts publish from, per platform. Each platform named replaces that platform's choice; a platform not named keeps its own. Replaces, never clears. <p>Not checked against your connections here: a connection can be deleted at any time, so the activation checks the choice. See `Campaign$SocialConnections`."""
    estimated_budget: NotRequired[
        "capo_partnercentral_marketing.types.monetary_value.MonetaryValue"
    ]
    """What the partner expects the campaign to cost."""
    total_budget: NotRequired[
        "capo_partnercentral_marketing.types.monetary_value.MonetaryValue"
    ]
    """The campaign's total budget."""
    target_audience: NotRequired[
        "capo_partnercentral_marketing.types.target_audience.TargetAudience"
    ]
    """Target audience configuration."""
    client_token: NotRequired[
        "capo_partnercentral_marketing.types.client_token.ClientToken"
    ]
    """Idempotency token. Accepted and not stored: this is a change-only partial update with last-writer-wins, so re-applying the same call produces the same result and the same response. There is nothing a replay cache would protect."""
    start_on: NotRequired["capo_partnercentral_marketing.types.utc_date.UtcDate"]
    """The first day of the campaign's run window. Not after `EndOn` (`ValidationException`, `INVALID_VALUE`)."""
    end_on: NotRequired["capo_partnercentral_marketing.types.utc_date.UtcDate"]
    """The last day of the campaign's run window, inclusive and in UTC. Editable only while the campaign is open, like everything else here: once the stored `EndOn` has passed the campaign is completed and this update is refused (`CAMPAIGN_COMPLETED`). Refused with `ValidationException` (`INVALID_VALUE`) when it is in the past, or earlier than the day of a scheduled send on one of the campaign's assets: move or cancel that send first. Setting it to today ends the campaign at the next UTC midnight."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateCampaignRequest) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.catalog

    out["Catalog"] = capo_partnercentral_marketing.types.catalog.serialize_cbor(
        value["catalog"]
    )
    out["CampaignIdentifier"] = value["campaign_identifier"]
    if "name" in value:
        out["Name"] = value["name"]
    if "sender_email" in value:
        out["SenderEmail"] = value["sender_email"]
    if "privacy_policy_url" in value:
        out["PrivacyPolicyUrl"] = value["privacy_policy_url"]
    if "partner_address" in value:
        out["PartnerAddress"] = value["partner_address"]
    if "partner_badge" in value:
        import capo_partnercentral_marketing.types.file_ref

        out["PartnerBadge"] = (
            capo_partnercentral_marketing.types.file_ref.serialize_cbor(
                value["partner_badge"]
            )
        )
    if "email_target" in value:
        import capo_partnercentral_marketing.types.file_ref

        out["EmailTarget"] = (
            capo_partnercentral_marketing.types.file_ref.serialize_cbor(
                value["email_target"]
            )
        )
    if "email_target_engagement_group_ids" in value:
        import capo_partnercentral_marketing.types.engagement_group_id_list

        out["EmailTargetEngagementGroupIds"] = (
            capo_partnercentral_marketing.types.engagement_group_id_list.serialize_cbor(
                value["email_target_engagement_group_ids"]
            )
        )
    if "social_connections" in value:
        import capo_partnercentral_marketing.types.campaign_social_connections

        out["SocialConnections"] = (
            capo_partnercentral_marketing.types.campaign_social_connections.serialize_cbor(
                value["social_connections"]
            )
        )
    if "estimated_budget" in value:
        import capo_partnercentral_marketing.types.monetary_value

        out["EstimatedBudget"] = (
            capo_partnercentral_marketing.types.monetary_value.serialize_cbor(
                value["estimated_budget"]
            )
        )
    if "total_budget" in value:
        import capo_partnercentral_marketing.types.monetary_value

        out["TotalBudget"] = (
            capo_partnercentral_marketing.types.monetary_value.serialize_cbor(
                value["total_budget"]
            )
        )
    if "target_audience" in value:
        import capo_partnercentral_marketing.types.target_audience

        out["TargetAudience"] = (
            capo_partnercentral_marketing.types.target_audience.serialize_cbor(
                value["target_audience"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "start_on" in value:
        out["StartOn"] = value["start_on"]
    if "end_on" in value:
        out["EndOn"] = value["end_on"]
    return out


def deserialize_cbor(data: dict) -> UpdateCampaignRequest:
    out: UpdateCampaignRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        import capo_partnercentral_marketing.types.catalog

        out["catalog"] = capo_partnercentral_marketing.types.catalog.deserialize_cbor(
            data["Catalog"]
        )
    else:
        import typing

        out["catalog"] = typing.cast(
            "capo_partnercentral_marketing.types.catalog.Catalog", ""
        )
    if data.get("CampaignIdentifier") is not None:
        out["campaign_identifier"] = data["CampaignIdentifier"]
    else:
        out["campaign_identifier"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("SenderEmail") is not None:
        out["sender_email"] = data["SenderEmail"]
    if data.get("PrivacyPolicyUrl") is not None:
        out["privacy_policy_url"] = data["PrivacyPolicyUrl"]
    if data.get("PartnerAddress") is not None:
        out["partner_address"] = data["PartnerAddress"]
    if data.get("PartnerBadge") is not None:
        import capo_partnercentral_marketing.types.file_ref

        out["partner_badge"] = (
            capo_partnercentral_marketing.types.file_ref.deserialize_cbor(
                data["PartnerBadge"]
            )
        )
    if data.get("EmailTarget") is not None:
        import capo_partnercentral_marketing.types.file_ref

        out["email_target"] = (
            capo_partnercentral_marketing.types.file_ref.deserialize_cbor(
                data["EmailTarget"]
            )
        )
    if data.get("EmailTargetEngagementGroupIds") is not None:
        import capo_partnercentral_marketing.types.engagement_group_id_list

        out["email_target_engagement_group_ids"] = (
            capo_partnercentral_marketing.types.engagement_group_id_list.deserialize_cbor(
                data["EmailTargetEngagementGroupIds"]
            )
        )
    if data.get("SocialConnections") is not None:
        import capo_partnercentral_marketing.types.campaign_social_connections

        out["social_connections"] = (
            capo_partnercentral_marketing.types.campaign_social_connections.deserialize_cbor(
                data["SocialConnections"]
            )
        )
    if data.get("EstimatedBudget") is not None:
        import capo_partnercentral_marketing.types.monetary_value

        out["estimated_budget"] = (
            capo_partnercentral_marketing.types.monetary_value.deserialize_cbor(
                data["EstimatedBudget"]
            )
        )
    if data.get("TotalBudget") is not None:
        import capo_partnercentral_marketing.types.monetary_value

        out["total_budget"] = (
            capo_partnercentral_marketing.types.monetary_value.deserialize_cbor(
                data["TotalBudget"]
            )
        )
    if data.get("TargetAudience") is not None:
        import capo_partnercentral_marketing.types.target_audience

        out["target_audience"] = (
            capo_partnercentral_marketing.types.target_audience.deserialize_cbor(
                data["TargetAudience"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("StartOn") is not None:
        out["start_on"] = data["StartOn"]
    if data.get("EndOn") is not None:
        out["end_on"] = data["EndOn"]
    return out


def redact_sensitive(value: UpdateCampaignRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sender_email" in value:
        out["sender_email"] = "*** Sensitive Data Redacted ***"
    if "partner_address" in value:
        out["partner_address"] = "*** Sensitive Data Redacted ***"
    return out
