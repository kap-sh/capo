"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateLinkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_networkmanager.types.bandwidth
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.site_id
    import capo_networkmanager.types.tag_list


class CreateLinkRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    description: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>A description of the link.</p> <p>Constraints: Maximum length of 256 characters.</p>"""
    type: NotRequired["capo_networkmanager.types.constrained_string.ConstrainedString"]
    r"""<p>The type of the link.</p> <p>Constraints: Maximum length of 128 characters. Cannot include the following characters: | \ ^</p>"""
    bandwidth: "capo_networkmanager.types.bandwidth.Bandwidth"
    """<p> The upload speed and download speed in Mbps. </p>"""
    provider: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    r"""<p>The provider of the link.</p> <p>Constraints: Maximum length of 128 characters. Cannot include the following characters: | \ ^</p>"""
    site_id: "capo_networkmanager.types.site_id.SiteId"
    """<p>The ID of the site.</p>"""
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The tags to apply to the resource during creation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLinkRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        out["Type"] = value["type"]
    import capo_networkmanager.types.bandwidth

    out["Bandwidth"] = capo_networkmanager.types.bandwidth.serialize_json(
        value["bandwidth"]
    )
    if "provider" in value:
        out["Provider"] = value["provider"]
    out["SiteId"] = value["site_id"]
    if "tags" in value:
        import capo_networkmanager.types.tag_list

        out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateLinkRequest:
    out: CreateLinkRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Bandwidth") is not None:
        import capo_networkmanager.types.bandwidth

        out["bandwidth"] = capo_networkmanager.types.bandwidth.deserialize_json(
            data["Bandwidth"]
        )
    else:
        raise DeserializationError("CreateLinkRequest.bandwidth required")
    if data.get("Provider") is not None:
        out["provider"] = data["Provider"]
    if data.get("SiteId") is not None:
        out["site_id"] = data["SiteId"]
    else:
        out["site_id"] = ""
    if data.get("Tags") is not None:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    return out
