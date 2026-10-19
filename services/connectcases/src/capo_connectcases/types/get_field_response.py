"""Generated from Smithy shape ``com.amazonaws.connectcases#GetFieldResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.created_time
    import capo_connectcases.types.deleted
    import capo_connectcases.types.field_arn
    import capo_connectcases.types.field_attributes
    import capo_connectcases.types.field_description
    import capo_connectcases.types.field_id
    import capo_connectcases.types.field_name
    import capo_connectcases.types.field_namespace
    import capo_connectcases.types.field_type
    import capo_connectcases.types.last_modified_time
    import capo_connectcases.types.tags


class GetFieldResponse(TypedDict, closed=True):
    field_id: "capo_connectcases.types.field_id.FieldId"
    """<p>Unique identifier of the field.</p>"""
    name: "capo_connectcases.types.field_name.FieldName"
    """<p>Name of the field.</p>"""
    field_arn: "capo_connectcases.types.field_arn.FieldArn"
    """<p>The Amazon Resource Name (ARN) of the field.</p>"""
    description: NotRequired[
        "capo_connectcases.types.field_description.FieldDescription"
    ]
    """<p>Description of the field.</p>"""
    type: "capo_connectcases.types.field_type.FieldType"
    """<p>Type of the field.</p>"""
    namespace: "capo_connectcases.types.field_namespace.FieldNamespace"
    """<p>Namespace of the field.</p>"""
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
    attributes: NotRequired["capo_connectcases.types.field_attributes.FieldAttributes"]
    """<p>Union of field attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFieldResponse) -> dict:
    out: dict = {}
    out["fieldId"] = value["field_id"]
    out["name"] = value["name"]
    out["fieldArn"] = value["field_arn"]
    if "description" in value:
        out["description"] = value["description"]
    out["type"] = value["type"]
    out["namespace"] = value["namespace"]
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
    if "attributes" in value:
        import capo_connectcases.types.field_attributes

        out["attributes"] = capo_connectcases.types.field_attributes.serialize_json(
            value["attributes"]
        )
    return out


def deserialize_json(data: dict) -> GetFieldResponse:
    out: GetFieldResponse = {}  # type: ignore[typeddict-item]
    if data.get("fieldId") is not None:
        out["field_id"] = data["fieldId"]
    else:
        out["field_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("fieldArn") is not None:
        out["field_arn"] = data["fieldArn"]
    else:
        out["field_arn"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    else:
        out["namespace"] = ""
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
    if data.get("attributes") is not None:
        import capo_connectcases.types.field_attributes

        out["attributes"] = capo_connectcases.types.field_attributes.deserialize_json(
            data["attributes"]
        )
    return out
