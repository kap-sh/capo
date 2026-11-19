"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityLabel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.float
    import capo_comprehend.types.pii_entity_type


class EntityLabel(TypedDict, closed=True):
    name: NotRequired["capo_comprehend.types.pii_entity_type.PiiEntityType"]
    """<p>The name of the label.</p>"""
    score: NotRequired["capo_comprehend.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of the detection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityLabel) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_comprehend.types.pii_entity_type

        out["Name"] = capo_comprehend.types.pii_entity_type.serialize_aws_json_1_1(
            value["name"]
        )
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
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityLabel:
    out: EntityLabel = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_comprehend.types.pii_entity_type

        out["name"] = capo_comprehend.types.pii_entity_type.deserialize_aws_json_1_1(
            data["Name"]
        )
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntityLabel) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_comprehend.types.pii_entity_type

        out["Name"] = capo_comprehend.types.pii_entity_type.serialize_cbor(
            value["name"]
        )
    if "score" in value:
        out["Score"] = value["score"]
    return out


def deserialize_cbor(data: dict) -> EntityLabel:
    out: EntityLabel = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_comprehend.types.pii_entity_type

        out["name"] = capo_comprehend.types.pii_entity_type.deserialize_cbor(
            data["Name"]
        )
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    return out
