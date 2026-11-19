"""Generated from Smithy shape ``com.amazonaws.textract#Relationship``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.id_list
    import capo_textract.types.relationship_type


class Relationship(TypedDict, closed=True):
    type: NotRequired["capo_textract.types.relationship_type.RelationshipType"]
    """<p>The type of relationship between the blocks in the IDs array and the current block. The following list describes the relationship types that can be returned. </p> <ul> <li> <p> <i>VALUE</i> - A list that contains the ID of the VALUE block that's associated with the KEY of a key-value pair.</p> </li> <li> <p> <i>CHILD</i> - A list of IDs that identify blocks found within the current block object. For example, WORD blocks have a CHILD relationship to the LINE block type.</p> </li> <li> <p> <i>MERGED_CELL</i> - A list of IDs that identify each of the MERGED_CELL block types in a table.</p> </li> <li> <p> <i>ANSWER</i> - A list that contains the ID of the QUERY_RESULT block that’s associated with the corresponding QUERY block. </p> </li> <li> <p> <i>TABLE</i> - A list of IDs that identify associated TABLE block types. </p> </li> <li> <p> <i>TABLE_TITLE</i> - A list that contains the ID for the TABLE_TITLE block type in a table. </p> </li> <li> <p> <i>TABLE_FOOTER</i> - A list of IDs that identify the TABLE_FOOTER block types in a table. </p> </li> </ul>"""
    ids: NotRequired["capo_textract.types.id_list.IdList"]
    """<p>An array of IDs for related blocks. You can get the type of the relationship from the <code>Type</code> element.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Relationship) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_textract.types.relationship_type

        out["Type"] = capo_textract.types.relationship_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "ids" in value:
        import capo_textract.types.id_list

        out["Ids"] = capo_textract.types.id_list.serialize_aws_json_1_1(value["ids"])
    return out


def deserialize_aws_json_1_1(data: dict) -> Relationship:
    out: Relationship = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_textract.types.relationship_type

        out["type"] = capo_textract.types.relationship_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("Ids") is not None:
        import capo_textract.types.id_list

        out["ids"] = capo_textract.types.id_list.deserialize_aws_json_1_1(data["Ids"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Relationship) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_textract.types.relationship_type

        out["Type"] = capo_textract.types.relationship_type.serialize_cbor(
            value["type"]
        )
    if "ids" in value:
        import capo_textract.types.id_list

        out["Ids"] = capo_textract.types.id_list.serialize_cbor(value["ids"])
    return out


def deserialize_cbor(data: dict) -> Relationship:
    out: Relationship = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_textract.types.relationship_type

        out["type"] = capo_textract.types.relationship_type.deserialize_cbor(
            data["Type"]
        )
    if data.get("Ids") is not None:
        import capo_textract.types.id_list

        out["ids"] = capo_textract.types.id_list.deserialize_cbor(data["Ids"])
    return out
