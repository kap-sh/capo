"""Generated from Smithy shape ``com.amazonaws.b2bi#UpdatePartnershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.capability_options
    import capo_b2bi.types.partner_name
    import capo_b2bi.types.partnership_capabilities
    import capo_b2bi.types.partnership_id


class UpdatePartnershipRequest(TypedDict, closed=True):
    partnership_id: "capo_b2bi.types.partnership_id.PartnershipId"
    """<p>Specifies the unique, system-generated identifier for a partnership.</p>"""
    name: NotRequired["capo_b2bi.types.partner_name.PartnerName"]
    """<p>The name of the partnership, used to identify it.</p>"""
    capabilities: NotRequired[
        "capo_b2bi.types.partnership_capabilities.PartnershipCapabilities"
    ]
    """<p>List of the capabilities associated with this partnership.</p>"""
    capability_options: NotRequired[
        "capo_b2bi.types.capability_options.CapabilityOptions"
    ]
    """<p>To update, specify the structure that contains the details for the associated capabilities.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdatePartnershipRequest) -> dict:
    out: dict = {}
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
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdatePartnershipRequest:
    out: UpdatePartnershipRequest = {}  # type: ignore[typeddict-item]
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
    return out
