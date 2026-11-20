"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#Campaign``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.activation_issue_list
    import capo_partnercentral_marketing.types.asset_language
    import capo_partnercentral_marketing.types.campaign_id
    import capo_partnercentral_marketing.types.campaign_name
    import capo_partnercentral_marketing.types.campaign_social_connections
    import capo_partnercentral_marketing.types.campaign_state
    import capo_partnercentral_marketing.types.campaign_template_id
    import capo_partnercentral_marketing.types.email_target_detail
    import capo_partnercentral_marketing.types.engagement_group_id_list
    import capo_partnercentral_marketing.types.monetary_value
    import capo_partnercentral_marketing.types.partner_address
    import capo_partnercentral_marketing.types.partner_badge_detail
    import capo_partnercentral_marketing.types.partner_profile_branding
    import capo_partnercentral_marketing.types.privacy_policy_url
    import capo_partnercentral_marketing.types.sender_email
    import capo_partnercentral_marketing.types.taggable_resource_arn
    import capo_partnercentral_marketing.types.target_audience
    import capo_partnercentral_marketing.types.timestamp
    import capo_partnercentral_marketing.types.utc_date


class Campaign(TypedDict, closed=True):
    campaign_id: "capo_partnercentral_marketing.types.campaign_id.CampaignId"
    """The campaign identifier."""
    arn: "capo_partnercentral_marketing.types.taggable_resource_arn.TaggableResourceArn"
    """The campaign ARN."""
    name: "capo_partnercentral_marketing.types.campaign_name.CampaignName"
    """The display name."""
    state: "capo_partnercentral_marketing.types.campaign_state.CampaignState"
    """The campaign's state, derived on every read from `EndOn` and its assets. See `CampaignState`."""
    campaign_template_id: NotRequired[
        "capo_partnercentral_marketing.types.campaign_template_id.CampaignTemplateId"
    ]
    """The campaign template this campaign draws its assets from. Set at create, immutable."""
    language: NotRequired[
        "capo_partnercentral_marketing.types.asset_language.AssetLanguage"
    ]
    """The language the campaign's assets are written and typeset in: its template's `LanguageCode`, set at create. To work in another language, create the campaign from that language's template."""
    partner_profile: NotRequired[
        "capo_partnercentral_marketing.types.partner_profile_branding.PartnerProfileBranding"
    ]
    """The partner's branding — display name, website and logo — from their AWS Partner Central profile, rendered onto every asset of this campaign. Read-only here: the partner edits it in Partner Central, and the next activation or export uses the change. Absent only when the partner has no profile."""
    sender_email: NotRequired[
        "capo_partnercentral_marketing.types.sender_email.SenderEmail"
    ]
    """The address the campaign's emails are sent from. Absent until one is set."""
    privacy_policy_url: NotRequired[
        "capo_partnercentral_marketing.types.privacy_policy_url.PrivacyPolicyUrl"
    ]
    """The URL of the partner's privacy policy. Absent until one is set."""
    partner_address: NotRequired[
        "capo_partnercentral_marketing.types.partner_address.PartnerAddress"
    ]
    """The partner's postal address. Absent until one is set."""
    partner_badge: NotRequired[
        "capo_partnercentral_marketing.types.partner_badge_detail.PartnerBadgeDetail"
    ]
    """The partner's badge. Absent until one is set, and every badge slot shows the Standalone AWS Partner badge while the partner's primary AWS Partner path is at stage Validated or Differentiated. Below that, no badge is shown."""
    email_target: NotRequired[
        "capo_partnercentral_marketing.types.email_target_detail.EmailTargetDetail"
    ]
    """The attached recipient list — metadata only. There is no read path for the addresses."""
    email_target_engagement_group_ids: NotRequired[
        "capo_partnercentral_marketing.types.engagement_group_id_list.EngagementGroupIdList"
    ]
    """The engagement groups set by `CreateCampaign` / `UpdateCampaign`. Absent until set. Resolved to recipients at Start, where the stage can."""
    social_connections: NotRequired[
        "capo_partnercentral_marketing.types.campaign_social_connections.CampaignSocialConnections"
    ]
    """The account the campaign's social posts publish from, per platform, as set by `UpdateCampaign`. Absent until one is set. <p>Needed only for a platform where you hold two or more connections. With none set, a post uses your one connection on its platform, and fails `SOCIAL_CONNECTION_NOT_CHOSEN` when you hold several. A choice that no longer names a connection on its platform fails `SOCIAL_CONNECTION_MISSING`. Join with `ListSocialConnections` for each connection's status."""
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
    start_on: NotRequired["capo_partnercentral_marketing.types.utc_date.UtcDate"]
    """The first day of the campaign's run window."""
    end_on: NotRequired["capo_partnercentral_marketing.types.utc_date.UtcDate"]
    """The last day of the campaign's run window."""
    created_at: NotRequired["capo_partnercentral_marketing.types.timestamp.Timestamp"]
    """Creation timestamp."""
    updated_at: NotRequired["capo_partnercentral_marketing.types.timestamp.Timestamp"]
    """Last update timestamp."""
    activation_issues: (
        "capo_partnercentral_marketing.types.activation_issue_list.ActivationIssueList"
    )
    """Campaign settings that must be set before the assets listed in each issue can be activated. Empty when nothing is missing. Each issue names the setting in `CampaignSetting` — set it with `UpdateCampaign` — or the profile value in `PartnerProfileField` — set it in Partner Central — and the assets it blocks in `AffectedAssetIds`. `StartCampaignAssetActivationTask` refuses with `ValidationException` (`CAMPAIGN_INCOMPLETE`) while a requested asset is affected."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Campaign) -> dict:
    out: dict = {}
    out["CampaignId"] = value["campaign_id"]
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    import capo_partnercentral_marketing.types.campaign_state

    out["State"] = capo_partnercentral_marketing.types.campaign_state.serialize_cbor(
        value["state"]
    )
    if "campaign_template_id" in value:
        out["CampaignTemplateId"] = value["campaign_template_id"]
    if "language" in value:
        import capo_partnercentral_marketing.types.asset_language

        out["Language"] = (
            capo_partnercentral_marketing.types.asset_language.serialize_cbor(
                value["language"]
            )
        )
    if "partner_profile" in value:
        import capo_partnercentral_marketing.types.partner_profile_branding

        out["PartnerProfile"] = (
            capo_partnercentral_marketing.types.partner_profile_branding.serialize_cbor(
                value["partner_profile"]
            )
        )
    if "sender_email" in value:
        out["SenderEmail"] = value["sender_email"]
    if "privacy_policy_url" in value:
        out["PrivacyPolicyUrl"] = value["privacy_policy_url"]
    if "partner_address" in value:
        out["PartnerAddress"] = value["partner_address"]
    if "partner_badge" in value:
        import capo_partnercentral_marketing.types.partner_badge_detail

        out["PartnerBadge"] = (
            capo_partnercentral_marketing.types.partner_badge_detail.serialize_cbor(
                value["partner_badge"]
            )
        )
    if "email_target" in value:
        import capo_partnercentral_marketing.types.email_target_detail

        out["EmailTarget"] = (
            capo_partnercentral_marketing.types.email_target_detail.serialize_cbor(
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
    if "start_on" in value:
        out["StartOn"] = value["start_on"]
    if "end_on" in value:
        out["EndOn"] = value["end_on"]
    if "created_at" in value:
        import capo_partnercentral_marketing.types.timestamp

        out["CreatedAt"] = capo_partnercentral_marketing.types.timestamp.serialize_cbor(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_partnercentral_marketing.types.timestamp

        out["UpdatedAt"] = capo_partnercentral_marketing.types.timestamp.serialize_cbor(
            value["updated_at"]
        )
    import capo_partnercentral_marketing.types.activation_issue_list

    out["ActivationIssues"] = (
        capo_partnercentral_marketing.types.activation_issue_list.serialize_cbor(
            value["activation_issues"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> Campaign:
    out: Campaign = {}  # type: ignore[typeddict-item]
    if data.get("CampaignId") is not None:
        out["campaign_id"] = data["CampaignId"]
    else:
        out["campaign_id"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("State") is not None:
        import capo_partnercentral_marketing.types.campaign_state

        out["state"] = (
            capo_partnercentral_marketing.types.campaign_state.deserialize_cbor(
                data["State"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_partnercentral_marketing.types.campaign_state.CampaignState", ""
        )
    if data.get("CampaignTemplateId") is not None:
        out["campaign_template_id"] = data["CampaignTemplateId"]
    if data.get("Language") is not None:
        import capo_partnercentral_marketing.types.asset_language

        out["language"] = (
            capo_partnercentral_marketing.types.asset_language.deserialize_cbor(
                data["Language"]
            )
        )
    if data.get("PartnerProfile") is not None:
        import capo_partnercentral_marketing.types.partner_profile_branding

        out["partner_profile"] = (
            capo_partnercentral_marketing.types.partner_profile_branding.deserialize_cbor(
                data["PartnerProfile"]
            )
        )
    if data.get("SenderEmail") is not None:
        out["sender_email"] = data["SenderEmail"]
    if data.get("PrivacyPolicyUrl") is not None:
        out["privacy_policy_url"] = data["PrivacyPolicyUrl"]
    if data.get("PartnerAddress") is not None:
        out["partner_address"] = data["PartnerAddress"]
    if data.get("PartnerBadge") is not None:
        import capo_partnercentral_marketing.types.partner_badge_detail

        out["partner_badge"] = (
            capo_partnercentral_marketing.types.partner_badge_detail.deserialize_cbor(
                data["PartnerBadge"]
            )
        )
    if data.get("EmailTarget") is not None:
        import capo_partnercentral_marketing.types.email_target_detail

        out["email_target"] = (
            capo_partnercentral_marketing.types.email_target_detail.deserialize_cbor(
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
    if data.get("StartOn") is not None:
        out["start_on"] = data["StartOn"]
    if data.get("EndOn") is not None:
        out["end_on"] = data["EndOn"]
    if data.get("CreatedAt") is not None:
        import capo_partnercentral_marketing.types.timestamp

        out["created_at"] = (
            capo_partnercentral_marketing.types.timestamp.deserialize_cbor(
                data["CreatedAt"]
            )
        )
    if data.get("UpdatedAt") is not None:
        import capo_partnercentral_marketing.types.timestamp

        out["updated_at"] = (
            capo_partnercentral_marketing.types.timestamp.deserialize_cbor(
                data["UpdatedAt"]
            )
        )
    if data.get("ActivationIssues") is not None:
        import capo_partnercentral_marketing.types.activation_issue_list

        out["activation_issues"] = (
            capo_partnercentral_marketing.types.activation_issue_list.deserialize_cbor(
                data["ActivationIssues"]
            )
        )
    else:
        out["activation_issues"] = []
    return out


def redact_sensitive(value: Campaign) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sender_email" in value:
        out["sender_email"] = "*** Sensitive Data Redacted ***"
    if "partner_address" in value:
        out["partner_address"] = "*** Sensitive Data Redacted ***"
    return out
