"""Generated from Smithy shape ``com.amazonaws.b2bi#X12ElementRequirementValidationRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import capo_b2bi.types.element_position
    import capo_b2bi.types.element_requirement


class X12ElementRequirementValidationRule(TypedDict, closed=True):
    element_position: "capo_b2bi.types.element_position.ElementPosition"
    """<p>Specifies the position of the element within an X12 segment for which the requirement status will be modified. The format follows the pattern of segment identifier followed by element position (e.g., "ST-01" for the first element of the ST segment).</p>"""
    requirement: "capo_b2bi.types.element_requirement.ElementRequirement"
    """<p>Specifies the requirement status for the element at the specified position. Valid values are OPTIONAL (the element may be omitted) or MANDATORY (the element must be present).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12ElementRequirementValidationRule) -> dict:
    out: dict = {}
    out["elementPosition"] = value["element_position"]
    import capo_b2bi.types.element_requirement

    out["requirement"] = capo_b2bi.types.element_requirement.serialize_aws_json_1_0(
        value["requirement"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> X12ElementRequirementValidationRule:
    out: X12ElementRequirementValidationRule = {}  # type: ignore[typeddict-item]
    if data.get("elementPosition") is not None:
        out["element_position"] = data["elementPosition"]
    else:
        raise DeserializationError(
            "X12ElementRequirementValidationRule.element_position required"
        )
    if data.get("requirement") is not None:
        import capo_b2bi.types.element_requirement

        out["requirement"] = (
            capo_b2bi.types.element_requirement.deserialize_aws_json_1_0(
                data["requirement"]
            )
        )
    else:
        raise DeserializationError(
            "X12ElementRequirementValidationRule.requirement required"
        )
    return out
