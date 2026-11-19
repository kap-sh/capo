"""Generated from Smithy shape ``com.amazonaws.comprehend#Block``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.block_type
    import capo_comprehend.types.geometry
    import capo_comprehend.types.integer
    import capo_comprehend.types.list_of_relationships
    import capo_comprehend.types.string


class Block(TypedDict, closed=True):
    id: NotRequired["capo_comprehend.types.string.String"]
    """<p>Unique identifier for the block.</p>"""
    block_type: NotRequired["capo_comprehend.types.block_type.BlockType"]
    """<p>The block represents a line of text or one word of text.</p> <ul> <li> <p>WORD - A word that's detected on a document page. A word is one or more ISO basic Latin script characters that aren't separated by spaces.</p> </li> <li> <p>LINE - A string of tab-delimited, contiguous words that are detected on a document page</p> </li> </ul>"""
    text: NotRequired["capo_comprehend.types.string.String"]
    """<p>The word or line of text extracted from the block.</p>"""
    page: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>Page number where the block appears.</p>"""
    geometry: NotRequired["capo_comprehend.types.geometry.Geometry"]
    """<p>Co-ordinates of the rectangle or polygon that contains the text.</p>"""
    relationships: NotRequired[
        "capo_comprehend.types.list_of_relationships.ListOfRelationships"
    ]
    """<p>A list of child blocks of the current block. For example, a LINE object has child blocks for each WORD block that's part of the line of text. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Block) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "block_type" in value:
        import capo_comprehend.types.block_type

        out["BlockType"] = capo_comprehend.types.block_type.serialize_aws_json_1_1(
            value["block_type"]
        )
    if "text" in value:
        out["Text"] = value["text"]
    if "page" in value:
        out["Page"] = value["page"]
    if "geometry" in value:
        import capo_comprehend.types.geometry

        out["Geometry"] = capo_comprehend.types.geometry.serialize_aws_json_1_1(
            value["geometry"]
        )
    if "relationships" in value:
        import capo_comprehend.types.list_of_relationships

        out["Relationships"] = (
            capo_comprehend.types.list_of_relationships.serialize_aws_json_1_1(
                value["relationships"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Block:
    out: Block = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("BlockType") is not None:
        import capo_comprehend.types.block_type

        out["block_type"] = capo_comprehend.types.block_type.deserialize_aws_json_1_1(
            data["BlockType"]
        )
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("Page") is not None:
        out["page"] = data["Page"]
    if data.get("Geometry") is not None:
        import capo_comprehend.types.geometry

        out["geometry"] = capo_comprehend.types.geometry.deserialize_aws_json_1_1(
            data["Geometry"]
        )
    if data.get("Relationships") is not None:
        import capo_comprehend.types.list_of_relationships

        out["relationships"] = (
            capo_comprehend.types.list_of_relationships.deserialize_aws_json_1_1(
                data["Relationships"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Block) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "block_type" in value:
        import capo_comprehend.types.block_type

        out["BlockType"] = capo_comprehend.types.block_type.serialize_cbor(
            value["block_type"]
        )
    if "text" in value:
        out["Text"] = value["text"]
    if "page" in value:
        out["Page"] = value["page"]
    if "geometry" in value:
        import capo_comprehend.types.geometry

        out["Geometry"] = capo_comprehend.types.geometry.serialize_cbor(
            value["geometry"]
        )
    if "relationships" in value:
        import capo_comprehend.types.list_of_relationships

        out["Relationships"] = (
            capo_comprehend.types.list_of_relationships.serialize_cbor(
                value["relationships"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> Block:
    out: Block = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("BlockType") is not None:
        import capo_comprehend.types.block_type

        out["block_type"] = capo_comprehend.types.block_type.deserialize_cbor(
            data["BlockType"]
        )
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("Page") is not None:
        out["page"] = data["Page"]
    if data.get("Geometry") is not None:
        import capo_comprehend.types.geometry

        out["geometry"] = capo_comprehend.types.geometry.deserialize_cbor(
            data["Geometry"]
        )
    if data.get("Relationships") is not None:
        import capo_comprehend.types.list_of_relationships

        out["relationships"] = (
            capo_comprehend.types.list_of_relationships.deserialize_cbor(
                data["Relationships"]
            )
        )
    return out
