"""Generated from Smithy shape ``com.amazonaws.comprehend#RelationshipsListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.relationship_type
    import capo_comprehend.types.string_list


class RelationshipsListItem(TypedDict, closed=True):
    ids: NotRequired["capo_comprehend.types.string_list.StringList"]
    """<p>Identifers of the child blocks.</p>"""
    type: NotRequired["capo_comprehend.types.relationship_type.RelationshipType"]
    """<p>Only supported relationship is a child relationship.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationshipsListItem) -> dict:
    out: dict = {}
    if "ids" in value:
        import capo_comprehend.types.string_list

        out["Ids"] = capo_comprehend.types.string_list.serialize_aws_json_1_1(
            value["ids"]
        )
    if "type" in value:
        import capo_comprehend.types.relationship_type

        out["Type"] = capo_comprehend.types.relationship_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RelationshipsListItem:
    out: RelationshipsListItem = {}  # type: ignore[typeddict-item]
    if data.get("Ids") is not None:
        import capo_comprehend.types.string_list

        out["ids"] = capo_comprehend.types.string_list.deserialize_aws_json_1_1(
            data["Ids"]
        )
    if data.get("Type") is not None:
        import capo_comprehend.types.relationship_type

        out["type"] = capo_comprehend.types.relationship_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RelationshipsListItem) -> dict:
    out: dict = {}
    if "ids" in value:
        import capo_comprehend.types.string_list

        out["Ids"] = capo_comprehend.types.string_list.serialize_cbor(value["ids"])
    if "type" in value:
        import capo_comprehend.types.relationship_type

        out["Type"] = capo_comprehend.types.relationship_type.serialize_cbor(
            value["type"]
        )
    return out


def deserialize_cbor(data: dict) -> RelationshipsListItem:
    out: RelationshipsListItem = {}  # type: ignore[typeddict-item]
    if data.get("Ids") is not None:
        import capo_comprehend.types.string_list

        out["ids"] = capo_comprehend.types.string_list.deserialize_cbor(data["Ids"])
    if data.get("Type") is not None:
        import capo_comprehend.types.relationship_type

        out["type"] = capo_comprehend.types.relationship_type.deserialize_cbor(
            data["Type"]
        )
    return out
