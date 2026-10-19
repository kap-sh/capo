"""Generated from Smithy shape ``com.amazonaws.b2bi#PartnershipSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.capability_options
    import capo_b2bi.types.created_date
    import capo_b2bi.types.modified_date
    import capo_b2bi.types.partner_name
    import capo_b2bi.types.partnership_capabilities
    import capo_b2bi.types.partnership_id
    import capo_b2bi.types.profile_id
    import capo_b2bi.types.trading_partner_id


class PartnershipSummary(TypedDict, closed=True):
    profile_id: "capo_b2bi.types.profile_id.ProfileId"
    """<p>Returns the unique, system-generated identifier for the profile connected to this partnership.</p>"""
    partnership_id: "capo_b2bi.types.partnership_id.PartnershipId"
    """<p>Returns the unique, system-generated identifier for a partnership.</p>"""
    name: NotRequired["capo_b2bi.types.partner_name.PartnerName"]
    """<p>Returns the name of the partnership.</p>"""
    capabilities: NotRequired[
        "capo_b2bi.types.partnership_capabilities.PartnershipCapabilities"
    ]
    """<p>Returns one or more capabilities associated with this partnership.</p>"""
    capability_options: NotRequired[
        "capo_b2bi.types.capability_options.CapabilityOptions"
    ]
    trading_partner_id: NotRequired[
        "capo_b2bi.types.trading_partner_id.TradingPartnerId"
    ]
    """<p>Returns the unique, system-generated identifier for a trading partner.</p>"""
    created_at: "capo_b2bi.types.created_date.CreatedDate"
    """<p>Returns a timestamp for creation date and time of the partnership.</p>"""
    modified_at: NotRequired["capo_b2bi.types.modified_date.ModifiedDate"]
    """<p>Returns a timestamp that identifies the most recent date and time that the partnership was modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartnershipSummary) -> dict:
    out: dict = {}
    out["profileId"] = value["profile_id"]
    out["partnershipId"] = value["partnership_id"]
    if "name" in value:
        out["name"] = value["name"]
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
    if "modified_at" in value:
        import capo_b2bi.types.modified_date

        out["modifiedAt"] = capo_b2bi.types.modified_date.serialize_aws_json_1_0(
            value["modified_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PartnershipSummary:
    out: PartnershipSummary = {}  # type: ignore[typeddict-item]
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    else:
        out["profile_id"] = ""
    if data.get("partnershipId") is not None:
        out["partnership_id"] = data["partnershipId"]
    else:
        out["partnership_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
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
    if data.get("modifiedAt") is not None:
        import capo_b2bi.types.modified_date

        out["modified_at"] = capo_b2bi.types.modified_date.deserialize_aws_json_1_0(
            data["modifiedAt"]
        )
    return out
