"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DeleteDbInstanceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.db_instance_identifier


class DeleteDbInstanceInput(TypedDict, closed=True):
    identifier: (
        "capo_timestream_influxdb.types.db_instance_identifier.DbInstanceIdentifier"
    )
    """<p>The id of the DB instance.</p>"""
    retain_automated_backups: NotRequired["bool"]
    """<p>Specifies whether to retain automated backups after the DB instance is deleted. If set to true, automated backups are not deleted and can be restored later.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteDbInstanceInput) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    if "retain_automated_backups" in value:
        out["retainAutomatedBackups"] = value["retain_automated_backups"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteDbInstanceInput:
    out: DeleteDbInstanceInput = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    if data.get("retainAutomatedBackups") is not None:
        out["retain_automated_backups"] = data["retainAutomatedBackups"]
    return out
