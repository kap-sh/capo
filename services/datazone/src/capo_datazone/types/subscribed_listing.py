"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedListing``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.description
    import capo_datazone.types.listing_id
    import capo_datazone.types.listing_name
    import capo_datazone.types.project_id
    import capo_datazone.types.revision
    import capo_datazone.types.subscribed_listing_item


class SubscribedListing(TypedDict, closed=True):
    id: "capo_datazone.types.listing_id.ListingId"
    """<p>The identifier of the published asset for which the subscription grant is created.</p>"""
    revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision of the published asset for which the subscription grant is created.</p>"""
    name: "capo_datazone.types.listing_name.ListingName"
    """<p>The name of the published asset for which the subscription grant is created.</p>"""
    description: "capo_datazone.types.description.Description"
    """<p>The description of the published asset for which the subscription grant is created.</p>"""
    item: "capo_datazone.types.subscribed_listing_item.SubscribedListingItem"
    """<p>The published asset for which the subscription grant is created.</p>"""
    owner_project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project of the published asset for which the subscription grant is created.</p>"""
    owner_project_name: NotRequired["str"]
    """<p>The name of the project that owns the published asset for which the subscription grant is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedListing) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "revision" in value:
        out["revision"] = value["revision"]
    out["name"] = value["name"]
    out["description"] = value["description"]
    import capo_datazone.types.subscribed_listing_item

    out["item"] = capo_datazone.types.subscribed_listing_item.serialize_json(
        value["item"]
    )
    out["ownerProjectId"] = value["owner_project_id"]
    if "owner_project_name" in value:
        out["ownerProjectName"] = value["owner_project_name"]
    return out


def deserialize_json(data: dict) -> SubscribedListing:
    out: SubscribedListing = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("item") is not None:
        import capo_datazone.types.subscribed_listing_item

        out["item"] = capo_datazone.types.subscribed_listing_item.deserialize_json(
            data["item"]
        )
    else:
        import capo_datazone.types._unknown

        out["item"] = capo_datazone.types._unknown.UnknownUnionMember("")
    if data.get("ownerProjectId") is not None:
        out["owner_project_id"] = data["ownerProjectId"]
    else:
        out["owner_project_id"] = ""
    if data.get("ownerProjectName") is not None:
        out["owner_project_name"] = data["ownerProjectName"]
    return out


def redact_sensitive(value: SubscribedListing) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "item" in value:
        import capo_datazone.types.subscribed_listing_item

        out["item"] = capo_datazone.types.subscribed_listing_item.redact_sensitive(
            value["item"]
        )
    return out
