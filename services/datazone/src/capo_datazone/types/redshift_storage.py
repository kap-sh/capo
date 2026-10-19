"""Generated from Smithy shape ``com.amazonaws.datazone#RedshiftStorage``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.redshift_cluster_storage
    import capo_datazone.types.redshift_serverless_storage


class _RedshiftStorage_redshiftClusterSource(TypedDict, closed=True):
    redshiftClusterSource: (
        "capo_datazone.types.redshift_cluster_storage.RedshiftClusterStorage"
    )


class _RedshiftStorage_redshiftServerlessSource(TypedDict, closed=True):
    redshiftServerlessSource: (
        "capo_datazone.types.redshift_serverless_storage.RedshiftServerlessStorage"
    )


RedshiftStorage: TypeAlias = (
    _RedshiftStorage_redshiftClusterSource
    | _RedshiftStorage_redshiftServerlessSource
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftStorage) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"RedshiftStorage: cannot serialize unknown variant {value.name!r}"
        )
    elif "redshiftClusterSource" in value:
        import capo_datazone.types.redshift_cluster_storage

        return {
            "redshiftClusterSource": capo_datazone.types.redshift_cluster_storage.serialize_json(
                value["redshiftClusterSource"]
            )
        }
    elif "redshiftServerlessSource" in value:
        import capo_datazone.types.redshift_serverless_storage

        return {
            "redshiftServerlessSource": capo_datazone.types.redshift_serverless_storage.serialize_json(
                value["redshiftServerlessSource"]
            )
        }
    else:
        raise SerializationError("RedshiftStorage: no variant present")


def deserialize_json(data: dict) -> RedshiftStorage:
    if data.get("redshiftClusterSource") is not None:
        import capo_datazone.types.redshift_cluster_storage

        return {
            "redshiftClusterSource": capo_datazone.types.redshift_cluster_storage.deserialize_json(
                data["redshiftClusterSource"]
            )
        }
    elif data.get("redshiftServerlessSource") is not None:
        import capo_datazone.types.redshift_serverless_storage

        return {
            "redshiftServerlessSource": capo_datazone.types.redshift_serverless_storage.deserialize_json(
                data["redshiftServerlessSource"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("RedshiftStorage: no recognized variant key")
