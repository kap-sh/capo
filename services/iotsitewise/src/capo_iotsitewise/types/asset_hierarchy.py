"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetHierarchy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.external_id
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name


class AssetHierarchy(TypedDict, closed=True):
    id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the hierarchy. This ID is a <code>hierarchyId</code>.</p>"""
    external_id: NotRequired["capo_iotsitewise.types.external_id.ExternalId"]
    """<p>The external ID of the hierarchy, if it has one. When you update an asset hierarchy, you may assign an external ID if it doesn't already have one. You can't change the external ID of an asset hierarchy that already has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    name: "capo_iotsitewise.types.name.Name"
    """<p>The hierarchy name provided in the <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html">CreateAssetModel</a> or <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html">UpdateAssetModel</a> API operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetHierarchy) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AssetHierarchy:
    out: AssetHierarchy = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssetHierarchy.name required")
    return out
