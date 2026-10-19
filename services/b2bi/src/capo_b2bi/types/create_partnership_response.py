"""Generated from Smithy shape ``com.amazonaws.b2bi#CreatePartnershipResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.capability_options
    import capo_b2bi.types.created_date
    import capo_b2bi.types.email
    import capo_b2bi.types.partner_name
    import capo_b2bi.types.partnership_capabilities
    import capo_b2bi.types.partnership_id
    import capo_b2bi.types.phone
    import capo_b2bi.types.profile_id
    import capo_b2bi.types.resource_arn
    import capo_b2bi.types.trading_partner_id


class CreatePartnershipResponse(TypedDict, closed=True):
    profile_id: "capo_b2bi.types.profile_id.ProfileId"
    """<p>Returns the unique, system-generated identifier for the profile connected to this partnership.</p>"""
    partnership_id: "capo_b2bi.types.partnership_id.PartnershipId"
    """<p>Returns the unique, system-generated identifier for a partnership.</p>"""
    partnership_arn: "capo_b2bi.types.resource_arn.ResourceArn"
    """<p>Returns an Amazon Resource Name (ARN) for a specific Amazon Web Services resource, such as a capability, partnership, profile, or transformer.</p>"""
    name: NotRequired["capo_b2bi.types.partner_name.PartnerName"]
    """<p>Returns a descriptive name for the partnership.</p>"""
    email: NotRequired["capo_b2bi.types.email.Email"]
    """<p>Returns the email address associated with this trading partner.</p>"""
    phone: NotRequired["capo_b2bi.types.phone.Phone"]
    """<p>Returns the phone number associated with the partnership.</p>"""
    capabilities: NotRequired[
        "capo_b2bi.types.partnership_capabilities.PartnershipCapabilities"
    ]
    """<p>Returns one or more capabilities associated with this partnership.</p>"""
    capability_options: NotRequired[
        "capo_b2bi.types.capability_options.CapabilityOptions"
    ]
    """<p>Returns the structure that contains the details for the associated capabilities.</p>"""
    trading_partner_id: NotRequired[
        "capo_b2bi.types.trading_partner_id.TradingPartnerId"
    ]
    """<p>Returns the unique, system-generated identifier for a trading partner.</p>"""
    created_at: "capo_b2bi.types.created_date.CreatedDate"
    """<p>Returns a timestamp for creation date and time of the partnership.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreatePartnershipResponse) -> dict:
    out: dict = {}
    out["profileId"] = value["profile_id"]
    out["partnershipId"] = value["partnership_id"]
    out["partnershipArn"] = value["partnership_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "email" in value:
        out["email"] = value["email"]
    if "phone" in value:
        out["phone"] = value["phone"]
    if "capabilities" in value:
        import capo_b2bi.types.partnership_capabilities

        out["capabilities"] = (
            capo_b2bi.types.partnership_capabilities.serialize_aws_json_1_0(
                value["capabilities"]
            )
        )
    if "capability_options" in value:
        import capo_b2bi.types.capability_options

        out["capabilityOptions"] = (
            capo_b2bi.types.capability_options.serialize_aws_json_1_0(
                value["capability_options"]
            )
        )
    if "trading_partner_id" in value:
        out["tradingPartnerId"] = value["trading_partner_id"]
    import capo_b2bi.types.created_date

    out["createdAt"] = capo_b2bi.types.created_date.serialize_aws_json_1_0(
        value["created_at"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreatePartnershipResponse:
    out: CreatePartnershipResponse = {}  # type: ignore[typeddict-item]
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    else:
        out["profile_id"] = ""
    if data.get("partnershipId") is not None:
        out["partnership_id"] = data["partnershipId"]
    else:
        out["partnership_id"] = ""
    if data.get("partnershipArn") is not None:
        out["partnership_arn"] = data["partnershipArn"]
    else:
        out["partnership_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("email") is not None:
        out["email"] = data["email"]
    if data.get("phone") is not None:
        out["phone"] = data["phone"]
    if data.get("capabilities") is not None:
        import capo_b2bi.types.partnership_capabilities

        out["capabilities"] = (
            capo_b2bi.types.partnership_capabilities.deserialize_aws_json_1_0(
                data["capabilities"]
            )
        )
    if data.get("capabilityOptions") is not None:
        import capo_b2bi.types.capability_options

        out["capability_options"] = (
            capo_b2bi.types.capability_options.deserialize_aws_json_1_0(
                data["capabilityOptions"]
            )
        )
    if data.get("tradingPartnerId") is not None:
        out["trading_partner_id"] = data["tradingPartnerId"]
    if data.get("createdAt") is not None:
        import capo_b2bi.types.created_date

        out["created_at"] = capo_b2bi.types.created_date.deserialize_aws_json_1_0(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out


def redact_sensitive(value: CreatePartnershipResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email" in value:
        out["email"] = "*** Sensitive Data Redacted ***"
    if "phone" in value:
        out["phone"] = "*** Sensitive Data Redacted ***"
    return out
