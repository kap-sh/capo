"""Generated from Smithy shape ``com.amazonaws.connectcases#UpdateRelatedItemResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.association_time
    import capo_connectcases.types.related_item_arn
    import capo_connectcases.types.related_item_content
    import capo_connectcases.types.related_item_id
    import capo_connectcases.types.related_item_type
    import capo_connectcases.types.tags
    import capo_connectcases.types.user_union


class UpdateRelatedItemResponse(TypedDict, closed=True):
    related_item_id: "capo_connectcases.types.related_item_id.RelatedItemId"
    """<p>The unique identifier of the updated related item.</p>"""
    related_item_arn: "capo_connectcases.types.related_item_arn.RelatedItemArn"
    """<p>The Amazon Resource Name (ARN) of the updated related item.</p>"""
    type: "capo_connectcases.types.related_item_type.RelatedItemType"
    """<p>Type of the updated related item.</p>"""
    content: "capo_connectcases.types.related_item_content.RelatedItemContent"
    """<p>Represents the content of the updated related item.</p>"""
    association_time: "capo_connectcases.types.association_time.AssociationTime"
    """<p>Time at which the related item was associated with the case.</p>"""
    tags: NotRequired["capo_connectcases.types.tags.Tags"]
    """<p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>"""
    last_updated_user: NotRequired["capo_connectcases.types.user_union.UserUnion"]
    """<p>Represents the last user that updated the related item.</p>"""
    created_by: NotRequired["capo_connectcases.types.user_union.UserUnion"]
    """<p>Represents the creator of the related item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRelatedItemResponse) -> dict:
    out: dict = {}
    out["relatedItemId"] = value["related_item_id"]
    out["relatedItemArn"] = value["related_item_arn"]
    out["type"] = value["type"]
    import capo_connectcases.types.related_item_content

    out["content"] = capo_connectcases.types.related_item_content.serialize_json(
        value["content"]
    )
    import capo_connectcases.types.association_time

    out["associationTime"] = capo_connectcases.types.association_time.serialize_json(
        value["association_time"]
    )
    if "tags" in value:
        import capo_connectcases.types.tags

        out["tags"] = capo_connectcases.types.tags.serialize_json(value["tags"])
    if "last_updated_user" in value:
        import capo_connectcases.types.user_union

        out["lastUpdatedUser"] = capo_connectcases.types.user_union.serialize_json(
            value["last_updated_user"]
        )
    if "created_by" in value:
        import capo_connectcases.types.user_union

        out["createdBy"] = capo_connectcases.types.user_union.serialize_json(
            value["created_by"]
        )
    return out


def deserialize_json(data: dict) -> UpdateRelatedItemResponse:
    out: UpdateRelatedItemResponse = {}  # type: ignore[typeddict-item]
    if data.get("relatedItemId") is not None:
        out["related_item_id"] = data["relatedItemId"]
    else:
        out["related_item_id"] = ""
    if data.get("relatedItemArn") is not None:
        out["related_item_arn"] = data["relatedItemArn"]
    else:
        out["related_item_arn"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("content") is not None:
        import capo_connectcases.types.related_item_content

        out["content"] = capo_connectcases.types.related_item_content.deserialize_json(
            data["content"]
        )
    else:
        import capo_connectcases.types._unknown

        out["content"] = capo_connectcases.types._unknown.UnknownUnionMember("")
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
    if data.get("tags") is not None:
        import capo_connectcases.types.tags

        out["tags"] = capo_connectcases.types.tags.deserialize_json(data["tags"])
    if data.get("lastUpdatedUser") is not None:
        import capo_connectcases.types.user_union

        out["last_updated_user"] = capo_connectcases.types.user_union.deserialize_json(
            data["lastUpdatedUser"]
        )
    if data.get("createdBy") is not None:
        import capo_connectcases.types.user_union

        out["created_by"] = capo_connectcases.types.user_union.deserialize_json(
            data["createdBy"]
        )
    return out


def redact_sensitive(value: UpdateRelatedItemResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        import capo_connectcases.types.related_item_content

        out["content"] = capo_connectcases.types.related_item_content.redact_sensitive(
            value["content"]
        )
    if "last_updated_user" in value:
        import capo_connectcases.types.user_union

        out["last_updated_user"] = capo_connectcases.types.user_union.redact_sensitive(
            value["last_updated_user"]
        )
    if "created_by" in value:
        import capo_connectcases.types.user_union

        out["created_by"] = capo_connectcases.types.user_union.redact_sensitive(
            value["created_by"]
        )
    return out
