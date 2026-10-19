"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.bounded_string


class ValidationExceptionField(TypedDict, closed=True):
    name: "capo_marketplace_agreement.types.bounded_string.BoundedString"
    """<p>The name of the field associated with the error.</p>"""
    message: "capo_marketplace_agreement.types.bounded_string.BoundedString"
    """<p>See applicable actions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
