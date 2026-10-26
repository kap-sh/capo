"""Generated from Smithy shape ``com.amazonaws.connectcases#SearchRelatedItemsResponseItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.association_time
    import capo_connectcases.types.related_item_content
    import capo_connectcases.types.related_item_id
    import capo_connectcases.types.related_item_type
    import capo_connectcases.types.tags
    import capo_connectcases.types.user_union


class SearchRelatedItemsResponseItem(TypedDict, closed=True):
    related_item_id: "capo_connectcases.types.related_item_id.RelatedItemId"
    """<p>Unique identifier of a related item.</p>"""
    type: "capo_connectcases.types.related_item_type.RelatedItemType"
    """<p>Type of a related item.</p>"""
    association_time: "capo_connectcases.types.association_time.AssociationTime"
    """<p>Time at which a related item was associated with a case.</p>"""
    content: "capo_connectcases.types.related_item_content.RelatedItemContent"
    """<p>Represents the content of a particular type of related item.</p>"""
    tags: NotRequired["capo_connectcases.types.tags.Tags"]
    """<p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>"""
    performed_by: NotRequired["capo_connectcases.types.user_union.UserUnion"]
    """<p>Represents the creator of the related item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchRelatedItemsResponseItem) -> dict:
    out: dict = {}
    out["relatedItemId"] = value["related_item_id"]
    out["type"] = value["type"]
    import capo_connectcases.types.association_time

    out["associationTime"] = capo_connectcases.types.association_time.serialize_json(
        value["association_time"]
    )
    import capo_connectcases.types.related_item_content

    out["content"] = capo_connectcases.types.related_item_content.serialize_json(
        value["content"]
    )
    if "tags" in value:
        import capo_connectcases.types.tags

        out["tags"] = capo_connectcases.types.tags.serialize_json(value["tags"])
    if "performed_by" in value:
        import capo_connectcases.types.user_union

        out["performedBy"] = capo_connectcases.types.user_union.serialize_json(
            value["performed_by"]
        )
    return out


def deserialize_json(data: dict) -> SearchRelatedItemsResponseItem:
    out: SearchRelatedItemsResponseItem = {}  # type: ignore[typeddict-item]
    if data.get("relatedItemId") is not None:
        out["related_item_id"] = data["relatedItemId"]
    else:
        out["related_item_id"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("associationTime") is not None:
        import capo_connectcases.types.association_time

        out["association_time"] = (
            capo_connectcases.types.association_time.deserialize_json(
                data["associationTime"]
            )
        )
    else:
        import datetime

        out["association_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("content") is not None:
        import capo_connectcases.types.related_item_content

        out["content"] = capo_connectcases.types.related_item_content.deserialize_json(
            data["content"]
        )
    else:
        out["content"] = {"$unknown": {"name": ""}}
    if data.get("tags") is not None:
        import capo_connectcases.types.tags

        out["tags"] = capo_connectcases.types.tags.deserialize_json(data["tags"])
    if data.get("performedBy") is not None:
        import capo_connectcases.types.user_union

        out["performed_by"] = capo_connectcases.types.user_union.deserialize_json(
            data["performedBy"]
        )
    return out


def redact_sensitive(value: SearchRelatedItemsResponseItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        import capo_connectcases.types.related_item_content

        out["content"] = capo_connectcases.types.related_item_content.redact_sensitive(
            value["content"]
        )
    if "performed_by" in value:
        import capo_connectcases.types.user_union

        out["performed_by"] = capo_connectcases.types.user_union.redact_sensitive(
            value["performed_by"]
        )
    return out
