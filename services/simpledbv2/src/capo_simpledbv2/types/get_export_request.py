"""Generated from Smithy shape ``com.amazonaws.simpledbv2#GetExportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_simpledbv2.types.export_arn


class GetExportRequest(TypedDict, closed=True):
    export_arn: "capo_simpledbv2.types.export_arn.ExportArn"
    """Unique ARN identifier of the export."""


# --- restJson1 ser/de ---
def serialize_json(value: GetExportRequest) -> dict:
    out: dict = {}
    out["exportArn"] = value["export_arn"]
    return out


def deserialize_json(data: dict) -> GetExportRequest:
    out: GetExportRequest = {}  # type: ignore[typeddict-item]
    if data.get("exportArn") is not None:
        out["export_arn"] = data["exportArn"]
    else:
        out["export_arn"] = ""
    return out
