"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.generic_string


class ValidationExceptionField(TypedDict, closed=True):
    name: "capo_bcm_data_exports.types.generic_string.GenericString"
    """<p>The field name where the invalid entry was detected.</p>"""
    message: "capo_bcm_data_exports.types.generic_string.GenericString"
    """<p>A message with the reason for the validation exception error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    return out
