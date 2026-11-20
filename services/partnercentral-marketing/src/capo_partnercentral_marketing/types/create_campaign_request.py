"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CreateCampaignRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_name
    import capo_partnercentral_marketing.types.campaign_template_id
    import capo_partnercentral_marketing.types.catalog
    import capo_partnercentral_marketing.types.client_token
    import capo_partnercentral_marketing.types.engagement_group_id_list
    import capo_partnercentral_marketing.types.file_ref
    import capo_partnercentral_marketing.types.monetary_value
    import capo_partnercentral_marketing.types.partner_address
    import capo_partnercentral_marketing.types.privacy_policy_url
    import capo_partnercentral_marketing.types.sender_email
    import capo_partnercentral_marketing.types.tag_list
    import capo_partnercentral_marketing.types.target_audience
    import capo_partnercentral_marketing.types.utc_date


class CreateCampaignRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_marketing.types.catalog.Catalog"
    """The catalog (AWS or Sandbox)."""
    name: "capo_partnercentral_marketing.types.campaign_name.CampaignName"
    """The display name."""
    campaign_template_id: (
        "capo_partnercentral_marketing.types.campaign_template_id.CampaignTemplateId"
    )
    """The campaign template this campaign draws its assets from. <p>Binds the campaign to a single source template: every asset must come from this template's asset templates, and one from another template is refused at `BatchCreateCampaignAsset`. Immutable once set. Every campaign has one: a campaign's language and its assets' blueprints both come from its template. <p>Templates are AWS-authored and read-only — they are discovered through `SearchCampaignTemplates` and `GetCampaignTemplate`, and there is no create, update or delete operation for one. <p>The template's id only: a campaign template has no ARN (DG-084). The member keeps the `<Resource>Id` name, which is the convention for referencing another resource from a body."""
    sender_email: NotRequired[
        "capo_partnercentral_marketing.types.sender_email.SenderEmail"
    ]
    """The address every email of this campaign is sent from. <p>Printable ASCII only, with no spaces or line breaks, or field code `PATTERN_MISMATCH`. Then three rules, all checked when the sender is set. Its domain must exactly match, ignoring case, the domain of the partner's alliance lead email in AWS Partner Central (a subdomain does not), or field code `SENDER_DOMAIN_NOT_ALLIANCE_LEAD`. Then, for a sender at example.com, DNS must hold the CNAME `dkim._domainkey.example.com` → `dkim._domainkey.md02.com` (field code `SENDER_DOMAIN_DKIM_MISSING`) and a DMARC record, one TXT `_dmarc.example.com` starting `v=DMARC1` with a `p` of `none`, `quarantine` or `reject` (field code `SENDER_DOMAIN_DMARC_MISSING`). Both DNS codes are reported together when both records are missing. <p>A partner who can't satisfy them can't set a sender, so can't run email campaigns. A shared mail provider's domain, such as gmail.com, can't carry the records. Optional here: a campaign with no sender can be created and edited, but its email assets cannot be activated until one is set."""
    privacy_policy_url: NotRequired[
        "capo_partnercentral_marketing.types.privacy_policy_url.PrivacyPolicyUrl"
    ]
    """The URL of the partner's privacy policy, linked from every email and landing page footer. Optional here: a campaign whose emails or landing pages show it cannot activate them until one is set."""
    partner_address: NotRequired[
        "capo_partnercentral_marketing.types.partner_address.PartnerAddress"
    ]
    """The partner's physical postal address, shown in every email footer and as a landing page's contact line. Optional here: an email that shows it cannot activate until one is set. A landing page that shows it publishes it empty when it is unset, and a document's footer then prints the partner's name alone."""
    partner_badge: NotRequired["capo_partnercentral_marketing.types.file_ref.FileRef"]
    """The partner's badge — a tier or designation badge from AWS Partner Badge Manager — shown in every badge slot of the campaign's emails, landing pages and documents. Optional: until one is set, every badge slot shows the Standalone AWS Partner badge. <p>A PNG or JPEG of at most 2 MB, staged like an asset image and checked the same way: it must have passed the staging scan (`SCAN_REJECTED`, or `SCAN_IN_PROGRESS` while it is pending), and its bytes must be the format its name says (`IMAGE_FORMAT_NOT_SUPPORTED`). Any shape is accepted: a badge is drawn whole, never cropped. Content moderation judges it when an asset that shows it is activated."""
    email_target: NotRequired["capo_partnercentral_marketing.types.file_ref.FileRef"]
    """The campaign's send audience — a CSV of recipient email addresses. <p>The campaign's *target*: who the campaign is sent to, as distinct from a `CampaignAsset`, which is the content that is sent. It sits on the campaign and not on the activation call because a partner assembles it in the same wizard flow that sets the name and the dates — and because attaching it here means it is validated, staged and resolved to a count before anything is activated, rather than at the last click. <p>Required format: a header row naming the email column `Email`, `E-mail`, `Email Address` or `E-mail Address` — compared without case, spaces or punctuation. Other columns are permitted and ignored, and with two email columns the first is used. A file without such a header is refused with field code `EMAIL_COLUMN_MISSING`: the address column is never guessed. The rows reach the delivery platform's importer as the partner wrote them — a partner's audience is never rewritten. <p>At most 5 MB, checked against the object's size before anything is copied, and at most 10,000 distinct addresses, refused with `RECIPIENT_LIST_TOO_LARGE`. A file with no valid address at all is refused with `RECIPIENT_LIST_EMPTY`; otherwise rows without a usable address are not a refusal: they are skipped and counted, and `GetCampaign` reports the counts. Optional here, because a campaign is a container and holds no state to be incomplete in — but an email asset cannot be activated without it, so the requirement moved to the point of activation. <p>Editable at any time, and an edit reaches the delivery platform only when an asset is activated after it. Each email activation loads the audience into a contact list of its own, so an address taken off the file is not sent to by the next activation. <p>The bytes are write-only. No response returns a URL or an `S3Uri` for this file; `GetCampaign` returns the scan verdict, when the list was attached and how its rows resolved, and nothing more."""
    email_target_engagement_group_ids: NotRequired[
        "capo_partnercentral_marketing.types.engagement_group_id_list.EngagementGroupIdList"
    ]
    """Engagement groups whose contacts the campaign's emails will also go to: the `Id`s `ListEngagementGroups` returns (AWS Partner Central Selling). 1–10, each named once. <p>Each group is named once: a repeated id is refused with field code `INVALID_VALUE`. Not checked against your groups when saved. StartCampaignAssetActivationTask resolves them to recipients. On a stage that can't resolve groups yet, Start refuses an email while groups are set (`ENGAGEMENT_GROUPS_UNAVAILABLE`), rather than send to `EmailTarget` alone."""
    target_audience: NotRequired[
        "capo_partnercentral_marketing.types.target_audience.TargetAudience"
    ]
    """Advisory targeting metadata. Refined later, and not validated here."""
    estimated_budget: NotRequired[
        "capo_partnercentral_marketing.types.monetary_value.MonetaryValue"
    ]
    """What the partner expects the campaign to cost."""
    total_budget: NotRequired[
        "capo_partnercentral_marketing.types.monetary_value.MonetaryValue"
    ]
    """The campaign's total budget."""
    start_on: NotRequired["capo_partnercentral_marketing.types.utc_date.UtcDate"]
    """The first day of the campaign's run window. Not after `EndOn` (`ValidationException`, `INVALID_VALUE`)."""
    end_on: NotRequired["capo_partnercentral_marketing.types.utc_date.UtcDate"]
    """The last day of the campaign's run window, inclusive and in UTC. Not in the past: the campaign completes at the UTC midnight after it (see `CampaignState`). A scheduled send must fall on or before it. Optional here, but required before any asset activates: until it is set, GetCampaign's `ActivationIssues` reports `END_ON_MISSING` and StartCampaignAssetActivationTask refuses (`CAMPAIGN_INCOMPLETE`). Set it with UpdateCampaign."""
    client_token: NotRequired[
        "capo_partnercentral_marketing.types.client_token.ClientToken"
    ]
    """Idempotency token. Same token within 24h returns existing resource."""
    tags: NotRequired["capo_partnercentral_marketing.types.tag_list.TagList"]
    """Tags to apply at creation. Tag-on-create rather than create-then-tag is a Tagris requirement, not a convenience: it is what lets a tag-based access control policy govern the creation itself. A campaign created untagged and tagged a moment later is briefly outside any such policy. <p>A key beginning `aws:` (any case) is reserved for AWS-applied system tags and is refused with `ValidationException`, as is a key repeated in the list; nothing is created. The tags are recorded before the campaign is written, so a create that cannot record them fails and creates nothing. A retry with the same `ClientToken` returns the campaign the first attempt created and does not re-apply tags — use `TagResource` to change them afterwards. `ListTagsForResource` returns them."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateCampaignRequest) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.catalog

    out["Catalog"] = capo_partnercentral_marketing.types.catalog.serialize_cbor(
        value["catalog"]
    )
    out["Name"] = value["name"]
    out["CampaignTemplateId"] = value["campaign_template_id"]
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
    if "target_audience" in value:
        import capo_partnercentral_marketing.types.target_audience

        out["TargetAudience"] = (
            capo_partnercentral_marketing.types.target_audience.serialize_cbor(
                value["target_audience"]
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
    if "start_on" in value:
        out["StartOn"] = value["start_on"]
    if "end_on" in value:
        out["EndOn"] = value["end_on"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_partnercentral_marketing.types.tag_list

        out["Tags"] = capo_partnercentral_marketing.types.tag_list.serialize_cbor(
            value["tags"]
        )
    return out


def deserialize_cbor(data: dict) -> CreateCampaignRequest:
    out: CreateCampaignRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("CampaignTemplateId") is not None:
        out["campaign_template_id"] = data["CampaignTemplateId"]
    else:
        out["campaign_template_id"] = ""
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
    if data.get("TargetAudience") is not None:
        import capo_partnercentral_marketing.types.target_audience

        out["target_audience"] = (
            capo_partnercentral_marketing.types.target_audience.deserialize_cbor(
                data["TargetAudience"]
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
    if data.get("StartOn") is not None:
        out["start_on"] = data["StartOn"]
    if data.get("EndOn") is not None:
        out["end_on"] = data["EndOn"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Tags") is not None:
        import capo_partnercentral_marketing.types.tag_list

        out["tags"] = capo_partnercentral_marketing.types.tag_list.deserialize_cbor(
            data["Tags"]
        )
    return out


def redact_sensitive(value: CreateCampaignRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sender_email" in value:
        out["sender_email"] = "*** Sensitive Data Redacted ***"
    if "partner_address" in value:
        out["partner_address"] = "*** Sensitive Data Redacted ***"
    return out
