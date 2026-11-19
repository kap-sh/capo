"""Generated from Smithy shape ``com.amazonaws.comprehend#BatchDetectEntitiesItemResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.integer
    import capo_comprehend.types.list_of_entities


class BatchDetectEntitiesItemResult(TypedDict, closed=True):
    index: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>The zero-based index of the document in the input list.</p>"""
    entities: NotRequired["capo_comprehend.types.list_of_entities.ListOfEntities"]
    """<p>One or more <a>Entity</a> objects, one for each entity detected in the document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDetectEntitiesItemResult) -> dict:
    out: dict = {}
    if "index" in value:
        out["Index"] = value["index"]
    if "entities" in value:
        import capo_comprehend.types.list_of_entities

        out["Entities"] = capo_comprehend.types.list_of_entities.serialize_aws_json_1_1(
            value["entities"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDetectEntitiesItemResult:
    out: BatchDetectEntitiesItemResult = {}  # type: ignore[typeddict-item]
    if data.get("Index") is not None:
        out["index"] = data["Index"]
    if data.get("Entities") is not None:
        import capo_comprehend.types.list_of_entities

        out["entities"] = (
            capo_comprehend.types.list_of_entities.deserialize_aws_json_1_1(
                data["Entities"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchDetectEntitiesItemResult) -> dict:
    out: dict = {}
    if "index" in value:
        out["Index"] = value["index"]
    if "entities" in value:
        import capo_comprehend.types.list_of_entities

        out["Entities"] = capo_comprehend.types.list_of_entities.serialize_cbor(
            value["entities"]
        )
    return out


def deserialize_cbor(data: dict) -> BatchDetectEntitiesItemResult:
    out: BatchDetectEntitiesItemResult = {}  # type: ignore[typeddict-item]
    if data.get("Index") is not None:
        out["index"] = data["Index"]
    if data.get("Entities") is not None:
        import capo_comprehend.types.list_of_entities

        out["entities"] = capo_comprehend.types.list_of_entities.deserialize_cbor(
            data["Entities"]
        )
    return out
