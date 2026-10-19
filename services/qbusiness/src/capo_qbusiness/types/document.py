"""Generated from Smithy shape ``com.amazonaws.qbusiness#Document``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.access_configuration
    import capo_qbusiness.types.content_type
    import capo_qbusiness.types.document_attributes
    import capo_qbusiness.types.document_content
    import capo_qbusiness.types.document_enrichment_configuration
    import capo_qbusiness.types.document_id
    import capo_qbusiness.types.media_extraction_configuration
    import capo_qbusiness.types.title


class Document(TypedDict, closed=True):
    id: "capo_qbusiness.types.document_id.DocumentId"
    """<p>The identifier of the document.</p>"""
    attributes: NotRequired[
        "capo_qbusiness.types.document_attributes.DocumentAttributes"
    ]
    """<p>Custom attributes to apply to the document for refining Amazon Q Business web experience responses.</p>"""
    content: NotRequired["capo_qbusiness.types.document_content.DocumentContent"]
    """<p>The contents of the document.</p>"""
    content_type: NotRequired["capo_qbusiness.types.content_type.ContentType"]
    """<p>The file type of the document in the Blob field.</p> <p>If you want to index snippets or subsets of HTML documents instead of the entirety of the HTML documents, you add the <code>HTML</code> start and closing tags (<code>&lt;HTML&gt;content&lt;/HTML&gt;</code>) around the content.</p>"""
    title: NotRequired["capo_qbusiness.types.title.Title"]
    """<p>The title of the document.</p>"""
    access_configuration: NotRequired[
        "capo_qbusiness.types.access_configuration.AccessConfiguration"
    ]
    """<p>Configuration information for access permission to a document.</p>"""
    document_enrichment_configuration: NotRequired[
        "capo_qbusiness.types.document_enrichment_configuration.DocumentEnrichmentConfiguration"
    ]
    """<p>The configuration information for altering document metadata and content during the document ingestion process.</p>"""
    media_extraction_configuration: NotRequired[
        "capo_qbusiness.types.media_extraction_configuration.MediaExtractionConfiguration"
    ]
    """<p>The configuration for extracting information from media in the document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Document) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "attributes" in value:
        import capo_qbusiness.types.document_attributes

        out["attributes"] = capo_qbusiness.types.document_attributes.serialize_json(
            value["attributes"]
        )
    if "content" in value:
        import capo_qbusiness.types.document_content

        out["content"] = capo_qbusiness.types.document_content.serialize_json(
            value["content"]
        )
    if "content_type" in value:
        import capo_qbusiness.types.content_type

        out["contentType"] = capo_qbusiness.types.content_type.serialize_json(
            value["content_type"]
        )
    if "title" in value:
        out["title"] = value["title"]
    if "access_configuration" in value:
        import capo_qbusiness.types.access_configuration

        out["accessConfiguration"] = (
            capo_qbusiness.types.access_configuration.serialize_json(
                value["access_configuration"]
            )
        )
    if "document_enrichment_configuration" in value:
        import capo_qbusiness.types.document_enrichment_configuration

        out["documentEnrichmentConfiguration"] = (
            capo_qbusiness.types.document_enrichment_configuration.serialize_json(
                value["document_enrichment_configuration"]
            )
        )
    if "media_extraction_configuration" in value:
        import capo_qbusiness.types.media_extraction_configuration

        out["mediaExtractionConfiguration"] = (
            capo_qbusiness.types.media_extraction_configuration.serialize_json(
                value["media_extraction_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> Document:
    out: Document = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("attributes") is not None:
        import capo_qbusiness.types.document_attributes

        out["attributes"] = capo_qbusiness.types.document_attributes.deserialize_json(
            data["attributes"]
        )
    if data.get("content") is not None:
        import capo_qbusiness.types.document_content

        out["content"] = capo_qbusiness.types.document_content.deserialize_json(
            data["content"]
        )
    if data.get("contentType") is not None:
        import capo_qbusiness.types.content_type

        out["content_type"] = capo_qbusiness.types.content_type.deserialize_json(
            data["contentType"]
        )
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("accessConfiguration") is not None:
        import capo_qbusiness.types.access_configuration

        out["access_configuration"] = (
            capo_qbusiness.types.access_configuration.deserialize_json(
                data["accessConfiguration"]
            )
        )
    if data.get("documentEnrichmentConfiguration") is not None:
        import capo_qbusiness.types.document_enrichment_configuration

        out["document_enrichment_configuration"] = (
            capo_qbusiness.types.document_enrichment_configuration.deserialize_json(
                data["documentEnrichmentConfiguration"]
            )
        )
    if data.get("mediaExtractionConfiguration") is not None:
        import capo_qbusiness.types.media_extraction_configuration

        out["media_extraction_configuration"] = (
            capo_qbusiness.types.media_extraction_configuration.deserialize_json(
                data["mediaExtractionConfiguration"]
            )
        )
    return out
