"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#WhatsAppOutboundConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.arn


class WhatsAppOutboundConfig(TypedDict, closed=True):
    connect_source_phone_number_arn: "capo_connectcampaignsv2.types.arn.Arn"
    wisdom_template_arn: "capo_connectcampaignsv2.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppOutboundConfig) -> dict:
    out: dict = {}
    out["connectSourcePhoneNumberArn"] = value["connect_source_phone_number_arn"]
    out["wisdomTemplateArn"] = value["wisdom_template_arn"]
    return out


def deserialize_json(data: dict) -> WhatsAppOutboundConfig:
    out: WhatsAppOutboundConfig = {}  # type: ignore[typeddict-item]
    if data.get("connectSourcePhoneNumberArn") is not None:
        out["connect_source_phone_number_arn"] = data["connectSourcePhoneNumberArn"]
    else:
        out["connect_source_phone_number_arn"] = ""
    if data.get("wisdomTemplateArn") is not None:
        out["wisdom_template_arn"] = data["wisdomTemplateArn"]
    else:
        out["wisdom_template_arn"] = ""
    return out
