"""Generated from Smithy shape ``com.amazonaws.comprehend#ContainsPiiEntitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.list_of_entity_labels


class ContainsPiiEntitiesResponse(TypedDict, closed=True):
    labels: NotRequired[
        "capo_comprehend.types.list_of_entity_labels.ListOfEntityLabels"
    ]
    """<p>The labels used in the document being analyzed. Individual labels represent personally identifiable information (PII) entity types.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainsPiiEntitiesResponse) -> dict:
    out: dict = {}
    if "labels" in value:
        import capo_comprehend.types.list_of_entity_labels

        out["Labels"] = (
            capo_comprehend.types.list_of_entity_labels.serialize_aws_json_1_1(
                value["labels"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainsPiiEntitiesResponse:
    out: ContainsPiiEntitiesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Labels") is not None:
        import capo_comprehend.types.list_of_entity_labels

        out["labels"] = (
            capo_comprehend.types.list_of_entity_labels.deserialize_aws_json_1_1(
                data["Labels"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainsPiiEntitiesResponse) -> dict:
    out: dict = {}
    if "labels" in value:
        import capo_comprehend.types.list_of_entity_labels

        out["Labels"] = capo_comprehend.types.list_of_entity_labels.serialize_cbor(
            value["labels"]
        )
    return out


def deserialize_cbor(data: dict) -> ContainsPiiEntitiesResponse:
    out: ContainsPiiEntitiesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Labels") is not None:
        import capo_comprehend.types.list_of_entity_labels

        out["labels"] = capo_comprehend.types.list_of_entity_labels.deserialize_cbor(
            data["Labels"]
        )
    return out
