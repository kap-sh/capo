"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#GetExportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.arn


class GetExportRequest(TypedDict, closed=True):
    export_arn: "capo_bcm_data_exports.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for this export.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetExportRequest) -> dict:
    out: dict = {}
    out["ExportArn"] = value["export_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetExportRequest:
    out: GetExportRequest = {}  # type: ignore[typeddict-item]
    if data.get("ExportArn") is not None:
        out["export_arn"] = data["ExportArn"]
    else:
        out["export_arn"] = ""
    return out
