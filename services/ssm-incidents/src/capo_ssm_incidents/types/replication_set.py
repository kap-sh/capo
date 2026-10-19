"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ReplicationSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.region_info_map
    import capo_ssm_incidents.types.replication_set_status


class ReplicationSet(TypedDict, closed=True):
    arn: NotRequired["capo_ssm_incidents.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the replication set.</p>"""
    region_map: "capo_ssm_incidents.types.region_info_map.RegionInfoMap"
    """<p>The map between each Amazon Web Services Region in your replication set and the KMS key that's used to encrypt the data in that Region.</p>"""
    status: "capo_ssm_incidents.types.replication_set_status.ReplicationSetStatus"
    """<p>The status of the replication set. If the replication set is still pending, you can't use Incident Manager functionality.</p>"""
    deletion_protected: "bool"
    """<p>Determines if the replication set deletion protection is enabled or not. If deletion protection is enabled, you can't delete the last Amazon Web Services Region in the replication set. </p>"""
    created_time: "datetime.datetime"
    """<p>When the replication set was created.</p>"""
    created_by: "capo_ssm_incidents.types.arn.Arn"
    """<p>Details about who created the replication set.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>When the replication set was last updated.</p>"""
    last_modified_by: "capo_ssm_incidents.types.arn.Arn"
    """<p>Who last modified the replication set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationSet) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    import capo_ssm_incidents.types.region_info_map

    out["regionMap"] = capo_ssm_incidents.types.region_info_map.serialize_json(
        value["region_map"]
    )
    out["status"] = value["status"]
    out["deletionProtected"] = value["deletion_protected"]
    import capo_ssm_incidents.types._prelude.timestamp

    out["createdTime"] = capo_ssm_incidents.types._prelude.timestamp.serialize_json(
        value["created_time"]
    )
    out["createdBy"] = value["created_by"]
    import capo_ssm_incidents.types._prelude.timestamp

    out["lastModifiedTime"] = (
        capo_ssm_incidents.types._prelude.timestamp.serialize_json(
            value["last_modified_time"]
        )
    )
    out["lastModifiedBy"] = value["last_modified_by"]
    return out


def deserialize_json(data: dict) -> ReplicationSet:
    out: ReplicationSet = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("regionMap") is not None:
        import capo_ssm_incidents.types.region_info_map

        out["region_map"] = capo_ssm_incidents.types.region_info_map.deserialize_json(
            data["regionMap"]
        )
    else:
        out["region_map"] = {}
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("deletionProtected") is not None:
        out["deletion_protected"] = data["deletionProtected"]
    else:
        out["deletion_protected"] = False
    if data.get("createdTime") is not None:
        import capo_ssm_incidents.types._prelude.timestamp

        out["created_time"] = (
            capo_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["createdTime"]
            )
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("lastModifiedTime") is not None:
        import capo_ssm_incidents.types._prelude.timestamp

        out["last_modified_time"] = (
            capo_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    else:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastModifiedBy") is not None:
        out["last_modified_by"] = data["lastModifiedBy"]
    else:
        out["last_modified_by"] = ""
    return out
