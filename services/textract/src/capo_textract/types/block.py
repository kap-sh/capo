"""Generated from Smithy shape ``com.amazonaws.textract#Block``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.block_type
    import capo_textract.types.entity_types
    import capo_textract.types.geometry
    import capo_textract.types.non_empty_string
    import capo_textract.types.percent
    import capo_textract.types.query
    import capo_textract.types.relationship_list
    import capo_textract.types.selection_status
    import capo_textract.types.string
    import capo_textract.types.text_type
    import capo_textract.types.u_integer


class Block(TypedDict, closed=True):
    block_type: NotRequired["capo_textract.types.block_type.BlockType"]
    """<p>The type of text item that's recognized. In operations for text detection, the following types are returned:</p> <ul> <li> <p> <i>PAGE</i> - Contains a list of the LINE <code>Block</code> objects that are detected on a document page.</p> </li> <li> <p> <i>WORD</i> - A word detected on a document page. A word is one or more ISO basic Latin script characters that aren't separated by spaces.</p> </li> <li> <p> <i>LINE</i> - A string of space-delimited, contiguous words that are detected on a document page.</p> </li> </ul> <p>In text analysis operations, the following types are returned:</p> <ul> <li> <p> <i>PAGE</i> - Contains a list of child <code>Block</code> objects that are detected on a document page.</p> </li> <li> <p> <i>KEY_VALUE_SET</i> - Stores the KEY and VALUE <code>Block</code> objects for linked text that's detected on a document page. Use the <code>EntityType</code> field to determine if a KEY_VALUE_SET object is a KEY <code>Block</code> object or a VALUE <code>Block</code> object. </p> </li> <li> <p> <i>WORD</i> - A word that's detected on a document page. A word is one or more ISO basic Latin script characters that aren't separated by spaces.</p> </li> <li> <p> <i>LINE</i> - A string of tab-delimited, contiguous words that are detected on a document page.</p> </li> <li> <p> <i>TABLE</i> - A table that's detected on a document page. A table is grid-based information with two or more rows or columns, with a cell span of one row and one column each. </p> </li> <li> <p> <i>TABLE_TITLE</i> - The title of a table. A title is typically a line of text above or below a table, or embedded as the first row of a table. </p> </li> <li> <p> <i>TABLE_FOOTER</i> - The footer associated with a table. A footer is typically a line or lines of text below a table or embedded as the last row of a table. </p> </li> <li> <p> <i>CELL</i> - A cell within a detected table. The cell is the parent of the block that contains the text in the cell.</p> </li> <li> <p> <i>MERGED_CELL</i> - A cell in a table whose content spans more than one row or column. The <code>Relationships</code> array for this cell contain data from individual cells.</p> </li> <li> <p> <i>SELECTION_ELEMENT</i> - A selection element such as an option button (radio button) or a check box that's detected on a document page. Use the value of <code>SelectionStatus</code> to determine the status of the selection element.</p> </li> <li> <p> <i>SIGNATURE</i> - The location and confidence score of a signature detected on a document page. Can be returned as part of a Key-Value pair or a detected cell.</p> </li> <li> <p> <i>QUERY</i> - A question asked during the call of AnalyzeDocument. Contains an alias and an ID that attaches it to its answer.</p> </li> <li> <p> <i>QUERY_RESULT</i> - A response to a question asked during the call of analyze document. Comes with an alias and ID for ease of locating in a response. Also contains location and confidence score.</p> </li> </ul> <p>The following BlockTypes are only returned for Amazon Textract Layout.</p> <ul> <li> <p> <code>LAYOUT_TITLE</code> - The main title of the document.</p> </li> <li> <p> <code>LAYOUT_HEADER</code> - Text located in the top margin of the document.</p> </li> <li> <p> <code>LAYOUT_FOOTER</code> - Text located in the bottom margin of the document.</p> </li> <li> <p> <code>LAYOUT_SECTION_HEADER</code> - The titles of sections within a document.</p> </li> <li> <p> <code>LAYOUT_PAGE_NUMBER</code> - The page number of the documents.</p> </li> <li> <p> <code>LAYOUT_LIST</code> - Any information grouped together in list form. </p> </li> <li> <p> <code>LAYOUT_FIGURE</code> - Indicates the location of an image in a document.</p> </li> <li> <p> <code>LAYOUT_TABLE</code> - Indicates the location of a table in the document.</p> </li> <li> <p> <code>LAYOUT_KEY_VALUE</code> - Indicates the location of form key-values in a document.</p> </li> <li> <p> <code>LAYOUT_TEXT</code> - Text that is present typically as a part of paragraphs in documents.</p> </li> </ul>"""
    confidence: NotRequired["capo_textract.types.percent.Percent"]
    """<p>The confidence score that Amazon Textract has in the accuracy of the recognized text and the accuracy of the geometry points around the recognized text.</p>"""
    text: NotRequired["capo_textract.types.string.String"]
    """<p>The word or line of text that's recognized by Amazon Textract. </p>"""
    text_type: NotRequired["capo_textract.types.text_type.TextType"]
    """<p>The kind of text that Amazon Textract has detected. Can check for handwritten text and printed text.</p>"""
    row_index: NotRequired["capo_textract.types.u_integer.UInteger"]
    """<p>The row in which a table cell is located. The first row position is 1. <code>RowIndex</code> isn't returned by <code>DetectDocumentText</code> and <code>GetDocumentTextDetection</code>.</p>"""
    column_index: NotRequired["capo_textract.types.u_integer.UInteger"]
    """<p>The column in which a table cell appears. The first column position is 1. <code>ColumnIndex</code> isn't returned by <code>DetectDocumentText</code> and <code>GetDocumentTextDetection</code>.</p>"""
    row_span: NotRequired["capo_textract.types.u_integer.UInteger"]
    """<p>The number of rows that a table cell spans. <code>RowSpan</code> isn't returned by <code>DetectDocumentText</code> and <code>GetDocumentTextDetection</code>.</p>"""
    column_span: NotRequired["capo_textract.types.u_integer.UInteger"]
    """<p>The number of columns that a table cell spans. <code>ColumnSpan</code> isn't returned by <code>DetectDocumentText</code> and <code>GetDocumentTextDetection</code>. </p>"""
    geometry: NotRequired["capo_textract.types.geometry.Geometry"]
    """<p>The location of the recognized text on the image. It includes an axis-aligned, coarse bounding box that surrounds the text, and a finer-grain polygon for more accurate spatial information. </p>"""
    id: NotRequired["capo_textract.types.non_empty_string.NonEmptyString"]
    """<p>The identifier for the recognized text. The identifier is only unique for a single operation. </p>"""
    relationships: NotRequired["capo_textract.types.relationship_list.RelationshipList"]
    """<p>A list of relationship objects that describe how blocks are related to each other. For example, a LINE block object contains a CHILD relationship type with the WORD blocks that make up the line of text. There aren't Relationship objects in the list for relationships that don't exist, such as when the current block has no child blocks.</p>"""
    entity_types: NotRequired["capo_textract.types.entity_types.EntityTypes"]
    """<p>The type of entity. </p> <p>The following entity types can be returned by FORMS analysis:</p> <ul> <li> <p> <i>KEY</i> - An identifier for a field on the document.</p> </li> <li> <p> <i>VALUE</i> - The field text.</p> </li> </ul> <p>The following entity types can be returned by TABLES analysis:</p> <ul> <li> <p> <i>COLUMN_HEADER</i> - Identifies a cell that is a header of a column. </p> </li> <li> <p> <i>TABLE_TITLE</i> - Identifies a cell that is a title within the table. </p> </li> <li> <p> <i>TABLE_SECTION_TITLE</i> - Identifies a cell that is a title of a section within a table. A section title is a cell that typically spans an entire row above a section. </p> </li> <li> <p> <i>TABLE_FOOTER</i> - Identifies a cell that is a footer of a table. </p> </li> <li> <p> <i>TABLE_SUMMARY</i> - Identifies a summary cell of a table. A summary cell can be a row of a table or an additional, smaller table that contains summary information for another table. </p> </li> <li> <p> <i>STRUCTURED_TABLE </i> - Identifies a table with column headers where the content of each row corresponds to the headers. </p> </li> <li> <p> <i>SEMI_STRUCTURED_TABLE</i> - Identifies a non-structured table. </p> </li> </ul> <p> <code>EntityTypes</code> isn't returned by <code>DetectDocumentText</code> and <code>GetDocumentTextDetection</code>.</p>"""
    selection_status: NotRequired[
        "capo_textract.types.selection_status.SelectionStatus"
    ]
    """<p>The selection status of a selection element, such as an option button or check box. </p>"""
    page: NotRequired["capo_textract.types.u_integer.UInteger"]
    """<p>The page on which a block was detected. <code>Page</code> is returned by synchronous and asynchronous operations. Page values greater than 1 are only returned for multipage documents that are in PDF or TIFF format. A scanned image (JPEG/PNG) provided to an asynchronous operation, even if it contains multiple document pages, is considered a single-page document. This means that for scanned images the value of <code>Page</code> is always 1. </p>"""
    query: NotRequired["capo_textract.types.query.Query"]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Block) -> dict:
    out: dict = {}
    if "block_type" in value:
        import capo_textract.types.block_type

        out["BlockType"] = capo_textract.types.block_type.serialize_aws_json_1_1(
            value["block_type"]
        )
    if "confidence" in value:
        out["Confidence"] = (
            "NaN"
            if value["confidence"] != value["confidence"]
            else "Infinity"
            if value["confidence"] == float("inf")
            else "-Infinity"
            if value["confidence"] == float("-inf")
            else value["confidence"]
        )
    if "text" in value:
        out["Text"] = value["text"]
    if "text_type" in value:
        import capo_textract.types.text_type

        out["TextType"] = capo_textract.types.text_type.serialize_aws_json_1_1(
            value["text_type"]
        )
    if "row_index" in value:
        out["RowIndex"] = value["row_index"]
    if "column_index" in value:
        out["ColumnIndex"] = value["column_index"]
    if "row_span" in value:
        out["RowSpan"] = value["row_span"]
    if "column_span" in value:
        out["ColumnSpan"] = value["column_span"]
    if "geometry" in value:
        import capo_textract.types.geometry

        out["Geometry"] = capo_textract.types.geometry.serialize_aws_json_1_1(
            value["geometry"]
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "relationships" in value:
        import capo_textract.types.relationship_list

        out["Relationships"] = (
            capo_textract.types.relationship_list.serialize_aws_json_1_1(
                value["relationships"]
            )
        )
    if "entity_types" in value:
        import capo_textract.types.entity_types

        out["EntityTypes"] = capo_textract.types.entity_types.serialize_aws_json_1_1(
            value["entity_types"]
        )
    if "selection_status" in value:
        import capo_textract.types.selection_status

        out["SelectionStatus"] = (
            capo_textract.types.selection_status.serialize_aws_json_1_1(
                value["selection_status"]
            )
        )
    if "page" in value:
        out["Page"] = value["page"]
    if "query" in value:
        import capo_textract.types.query

        out["Query"] = capo_textract.types.query.serialize_aws_json_1_1(value["query"])
    return out


def deserialize_aws_json_1_1(data: dict) -> Block:
    out: Block = {}  # type: ignore[typeddict-item]
    if data.get("BlockType") is not None:
        import capo_textract.types.block_type

        out["block_type"] = capo_textract.types.block_type.deserialize_aws_json_1_1(
            data["BlockType"]
        )
    if data.get("Confidence") is not None:
        out["confidence"] = float(data["Confidence"])
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("TextType") is not None:
        import capo_textract.types.text_type

        out["text_type"] = capo_textract.types.text_type.deserialize_aws_json_1_1(
            data["TextType"]
        )
    if data.get("RowIndex") is not None:
        out["row_index"] = data["RowIndex"]
    if data.get("ColumnIndex") is not None:
        out["column_index"] = data["ColumnIndex"]
    if data.get("RowSpan") is not None:
        out["row_span"] = data["RowSpan"]
    if data.get("ColumnSpan") is not None:
        out["column_span"] = data["ColumnSpan"]
    if data.get("Geometry") is not None:
        import capo_textract.types.geometry

        out["geometry"] = capo_textract.types.geometry.deserialize_aws_json_1_1(
            data["Geometry"]
        )
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Relationships") is not None:
        import capo_textract.types.relationship_list

        out["relationships"] = (
            capo_textract.types.relationship_list.deserialize_aws_json_1_1(
                data["Relationships"]
            )
        )
    if data.get("EntityTypes") is not None:
        import capo_textract.types.entity_types

        out["entity_types"] = capo_textract.types.entity_types.deserialize_aws_json_1_1(
            data["EntityTypes"]
        )
    if data.get("SelectionStatus") is not None:
        import capo_textract.types.selection_status

        out["selection_status"] = (
            capo_textract.types.selection_status.deserialize_aws_json_1_1(
                data["SelectionStatus"]
            )
        )
    if data.get("Page") is not None:
        out["page"] = data["Page"]
    if data.get("Query") is not None:
        import capo_textract.types.query

        out["query"] = capo_textract.types.query.deserialize_aws_json_1_1(data["Query"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Block) -> dict:
    out: dict = {}
    if "block_type" in value:
        import capo_textract.types.block_type

        out["BlockType"] = capo_textract.types.block_type.serialize_cbor(
            value["block_type"]
        )
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    if "text" in value:
        out["Text"] = value["text"]
    if "text_type" in value:
        import capo_textract.types.text_type

        out["TextType"] = capo_textract.types.text_type.serialize_cbor(
            value["text_type"]
        )
    if "row_index" in value:
        out["RowIndex"] = value["row_index"]
    if "column_index" in value:
        out["ColumnIndex"] = value["column_index"]
    if "row_span" in value:
        out["RowSpan"] = value["row_span"]
    if "column_span" in value:
        out["ColumnSpan"] = value["column_span"]
    if "geometry" in value:
        import capo_textract.types.geometry

        out["Geometry"] = capo_textract.types.geometry.serialize_cbor(value["geometry"])
    if "id" in value:
        out["Id"] = value["id"]
    if "relationships" in value:
        import capo_textract.types.relationship_list

        out["Relationships"] = capo_textract.types.relationship_list.serialize_cbor(
            value["relationships"]
        )
    if "entity_types" in value:
        import capo_textract.types.entity_types

        out["EntityTypes"] = capo_textract.types.entity_types.serialize_cbor(
            value["entity_types"]
        )
    if "selection_status" in value:
        import capo_textract.types.selection_status

        out["SelectionStatus"] = capo_textract.types.selection_status.serialize_cbor(
            value["selection_status"]
        )
    if "page" in value:
        out["Page"] = value["page"]
    if "query" in value:
        import capo_textract.types.query

        out["Query"] = capo_textract.types.query.serialize_cbor(value["query"])
    return out


def deserialize_cbor(data: dict) -> Block:
    out: Block = {}  # type: ignore[typeddict-item]
    if data.get("BlockType") is not None:
        import capo_textract.types.block_type

        out["block_type"] = capo_textract.types.block_type.deserialize_cbor(
            data["BlockType"]
        )
    if data.get("Confidence") is not None:
        out["confidence"] = float(data["Confidence"])
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("TextType") is not None:
        import capo_textract.types.text_type

        out["text_type"] = capo_textract.types.text_type.deserialize_cbor(
            data["TextType"]
        )
    if data.get("RowIndex") is not None:
        out["row_index"] = data["RowIndex"]
    if data.get("ColumnIndex") is not None:
        out["column_index"] = data["ColumnIndex"]
    if data.get("RowSpan") is not None:
        out["row_span"] = data["RowSpan"]
    if data.get("ColumnSpan") is not None:
        out["column_span"] = data["ColumnSpan"]
    if data.get("Geometry") is not None:
        import capo_textract.types.geometry

        out["geometry"] = capo_textract.types.geometry.deserialize_cbor(
            data["Geometry"]
        )
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Relationships") is not None:
        import capo_textract.types.relationship_list

        out["relationships"] = capo_textract.types.relationship_list.deserialize_cbor(
            data["Relationships"]
        )
    if data.get("EntityTypes") is not None:
        import capo_textract.types.entity_types

        out["entity_types"] = capo_textract.types.entity_types.deserialize_cbor(
            data["EntityTypes"]
        )
    if data.get("SelectionStatus") is not None:
        import capo_textract.types.selection_status

        out["selection_status"] = capo_textract.types.selection_status.deserialize_cbor(
            data["SelectionStatus"]
        )
    if data.get("Page") is not None:
        out["page"] = data["Page"]
    if data.get("Query") is not None:
        import capo_textract.types.query

        out["query"] = capo_textract.types.query.deserialize_cbor(data["Query"])
    return out
