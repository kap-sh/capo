"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchReadSuccessfulResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.batch_get_link_attributes_response
    import capo_clouddirectory.types.batch_get_object_attributes_response
    import capo_clouddirectory.types.batch_get_object_information_response
    import capo_clouddirectory.types.batch_list_attached_indices_response
    import capo_clouddirectory.types.batch_list_incoming_typed_links_response
    import capo_clouddirectory.types.batch_list_index_response
    import capo_clouddirectory.types.batch_list_object_attributes_response
    import capo_clouddirectory.types.batch_list_object_children_response
    import capo_clouddirectory.types.batch_list_object_parent_paths_response
    import capo_clouddirectory.types.batch_list_object_parents_response
    import capo_clouddirectory.types.batch_list_object_policies_response
    import capo_clouddirectory.types.batch_list_outgoing_typed_links_response
    import capo_clouddirectory.types.batch_list_policy_attachments_response
    import capo_clouddirectory.types.batch_lookup_policy_response


class BatchReadSuccessfulResponse(TypedDict, closed=True):
    list_object_attributes: NotRequired[
        "capo_clouddirectory.types.batch_list_object_attributes_response.BatchListObjectAttributesResponse"
    ]
    """<p>Lists all attributes that are associated with an object.</p>"""
    list_object_children: NotRequired[
        "capo_clouddirectory.types.batch_list_object_children_response.BatchListObjectChildrenResponse"
    ]
    """<p>Returns a paginated list of child objects that are associated with a given object.</p>"""
    get_object_information: NotRequired[
        "capo_clouddirectory.types.batch_get_object_information_response.BatchGetObjectInformationResponse"
    ]
    """<p>Retrieves metadata about an object.</p>"""
    get_object_attributes: NotRequired[
        "capo_clouddirectory.types.batch_get_object_attributes_response.BatchGetObjectAttributesResponse"
    ]
    """<p>Retrieves attributes within a facet that are associated with an object.</p>"""
    list_attached_indices: NotRequired[
        "capo_clouddirectory.types.batch_list_attached_indices_response.BatchListAttachedIndicesResponse"
    ]
    """<p>Lists indices attached to an object.</p>"""
    list_object_parent_paths: NotRequired[
        "capo_clouddirectory.types.batch_list_object_parent_paths_response.BatchListObjectParentPathsResponse"
    ]
    """<p>Retrieves all available parent paths for any object type such as node, leaf node, policy node, and index node objects. For more information about objects, see <a href="https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directorystructure.html">Directory Structure</a>.</p>"""
    list_object_policies: NotRequired[
        "capo_clouddirectory.types.batch_list_object_policies_response.BatchListObjectPoliciesResponse"
    ]
    """<p>Returns policies attached to an object in pagination fashion.</p>"""
    list_policy_attachments: NotRequired[
        "capo_clouddirectory.types.batch_list_policy_attachments_response.BatchListPolicyAttachmentsResponse"
    ]
    """<p>Returns all of the <code>ObjectIdentifiers</code> to which a given policy is attached.</p>"""
    lookup_policy: NotRequired[
        "capo_clouddirectory.types.batch_lookup_policy_response.BatchLookupPolicyResponse"
    ]
    """<p>Lists all policies from the root of the <a>Directory</a> to the object specified. If there are no policies present, an empty list is returned. If policies are present, and if some objects don't have the policies attached, it returns the <code>ObjectIdentifier</code> for such objects. If policies are present, it returns <code>ObjectIdentifier</code>, <code>policyId</code>, and <code>policyType</code>. Paths that don't lead to the root from the target object are ignored. For more information, see <a href="https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies">Policies</a>.</p>"""
    list_index: NotRequired[
        "capo_clouddirectory.types.batch_list_index_response.BatchListIndexResponse"
    ]
    """<p>Lists objects attached to the specified index.</p>"""
    list_outgoing_typed_links: NotRequired[
        "capo_clouddirectory.types.batch_list_outgoing_typed_links_response.BatchListOutgoingTypedLinksResponse"
    ]
    """<p>Returns a paginated list of all the outgoing <a>TypedLinkSpecifier</a> information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see <a href="https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink">Typed Links</a>.</p>"""
    list_incoming_typed_links: NotRequired[
        "capo_clouddirectory.types.batch_list_incoming_typed_links_response.BatchListIncomingTypedLinksResponse"
    ]
    """<p>Returns a paginated list of all the incoming <a>TypedLinkSpecifier</a> information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see <a href="https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink">Typed Links</a>.</p>"""
    get_link_attributes: NotRequired[
        "capo_clouddirectory.types.batch_get_link_attributes_response.BatchGetLinkAttributesResponse"
    ]
    """<p>The list of attributes to retrieve from the typed link.</p>"""
    list_object_parents: NotRequired[
        "capo_clouddirectory.types.batch_list_object_parents_response.BatchListObjectParentsResponse"
    ]
    """<p>The list of parent objects to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchReadSuccessfulResponse) -> dict:
    out: dict = {}
    if "list_object_attributes" in value:
        import capo_clouddirectory.types.batch_list_object_attributes_response

        out["ListObjectAttributes"] = (
            capo_clouddirectory.types.batch_list_object_attributes_response.serialize_json(
                value["list_object_attributes"]
            )
        )
    if "list_object_children" in value:
        import capo_clouddirectory.types.batch_list_object_children_response

        out["ListObjectChildren"] = (
            capo_clouddirectory.types.batch_list_object_children_response.serialize_json(
                value["list_object_children"]
            )
        )
    if "get_object_information" in value:
        import capo_clouddirectory.types.batch_get_object_information_response

        out["GetObjectInformation"] = (
            capo_clouddirectory.types.batch_get_object_information_response.serialize_json(
                value["get_object_information"]
            )
        )
    if "get_object_attributes" in value:
        import capo_clouddirectory.types.batch_get_object_attributes_response

        out["GetObjectAttributes"] = (
            capo_clouddirectory.types.batch_get_object_attributes_response.serialize_json(
                value["get_object_attributes"]
            )
        )
    if "list_attached_indices" in value:
        import capo_clouddirectory.types.batch_list_attached_indices_response

        out["ListAttachedIndices"] = (
            capo_clouddirectory.types.batch_list_attached_indices_response.serialize_json(
                value["list_attached_indices"]
            )
        )
    if "list_object_parent_paths" in value:
        import capo_clouddirectory.types.batch_list_object_parent_paths_response

        out["ListObjectParentPaths"] = (
            capo_clouddirectory.types.batch_list_object_parent_paths_response.serialize_json(
                value["list_object_parent_paths"]
            )
        )
    if "list_object_policies" in value:
        import capo_clouddirectory.types.batch_list_object_policies_response

        out["ListObjectPolicies"] = (
            capo_clouddirectory.types.batch_list_object_policies_response.serialize_json(
                value["list_object_policies"]
            )
        )
    if "list_policy_attachments" in value:
        import capo_clouddirectory.types.batch_list_policy_attachments_response

        out["ListPolicyAttachments"] = (
            capo_clouddirectory.types.batch_list_policy_attachments_response.serialize_json(
                value["list_policy_attachments"]
            )
        )
    if "lookup_policy" in value:
        import capo_clouddirectory.types.batch_lookup_policy_response

        out["LookupPolicy"] = (
            capo_clouddirectory.types.batch_lookup_policy_response.serialize_json(
                value["lookup_policy"]
            )
        )
    if "list_index" in value:
        import capo_clouddirectory.types.batch_list_index_response

        out["ListIndex"] = (
            capo_clouddirectory.types.batch_list_index_response.serialize_json(
                value["list_index"]
            )
        )
    if "list_outgoing_typed_links" in value:
        import capo_clouddirectory.types.batch_list_outgoing_typed_links_response

        out["ListOutgoingTypedLinks"] = (
            capo_clouddirectory.types.batch_list_outgoing_typed_links_response.serialize_json(
                value["list_outgoing_typed_links"]
            )
        )
    if "list_incoming_typed_links" in value:
        import capo_clouddirectory.types.batch_list_incoming_typed_links_response

        out["ListIncomingTypedLinks"] = (
            capo_clouddirectory.types.batch_list_incoming_typed_links_response.serialize_json(
                value["list_incoming_typed_links"]
            )
        )
    if "get_link_attributes" in value:
        import capo_clouddirectory.types.batch_get_link_attributes_response

        out["GetLinkAttributes"] = (
            capo_clouddirectory.types.batch_get_link_attributes_response.serialize_json(
                value["get_link_attributes"]
            )
        )
    if "list_object_parents" in value:
        import capo_clouddirectory.types.batch_list_object_parents_response

        out["ListObjectParents"] = (
            capo_clouddirectory.types.batch_list_object_parents_response.serialize_json(
                value["list_object_parents"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchReadSuccessfulResponse:
    out: BatchReadSuccessfulResponse = {}  # type: ignore[typeddict-item]
    if data.get("ListObjectAttributes") is not None:
        import capo_clouddirectory.types.batch_list_object_attributes_response

        out["list_object_attributes"] = (
            capo_clouddirectory.types.batch_list_object_attributes_response.deserialize_json(
                data["ListObjectAttributes"]
            )
        )
    if data.get("ListObjectChildren") is not None:
        import capo_clouddirectory.types.batch_list_object_children_response

        out["list_object_children"] = (
            capo_clouddirectory.types.batch_list_object_children_response.deserialize_json(
                data["ListObjectChildren"]
            )
        )
    if data.get("GetObjectInformation") is not None:
        import capo_clouddirectory.types.batch_get_object_information_response

        out["get_object_information"] = (
            capo_clouddirectory.types.batch_get_object_information_response.deserialize_json(
                data["GetObjectInformation"]
            )
        )
    if data.get("GetObjectAttributes") is not None:
        import capo_clouddirectory.types.batch_get_object_attributes_response

        out["get_object_attributes"] = (
            capo_clouddirectory.types.batch_get_object_attributes_response.deserialize_json(
                data["GetObjectAttributes"]
            )
        )
    if data.get("ListAttachedIndices") is not None:
        import capo_clouddirectory.types.batch_list_attached_indices_response

        out["list_attached_indices"] = (
            capo_clouddirectory.types.batch_list_attached_indices_response.deserialize_json(
                data["ListAttachedIndices"]
            )
        )
    if data.get("ListObjectParentPaths") is not None:
        import capo_clouddirectory.types.batch_list_object_parent_paths_response

        out["list_object_parent_paths"] = (
            capo_clouddirectory.types.batch_list_object_parent_paths_response.deserialize_json(
                data["ListObjectParentPaths"]
            )
        )
    if data.get("ListObjectPolicies") is not None:
        import capo_clouddirectory.types.batch_list_object_policies_response

        out["list_object_policies"] = (
            capo_clouddirectory.types.batch_list_object_policies_response.deserialize_json(
                data["ListObjectPolicies"]
            )
        )
    if data.get("ListPolicyAttachments") is not None:
        import capo_clouddirectory.types.batch_list_policy_attachments_response

        out["list_policy_attachments"] = (
            capo_clouddirectory.types.batch_list_policy_attachments_response.deserialize_json(
                data["ListPolicyAttachments"]
            )
        )
    if data.get("LookupPolicy") is not None:
        import capo_clouddirectory.types.batch_lookup_policy_response

        out["lookup_policy"] = (
            capo_clouddirectory.types.batch_lookup_policy_response.deserialize_json(
                data["LookupPolicy"]
            )
        )
    if data.get("ListIndex") is not None:
        import capo_clouddirectory.types.batch_list_index_response

        out["list_index"] = (
            capo_clouddirectory.types.batch_list_index_response.deserialize_json(
                data["ListIndex"]
            )
        )
    if data.get("ListOutgoingTypedLinks") is not None:
        import capo_clouddirectory.types.batch_list_outgoing_typed_links_response

        out["list_outgoing_typed_links"] = (
            capo_clouddirectory.types.batch_list_outgoing_typed_links_response.deserialize_json(
                data["ListOutgoingTypedLinks"]
            )
        )
    if data.get("ListIncomingTypedLinks") is not None:
        import capo_clouddirectory.types.batch_list_incoming_typed_links_response

        out["list_incoming_typed_links"] = (
            capo_clouddirectory.types.batch_list_incoming_typed_links_response.deserialize_json(
                data["ListIncomingTypedLinks"]
            )
        )
    if data.get("GetLinkAttributes") is not None:
        import capo_clouddirectory.types.batch_get_link_attributes_response

        out["get_link_attributes"] = (
            capo_clouddirectory.types.batch_get_link_attributes_response.deserialize_json(
                data["GetLinkAttributes"]
            )
        )
    if data.get("ListObjectParents") is not None:
        import capo_clouddirectory.types.batch_list_object_parents_response

        out["list_object_parents"] = (
            capo_clouddirectory.types.batch_list_object_parents_response.deserialize_json(
                data["ListObjectParents"]
            )
        )
    return out
