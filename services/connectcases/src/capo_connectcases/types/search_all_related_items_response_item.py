"""Generated from Smithy shape ``com.amazonaws.connectcases#SearchAllRelatedItemsResponseItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.association_time
    import capo_connectcases.types.case_id
    import capo_connectcases.types.related_item_content
    import capo_connectcases.types.related_item_id
    import capo_connectcases.types.related_item_type
    import capo_connectcases.types.tags
    import capo_connectcases.types.user_union


class SearchAllRelatedItemsResponseItem(TypedDict, closed=True):
    related_item_id: "capo_connectcases.types.related_item_id.RelatedItemId"
    """<p>Unique identifier of a related item.</p>"""
    case_id: "capo_connectcases.types.case_id.CaseId"
    """<p>A unique identifier of the case.</p>"""
    type: "capo_connectcases.types.related_item_type.RelatedItemType"
    """<p>Type of a related item.</p>"""
    association_time: "capo_connectcases.types.association_time.AssociationTime"
    """<p>Time at which a related item was associated with a case.</p>"""
    content: "capo_connectcases.types.related_item_content.RelatedItemContent"
    performed_by: NotRequired["capo_connectcases.types.user_union.UserUnion"]
    tags: NotRequired["capo_connectcases.types.tags.Tags"]
    """<p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAllRelatedItemsResponseItem) -> dict:
    out: dict = {}
    out["relatedItemId"] = value["related_item_id"]
    out["caseId"] = value["case_id"]
    out["type"] = value["type"]
    import capo_connectcases.types.association_time

    out["associationTime"] = capo_connectcases.types.association_time.serialize_json(
        value["association_time"]
    )
    import capo_connectcases.types.related_item_content

    out["content"] = capo_connectcases.types.related_item_content.serialize_json(
        value["content"]
    )
    if "performed_by" in value:
        import capo_connectcases.types.user_union

        out["performedBy"] = capo_connectcases.types.user_union.serialize_json(
            value["performed_by"]
        )
    if "tags" in value:
        import capo_connectcases.types.tags

        out["tags"] = capo_connectcases.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> SearchAllRelatedItemsResponseItem:
    out: SearchAllRelatedItemsResponseItem = {}  # type: ignore[typeddict-item]
    if data.get("relatedItemId") is not None:
        out["related_item_id"] = data["relatedItemId"]
    else:
        out["related_item_id"] = ""
    if data.get("caseId") is not None:
        out["case_id"] = data["caseId"]
    else:
        out["case_id"] = ""
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
    if data.get("performedBy") is not None:
        import capo_connectcases.types.user_union

        out["performed_by"] = capo_connectcases.types.user_union.deserialize_json(
            data["performedBy"]
        )
    if data.get("tags") is not None:
        import capo_connectcases.types.tags

        out["tags"] = capo_connectcases.types.tags.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: SearchAllRelatedItemsResponseItem) -> dict[str, Any]:
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
