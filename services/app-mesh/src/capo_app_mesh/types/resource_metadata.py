"""Generated from Smithy shape ``com.amazonaws.appmesh#ResourceMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_app_mesh.types.account_id
    import capo_app_mesh.types.arn


class ResourceMetadata(TypedDict, closed=True):
    arn: "capo_app_mesh.types.arn.Arn"
    """<p>The full Amazon Resource Name (ARN) for the resource.</p>"""
    version: "int"
    """<p>The version of the resource. Resources are created at version 1, and this version is incremented each time that they're updated.</p>"""
    uid: "str"
    """<p>The unique identifier for the resource.</p>"""
    created_at: "datetime.datetime"
    """<p>The Unix epoch timestamp in seconds for when the resource was created.</p>"""
    last_updated_at: "datetime.datetime"
    """<p>The Unix epoch timestamp in seconds for when the resource was last updated.</p>"""
    mesh_owner: "capo_app_mesh.types.account_id.AccountId"
    """<p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>"""
    resource_owner: "capo_app_mesh.types.account_id.AccountId"
    """<p>The Amazon Web Services IAM account ID of the resource owner. If the account ID is not your own, then it's the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceMetadata) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["version"] = value["version"]
    out["uid"] = value["uid"]
    import capo_app_mesh.types._prelude.timestamp

    out["createdAt"] = capo_app_mesh.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_app_mesh.types._prelude.timestamp

    out["lastUpdatedAt"] = capo_app_mesh.types._prelude.timestamp.serialize_json(
        value["last_updated_at"]
    )
    out["meshOwner"] = value["mesh_owner"]
    out["resourceOwner"] = value["resource_owner"]
    return out


def deserialize_json(data: dict) -> ResourceMetadata:
    out: ResourceMetadata = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ResourceMetadata.arn required")
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("ResourceMetadata.version required")
    if data.get("uid") is not None:
        out["uid"] = data["uid"]
    else:
        raise DeserializationError("ResourceMetadata.uid required")
    if data.get("createdAt") is not None:
        import capo_app_mesh.types._prelude.timestamp

        out["created_at"] = capo_app_mesh.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("ResourceMetadata.created_at required")
    if data.get("lastUpdatedAt") is not None:
        import capo_app_mesh.types._prelude.timestamp

        out["last_updated_at"] = (
            capo_app_mesh.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError("ResourceMetadata.last_updated_at required")
    if data.get("meshOwner") is not None:
        out["mesh_owner"] = data["meshOwner"]
    else:
        raise DeserializationError("ResourceMetadata.mesh_owner required")
    if data.get("resourceOwner") is not None:
        out["resource_owner"] = data["resourceOwner"]
    else:
        raise DeserializationError("ResourceMetadata.resource_owner required")
    return out
