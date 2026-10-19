"""Generated from Smithy shape ``com.amazonaws.datazone#SelfGrantStatusDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.self_grant_status


class SelfGrantStatusDetail(TypedDict, closed=True):
    database_name: "str"
    """<p>The name of the database used for the data source.</p>"""
    schema_name: NotRequired["str"]
    """<p>The name of the schema used in the data source.</p>"""
    status: "capo_datazone.types.self_grant_status.SelfGrantStatus"
    """<p>The self granting status of the data source.</p>"""
    failure_cause: NotRequired["str"]
    """<p>The reason for why the operation failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelfGrantStatusDetail) -> dict:
    out: dict = {}
    out["databaseName"] = value["database_name"]
    if "schema_name" in value:
        out["schemaName"] = value["schema_name"]
    import capo_datazone.types.self_grant_status

    out["status"] = capo_datazone.types.self_grant_status.serialize_json(
        value["status"]
    )
    if "failure_cause" in value:
        out["failureCause"] = value["failure_cause"]
    return out


def deserialize_json(data: dict) -> SelfGrantStatusDetail:
    out: SelfGrantStatusDetail = {}  # type: ignore[typeddict-item]
    if data.get("databaseName") is not None:
        out["database_name"] = data["databaseName"]
    else:
        out["database_name"] = ""
    if data.get("schemaName") is not None:
        out["schema_name"] = data["schemaName"]
    if data.get("status") is not None:
        import capo_datazone.types.self_grant_status

        out["status"] = capo_datazone.types.self_grant_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_datazone.types.self_grant_status.SelfGrantStatus", ""
        )
    if data.get("failureCause") is not None:
        out["failure_cause"] = data["failureCause"]
    return out
