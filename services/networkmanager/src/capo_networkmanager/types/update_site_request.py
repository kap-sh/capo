"""Generated from Smithy shape ``com.amazonaws.networkmanager#UpdateSiteRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.location
    import capo_networkmanager.types.site_id


class UpdateSiteRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    site_id: "capo_networkmanager.types.site_id.SiteId"
    """<p>The ID of your site.</p>"""
    description: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>A description of your site.</p> <p>Constraints: Maximum length of 256 characters.</p>"""
    location: NotRequired["capo_networkmanager.types.location.Location"]
    """<p>The site location:</p> <ul> <li> <p> <code>Address</code>: The physical address of the site.</p> </li> <li> <p> <code>Latitude</code>: The latitude of the site. </p> </li> <li> <p> <code>Longitude</code>: The longitude of the site.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSiteRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "location" in value:
        import capo_networkmanager.types.location

        out["Location"] = capo_networkmanager.types.location.serialize_json(
            value["location"]
        )
    return out


def deserialize_json(data: dict) -> UpdateSiteRequest:
    out: UpdateSiteRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Location") is not None:
        import capo_networkmanager.types.location

        out["location"] = capo_networkmanager.types.location.deserialize_json(
            data["Location"]
        )
    return out


def redact_sensitive(value: UpdateSiteRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "location" in value:
        out["location"] = "*** Sensitive Data Redacted ***"
    return out
