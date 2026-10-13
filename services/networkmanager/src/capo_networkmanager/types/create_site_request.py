"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateSiteRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.location
    import capo_networkmanager.types.tag_list


class CreateSiteRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    description: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>A description of your site.</p> <p>Constraints: Maximum length of 256 characters.</p>"""
    location: NotRequired["capo_networkmanager.types.location.Location"]
    """<p>The site location. This information is used for visualization in the Network Manager console. If you specify the address, the latitude and longitude are automatically calculated.</p> <ul> <li> <p> <code>Address</code>: The physical address of the site.</p> </li> <li> <p> <code>Latitude</code>: The latitude of the site. </p> </li> <li> <p> <code>Longitude</code>: The longitude of the site.</p> </li> </ul>"""
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The tags to apply to the resource during creation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSiteRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "location" in value:
        import capo_networkmanager.types.location

        out["Location"] = capo_networkmanager.types.location.serialize_json(
            value["location"]
        )
    if "tags" in value:
        import capo_networkmanager.types.tag_list

        out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSiteRequest:
    out: CreateSiteRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Location") is not None:
        import capo_networkmanager.types.location

        out["location"] = capo_networkmanager.types.location.deserialize_json(
            data["Location"]
        )
    if data.get("Tags") is not None:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    return out


def redact_sensitive(value: CreateSiteRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "location" in value:
        out["location"] = "*** Sensitive Data Redacted ***"
    return out
