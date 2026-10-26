"""Generated from Smithy shape ``com.amazonaws.connectcases#GetLayoutResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.created_time
    import capo_connectcases.types.deleted
    import capo_connectcases.types.last_modified_time
    import capo_connectcases.types.layout_arn
    import capo_connectcases.types.layout_content
    import capo_connectcases.types.layout_id
    import capo_connectcases.types.layout_name
    import capo_connectcases.types.tags


class GetLayoutResponse(TypedDict, closed=True):
    layout_id: "capo_connectcases.types.layout_id.LayoutId"
    """<p>The unique identifier of the layout.</p>"""
    layout_arn: "capo_connectcases.types.layout_arn.LayoutArn"
    """<p>The Amazon Resource Name (ARN) of the newly created layout.</p>"""
    name: "capo_connectcases.types.layout_name.LayoutName"
    """<p>The name of the layout. It must be unique.</p>"""
    content: "capo_connectcases.types.layout_content.LayoutContent"
    """<p>Information about which fields will be present in the layout, the order of the fields, and read-only attribute of the field. </p>"""
    tags: NotRequired["capo_connectcases.types.tags.Tags"]
    """<p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>"""
    deleted: "capo_connectcases.types.deleted.Deleted"
    """<p>Denotes whether or not the resource has been deleted.</p>"""
    created_time: NotRequired["capo_connectcases.types.created_time.CreatedTime"]
    """<p>Timestamp at which the resource was created.</p>"""
    last_modified_time: NotRequired[
        "capo_connectcases.types.last_modified_time.LastModifiedTime"
    ]
    """<p>Timestamp at which the resource was created or last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLayoutResponse) -> dict:
    out: dict = {}
    out["layoutId"] = value["layout_id"]
    out["layoutArn"] = value["layout_arn"]
    out["name"] = value["name"]
    import capo_connectcases.types.layout_content

    out["content"] = capo_connectcases.types.layout_content.serialize_json(
        value["content"]
    )
    if "tags" in value:
        import capo_connectcases.types.tags

        out["tags"] = capo_connectcases.types.tags.serialize_json(value["tags"])
    out["deleted"] = value.get("deleted", False)
    if "created_time" in value:
        import capo_connectcases.types.created_time

        out["createdTime"] = capo_connectcases.types.created_time.serialize_json(
            value["created_time"]
        )
    if "last_modified_time" in value:
        import capo_connectcases.types.last_modified_time

        out["lastModifiedTime"] = (
            capo_connectcases.types.last_modified_time.serialize_json(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetLayoutResponse:
    out: GetLayoutResponse = {}  # type: ignore[typeddict-item]
    if data.get("layoutId") is not None:
        out["layout_id"] = data["layoutId"]
    else:
        out["layout_id"] = ""
    if data.get("layoutArn") is not None:
        out["layout_arn"] = data["layoutArn"]
    else:
        out["layout_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("content") is not None:
        import capo_connectcases.types.layout_content

        out["content"] = capo_connectcases.types.layout_content.deserialize_json(
            data["content"]
        )
    else:
        out["content"] = {"$unknown": {"name": ""}}
    if data.get("tags") is not None:
        import capo_connectcases.types.tags

        out["tags"] = capo_connectcases.types.tags.deserialize_json(data["tags"])
    if data.get("deleted") is not None:
        out["deleted"] = data["deleted"]
    else:
        out["deleted"] = False
    if data.get("createdTime") is not None:
        import capo_connectcases.types.created_time

        out["created_time"] = capo_connectcases.types.created_time.deserialize_json(
            data["createdTime"]
        )
    if data.get("lastModifiedTime") is not None:
        import capo_connectcases.types.last_modified_time

        out["last_modified_time"] = (
            capo_connectcases.types.last_modified_time.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    return out
