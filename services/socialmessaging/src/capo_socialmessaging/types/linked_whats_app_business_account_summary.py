"""Generated from Smithy shape ``com.amazonaws.socialmessaging#LinkedWhatsAppBusinessAccountSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.direct_send_enforcement_status
    import capo_socialmessaging.types.direct_send_enforcement_status_expires_at
    import capo_socialmessaging.types.linked_whats_app_business_account_arn
    import capo_socialmessaging.types.linked_whats_app_business_account_id
    import capo_socialmessaging.types.registration_status
    import capo_socialmessaging.types.whats_app_business_account_event_destinations
    import capo_socialmessaging.types.whats_app_business_account_id
    import capo_socialmessaging.types.whats_app_business_account_link_date
    import capo_socialmessaging.types.whats_app_business_account_marketing_messages_onboarding_status
    import capo_socialmessaging.types.whats_app_business_account_name
    import capo_socialmessaging.types.whats_app_dataset_id


class LinkedWhatsAppBusinessAccountSummary(TypedDict, closed=True):
    arn: "capo_socialmessaging.types.linked_whats_app_business_account_arn.LinkedWhatsAppBusinessAccountArn"
    """<p>The ARN of the linked WhatsApp Business Account.</p>"""
    id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the linked WhatsApp Business Account, formatted as <code>waba-01234567890123456789012345678901</code>.</p>"""
    waba_id: "capo_socialmessaging.types.whats_app_business_account_id.WhatsAppBusinessAccountId"
    """<p>The WhatsApp Business Account ID provided by Meta.</p>"""
    registration_status: (
        "capo_socialmessaging.types.registration_status.RegistrationStatus"
    )
    """<p>The registration status of the linked WhatsApp Business Account.</p>"""
    link_date: "capo_socialmessaging.types.whats_app_business_account_link_date.WhatsAppBusinessAccountLinkDate"
    """<p>The date the WhatsApp Business Account was linked.</p>"""
    waba_name: "capo_socialmessaging.types.whats_app_business_account_name.WhatsAppBusinessAccountName"
    """<p>The name of the linked WhatsApp Business Account.</p>"""
    event_destinations: "capo_socialmessaging.types.whats_app_business_account_event_destinations.WhatsAppBusinessAccountEventDestinations"
    """<p>The event destinations for the linked WhatsApp Business Account.</p>"""
    marketing_messages_onboarding_status: NotRequired[
        "capo_socialmessaging.types.whats_app_business_account_marketing_messages_onboarding_status.WhatsAppBusinessAccountMarketingMessagesOnboardingStatus"
    ]
    """<p>The onboarding status for the Marketing Messages API. This value is fetched from Meta and indicates whether the WhatsApp Business Account is onboarded for Meta's Marketing Messages API.</p>"""
    direct_send_enforcement_status: NotRequired[
        "capo_socialmessaging.types.direct_send_enforcement_status.DirectSendEnforcementStatus"
    ]
    """<p>The Direct Send enforcement status for the WhatsApp Business Account. Enforcement applies when an account repeatedly sends messages in a category that does not match the content. This field is not present when no enforcement is active.</p>"""
    direct_send_enforcement_status_expires_at: NotRequired[
        "capo_socialmessaging.types.direct_send_enforcement_status_expires_at.DirectSendEnforcementStatusExpiresAt"
    ]
    """<p>The time when the current Direct Send enforcement is expected to lift. This field is not present for permanent enforcement or when no enforcement is active.</p>"""
    dataset_id: NotRequired[
        "capo_socialmessaging.types.whats_app_dataset_id.WhatsAppDatasetId"
    ]
    """<p>The Meta Conversions API dataset ID associated with this WhatsApp Business Account. This value is a numeric string of 10 to 20 digits. This field is not present when no dataset has been created for this account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinkedWhatsAppBusinessAccountSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    out["wabaId"] = value["waba_id"]
    import capo_socialmessaging.types.registration_status

    out["registrationStatus"] = (
        capo_socialmessaging.types.registration_status.serialize_json(
            value["registration_status"]
        )
    )
    import capo_socialmessaging.types.whats_app_business_account_link_date

    out["linkDate"] = (
        capo_socialmessaging.types.whats_app_business_account_link_date.serialize_json(
            value["link_date"]
        )
    )
    out["wabaName"] = value["waba_name"]
    import capo_socialmessaging.types.whats_app_business_account_event_destinations

    out["eventDestinations"] = (
        capo_socialmessaging.types.whats_app_business_account_event_destinations.serialize_json(
            value["event_destinations"]
        )
    )
    if "marketing_messages_onboarding_status" in value:
        out["marketingMessagesOnboardingStatus"] = value[
            "marketing_messages_onboarding_status"
        ]
    if "direct_send_enforcement_status" in value:
        out["directSendEnforcementStatus"] = value["direct_send_enforcement_status"]
    if "direct_send_enforcement_status_expires_at" in value:
        import capo_socialmessaging.types.direct_send_enforcement_status_expires_at

        out["directSendEnforcementStatusExpiresAt"] = (
            capo_socialmessaging.types.direct_send_enforcement_status_expires_at.serialize_json(
                value["direct_send_enforcement_status_expires_at"]
            )
        )
    if "dataset_id" in value:
        out["datasetId"] = value["dataset_id"]
    return out


def deserialize_json(data: dict) -> LinkedWhatsAppBusinessAccountSummary:
    out: LinkedWhatsAppBusinessAccountSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("wabaId") is not None:
        out["waba_id"] = data["wabaId"]
    else:
        out["waba_id"] = ""
    if data.get("registrationStatus") is not None:
        import capo_socialmessaging.types.registration_status

        out["registration_status"] = (
            capo_socialmessaging.types.registration_status.deserialize_json(
                data["registrationStatus"]
            )
        )
    else:
        import typing

        out["registration_status"] = typing.cast(
            "capo_socialmessaging.types.registration_status.RegistrationStatus", ""
        )
    if data.get("linkDate") is not None:
        import capo_socialmessaging.types.whats_app_business_account_link_date

        out["link_date"] = (
            capo_socialmessaging.types.whats_app_business_account_link_date.deserialize_json(
                data["linkDate"]
            )
        )
    else:
        import datetime

        out["link_date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("wabaName") is not None:
        out["waba_name"] = data["wabaName"]
    else:
        out["waba_name"] = ""
    if data.get("eventDestinations") is not None:
        import capo_socialmessaging.types.whats_app_business_account_event_destinations

        out["event_destinations"] = (
            capo_socialmessaging.types.whats_app_business_account_event_destinations.deserialize_json(
                data["eventDestinations"]
            )
        )
    else:
        out["event_destinations"] = []
    if data.get("marketingMessagesOnboardingStatus") is not None:
        out["marketing_messages_onboarding_status"] = data[
            "marketingMessagesOnboardingStatus"
        ]
    if data.get("directSendEnforcementStatus") is not None:
        out["direct_send_enforcement_status"] = data["directSendEnforcementStatus"]
    if data.get("directSendEnforcementStatusExpiresAt") is not None:
        import capo_socialmessaging.types.direct_send_enforcement_status_expires_at

        out["direct_send_enforcement_status_expires_at"] = (
            capo_socialmessaging.types.direct_send_enforcement_status_expires_at.deserialize_json(
                data["directSendEnforcementStatusExpiresAt"]
            )
        )
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    return out
