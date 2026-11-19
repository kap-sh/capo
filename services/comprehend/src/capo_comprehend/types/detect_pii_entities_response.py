"""Generated from Smithy shape ``com.amazonaws.comprehend#DetectPiiEntitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.list_of_pii_entities


class DetectPiiEntitiesResponse(TypedDict, closed=True):
    entities: NotRequired[
        "capo_comprehend.types.list_of_pii_entities.ListOfPiiEntities"
    ]
    """<p>A collection of PII entities identified in the input text. For each entity, the response provides the entity type, where the entity text begins and ends, and the level of confidence that Amazon Comprehend has in the detection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectPiiEntitiesResponse) -> dict:
    out: dict = {}
    if "entities" in value:
        import capo_comprehend.types.list_of_pii_entities

        out["Entities"] = (
            capo_comprehend.types.list_of_pii_entities.serialize_aws_json_1_1(
                value["entities"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectPiiEntitiesResponse:
    out: DetectPiiEntitiesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Entities") is not None:
        import capo_comprehend.types.list_of_pii_entities

        out["entities"] = (
            capo_comprehend.types.list_of_pii_entities.deserialize_aws_json_1_1(
                data["Entities"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DetectPiiEntitiesResponse) -> dict:
    out: dict = {}
    if "entities" in value:
        import capo_comprehend.types.list_of_pii_entities

        out["Entities"] = capo_comprehend.types.list_of_pii_entities.serialize_cbor(
            value["entities"]
        )
    return out


def deserialize_cbor(data: dict) -> DetectPiiEntitiesResponse:
    out: DetectPiiEntitiesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Entities") is not None:
        import capo_comprehend.types.list_of_pii_entities

        out["entities"] = capo_comprehend.types.list_of_pii_entities.deserialize_cbor(
            data["Entities"]
        )
    return out
