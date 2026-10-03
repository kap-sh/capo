"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.asset_hierarchies
    import capo_iotsitewise.types.asset_status
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.external_id
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name
    import capo_iotsitewise.types.timestamp


class AssetSummary(TypedDict, closed=True):
    id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset, in UUID format.</p>"""
    external_id: NotRequired["capo_iotsitewise.types.external_id.ExternalId"]
    """<p>The external ID of the asset. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the asset, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:asset/${AssetId}</code> </p>"""
    name: "capo_iotsitewise.types.name.Name"
    """<p>The name of the asset.</p>"""
    asset_model_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset model used to create this asset.</p>"""
    creation_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the asset was created, in Unix epoch time.</p>"""
    last_update_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the asset was last updated, in Unix epoch time.</p>"""
    status: "capo_iotsitewise.types.asset_status.AssetStatus"
    """<p>The current status of the asset.</p>"""
    hierarchies: "capo_iotsitewise.types.asset_hierarchies.AssetHierarchies"
    """<p>A list of asset hierarchies that each contain a <code>hierarchyId</code>. A hierarchy specifies allowed parent/child asset relationships.</p>"""
    description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>A description for the asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["assetModelId"] = value["asset_model_id"]
    import capo_iotsitewise.types.timestamp

    out["creationDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["creation_date"]
    )
    import capo_iotsitewise.types.timestamp

    out["lastUpdateDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["last_update_date"]
    )
    import capo_iotsitewise.types.asset_status

    out["status"] = capo_iotsitewise.types.asset_status.serialize_json(value["status"])
    import capo_iotsitewise.types.asset_hierarchies

    out["hierarchies"] = capo_iotsitewise.types.asset_hierarchies.serialize_json(
        value["hierarchies"]
    )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> AssetSummary:
    out: AssetSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AssetSummary.id required")
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("AssetSummary.arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssetSummary.name required")
    if data.get("assetModelId") is not None:
        out["asset_model_id"] = data["assetModelId"]
    else:
        raise DeserializationError("AssetSummary.asset_model_id required")
    if data.get("creationDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["creation_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    else:
        raise DeserializationError("AssetSummary.creation_date required")
    if data.get("lastUpdateDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["last_update_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["lastUpdateDate"]
        )
    else:
        raise DeserializationError("AssetSummary.last_update_date required")
    if data.get("status") is not None:
        import capo_iotsitewise.types.asset_status

        out["status"] = capo_iotsitewise.types.asset_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("AssetSummary.status required")
    if data.get("hierarchies") is not None:
        import capo_iotsitewise.types.asset_hierarchies

        out["hierarchies"] = capo_iotsitewise.types.asset_hierarchies.deserialize_json(
            data["hierarchies"]
        )
    else:
        raise DeserializationError("AssetSummary.hierarchies required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
