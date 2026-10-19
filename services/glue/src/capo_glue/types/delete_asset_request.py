"""Generated from Smithy shape ``com.amazonaws.glue#DeleteAssetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.asset_id


class DeleteAssetRequest(TypedDict, closed=True):
    identifier: "capo_glue.types.asset_id.AssetId"
    """<p>The unique identifier of the asset to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAssetRequest) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAssetRequest:
    out: DeleteAssetRequest = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    return out
