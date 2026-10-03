"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchWriteOperationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.batch_add_facet_to_object_response
    import capo_clouddirectory.types.batch_attach_object_response
    import capo_clouddirectory.types.batch_attach_policy_response
    import capo_clouddirectory.types.batch_attach_to_index_response
    import capo_clouddirectory.types.batch_attach_typed_link_response
    import capo_clouddirectory.types.batch_create_index_response
    import capo_clouddirectory.types.batch_create_object_response
    import capo_clouddirectory.types.batch_delete_object_response
    import capo_clouddirectory.types.batch_detach_from_index_response
    import capo_clouddirectory.types.batch_detach_object_response
    import capo_clouddirectory.types.batch_detach_policy_response
    import capo_clouddirectory.types.batch_detach_typed_link_response
    import capo_clouddirectory.types.batch_remove_facet_from_object_response
    import capo_clouddirectory.types.batch_update_link_attributes_response
    import capo_clouddirectory.types.batch_update_object_attributes_response


class BatchWriteOperationResponse(TypedDict, closed=True):
    create_object: NotRequired[
        "capo_clouddirectory.types.batch_create_object_response.BatchCreateObjectResponse"
    ]
    """<p>Creates an object in a <a>Directory</a>.</p>"""
    attach_object: NotRequired[
        "capo_clouddirectory.types.batch_attach_object_response.BatchAttachObjectResponse"
    ]
    """<p>Attaches an object to a <a>Directory</a>.</p>"""
    detach_object: NotRequired[
        "capo_clouddirectory.types.batch_detach_object_response.BatchDetachObjectResponse"
    ]
    """<p>Detaches an object from a <a>Directory</a>.</p>"""
    update_object_attributes: NotRequired[
        "capo_clouddirectory.types.batch_update_object_attributes_response.BatchUpdateObjectAttributesResponse"
    ]
    """<p>Updates a given object’s attributes.</p>"""
    delete_object: NotRequired[
        "capo_clouddirectory.types.batch_delete_object_response.BatchDeleteObjectResponse"
    ]
    """<p>Deletes an object in a <a>Directory</a>.</p>"""
    add_facet_to_object: NotRequired[
        "capo_clouddirectory.types.batch_add_facet_to_object_response.BatchAddFacetToObjectResponse"
    ]
    """<p>The result of an add facet to object batch operation.</p>"""
    remove_facet_from_object: NotRequired[
        "capo_clouddirectory.types.batch_remove_facet_from_object_response.BatchRemoveFacetFromObjectResponse"
    ]
    """<p>The result of a batch remove facet from object operation.</p>"""
    attach_policy: NotRequired[
        "capo_clouddirectory.types.batch_attach_policy_response.BatchAttachPolicyResponse"
    ]
    """<p>Attaches a policy object to a regular object. An object can have a limited number of attached policies.</p>"""
    detach_policy: NotRequired[
        "capo_clouddirectory.types.batch_detach_policy_response.BatchDetachPolicyResponse"
    ]
    """<p>Detaches a policy from a <a>Directory</a>.</p>"""
    create_index: NotRequired[
        "capo_clouddirectory.types.batch_create_index_response.BatchCreateIndexResponse"
    ]
    """<p>Creates an index object. See <a href="https://docs.aws.amazon.com/clouddirectory/latest/developerguide/indexing_search.htm">Indexing and search</a> for more information.</p>"""
    attach_to_index: NotRequired[
        "capo_clouddirectory.types.batch_attach_to_index_response.BatchAttachToIndexResponse"
    ]
    """<p>Attaches the specified object to the specified index.</p>"""
    detach_from_index: NotRequired[
        "capo_clouddirectory.types.batch_detach_from_index_response.BatchDetachFromIndexResponse"
    ]
    """<p>Detaches the specified object from the specified index.</p>"""
    attach_typed_link: NotRequired[
        "capo_clouddirectory.types.batch_attach_typed_link_response.BatchAttachTypedLinkResponse"
    ]
    """<p>Attaches a typed link to a specified source and target object. For more information, see <a href="https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink">Typed Links</a>.</p>"""
    detach_typed_link: NotRequired[
        "capo_clouddirectory.types.batch_detach_typed_link_response.BatchDetachTypedLinkResponse"
    ]
    """<p>Detaches a typed link from a specified source and target object. For more information, see <a href="https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink">Typed Links</a>.</p>"""
    update_link_attributes: NotRequired[
        "capo_clouddirectory.types.batch_update_link_attributes_response.BatchUpdateLinkAttributesResponse"
    ]
    """<p>Represents the output of a <code>BatchWrite</code> response operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchWriteOperationResponse) -> dict:
    out: dict = {}
    if "create_object" in value:
        import capo_clouddirectory.types.batch_create_object_response

        out["CreateObject"] = (
            capo_clouddirectory.types.batch_create_object_response.serialize_json(
                value["create_object"]
            )
        )
    if "attach_object" in value:
        import capo_clouddirectory.types.batch_attach_object_response

        out["AttachObject"] = (
            capo_clouddirectory.types.batch_attach_object_response.serialize_json(
                value["attach_object"]
            )
        )
    if "detach_object" in value:
        import capo_clouddirectory.types.batch_detach_object_response

        out["DetachObject"] = (
            capo_clouddirectory.types.batch_detach_object_response.serialize_json(
                value["detach_object"]
            )
        )
    if "update_object_attributes" in value:
        import capo_clouddirectory.types.batch_update_object_attributes_response

        out["UpdateObjectAttributes"] = (
            capo_clouddirectory.types.batch_update_object_attributes_response.serialize_json(
                value["update_object_attributes"]
            )
        )
    if "delete_object" in value:
        import capo_clouddirectory.types.batch_delete_object_response

        out["DeleteObject"] = (
            capo_clouddirectory.types.batch_delete_object_response.serialize_json(
                value["delete_object"]
            )
        )
    if "add_facet_to_object" in value:
        import capo_clouddirectory.types.batch_add_facet_to_object_response

        out["AddFacetToObject"] = (
            capo_clouddirectory.types.batch_add_facet_to_object_response.serialize_json(
                value["add_facet_to_object"]
            )
        )
    if "remove_facet_from_object" in value:
        import capo_clouddirectory.types.batch_remove_facet_from_object_response

        out["RemoveFacetFromObject"] = (
            capo_clouddirectory.types.batch_remove_facet_from_object_response.serialize_json(
                value["remove_facet_from_object"]
            )
        )
    if "attach_policy" in value:
        import capo_clouddirectory.types.batch_attach_policy_response

        out["AttachPolicy"] = (
            capo_clouddirectory.types.batch_attach_policy_response.serialize_json(
                value["attach_policy"]
            )
        )
    if "detach_policy" in value:
        import capo_clouddirectory.types.batch_detach_policy_response

        out["DetachPolicy"] = (
            capo_clouddirectory.types.batch_detach_policy_response.serialize_json(
                value["detach_policy"]
            )
        )
    if "create_index" in value:
        import capo_clouddirectory.types.batch_create_index_response

        out["CreateIndex"] = (
            capo_clouddirectory.types.batch_create_index_response.serialize_json(
                value["create_index"]
            )
        )
    if "attach_to_index" in value:
        import capo_clouddirectory.types.batch_attach_to_index_response

        out["AttachToIndex"] = (
            capo_clouddirectory.types.batch_attach_to_index_response.serialize_json(
                value["attach_to_index"]
            )
        )
    if "detach_from_index" in value:
        import capo_clouddirectory.types.batch_detach_from_index_response

        out["DetachFromIndex"] = (
            capo_clouddirectory.types.batch_detach_from_index_response.serialize_json(
                value["detach_from_index"]
            )
        )
    if "attach_typed_link" in value:
        import capo_clouddirectory.types.batch_attach_typed_link_response

        out["AttachTypedLink"] = (
            capo_clouddirectory.types.batch_attach_typed_link_response.serialize_json(
                value["attach_typed_link"]
            )
        )
    if "detach_typed_link" in value:
        import capo_clouddirectory.types.batch_detach_typed_link_response

        out["DetachTypedLink"] = (
            capo_clouddirectory.types.batch_detach_typed_link_response.serialize_json(
                value["detach_typed_link"]
            )
        )
    if "update_link_attributes" in value:
        import capo_clouddirectory.types.batch_update_link_attributes_response

        out["UpdateLinkAttributes"] = (
            capo_clouddirectory.types.batch_update_link_attributes_response.serialize_json(
                value["update_link_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchWriteOperationResponse:
    out: BatchWriteOperationResponse = {}  # type: ignore[typeddict-item]
    if data.get("CreateObject") is not None:
        import capo_clouddirectory.types.batch_create_object_response

        out["create_object"] = (
            capo_clouddirectory.types.batch_create_object_response.deserialize_json(
                data["CreateObject"]
            )
        )
    if data.get("AttachObject") is not None:
        import capo_clouddirectory.types.batch_attach_object_response

        out["attach_object"] = (
            capo_clouddirectory.types.batch_attach_object_response.deserialize_json(
                data["AttachObject"]
            )
        )
    if data.get("DetachObject") is not None:
        import capo_clouddirectory.types.batch_detach_object_response

        out["detach_object"] = (
            capo_clouddirectory.types.batch_detach_object_response.deserialize_json(
                data["DetachObject"]
            )
        )
    if data.get("UpdateObjectAttributes") is not None:
        import capo_clouddirectory.types.batch_update_object_attributes_response

        out["update_object_attributes"] = (
            capo_clouddirectory.types.batch_update_object_attributes_response.deserialize_json(
                data["UpdateObjectAttributes"]
            )
        )
    if data.get("DeleteObject") is not None:
        import capo_clouddirectory.types.batch_delete_object_response

        out["delete_object"] = (
            capo_clouddirectory.types.batch_delete_object_response.deserialize_json(
                data["DeleteObject"]
            )
        )
    if data.get("AddFacetToObject") is not None:
        import capo_clouddirectory.types.batch_add_facet_to_object_response

        out["add_facet_to_object"] = (
            capo_clouddirectory.types.batch_add_facet_to_object_response.deserialize_json(
                data["AddFacetToObject"]
            )
        )
    if data.get("RemoveFacetFromObject") is not None:
        import capo_clouddirectory.types.batch_remove_facet_from_object_response

        out["remove_facet_from_object"] = (
            capo_clouddirectory.types.batch_remove_facet_from_object_response.deserialize_json(
                data["RemoveFacetFromObject"]
            )
        )
    if data.get("AttachPolicy") is not None:
        import capo_clouddirectory.types.batch_attach_policy_response

        out["attach_policy"] = (
            capo_clouddirectory.types.batch_attach_policy_response.deserialize_json(
                data["AttachPolicy"]
            )
        )
    if data.get("DetachPolicy") is not None:
        import capo_clouddirectory.types.batch_detach_policy_response

        out["detach_policy"] = (
            capo_clouddirectory.types.batch_detach_policy_response.deserialize_json(
                data["DetachPolicy"]
            )
        )
    if data.get("CreateIndex") is not None:
        import capo_clouddirectory.types.batch_create_index_response

        out["create_index"] = (
            capo_clouddirectory.types.batch_create_index_response.deserialize_json(
                data["CreateIndex"]
            )
        )
    if data.get("AttachToIndex") is not None:
        import capo_clouddirectory.types.batch_attach_to_index_response

        out["attach_to_index"] = (
            capo_clouddirectory.types.batch_attach_to_index_response.deserialize_json(
                data["AttachToIndex"]
            )
        )
    if data.get("DetachFromIndex") is not None:
        import capo_clouddirectory.types.batch_detach_from_index_response

        out["detach_from_index"] = (
            capo_clouddirectory.types.batch_detach_from_index_response.deserialize_json(
                data["DetachFromIndex"]
            )
        )
    if data.get("AttachTypedLink") is not None:
        import capo_clouddirectory.types.batch_attach_typed_link_response

        out["attach_typed_link"] = (
            capo_clouddirectory.types.batch_attach_typed_link_response.deserialize_json(
                data["AttachTypedLink"]
            )
        )
    if data.get("DetachTypedLink") is not None:
        import capo_clouddirectory.types.batch_detach_typed_link_response

        out["detach_typed_link"] = (
            capo_clouddirectory.types.batch_detach_typed_link_response.deserialize_json(
                data["DetachTypedLink"]
            )
        )
    if data.get("UpdateLinkAttributes") is not None:
        import capo_clouddirectory.types.batch_update_link_attributes_response

        out["update_link_attributes"] = (
            capo_clouddirectory.types.batch_update_link_attributes_response.deserialize_json(
                data["UpdateLinkAttributes"]
            )
        )
    return out
