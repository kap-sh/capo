"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#EmailOutboundConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.arn
    import capo_connectcampaignsv2.types.email_address
    import capo_connectcampaignsv2.types.email_display_name


class EmailOutboundConfig(TypedDict, closed=True):
    connect_source_email_address: (
        "capo_connectcampaignsv2.types.email_address.EmailAddress"
    )
    source_email_address_display_name: NotRequired[
        "capo_connectcampaignsv2.types.email_display_name.EmailDisplayName"
    ]
    wisdom_template_arn: "capo_connectcampaignsv2.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: EmailOutboundConfig) -> dict:
    out: dict = {}
    out["connectSourceEmailAddress"] = value["connect_source_email_address"]
    if "source_email_address_display_name" in value:
        out["sourceEmailAddressDisplayName"] = value[
            "source_email_address_display_name"
        ]
    out["wisdomTemplateArn"] = value["wisdom_template_arn"]
    return out


def deserialize_json(data: dict) -> EmailOutboundConfig:
    out: EmailOutboundConfig = {}  # type: ignore[typeddict-item]
    if data.get("connectSourceEmailAddress") is not None:
        out["connect_source_email_address"] = data["connectSourceEmailAddress"]
    else:
        raise DeserializationError(
            "EmailOutboundConfig.connect_source_email_address required"
        )
    if data.get("sourceEmailAddressDisplayName") is not None:
        out["source_email_address_display_name"] = data["sourceEmailAddressDisplayName"]
    if data.get("wisdomTemplateArn") is not None:
        out["wisdom_template_arn"] = data["wisdomTemplateArn"]
    else:
        raise DeserializationError("EmailOutboundConfig.wisdom_template_arn required")
    return out


def redact_sensitive(value: EmailOutboundConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connect_source_email_address" in value:
        out["connect_source_email_address"] = "*** Sensitive Data Redacted ***"
    if "source_email_address_display_name" in value:
        out["source_email_address_display_name"] = "*** Sensitive Data Redacted ***"
    return out
