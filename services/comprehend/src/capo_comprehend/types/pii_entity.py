"""Generated from Smithy shape ``com.amazonaws.comprehend#PiiEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.float
    import capo_comprehend.types.integer
    import capo_comprehend.types.pii_entity_type


class PiiEntity(TypedDict, closed=True):
    score: NotRequired["capo_comprehend.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of the detection.</p>"""
    type: NotRequired["capo_comprehend.types.pii_entity_type.PiiEntityType"]
    """<p>The entity's type.</p>"""
    begin_offset: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>The zero-based offset from the beginning of the source text to the first character in the entity.</p>"""
    end_offset: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>The zero-based offset from the beginning of the source text to the last character in the entity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PiiEntity) -> dict:
    out: dict = {}
    if "score" in value:
        out["Score"] = (
            "NaN"
            if value["score"] != value["score"]
            else "Infinity"
            if value["score"] == float("inf")
            else "-Infinity"
            if value["score"] == float("-inf")
            else value["score"]
        )
    if "type" in value:
        import capo_comprehend.types.pii_entity_type

        out["Type"] = capo_comprehend.types.pii_entity_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PiiEntity:
    out: PiiEntity = {}  # type: ignore[typeddict-item]
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    if data.get("Type") is not None:
        import capo_comprehend.types.pii_entity_type

        out["type"] = capo_comprehend.types.pii_entity_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("BeginOffset") is not None:
        out["begin_offset"] = data["BeginOffset"]
    if data.get("EndOffset") is not None:
        out["end_offset"] = data["EndOffset"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PiiEntity) -> dict:
    out: dict = {}
    if "score" in value:
        out["Score"] = value["score"]
    if "type" in value:
        import capo_comprehend.types.pii_entity_type

        out["Type"] = capo_comprehend.types.pii_entity_type.serialize_cbor(
            value["type"]
        )
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    return out


def deserialize_cbor(data: dict) -> PiiEntity:
    out: PiiEntity = {}  # type: ignore[typeddict-item]
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    if data.get("Type") is not None:
        import capo_comprehend.types.pii_entity_type

        out["type"] = capo_comprehend.types.pii_entity_type.deserialize_cbor(
            data["Type"]
        )
    if data.get("BeginOffset") is not None:
        out["begin_offset"] = data["BeginOffset"]
    if data.get("EndOffset") is not None:
        out["end_offset"] = data["EndOffset"]
    return out
