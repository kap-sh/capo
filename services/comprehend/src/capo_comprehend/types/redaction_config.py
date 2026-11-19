"""Generated from Smithy shape ``com.amazonaws.comprehend#RedactionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.list_of_pii_entity_types
    import capo_comprehend.types.mask_character
    import capo_comprehend.types.pii_entities_detection_mask_mode


class RedactionConfig(TypedDict, closed=True):
    pii_entity_types: NotRequired[
        "capo_comprehend.types.list_of_pii_entity_types.ListOfPiiEntityTypes"
    ]
    """<p>An array of the types of PII entities that Amazon Comprehend detects in the input text for your request.</p>"""
    mask_mode: NotRequired[
        "capo_comprehend.types.pii_entities_detection_mask_mode.PiiEntitiesDetectionMaskMode"
    ]
    """<p>Specifies whether the PII entity is redacted with the mask character or the entity type.</p>"""
    mask_character: NotRequired["capo_comprehend.types.mask_character.MaskCharacter"]
    """<p>A character that replaces each character in the redacted PII entity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedactionConfig) -> dict:
    out: dict = {}
    if "pii_entity_types" in value:
        import capo_comprehend.types.list_of_pii_entity_types

        out["PiiEntityTypes"] = (
            capo_comprehend.types.list_of_pii_entity_types.serialize_aws_json_1_1(
                value["pii_entity_types"]
            )
        )
    if "mask_mode" in value:
        import capo_comprehend.types.pii_entities_detection_mask_mode

        out["MaskMode"] = (
            capo_comprehend.types.pii_entities_detection_mask_mode.serialize_aws_json_1_1(
                value["mask_mode"]
            )
        )
    if "mask_character" in value:
        out["MaskCharacter"] = value["mask_character"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RedactionConfig:
    out: RedactionConfig = {}  # type: ignore[typeddict-item]
    if data.get("PiiEntityTypes") is not None:
        import capo_comprehend.types.list_of_pii_entity_types

        out["pii_entity_types"] = (
            capo_comprehend.types.list_of_pii_entity_types.deserialize_aws_json_1_1(
                data["PiiEntityTypes"]
            )
        )
    if data.get("MaskMode") is not None:
        import capo_comprehend.types.pii_entities_detection_mask_mode

        out["mask_mode"] = (
            capo_comprehend.types.pii_entities_detection_mask_mode.deserialize_aws_json_1_1(
                data["MaskMode"]
            )
        )
    if data.get("MaskCharacter") is not None:
        out["mask_character"] = data["MaskCharacter"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RedactionConfig) -> dict:
    out: dict = {}
    if "pii_entity_types" in value:
        import capo_comprehend.types.list_of_pii_entity_types

        out["PiiEntityTypes"] = (
            capo_comprehend.types.list_of_pii_entity_types.serialize_cbor(
                value["pii_entity_types"]
            )
        )
    if "mask_mode" in value:
        import capo_comprehend.types.pii_entities_detection_mask_mode

        out["MaskMode"] = (
            capo_comprehend.types.pii_entities_detection_mask_mode.serialize_cbor(
                value["mask_mode"]
            )
        )
    if "mask_character" in value:
        out["MaskCharacter"] = value["mask_character"]
    return out


def deserialize_cbor(data: dict) -> RedactionConfig:
    out: RedactionConfig = {}  # type: ignore[typeddict-item]
    if data.get("PiiEntityTypes") is not None:
        import capo_comprehend.types.list_of_pii_entity_types

        out["pii_entity_types"] = (
            capo_comprehend.types.list_of_pii_entity_types.deserialize_cbor(
                data["PiiEntityTypes"]
            )
        )
    if data.get("MaskMode") is not None:
        import capo_comprehend.types.pii_entities_detection_mask_mode

        out["mask_mode"] = (
            capo_comprehend.types.pii_entities_detection_mask_mode.deserialize_cbor(
                data["MaskMode"]
            )
        )
    if data.get("MaskCharacter") is not None:
        out["mask_character"] = data["MaskCharacter"]
    return out
