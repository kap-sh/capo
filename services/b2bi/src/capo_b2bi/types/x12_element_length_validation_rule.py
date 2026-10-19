"""Generated from Smithy shape ``com.amazonaws.b2bi#X12ElementLengthValidationRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.element_id


class X12ElementLengthValidationRule(TypedDict, closed=True):
    element_id: "capo_b2bi.types.element_id.ElementId"
    """<p>Specifies the four-digit element ID to which the length constraints will be applied. This identifies which X12 element will have its length requirements modified.</p>"""
    max_length: "int"
    """<p>Specifies the maximum allowed length for the identified element. This value must be between 1 and 200 characters and defines the upper limit for the element's content length.</p>"""
    min_length: "int"
    """<p>Specifies the minimum required length for the identified element. This value must be between 1 and 200 characters and defines the lower limit for the element's content length.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12ElementLengthValidationRule) -> dict:
    out: dict = {}
    out["elementId"] = value["element_id"]
    out["maxLength"] = value["max_length"]
    out["minLength"] = value["min_length"]
    return out


def deserialize_aws_json_1_0(data: dict) -> X12ElementLengthValidationRule:
    out: X12ElementLengthValidationRule = {}  # type: ignore[typeddict-item]
    if data.get("elementId") is not None:
        out["element_id"] = data["elementId"]
    else:
        out["element_id"] = ""
    if data.get("maxLength") is not None:
        out["max_length"] = data["maxLength"]
    else:
        out["max_length"] = 0
    if data.get("minLength") is not None:
        out["min_length"] = data["minLength"]
    else:
        out["min_length"] = 0
    return out
