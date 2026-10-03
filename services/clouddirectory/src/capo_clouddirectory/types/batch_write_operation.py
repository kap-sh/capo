"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchWriteOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.batch_add_facet_to_object
    import capo_clouddirectory.types.batch_attach_object
    import capo_clouddirectory.types.batch_attach_policy
    import capo_clouddirectory.types.batch_attach_to_index
    import capo_clouddirectory.types.batch_attach_typed_link
    import capo_clouddirectory.types.batch_create_index
    import capo_clouddirectory.types.batch_create_object
    import capo_clouddirectory.types.batch_delete_object
    import capo_clouddirectory.types.batch_detach_from_index
    import capo_clouddirectory.types.batch_detach_object
    import capo_clouddirectory.types.batch_detach_policy
    import capo_clouddirectory.types.batch_detach_typed_link
    import capo_clouddirectory.types.batch_remove_facet_from_object
    import capo_clouddirectory.types.batch_update_link_attributes
    import capo_clouddirectory.types.batch_update_object_attributes


class BatchWriteOperation(TypedDict, closed=True):
    create_object: NotRequired[
        "capo_clouddirectory.types.batch_create_object.BatchCreateObject"
    ]
    """<p>Creates an object.</p>"""
    attach_object: NotRequired[
        "capo_clouddirectory.types.batch_attach_object.BatchAttachObject"
    ]
    """<p>Attaches an object to a <a>Directory</a>.</p>"""
    detach_object: NotRequired[
        "capo_clouddirectory.types.batch_detach_object.BatchDetachObject"
    ]
    """<p>Detaches an object from a <a>Directory</a>.</p>"""
    update_object_attributes: NotRequired[
        "capo_clouddirectory.types.batch_update_object_attributes.BatchUpdateObjectAttributes"
    ]
    """<p>Updates a given object's attributes.</p>"""
    delete_object: NotRequired[
        "capo_clouddirectory.types.batch_delete_object.BatchDeleteObject"
    ]
    """<p>Deletes an object in a <a>Directory</a>.</p>"""
    add_facet_to_object: NotRequired[
        "capo_clouddirectory.types.batch_add_facet_to_object.BatchAddFacetToObject"
    ]
    """<p>A batch operation that adds a facet to an object.</p>"""
    remove_facet_from_object: NotRequired[
        "capo_clouddirectory.types.batch_remove_facet_from_object.BatchRemoveFacetFromObject"
    ]
    """<p>A batch operation that removes a facet from an object.</p>"""
    attach_policy: NotRequired[
        "capo_clouddirectory.types.batch_attach_policy.BatchAttachPolicy"
    ]
    """<p>Attaches a policy object to a regular object. An object can have a limited number of attached policies.</p>"""
    detach_policy: NotRequired[
        "capo_clouddirectory.types.batch_detach_policy.BatchDetachPolicy"
    ]
    """<p>Detaches a policy from a <a>Directory</a>.</p>"""
    create_index: NotRequired[
        "capo_clouddirectory.types.batch_create_index.BatchCreateIndex"
    ]
    """<p>Creates an index object. See <a href="https://docs.aws.amazon.com/clouddirectory/latest/developerguide/indexing_search.htm">Indexing and search</a> for more information.</p>"""
    attach_to_index: NotRequired[
        "capo_clouddirectory.types.batch_attach_to_index.BatchAttachToIndex"
    ]
    """<p>Attaches the specified object to the specified index.</p>"""
    detach_from_index: NotRequired[
        "capo_clouddirectory.types.batch_detach_from_index.BatchDetachFromIndex"
    ]
    """<p>Detaches the specified object from the specified index.</p>"""
    attach_typed_link: NotRequired[
        "capo_clouddirectory.types.batch_attach_typed_link.BatchAttachTypedLink"
    ]
    """<p>Attaches a typed link to a specified source and target object. For more information, see <a href="https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink">Typed Links</a>.</p>"""
    detach_typed_link: NotRequired[
        "capo_clouddirectory.types.batch_detach_typed_link.BatchDetachTypedLink"
    ]
    """<p>Detaches a typed link from a specified source and target object. For more information, see <a href="https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink">Typed Links</a>.</p>"""
    update_link_attributes: NotRequired[
        "capo_clouddirectory.types.batch_update_link_attributes.BatchUpdateLinkAttributes"
    ]
    """<p>Updates a given object's attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchWriteOperation) -> dict:
    out: dict = {}
    if "create_object" in value:
        import capo_clouddirectory.types.batch_create_object

        out["CreateObject"] = (
            capo_clouddirectory.types.batch_create_object.serialize_json(
                value["create_object"]
            )
        )
    if "attach_object" in value:
        import capo_clouddirectory.types.batch_attach_object

        out["AttachObject"] = (
            capo_clouddirectory.types.batch_attach_object.serialize_json(
                value["attach_object"]
            )
        )
    if "detach_object" in value:
        import capo_clouddirectory.types.batch_detach_object

        out["DetachObject"] = (
            capo_clouddirectory.types.batch_detach_object.serialize_json(
                value["detach_object"]
            )
        )
    if "update_object_attributes" in value:
        import capo_clouddirectory.types.batch_update_object_attributes

        out["UpdateObjectAttributes"] = (
            capo_clouddirectory.types.batch_update_object_attributes.serialize_json(
                value["update_object_attributes"]
            )
        )
    if "delete_object" in value:
        import capo_clouddirectory.types.batch_delete_object

        out["DeleteObject"] = (
            capo_clouddirectory.types.batch_delete_object.serialize_json(
                value["delete_object"]
            )
        )
    if "add_facet_to_object" in value:
        import capo_clouddirectory.types.batch_add_facet_to_object

        out["AddFacetToObject"] = (
            capo_clouddirectory.types.batch_add_facet_to_object.serialize_json(
                value["add_facet_to_object"]
            )
        )
    if "remove_facet_from_object" in value:
        import capo_clouddirectory.types.batch_remove_facet_from_object

        out["RemoveFacetFromObject"] = (
            capo_clouddirectory.types.batch_remove_facet_from_object.serialize_json(
                value["remove_facet_from_object"]
            )
        )
    if "attach_policy" in value:
        import capo_clouddirectory.types.batch_attach_policy

        out["AttachPolicy"] = (
            capo_clouddirectory.types.batch_attach_policy.serialize_json(
                value["attach_policy"]
            )
        )
    if "detach_policy" in value:
        import capo_clouddirectory.types.batch_detach_policy

        out["DetachPolicy"] = (
            capo_clouddirectory.types.batch_detach_policy.serialize_json(
                value["detach_policy"]
            )
        )
    if "create_index" in value:
        import capo_clouddirectory.types.batch_create_index

        out["CreateIndex"] = (
            capo_clouddirectory.types.batch_create_index.serialize_json(
                value["create_index"]
            )
        )
    if "attach_to_index" in value:
        import capo_clouddirectory.types.batch_attach_to_index

        out["AttachToIndex"] = (
            capo_clouddirectory.types.batch_attach_to_index.serialize_json(
                value["attach_to_index"]
            )
        )
    if "detach_from_index" in value:
        import capo_clouddirectory.types.batch_detach_from_index

        out["DetachFromIndex"] = (
            capo_clouddirectory.types.batch_detach_from_index.serialize_json(
                value["detach_from_index"]
            )
        )
    if "attach_typed_link" in value:
        import capo_clouddirectory.types.batch_attach_typed_link

        out["AttachTypedLink"] = (
            capo_clouddirectory.types.batch_attach_typed_link.serialize_json(
                value["attach_typed_link"]
            )
        )
    if "detach_typed_link" in value:
        import capo_clouddirectory.types.batch_detach_typed_link

        out["DetachTypedLink"] = (
            capo_clouddirectory.types.batch_detach_typed_link.serialize_json(
                value["detach_typed_link"]
            )
        )
    if "update_link_attributes" in value:
        import capo_clouddirectory.types.batch_update_link_attributes

        out["UpdateLinkAttributes"] = (
            capo_clouddirectory.types.batch_update_link_attributes.serialize_json(
                value["update_link_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchWriteOperation:
    out: BatchWriteOperation = {}  # type: ignore[typeddict-item]
    if data.get("CreateObject") is not None:
        import capo_clouddirectory.types.batch_create_object

        out["create_object"] = (
            capo_clouddirectory.types.batch_create_object.deserialize_json(
                data["CreateObject"]
            )
        )
    if data.get("AttachObject") is not None:
        import capo_clouddirectory.types.batch_attach_object

        out["attach_object"] = (
            capo_clouddirectory.types.batch_attach_object.deserialize_json(
                data["AttachObject"]
            )
        )
    if data.get("DetachObject") is not None:
        import capo_clouddirectory.types.batch_detach_object

        out["detach_object"] = (
            capo_clouddirectory.types.batch_detach_object.deserialize_json(
                data["DetachObject"]
            )
        )
    if data.get("UpdateObjectAttributes") is not None:
        import capo_clouddirectory.types.batch_update_object_attributes

        out["update_object_attributes"] = (
            capo_clouddirectory.types.batch_update_object_attributes.deserialize_json(
                data["UpdateObjectAttributes"]
            )
        )
    if data.get("DeleteObject") is not None:
        import capo_clouddirectory.types.batch_delete_object

        out["delete_object"] = (
            capo_clouddirectory.types.batch_delete_object.deserialize_json(
                data["DeleteObject"]
            )
        )
    if data.get("AddFacetToObject") is not None:
        import capo_clouddirectory.types.batch_add_facet_to_object

        out["add_facet_to_object"] = (
            capo_clouddirectory.types.batch_add_facet_to_object.deserialize_json(
                data["AddFacetToObject"]
            )
        )
    if data.get("RemoveFacetFromObject") is not None:
        import capo_clouddirectory.types.batch_remove_facet_from_object

        out["remove_facet_from_object"] = (
            capo_clouddirectory.types.batch_remove_facet_from_object.deserialize_json(
                data["RemoveFacetFromObject"]
            )
        )
    if data.get("AttachPolicy") is not None:
        import capo_clouddirectory.types.batch_attach_policy

        out["attach_policy"] = (
            capo_clouddirectory.types.batch_attach_policy.deserialize_json(
                data["AttachPolicy"]
            )
        )
    if data.get("DetachPolicy") is not None:
        import capo_clouddirectory.types.batch_detach_policy

        out["detach_policy"] = (
            capo_clouddirectory.types.batch_detach_policy.deserialize_json(
                data["DetachPolicy"]
            )
        )
    if data.get("CreateIndex") is not None:
        import capo_clouddirectory.types.batch_create_index

        out["create_index"] = (
            capo_clouddirectory.types.batch_create_index.deserialize_json(
                data["CreateIndex"]
            )
        )
    if data.get("AttachToIndex") is not None:
        import capo_clouddirectory.types.batch_attach_to_index

        out["attach_to_index"] = (
            capo_clouddirectory.types.batch_attach_to_index.deserialize_json(
                data["AttachToIndex"]
            )
        )
    if data.get("DetachFromIndex") is not None:
        import capo_clouddirectory.types.batch_detach_from_index

        out["detach_from_index"] = (
            capo_clouddirectory.types.batch_detach_from_index.deserialize_json(
                data["DetachFromIndex"]
            )
        )
    if data.get("AttachTypedLink") is not None:
        import capo_clouddirectory.types.batch_attach_typed_link

        out["attach_typed_link"] = (
            capo_clouddirectory.types.batch_attach_typed_link.deserialize_json(
                data["AttachTypedLink"]
            )
        )
    if data.get("DetachTypedLink") is not None:
        import capo_clouddirectory.types.batch_detach_typed_link

        out["detach_typed_link"] = (
            capo_clouddirectory.types.batch_detach_typed_link.deserialize_json(
                data["DetachTypedLink"]
            )
        )
    if data.get("UpdateLinkAttributes") is not None:
        import capo_clouddirectory.types.batch_update_link_attributes

        out["update_link_attributes"] = (
            capo_clouddirectory.types.batch_update_link_attributes.deserialize_json(
                data["UpdateLinkAttributes"]
            )
        )
    return out
