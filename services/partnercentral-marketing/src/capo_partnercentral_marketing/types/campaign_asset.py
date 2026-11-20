"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAsset``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.activation_issue_list
    import capo_partnercentral_marketing.types.asset_name
    import capo_partnercentral_marketing.types.attempt_status
    import capo_partnercentral_marketing.types.campaign_asset_category
    import capo_partnercentral_marketing.types.campaign_asset_field_value_list
    import capo_partnercentral_marketing.types.campaign_asset_id
    import capo_partnercentral_marketing.types.campaign_asset_layout
    import capo_partnercentral_marketing.types.campaign_asset_state
    import capo_partnercentral_marketing.types.campaign_asset_state_reason
    import capo_partnercentral_marketing.types.campaign_id
    import capo_partnercentral_marketing.types.delivery_status
    import capo_partnercentral_marketing.types.file_format
    import capo_partnercentral_marketing.types.id
    import capo_partnercentral_marketing.types.layout_preview_list
    import capo_partnercentral_marketing.types.link_label
    import capo_partnercentral_marketing.types.platform
    import capo_partnercentral_marketing.types.public_url
    import capo_partnercentral_marketing.types.send_mode
    import capo_partnercentral_marketing.types.timestamp


class CampaignAsset(TypedDict, closed=True):
    id: "capo_partnercentral_marketing.types.campaign_asset_id.CampaignAssetId"
    """The asset identifier."""
    campaign_id: "capo_partnercentral_marketing.types.campaign_id.CampaignId"
    """The campaign identifier."""
    category: "capo_partnercentral_marketing.types.campaign_asset_category.CampaignAssetCategory"
    """The asset category."""
    name: "capo_partnercentral_marketing.types.asset_name.AssetName"
    """The display name."""
    link_label: NotRequired["capo_partnercentral_marketing.types.link_label.LinkLabel"]
    """DOCUMENT only: the words a page uses for this document, such as "eBook". Fill an `AssetLink` field's `LabelFieldId` with it when the partner picks this asset."""
    state: "capo_partnercentral_marketing.types.campaign_asset_state.CampaignAssetState"
    """Whether the asset is live. Reports current truth only, and nothing else on this shape overrides it. During an *initial* publication it stays INACTIVE until the delivery platform holds the object; during a *re*-publication it stays ACTIVE, because the previously published content is still serving. A stopped asset and one never started both read INACTIVE; `LastActivationStatus` tells them apart, because a stop does not change how the last activation went — stopped is INACTIVE with that member `SUCCEEDED`, never started is INACTIVE with it absent. An update never moves this member."""
    last_activation_status: NotRequired[
        "capo_partnercentral_marketing.types.attempt_status.AttemptStatus"
    ]
    """How the most recent hand-over to the delivery platform ended. The hand-over, not the delivery: if DG got the artifact scheduled at the platform this is SUCCEEDED, and whether the platform then delivered is `DeliveryStatus`. Per category the hand-over point is — email: the mailing armed; social: the create, which *is* the schedule; landing page: create plus publish-personalisation; document: bytes written. Read with `State` this is what separates a stopped asset (INACTIVE with SUCCEEDED here) from one never activated (INACTIVE with this member absent) — a stop does not change how the last *activation* went. There is no public UNKNOWN. A hand-over whose outcome DG cannot yet determine reports IN_PROGRESS, because a partner's action is identical either way and there is nothing to do with "unknown". Reporting it as FAILED would be the harmful collapse: that reads as safe to retry, and a retry on an at-most-once create publishes a second live object. Omitted before the first activation attempt."""
    delivery_status: NotRequired[
        "capo_partnercentral_marketing.types.delivery_status.DeliveryStatus"
    ]
    """What the platform did with the artifact after accepting it. EMAIL and SOCIAL_POST only — absent on every other category, which has no delivery event. See the DeliveryStatus docs."""
    delivery_status_reason: NotRequired[
        "capo_partnercentral_marketing.types.campaign_asset_state_reason.CampaignAssetStateReason"
    ]
    """Why delivery failed. Present only when DeliveryStatus is FAILED. For an email the platform rejected: SENDER_EMAIL_INVALID, RECIPIENT_LIST_EMPTY, MAILING_CREDITS_EXHAUSTED or RECIPIENT_LIMIT_EXCEEDED. Otherwise DELIVERY_FAILED. A Facebook post refused because its connection has no Page is FAILED with SOCIAL_CONNECTION_PAGE_REQUIRED, and withdrawn: reconnect Facebook with a Page selected. A social post the platform stopped retrying, because it could not publish within 12 hours of its scheduled time, is FAILED with DELIVERY_FAILED. Any other social post that could not be published stays PENDING while it is investigated, and is reported FAILED with DELIVERY_FAILED once it is confirmed it will not go out. Deactivate and activate the asset again to retry."""
    source_asset_template_id: NotRequired["capo_partnercentral_marketing.types.id.Id"]
    """The asset template this asset was created from: the `SourceAssetTemplateIdentifier` its `BatchCreateCampaignAsset` entry named, one of `GetCampaignTemplate`'s `CampaignTemplate.AssetTemplates[].Id`. Set at create and never writable. Absent on an asset created before DG recorded it, which can't be activated either. A campaign holds at most one asset per asset template, so this is how a client matches a campaign's assets to its template's asset templates, for example to create the same assets in another campaign. Names don't identify one: two asset templates can share a name."""
    social_platform: NotRequired[
        "capo_partnercentral_marketing.types.platform.Platform"
    ]
    """SOCIAL_POST only: the platform the post goes to, set from its template and never writable. The same value `CampaignAssetSummary.SocialPlatform` reports. Absent for every other category."""
    file_format: NotRequired[
        "capo_partnercentral_marketing.types.file_format.FileFormat"
    ]
    """Concrete file format of the finished artifact. For `DOWNLOAD_ONLY` this is the format of the object export copies through verbatim."""
    send_mode: NotRequired["capo_partnercentral_marketing.types.send_mode.SendMode"]
    """When this asset sends, as chosen with UpdateCampaignAsset. `EMAIL` and `SOCIAL_POST` only — the two categories whose delivery platform holds a schedule of its own. Absent until chosen, and then the asset reports `SEND_MODE_MISSING`."""
    scheduled_send_at: NotRequired[
        "capo_partnercentral_marketing.types.timestamp.Timestamp"
    ]
    """The send time, present only when `SendMode` is `SCHEDULED`. It reaches the delivery platform at the asset's next activation. Was `scheduleDate: UtcDate`; retyped with the write member of the same name."""
    field_values: NotRequired[
        "capo_partnercentral_marketing.types.campaign_asset_field_value_list.CampaignAssetFieldValueList"
    ]
    """The asset's pinned template fields — the field schema copied from the blueprint at instantiation, each paired with the partner's current value. Present on every asset instantiated from a blueprint that offers editable fields, whatever its category (design section 3.1); absent on one whose blueprint offers none."""
    layout_previews: NotRequired[
        "capo_partnercentral_marketing.types.layout_preview_list.LayoutPreviewList"
    ]
    """The asset's AWS-authored layout, as stable public CDN URLs composed from the fileKeys copied off the blueprint at instantiation. Together with FieldValues this makes the asset self-describing: a client renders the edit form and shows the real layout while editing, with no template lookup. The stored form is a bare object key and the URL is composed on read. The key is revision-addressed and prior revisions are retained, so the key IS the pin — nothing is copied into the asset bucket, and there is no version parameter to carry (DG-038). One entry for every category except LANDING_PAGE, which has two and distinguishes them with PageType. On a multi-layout asset, the SELECTED option's pages only (its first option when none is stored); each option's own previews are on layout.options."""
    layout: NotRequired[
        "capo_partnercentral_marketing.types.campaign_asset_layout.CampaignAssetLayout"
    ]
    """A multi-layout asset's layout choice (DG-044): the selection once made, and every option the asset was created with. Absent for a single-layout asset. FieldValues is always the union of every option's fields, selected or not, so a client can switch layouts without a round trip: each option lists its own FieldIds. The selection drives layout.selected and the top-level LayoutPreviews only."""
    activation_issues: (
        "capo_partnercentral_marketing.types.activation_issue_list.ActivationIssueList"
    )
    """What must be fixed on this asset before it can be activated. Empty when the asset is ready. Issues don't block saving: an asset can be saved incomplete and fixed over several updates. `StartCampaignAssetActivationTask` refuses an asset that still has issues: an issue blocks activation when only an edit to the asset can change the outcome. Most issues name the field to fix in `FieldId`. Fix it with `UpdateCampaignAsset`, then read this list again. Besides the issues computed from the asset's content, the list carries what the last activation found: `CONTENT_REJECTED` and `PARTNER_IMAGE_REJECTED` when moderation refused a field. Editing that field removes its issue. A `CONTENT_REJECTED` without a `FieldId` means the text was refused as a whole; editing any text field removes it. Problems with the campaign's own settings, such as a missing recipient list, and with the partner's profile, such as a missing logo, are reported on `Campaign.ActivationIssues`, not here."""
    public_url: NotRequired["capo_partnercentral_marketing.types.public_url.PublicUrl"]
    """The live public address this asset's activation produced. A landing page's page URL, read back from the delivery platform at activation and preserved across every convergence; a document's public CDN URL, composed on read from the key the publish wrote. Absent until the asset activates, and absent for EMAIL and SOCIAL_POST, which produce no partner-addressable URL of their own. For a landing page this is the entire deliverable — without it a partner has no way to learn where their live page is. A WIDGET landing page reports none: it is embedded rather than standalone, so absence there is expected rather than a fault."""
    created_at: NotRequired["capo_partnercentral_marketing.types.timestamp.Timestamp"]
    """Creation timestamp."""
    updated_at: NotRequired["capo_partnercentral_marketing.types.timestamp.Timestamp"]
    """Last update timestamp."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAsset) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["CampaignId"] = value["campaign_id"]
    import capo_partnercentral_marketing.types.campaign_asset_category

    out["Category"] = (
        capo_partnercentral_marketing.types.campaign_asset_category.serialize_cbor(
            value["category"]
        )
    )
    out["Name"] = value["name"]
    if "link_label" in value:
        out["LinkLabel"] = value["link_label"]
    import capo_partnercentral_marketing.types.campaign_asset_state

    out["State"] = (
        capo_partnercentral_marketing.types.campaign_asset_state.serialize_cbor(
            value["state"]
        )
    )
    if "last_activation_status" in value:
        import capo_partnercentral_marketing.types.attempt_status

        out["LastActivationStatus"] = (
            capo_partnercentral_marketing.types.attempt_status.serialize_cbor(
                value["last_activation_status"]
            )
        )
    if "delivery_status" in value:
        import capo_partnercentral_marketing.types.delivery_status

        out["DeliveryStatus"] = (
            capo_partnercentral_marketing.types.delivery_status.serialize_cbor(
                value["delivery_status"]
            )
        )
    if "delivery_status_reason" in value:
        import capo_partnercentral_marketing.types.campaign_asset_state_reason

        out["DeliveryStatusReason"] = (
            capo_partnercentral_marketing.types.campaign_asset_state_reason.serialize_cbor(
                value["delivery_status_reason"]
            )
        )
    if "source_asset_template_id" in value:
        out["SourceAssetTemplateId"] = value["source_asset_template_id"]
    if "social_platform" in value:
        import capo_partnercentral_marketing.types.platform

        out["SocialPlatform"] = (
            capo_partnercentral_marketing.types.platform.serialize_cbor(
                value["social_platform"]
            )
        )
    if "file_format" in value:
        import capo_partnercentral_marketing.types.file_format

        out["FileFormat"] = (
            capo_partnercentral_marketing.types.file_format.serialize_cbor(
                value["file_format"]
            )
        )
    if "send_mode" in value:
        import capo_partnercentral_marketing.types.send_mode

        out["SendMode"] = capo_partnercentral_marketing.types.send_mode.serialize_cbor(
            value["send_mode"]
        )
    if "scheduled_send_at" in value:
        import capo_partnercentral_marketing.types.timestamp

        out["ScheduledSendAt"] = (
            capo_partnercentral_marketing.types.timestamp.serialize_cbor(
                value["scheduled_send_at"]
            )
        )
    if "field_values" in value:
        import capo_partnercentral_marketing.types.campaign_asset_field_value_list

        out["FieldValues"] = (
            capo_partnercentral_marketing.types.campaign_asset_field_value_list.serialize_cbor(
                value["field_values"]
            )
        )
    if "layout_previews" in value:
        import capo_partnercentral_marketing.types.layout_preview_list

        out["LayoutPreviews"] = (
            capo_partnercentral_marketing.types.layout_preview_list.serialize_cbor(
                value["layout_previews"]
            )
        )
    if "layout" in value:
        import capo_partnercentral_marketing.types.campaign_asset_layout

        out["Layout"] = (
            capo_partnercentral_marketing.types.campaign_asset_layout.serialize_cbor(
                value["layout"]
            )
        )
    import capo_partnercentral_marketing.types.activation_issue_list

    out["ActivationIssues"] = (
        capo_partnercentral_marketing.types.activation_issue_list.serialize_cbor(
            value["activation_issues"]
        )
    )
    if "public_url" in value:
        out["PublicUrl"] = value["public_url"]
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
    return out


def deserialize_cbor(data: dict) -> CampaignAsset:
    out: CampaignAsset = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("CampaignId") is not None:
        out["campaign_id"] = data["CampaignId"]
    else:
        out["campaign_id"] = ""
    if data.get("Category") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_category

        out["category"] = (
            capo_partnercentral_marketing.types.campaign_asset_category.deserialize_cbor(
                data["Category"]
            )
        )
    else:
        import typing

        out["category"] = typing.cast(
            "capo_partnercentral_marketing.types.campaign_asset_category.CampaignAssetCategory",
            "",
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("LinkLabel") is not None:
        out["link_label"] = data["LinkLabel"]
    if data.get("State") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_state

        out["state"] = (
            capo_partnercentral_marketing.types.campaign_asset_state.deserialize_cbor(
                data["State"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_partnercentral_marketing.types.campaign_asset_state.CampaignAssetState",
            "",
        )
    if data.get("LastActivationStatus") is not None:
        import capo_partnercentral_marketing.types.attempt_status

        out["last_activation_status"] = (
            capo_partnercentral_marketing.types.attempt_status.deserialize_cbor(
                data["LastActivationStatus"]
            )
        )
    if data.get("DeliveryStatus") is not None:
        import capo_partnercentral_marketing.types.delivery_status

        out["delivery_status"] = (
            capo_partnercentral_marketing.types.delivery_status.deserialize_cbor(
                data["DeliveryStatus"]
            )
        )
    if data.get("DeliveryStatusReason") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_state_reason

        out["delivery_status_reason"] = (
            capo_partnercentral_marketing.types.campaign_asset_state_reason.deserialize_cbor(
                data["DeliveryStatusReason"]
            )
        )
    if data.get("SourceAssetTemplateId") is not None:
        out["source_asset_template_id"] = data["SourceAssetTemplateId"]
    if data.get("SocialPlatform") is not None:
        import capo_partnercentral_marketing.types.platform

        out["social_platform"] = (
            capo_partnercentral_marketing.types.platform.deserialize_cbor(
                data["SocialPlatform"]
            )
        )
    if data.get("FileFormat") is not None:
        import capo_partnercentral_marketing.types.file_format

        out["file_format"] = (
            capo_partnercentral_marketing.types.file_format.deserialize_cbor(
                data["FileFormat"]
            )
        )
    if data.get("SendMode") is not None:
        import capo_partnercentral_marketing.types.send_mode

        out["send_mode"] = (
            capo_partnercentral_marketing.types.send_mode.deserialize_cbor(
                data["SendMode"]
            )
        )
    if data.get("ScheduledSendAt") is not None:
        import capo_partnercentral_marketing.types.timestamp

        out["scheduled_send_at"] = (
            capo_partnercentral_marketing.types.timestamp.deserialize_cbor(
                data["ScheduledSendAt"]
            )
        )
    if data.get("FieldValues") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_field_value_list

        out["field_values"] = (
            capo_partnercentral_marketing.types.campaign_asset_field_value_list.deserialize_cbor(
                data["FieldValues"]
            )
        )
    if data.get("LayoutPreviews") is not None:
        import capo_partnercentral_marketing.types.layout_preview_list

        out["layout_previews"] = (
            capo_partnercentral_marketing.types.layout_preview_list.deserialize_cbor(
                data["LayoutPreviews"]
            )
        )
    if data.get("Layout") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_layout

        out["layout"] = (
            capo_partnercentral_marketing.types.campaign_asset_layout.deserialize_cbor(
                data["Layout"]
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
    if data.get("PublicUrl") is not None:
        out["public_url"] = data["PublicUrl"]
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
    return out


def redact_sensitive(value: CampaignAsset) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_values" in value:
        import capo_partnercentral_marketing.types.campaign_asset_field_value_list

        out["field_values"] = (
            capo_partnercentral_marketing.types.campaign_asset_field_value_list.redact_sensitive(
                value["field_values"]
            )
        )
    return out
