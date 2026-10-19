"""Generated from Smithy shape ``com.amazonaws.b2bi#CreatePartnershipRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.capability_options
    import capo_b2bi.types.email
    import capo_b2bi.types.partner_name
    import capo_b2bi.types.partnership_capabilities
    import capo_b2bi.types.phone
    import capo_b2bi.types.profile_id
    import capo_b2bi.types.tag_list


class CreatePartnershipRequest(TypedDict, closed=True):
    profile_id: "capo_b2bi.types.profile_id.ProfileId"
    """<p>Specifies the unique, system-generated identifier for the profile connected to this partnership.</p>"""
    name: "capo_b2bi.types.partner_name.PartnerName"
    """<p>Specifies a descriptive name for the partnership.</p>"""
    email: "capo_b2bi.types.email.Email"
    """<p>Specifies the email address associated with this trading partner.</p>"""
    phone: NotRequired["capo_b2bi.types.phone.Phone"]
    """<p>Specifies the phone number associated with the partnership.</p>"""
    capabilities: "capo_b2bi.types.partnership_capabilities.PartnershipCapabilities"
    """<p>Specifies a list of the capabilities associated with this partnership.</p>"""
    capability_options: NotRequired[
        "capo_b2bi.types.capability_options.CapabilityOptions"
    ]
    """<p>Specify the structure that contains the details for the associated capabilities.</p>"""
    client_token: NotRequired["str"]
    """<p>Reserved for future use.</p>"""
    tags: NotRequired["capo_b2bi.types.tag_list.TagList"]
    """<p>Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreatePartnershipRequest) -> dict:
    out: dict = {}
    out["profileId"] = value["profile_id"]
    out["name"] = value["name"]
    out["email"] = value["email"]
    if "phone" in value:
        out["phone"] = value["phone"]
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_b2bi.types.tag_list

        out["tags"] = capo_b2bi.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> CreatePartnershipRequest:
    out: CreatePartnershipRequest = {}  # type: ignore[typeddict-item]
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    else:
        out["profile_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("email") is not None:
        out["email"] = data["email"]
    else:
        out["email"] = ""
    if data.get("phone") is not None:
        out["phone"] = data["phone"]
    if data.get("capabilities") is not None:
        import capo_b2bi.types.partnership_capabilities

        out["capabilities"] = (
            capo_b2bi.types.partnership_capabilities.deserialize_aws_json_1_0(
                data["capabilities"]
            )
        )
    else:
        out["capabilities"] = []
    if data.get("capabilityOptions") is not None:
        import capo_b2bi.types.capability_options

        out["capability_options"] = (
            capo_b2bi.types.capability_options.deserialize_aws_json_1_0(
                data["capabilityOptions"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_b2bi.types.tag_list

        out["tags"] = capo_b2bi.types.tag_list.deserialize_aws_json_1_0(data["tags"])
    return out


def redact_sensitive(value: CreatePartnershipRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email" in value:
        out["email"] = "*** Sensitive Data Redacted ***"
    if "phone" in value:
        out["phone"] = "*** Sensitive Data Redacted ***"
    return out
