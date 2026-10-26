"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#RdsDbClusterSnapshotAttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError, SerializationError
from capo_accessanalyzer.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_accessanalyzer.types.rds_db_cluster_snapshot_account_ids_list


class _RdsDbClusterSnapshotAttributeValue_accountIds(TypedDict, closed=True):
    accountIds: "capo_accessanalyzer.types.rds_db_cluster_snapshot_account_ids_list.RdsDbClusterSnapshotAccountIdsList"


RdsDbClusterSnapshotAttributeValue: TypeAlias = (
    _RdsDbClusterSnapshotAttributeValue_accountIds | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RdsDbClusterSnapshotAttributeValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RdsDbClusterSnapshotAttributeValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "accountIds" in value:
        import capo_accessanalyzer.types.rds_db_cluster_snapshot_account_ids_list

        return {
            "accountIds": capo_accessanalyzer.types.rds_db_cluster_snapshot_account_ids_list.serialize_json(
                value["accountIds"]
            )
        }
    else:
        raise SerializationError(
            "RdsDbClusterSnapshotAttributeValue: no variant present"
        )


def deserialize_json(data: dict) -> RdsDbClusterSnapshotAttributeValue:
    if data.get("accountIds") is not None:
        import capo_accessanalyzer.types.rds_db_cluster_snapshot_account_ids_list

        return {
            "accountIds": capo_accessanalyzer.types.rds_db_cluster_snapshot_account_ids_list.deserialize_json(
                data["accountIds"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "RdsDbClusterSnapshotAttributeValue: no recognized variant key"
        )
