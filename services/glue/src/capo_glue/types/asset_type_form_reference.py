"""Generated from Smithy shape ``com.amazonaws.glue#AssetTypeFormReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.form_type_id


class AssetTypeFormReference(TypedDict, closed=True):
    form_type_identifier: "capo_glue.types.form_type_id.FormTypeId"
    """<p>The identifier of the referenced form type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssetTypeFormReference) -> dict:
    out: dict = {}
    out["FormTypeIdentifier"] = value["form_type_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssetTypeFormReference:
    out: AssetTypeFormReference = {}  # type: ignore[typeddict-item]
    if data.get("FormTypeIdentifier") is not None:
        out["form_type_identifier"] = data["FormTypeIdentifier"]
    else:
        out["form_type_identifier"] = ""
    return out
