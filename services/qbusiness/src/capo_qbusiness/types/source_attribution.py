"""Generated from Smithy shape ``com.amazonaws.qbusiness#SourceAttribution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.integer
    import capo_qbusiness.types.string
    import capo_qbusiness.types.text_segment_list
    import capo_qbusiness.types.timestamp


class SourceAttribution(TypedDict, closed=True):
    title: NotRequired["capo_qbusiness.types.string.String"]
    """<p>The title of the document which is the source for the Amazon Q Business generated response. </p>"""
    snippet: NotRequired["capo_qbusiness.types.string.String"]
    """<p>The content extract from the document on which the generated response is based. </p>"""
    url: NotRequired["capo_qbusiness.types.string.String"]
    """<p>The URL of the document which is the source for the Amazon Q Business generated response. </p>"""
    citation_number: NotRequired["capo_qbusiness.types.integer.Integer"]
    """<p>The number attached to a citation in an Amazon Q Business generated response.</p>"""
    updated_at: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the Amazon Q Business application was last updated.</p>"""
    text_message_segments: NotRequired[
        "capo_qbusiness.types.text_segment_list.TextSegmentList"
    ]
    """<p>A text extract from a source document that is used for source attribution.</p>"""
    document_id: NotRequired["capo_qbusiness.types.string.String"]
    """<p>The unique identifier of the source document used in the citation, obtained from the Amazon Q Business index during chat response generation. This ID is used as input to the <code>GetDocumentContent</code> API to retrieve the actual document content for user verification.</p>"""
    index_id: NotRequired["capo_qbusiness.types.string.String"]
    """<p>The identifier of the index containing the source document's metadata and access control information. This links the citation back to the specific Amazon Q Business index where the document's searchable content and permissions are stored.</p>"""
    datasource_id: NotRequired["capo_qbusiness.types.string.String"]
    """<p>The identifier of the data source from which the document was ingested. This field is not present if the document is ingested by directly calling the BatchPutDocument API (similar to checkDocumentAccess). If the document is from a file-upload data source, the datasource will be "uploaded-docs-file-stat-datasourceid".</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceAttribution) -> dict:
    out: dict = {}
    if "title" in value:
        out["title"] = value["title"]
    if "snippet" in value:
        out["snippet"] = value["snippet"]
    if "url" in value:
        out["url"] = value["url"]
    if "citation_number" in value:
        out["citationNumber"] = value["citation_number"]
    if "updated_at" in value:
        import capo_qbusiness.types.timestamp

        out["updatedAt"] = capo_qbusiness.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "text_message_segments" in value:
        import capo_qbusiness.types.text_segment_list

        out["textMessageSegments"] = (
            capo_qbusiness.types.text_segment_list.serialize_json(
                value["text_message_segments"]
            )
        )
    if "document_id" in value:
        out["documentId"] = value["document_id"]
    if "index_id" in value:
        out["indexId"] = value["index_id"]
    if "datasource_id" in value:
        out["datasourceId"] = value["datasource_id"]
    return out


def deserialize_json(data: dict) -> SourceAttribution:
    out: SourceAttribution = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("snippet") is not None:
        out["snippet"] = data["snippet"]
    if data.get("url") is not None:
        out["url"] = data["url"]
    if data.get("citationNumber") is not None:
        out["citation_number"] = data["citationNumber"]
    if data.get("updatedAt") is not None:
        import capo_qbusiness.types.timestamp

        out["updated_at"] = capo_qbusiness.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if data.get("textMessageSegments") is not None:
        import capo_qbusiness.types.text_segment_list

        out["text_message_segments"] = (
            capo_qbusiness.types.text_segment_list.deserialize_json(
                data["textMessageSegments"]
            )
        )
    if data.get("documentId") is not None:
        out["document_id"] = data["documentId"]
    if data.get("indexId") is not None:
        out["index_id"] = data["indexId"]
    if data.get("datasourceId") is not None:
        out["datasource_id"] = data["datasourceId"]
    return out
