"""Generated from Smithy shape ``com.amazonaws.kendra#Document``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.access_control_configuration_id
    import capo_kendra.types.blob
    import capo_kendra.types.content_type
    import capo_kendra.types.document_attribute_list
    import capo_kendra.types.document_id
    import capo_kendra.types.hierarchical_principal_list
    import capo_kendra.types.principal_list
    import capo_kendra.types.s3_path
    import capo_kendra.types.title


class Document(TypedDict, closed=True):
    id: "capo_kendra.types.document_id.DocumentId"
    """<p>A identifier of the document in the index.</p> <p>Note, each document ID must be unique per index. You cannot create a data source to index your documents with their unique IDs and then use the <code>BatchPutDocument</code> API to index the same documents, or vice versa. You can delete a data source and then use the <code>BatchPutDocument</code> API to index the same documents, or vice versa.</p>"""
    title: NotRequired["capo_kendra.types.title.Title"]
    """<p>The title of the document.</p>"""
    blob: NotRequired["capo_kendra.types.blob.Blob"]
    """<p>The contents of the document. </p> <p>Documents passed to the <code>Blob</code> parameter must be base64 encoded. Your code might not need to encode the document file bytes if you're using an Amazon Web Services SDK to call Amazon Kendra APIs. If you are calling the Amazon Kendra endpoint directly using REST, you must base64 encode the contents before sending.</p>"""
    s3_path: NotRequired["capo_kendra.types.s3_path.S3Path"]
    attributes: NotRequired[
        "capo_kendra.types.document_attribute_list.DocumentAttributeList"
    ]
    """<p>Custom attributes to apply to the document. Use the custom attributes to provide additional information for searching, to provide facets for refining searches, and to provide additional information in the query response.</p> <p>For example, 'DataSourceId' and 'DataSourceSyncJobId' are custom attributes that provide information on the synchronization of documents running on a data source. Note, 'DataSourceSyncJobId' could be an optional custom attribute as Amazon Kendra will use the ID of a running sync job.</p>"""
    access_control_list: NotRequired["capo_kendra.types.principal_list.PrincipalList"]
    """<p>Information on principals (users and/or groups) and which documents they should have access to. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.</p>"""
    hierarchical_access_control_list: NotRequired[
        "capo_kendra.types.hierarchical_principal_list.HierarchicalPrincipalList"
    ]
    """<p>The list of <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_Principal.html">principal</a> lists that define the hierarchy for which documents users should have access to.</p>"""
    content_type: NotRequired["capo_kendra.types.content_type.ContentType"]
    """<p>The file type of the document in the <code>Blob</code> field.</p> <p>If you want to index snippets or subsets of HTML documents instead of the entirety of the HTML documents, you must add the <code>HTML</code> start and closing tags (<code><HTML>content</HTML></code>) around the content.</p>"""
    access_control_configuration_id: NotRequired[
        "capo_kendra.types.access_control_configuration_id.AccessControlConfigurationId"
    ]
    """<p>The identifier of the access control configuration that you want to apply to the document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Document) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "title" in value:
        out["Title"] = value["title"]
    if "blob" in value:
        import capo_kendra.types.blob

        out["Blob"] = capo_kendra.types.blob.serialize_aws_json_1_1(value["blob"])
    if "s3_path" in value:
        import capo_kendra.types.s3_path

        out["S3Path"] = capo_kendra.types.s3_path.serialize_aws_json_1_1(
            value["s3_path"]
        )
    if "attributes" in value:
        import capo_kendra.types.document_attribute_list

        out["Attributes"] = (
            capo_kendra.types.document_attribute_list.serialize_aws_json_1_1(
                value["attributes"]
            )
        )
    if "access_control_list" in value:
        import capo_kendra.types.principal_list

        out["AccessControlList"] = (
            capo_kendra.types.principal_list.serialize_aws_json_1_1(
                value["access_control_list"]
            )
        )
    if "hierarchical_access_control_list" in value:
        import capo_kendra.types.hierarchical_principal_list

        out["HierarchicalAccessControlList"] = (
            capo_kendra.types.hierarchical_principal_list.serialize_aws_json_1_1(
                value["hierarchical_access_control_list"]
            )
        )
    if "content_type" in value:
        import capo_kendra.types.content_type

        out["ContentType"] = capo_kendra.types.content_type.serialize_aws_json_1_1(
            value["content_type"]
        )
    if "access_control_configuration_id" in value:
        out["AccessControlConfigurationId"] = value["access_control_configuration_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Document:
    out: Document = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("Document.id required")
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("Blob") is not None:
        import capo_kendra.types.blob

        out["blob"] = capo_kendra.types.blob.deserialize_aws_json_1_1(data["Blob"])
    if data.get("S3Path") is not None:
        import capo_kendra.types.s3_path

        out["s3_path"] = capo_kendra.types.s3_path.deserialize_aws_json_1_1(
            data["S3Path"]
        )
    if data.get("Attributes") is not None:
        import capo_kendra.types.document_attribute_list

        out["attributes"] = (
            capo_kendra.types.document_attribute_list.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    if data.get("AccessControlList") is not None:
        import capo_kendra.types.principal_list

        out["access_control_list"] = (
            capo_kendra.types.principal_list.deserialize_aws_json_1_1(
                data["AccessControlList"]
            )
        )
    if data.get("HierarchicalAccessControlList") is not None:
        import capo_kendra.types.hierarchical_principal_list

        out["hierarchical_access_control_list"] = (
            capo_kendra.types.hierarchical_principal_list.deserialize_aws_json_1_1(
                data["HierarchicalAccessControlList"]
            )
        )
    if data.get("ContentType") is not None:
        import capo_kendra.types.content_type

        out["content_type"] = capo_kendra.types.content_type.deserialize_aws_json_1_1(
            data["ContentType"]
        )
    if data.get("AccessControlConfigurationId") is not None:
        out["access_control_configuration_id"] = data["AccessControlConfigurationId"]
    return out
