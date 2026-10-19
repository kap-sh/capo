"""Generated from Smithy shape ``com.amazonaws.devopsagent#Asset``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_devops_agent.types.asset_type
    import capo_devops_agent.types.resource_id


class Asset(TypedDict, closed=True):
    asset_id: "capo_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier for this asset</p>"""
    asset_type: "capo_devops_agent.types.asset_type.AssetType"
    """<p>The type of this asset</p>"""
    metadata: "object"
    """<p>The metadata for this asset</p>"""
    version: "int"
    """<p>The version number of this asset</p>"""
    created_at: "datetime.datetime"
    """<p>Timestamp when this asset was created</p>"""
    updated_at: "datetime.datetime"
    """<p>Timestamp when this asset was last updated</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Asset) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    out["assetType"] = value["asset_type"]
    out["metadata"] = value["metadata"]
    out["version"] = value["version"]
    import capo_devops_agent.types._prelude.timestamp

    out["createdAt"] = capo_devops_agent.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_devops_agent.types._prelude.timestamp

    out["updatedAt"] = capo_devops_agent.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> Asset:
    out: Asset = {}  # type: ignore[typeddict-item]
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    else:
        out["asset_id"] = ""
    if data.get("assetType") is not None:
        out["asset_type"] = data["assetType"]
    else:
        out["asset_type"] = ""
    if data.get("metadata") is not None:
        out["metadata"] = data["metadata"]
    else:
        out["metadata"] = None
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = 0
    if data.get("createdAt") is not None:
        import capo_devops_agent.types._prelude.timestamp

        out["created_at"] = capo_devops_agent.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_devops_agent.types._prelude.timestamp

        out["updated_at"] = capo_devops_agent.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
