"""Generated from Smithy shape ``com.amazonaws.glue#GetAssetTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.asset_type_id


class GetAssetTypeRequest(TypedDict, closed=True):
    identifier: "capo_glue.types.asset_type_id.AssetTypeId"
    """<p>The identifier of the asset type to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAssetTypeRequest) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAssetTypeRequest:
    out: GetAssetTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    return out
