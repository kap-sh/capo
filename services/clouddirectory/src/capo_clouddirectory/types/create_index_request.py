"""Generated from Smithy shape ``com.amazonaws.clouddirectory#CreateIndexRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.attribute_key_list
    import capo_clouddirectory.types.bool
    import capo_clouddirectory.types.link_name
    import capo_clouddirectory.types.object_reference


class CreateIndexRequest(TypedDict, closed=True):
    directory_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The ARN of the directory where the index should be created.</p>"""
    ordered_indexed_attribute_list: (
        "capo_clouddirectory.types.attribute_key_list.AttributeKeyList"
    )
    """<p>Specifies the attributes that should be indexed on. Currently only a single attribute is supported.</p>"""
    is_unique: "capo_clouddirectory.types.bool.Bool"
    """<p>Indicates whether the attribute that is being indexed has unique values or not.</p>"""
    parent_reference: NotRequired[
        "capo_clouddirectory.types.object_reference.ObjectReference"
    ]
    """<p>A reference to the parent object that contains the index object.</p>"""
    link_name: NotRequired["capo_clouddirectory.types.link_name.LinkName"]
    """<p>The name of the link between the parent object and the index object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIndexRequest) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.attribute_key_list

    out["OrderedIndexedAttributeList"] = (
        capo_clouddirectory.types.attribute_key_list.serialize_json(
            value["ordered_indexed_attribute_list"]
        )
    )
    out["IsUnique"] = value["is_unique"]
    if "parent_reference" in value:
        import capo_clouddirectory.types.object_reference

        out["ParentReference"] = (
            capo_clouddirectory.types.object_reference.serialize_json(
                value["parent_reference"]
            )
        )
    if "link_name" in value:
        out["LinkName"] = value["link_name"]
    return out


def deserialize_json(data: dict) -> CreateIndexRequest:
    out: CreateIndexRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrderedIndexedAttributeList") is not None:
        import capo_clouddirectory.types.attribute_key_list

        out["ordered_indexed_attribute_list"] = (
            capo_clouddirectory.types.attribute_key_list.deserialize_json(
                data["OrderedIndexedAttributeList"]
            )
        )
    else:
        raise DeserializationError(
            "CreateIndexRequest.ordered_indexed_attribute_list required"
        )
    if data.get("IsUnique") is not None:
        out["is_unique"] = data["IsUnique"]
    else:
        raise DeserializationError("CreateIndexRequest.is_unique required")
    if data.get("ParentReference") is not None:
        import capo_clouddirectory.types.object_reference

        out["parent_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["ParentReference"]
            )
        )
    if data.get("LinkName") is not None:
        out["link_name"] = data["LinkName"]
    return out
