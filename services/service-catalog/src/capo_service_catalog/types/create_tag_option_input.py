"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CreateTagOptionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.tag_option_key
    import capo_service_catalog.types.tag_option_value


class CreateTagOptionInput(TypedDict, closed=True):
    key: "capo_service_catalog.types.tag_option_key.TagOptionKey"
    """<p>The TagOption key.</p>"""
    value: "capo_service_catalog.types.tag_option_value.TagOptionValue"
    """<p>The TagOption value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTagOptionInput) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTagOptionInput:
    out: CreateTagOptionInput = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
