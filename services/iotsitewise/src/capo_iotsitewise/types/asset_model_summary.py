"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.asset_model_status
    import capo_iotsitewise.types.asset_model_type
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.external_id
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name
    import capo_iotsitewise.types.timestamp
    import capo_iotsitewise.types.version


class AssetModelSummary(TypedDict, closed=True):
    id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset model (used with IoT SiteWise API operations).</p>"""
    external_id: NotRequired["capo_iotsitewise.types.external_id.ExternalId"]
    """<p>The external ID of the asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the asset model, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:asset-model/${AssetModelId}</code> </p>"""
    name: "capo_iotsitewise.types.name.Name"
    """<p>The name of the asset model.</p>"""
    asset_model_type: NotRequired[
        "capo_iotsitewise.types.asset_model_type.AssetModelType"
    ]
    """<p>The type of asset model.</p> <ul> <li> <p> <b>ASSET_MODEL</b> – (default) An asset model that you can use to create assets. Can't be included as a component in another asset model.</p> </li> <li> <p> <b>COMPONENT_MODEL</b> – A reusable component that you can include in the composite models of other asset models. You can't create assets directly from this type of asset model. </p> </li> </ul>"""
    description: "capo_iotsitewise.types.description.Description"
    """<p>The asset model description.</p>"""
    creation_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the asset model was created, in Unix epoch time.</p>"""
    last_update_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the asset model was last updated, in Unix epoch time.</p>"""
    status: "capo_iotsitewise.types.asset_model_status.AssetModelStatus"
    """<p>The current status of the asset model.</p>"""
    version: NotRequired["capo_iotsitewise.types.version.Version"]
    """<p>The version number of the asset model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "asset_model_type" in value:
        import capo_iotsitewise.types.asset_model_type

        out["assetModelType"] = capo_iotsitewise.types.asset_model_type.serialize_json(
            value["asset_model_type"]
        )
    out["description"] = value["description"]
    import capo_iotsitewise.types.timestamp

    out["creationDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["creation_date"]
    )
    import capo_iotsitewise.types.timestamp

    out["lastUpdateDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["last_update_date"]
    )
    import capo_iotsitewise.types.asset_model_status

    out["status"] = capo_iotsitewise.types.asset_model_status.serialize_json(
        value["status"]
    )
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> AssetModelSummary:
    out: AssetModelSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AssetModelSummary.id required")
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("AssetModelSummary.arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssetModelSummary.name required")
    if data.get("assetModelType") is not None:
        import capo_iotsitewise.types.asset_model_type

        out["asset_model_type"] = (
            capo_iotsitewise.types.asset_model_type.deserialize_json(
                data["assetModelType"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        raise DeserializationError("AssetModelSummary.description required")
    if data.get("creationDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["creation_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    else:
        raise DeserializationError("AssetModelSummary.creation_date required")
    if data.get("lastUpdateDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["last_update_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["lastUpdateDate"]
        )
    else:
        raise DeserializationError("AssetModelSummary.last_update_date required")
    if data.get("status") is not None:
        import capo_iotsitewise.types.asset_model_status

        out["status"] = capo_iotsitewise.types.asset_model_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("AssetModelSummary.status required")
    if data.get("version") is not None:
        out["version"] = data["version"]
    return out
