"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#UnmappedAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.attribute
    import capo_comprehendmedical.types.entity_type


class UnmappedAttribute(TypedDict, closed=True):
    type: NotRequired["capo_comprehendmedical.types.entity_type.EntityType"]
    """<p> The type of the unmapped attribute, could be one of the following values: "MEDICATION", "MEDICAL_CONDITION", "ANATOMY", "TEST_AND_TREATMENT_PROCEDURE" or "PROTECTED_HEALTH_INFORMATION". </p>"""
    attribute: NotRequired["capo_comprehendmedical.types.attribute.Attribute"]
    """<p> The specific attribute that has been extracted but not mapped to an entity. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnmappedAttribute) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_comprehendmedical.types.entity_type

        out["Type"] = capo_comprehendmedical.types.entity_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "attribute" in value:
        import capo_comprehendmedical.types.attribute

        out["Attribute"] = (
            capo_comprehendmedical.types.attribute.serialize_aws_json_1_1(
                value["attribute"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UnmappedAttribute:
    out: UnmappedAttribute = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_comprehendmedical.types.entity_type

        out["type"] = capo_comprehendmedical.types.entity_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("Attribute") is not None:
        import capo_comprehendmedical.types.attribute

        out["attribute"] = (
            capo_comprehendmedical.types.attribute.deserialize_aws_json_1_1(
                data["Attribute"]
            )
        )
    return out
