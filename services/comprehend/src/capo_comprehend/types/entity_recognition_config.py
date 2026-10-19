"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognitionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.entity_types_list


class EntityRecognitionConfig(TypedDict, closed=True):
    entity_types: "capo_comprehend.types.entity_types_list.EntityTypesList"
    """<p>Up to 25 entity types that the model is trained to recognize.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognitionConfig) -> dict:
    out: dict = {}
    import capo_comprehend.types.entity_types_list

    out["EntityTypes"] = capo_comprehend.types.entity_types_list.serialize_aws_json_1_1(
        value["entity_types"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityRecognitionConfig:
    out: EntityRecognitionConfig = {}  # type: ignore[typeddict-item]
    if data.get("EntityTypes") is not None:
        import capo_comprehend.types.entity_types_list

        out["entity_types"] = (
            capo_comprehend.types.entity_types_list.deserialize_aws_json_1_1(
                data["EntityTypes"]
            )
        )
    else:
        out["entity_types"] = []
    return out
