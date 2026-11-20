"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetStateReason``."""

from typing import Literal, TypeAlias, cast

"""Why an asset could not be, or was not, activated or delivered — the one per-asset reason vocabulary: a task outcome's `Reason` (refused up front or failed during the run), an `ActivationIssue`'s `Code`, DeactivateCampaignAsset's `StateReason`, and an asset's `DeliveryStatusReason`. Some of these require a change before another attempt can succeed; others are transient and a retry is enough. Treat an unrecognised value as transient and retryable."""
CampaignAssetStateReason: TypeAlias = Literal[
    "ASSET_NOT_FOUND",
    "ASSET_NOT_STARTABLE",
    "ASSET_START_IN_PROGRESS",
    "ASSET_ALREADY_ACTIVE",
    "SEND_WINDOW_TOO_SOON",
    "REQUIRED_FIELD_MISSING",
    "RECIPIENT_LIST_MISSING",
    "ENGAGEMENT_GROUPS_UNAVAILABLE",
    "SENDER_EMAIL_MISSING",
    "END_ON_MISSING",
    "ASSET_CONTENT_MISSING",
    "ASSET_NOT_ACTIVATABLE",
    "TEMPLATE_CHANGED",
    "PARTNER_IMAGE_REJECTED",
    "PREREQUISITE_ASSET_NOT_ACTIVE",
    "PARTNER_NOT_PROVISIONED",
    "RECIPIENT_LIST_EMPTY",
    "RECIPIENT_LIMIT_EXCEEDED",
    "CONTACT_OPT_IN_REQUIRED",
    "MAILING_CREDITS_EXHAUSTED",
    "SENDER_EMAIL_INVALID",
    "SOCIAL_CONNECTION_MISSING",
    "SOCIAL_CONNECTION_EXPIRED",
    "SOCIAL_CONNECTION_PAGE_REQUIRED",
    "DELIVERY_FAILED",
    "INTERNAL_ERROR",
    "MAILING_CREDITS_INSUFFICIENT",
    "PARTNER_PROFILE_FIELD_MISSING",
    "PARTNER_PROFILE_FIELD_DOES_NOT_FIT",
    "SOCIAL_CONNECTION_NOT_CHOSEN",
    "PRIVACY_POLICY_URL_MISSING",
    "PARTNER_ADDRESS_MISSING",
    "SEND_MODE_MISSING",
    "CONTENT_REJECTED",
    "URL_NOT_ALLOWED",
    "SENDER_NOT_APPROVED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetStateReason) -> str:
    return value


def deserialize_cbor(data: str) -> CampaignAssetStateReason:
    return cast(CampaignAssetStateReason, data)
