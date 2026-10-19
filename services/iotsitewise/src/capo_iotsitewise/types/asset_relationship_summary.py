"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetRelationshipSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_hierarchy_info
    import capo_iotsitewise.types.asset_relationship_type


class AssetRelationshipSummary(TypedDict, closed=True):
    hierarchy_info: NotRequired[
        "capo_iotsitewise.types.asset_hierarchy_info.AssetHierarchyInfo"
    ]
    """<p>The assets that are related through an asset hierarchy.</p> <p>This object is present if the <code>relationshipType</code> is <code>HIERARCHY</code>.</p>"""
    relationship_type: (
        "capo_iotsitewise.types.asset_relationship_type.AssetRelationshipType"
    )
    """<p>The relationship type of the assets in this relationship. This value is one of the following:</p> <ul> <li> <p> <code>HIERARCHY</code> – The assets are related through an asset hierarchy. If you specify this relationship type, this asset relationship includes the <code>hierarchyInfo</code> object.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetRelationshipSummary) -> dict:
    out: dict = {}
    if "hierarchy_info" in value:
        import capo_iotsitewise.types.asset_hierarchy_info

        out["hierarchyInfo"] = (
            capo_iotsitewise.types.asset_hierarchy_info.serialize_json(
                value["hierarchy_info"]
            )
        )
    import capo_iotsitewise.types.asset_relationship_type

    out["relationshipType"] = (
        capo_iotsitewise.types.asset_relationship_type.serialize_json(
            value["relationship_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssetRelationshipSummary:
    out: AssetRelationshipSummary = {}  # type: ignore[typeddict-item]
    if data.get("hierarchyInfo") is not None:
        import capo_iotsitewise.types.asset_hierarchy_info

        out["hierarchy_info"] = (
            capo_iotsitewise.types.asset_hierarchy_info.deserialize_json(
                data["hierarchyInfo"]
            )
        )
    if data.get("relationshipType") is not None:
        import capo_iotsitewise.types.asset_relationship_type

        out["relationship_type"] = (
            capo_iotsitewise.types.asset_relationship_type.deserialize_json(
                data["relationshipType"]
            )
        )
    else:
        import typing

        out["relationship_type"] = typing.cast(
            "capo_iotsitewise.types.asset_relationship_type.AssetRelationshipType", ""
        )
    return out
