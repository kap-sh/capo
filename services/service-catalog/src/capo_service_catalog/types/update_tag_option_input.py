"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdateTagOptionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.tag_option_active
    import capo_service_catalog.types.tag_option_id
    import capo_service_catalog.types.tag_option_value


class UpdateTagOptionInput(TypedDict, closed=True):
    id: "capo_service_catalog.types.tag_option_id.TagOptionId"
    """<p>The TagOption identifier.</p>"""
    value: NotRequired["capo_service_catalog.types.tag_option_value.TagOptionValue"]
    """<p>The updated value.</p>"""
    active: NotRequired["capo_service_catalog.types.tag_option_active.TagOptionActive"]
    """<p>The updated active state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTagOptionInput) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "value" in value:
        out["Value"] = value["value"]
    if "active" in value:
        out["Active"] = value["active"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTagOptionInput:
    out: UpdateTagOptionInput = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("Active") is not None:
        out["active"] = data["Active"]
    return out
