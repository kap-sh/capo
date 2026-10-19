"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.string


class ValidationExceptionField(TypedDict, closed=True):
    name: "capo_ssm_contacts.types.string.String"
    """<p>The name of the field that caused the exception.</p>"""
    message: "capo_ssm_contacts.types.string.String"
    """<p>Information about what caused the field to cause an exception.</p>"""


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
