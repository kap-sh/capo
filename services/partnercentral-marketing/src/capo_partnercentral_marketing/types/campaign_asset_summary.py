"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.asset_name
    import capo_partnercentral_marketing.types.attempt_status
    import capo_partnercentral_marketing.types.campaign_asset_category
    import capo_partnercentral_marketing.types.campaign_asset_id
    import capo_partnercentral_marketing.types.campaign_asset_state
    import capo_partnercentral_marketing.types.campaign_asset_state_reason
    import capo_partnercentral_marketing.types.delivery_status
    import capo_partnercentral_marketing.types.file_format
    import capo_partnercentral_marketing.types.id
    import capo_partnercentral_marketing.types.link_label
    import capo_partnercentral_marketing.types.platform
    import capo_partnercentral_marketing.types.send_mode
    import capo_partnercentral_marketing.types.timestamp


class CampaignAssetSummary(TypedDict, closed=True):
    id: "capo_partnercentral_marketing.types.campaign_asset_id.CampaignAssetId"
    """The asset identifier."""
    category: "capo_partnercentral_marketing.types.campaign_asset_category.CampaignAssetCategory"
    """The asset category."""
    name: "capo_partnercentral_marketing.types.asset_name.AssetName"
    """The display name."""
    link_label: NotRequired["capo_partnercentral_marketing.types.link_label.LinkLabel"]
    """DOCUMENT only: the words a page uses for this document, such as "eBook". A client listing the candidates for an `AssetLink` field reads it here, so a preview can update on pick without a fetch."""
    state: NotRequired[
        "capo_partnercentral_marketing.types.campaign_asset_state.CampaignAssetState"
    ]
    """Where the asset sits in its lifecycle."""
    last_activation_status: NotRequired[
        "capo_partnercentral_marketing.types.attempt_status.AttemptStatus"
    ]
    """How the last hand-over to the delivery platform ended. Absent before the first activation."""
    delivery_status: NotRequired[
        "capo_partnercentral_marketing.types.delivery_status.DeliveryStatus"
    ]
    """Whether the platform has delivered the asset."""
    delivery_status_reason: NotRequired[
        "capo_partnercentral_marketing.types.campaign_asset_state_reason.CampaignAssetStateReason"
    ]
    """Why delivery failed. Present only when DeliveryStatus is FAILED. For an email the platform rejected: SENDER_EMAIL_INVALID, RECIPIENT_LIST_EMPTY, MAILING_CREDITS_EXHAUSTED or RECIPIENT_LIMIT_EXCEEDED. Otherwise DELIVERY_FAILED. A Facebook post refused because its connection has no Page is FAILED with SOCIAL_CONNECTION_PAGE_REQUIRED, and withdrawn: reconnect Facebook with a Page selected. A social post the platform stopped retrying, because it could not publish within 12 hours of its scheduled time, is FAILED with DELIVERY_FAILED. Any other social post that could not be published stays PENDING while it is investigated, and is reported FAILED with DELIVERY_FAILED once it is confirmed it will not go out. Deactivate and activate the asset again to retry."""
    source_asset_template_id: NotRequired["capo_partnercentral_marketing.types.id.Id"]
    """The asset template this asset was created from. The same value `CampaignAsset.SourceAssetTemplateId` reports, and absent when it is."""
    social_platform: NotRequired[
        "capo_partnercentral_marketing.types.platform.Platform"
    ]
    """SOCIAL_POST only: the platform the post goes to. Join it with ListSocialConnections' status for that platform to show a post that cannot activate (a connection missing, EXPIRED or PAGE_REQUIRED) before Start is pressed."""
    started_at: NotRequired["capo_partnercentral_marketing.types.timestamp.Timestamp"]
    """When the asset first went live, set once. Absent if it never has."""
    file_format: NotRequired[
        "capo_partnercentral_marketing.types.file_format.FileFormat"
    ]
    """Concrete file format of the finished artifact."""
    send_mode: NotRequired["capo_partnercentral_marketing.types.send_mode.SendMode"]
    """When this asset sends, as chosen with UpdateCampaignAsset. `EMAIL` and `SOCIAL_POST` only — the two categories whose delivery platform holds a schedule of its own. Absent until chosen, and then the asset reports `SEND_MODE_MISSING`."""
    scheduled_send_at: NotRequired[
        "capo_partnercentral_marketing.types.timestamp.Timestamp"
    ]
    """The send time, present only when `SendMode` is `SCHEDULED`. It reaches the delivery platform at the asset's next activation. Was `scheduleDate: UtcDate`; retyped with the write member of the same name."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetSummary) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import capo_partnercentral_marketing.types.campaign_asset_category

    out["Category"] = (
        capo_partnercentral_marketing.types.campaign_asset_category.serialize_cbor(
            value["category"]
        )
    )
    out["Name"] = value["name"]
    if "link_label" in value:
        out["LinkLabel"] = value["link_label"]
    if "state" in value:
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
    if "started_at" in value:
        import capo_partnercentral_marketing.types.timestamp

        out["StartedAt"] = capo_partnercentral_marketing.types.timestamp.serialize_cbor(
            value["started_at"]
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
    return out


def deserialize_cbor(data: dict) -> CampaignAssetSummary:
    out: CampaignAssetSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
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
    if data.get("StartedAt") is not None:
        import capo_partnercentral_marketing.types.timestamp

        out["started_at"] = (
            capo_partnercentral_marketing.types.timestamp.deserialize_cbor(
                data["StartedAt"]
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
    return out
