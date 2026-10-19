"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchAssociateProjectAssetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.i_ds
    import capo_iotsitewise.types.id


class BatchAssociateProjectAssetsRequest(TypedDict, closed=True):
    project_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the project to which to associate the assets.</p>"""
    asset_ids: "capo_iotsitewise.types.i_ds.IDs"
    """<p>The IDs of the assets to be associated to the project.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAssociateProjectAssetsRequest) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.i_ds

    out["assetIds"] = capo_iotsitewise.types.i_ds.serialize_json(value["asset_ids"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> BatchAssociateProjectAssetsRequest:
    out: BatchAssociateProjectAssetsRequest = {}  # type: ignore[typeddict-item]
    if data.get("assetIds") is not None:
        import capo_iotsitewise.types.i_ds

        out["asset_ids"] = capo_iotsitewise.types.i_ds.deserialize_json(
            data["assetIds"]
        )
    else:
        out["asset_ids"] = []
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
