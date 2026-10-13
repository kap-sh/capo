"""Generated from Smithy shape ``com.amazonaws.networkmanager#Site``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.date_time
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.location
    import capo_networkmanager.types.site_arn
    import capo_networkmanager.types.site_id
    import capo_networkmanager.types.site_state
    import capo_networkmanager.types.tag_list


class Site(TypedDict, closed=True):
    site_id: NotRequired["capo_networkmanager.types.site_id.SiteId"]
    """<p>The ID of the site.</p>"""
    site_arn: NotRequired["capo_networkmanager.types.site_arn.SiteArn"]
    """<p>The Amazon Resource Name (ARN) of the site.</p>"""
    global_network_id: NotRequired[
        "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    ]
    """<p>The ID of the global network.</p>"""
    description: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The description of the site.</p>"""
    location: NotRequired["capo_networkmanager.types.location.Location"]
    """<p>The location of the site.</p>"""
    created_at: NotRequired["capo_networkmanager.types.date_time.DateTime"]
    """<p>The date and time that the site was created.</p>"""
    state: NotRequired["capo_networkmanager.types.site_state.SiteState"]
    """<p>The state of the site.</p>"""
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The tags for the site.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Site) -> dict:
    out: dict = {}
    if "site_id" in value:
        out["SiteId"] = value["site_id"]
    if "site_arn" in value:
        out["SiteArn"] = value["site_arn"]
    if "global_network_id" in value:
        out["GlobalNetworkId"] = value["global_network_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "location" in value:
        import capo_networkmanager.types.location

        out["Location"] = capo_networkmanager.types.location.serialize_json(
            value["location"]
        )
    if "created_at" in value:
        import capo_networkmanager.types.date_time

        out["CreatedAt"] = capo_networkmanager.types.date_time.serialize_json(
            value["created_at"]
        )
    if "state" in value:
        import capo_networkmanager.types.site_state

        out["State"] = capo_networkmanager.types.site_state.serialize_json(
            value["state"]
        )
    if "tags" in value:
        import capo_networkmanager.types.tag_list

        out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Site:
    out: Site = {}  # type: ignore[typeddict-item]
    if data.get("SiteId") is not None:
        out["site_id"] = data["SiteId"]
    if data.get("SiteArn") is not None:
        out["site_arn"] = data["SiteArn"]
    if data.get("GlobalNetworkId") is not None:
        out["global_network_id"] = data["GlobalNetworkId"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Location") is not None:
        import capo_networkmanager.types.location

        out["location"] = capo_networkmanager.types.location.deserialize_json(
            data["Location"]
        )
    if data.get("CreatedAt") is not None:
        import capo_networkmanager.types.date_time

        out["created_at"] = capo_networkmanager.types.date_time.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("State") is not None:
        import capo_networkmanager.types.site_state

        out["state"] = capo_networkmanager.types.site_state.deserialize_json(
            data["State"]
        )
    if data.get("Tags") is not None:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    return out


def redact_sensitive(value: Site) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "location" in value:
        out["location"] = "*** Sensitive Data Redacted ***"
    return out
