"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#UpdateExportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bcm_data_exports.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.arn
    import capo_bcm_data_exports.types.export


class UpdateExportRequest(TypedDict, closed=True):
    export_arn: "capo_bcm_data_exports.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for this export.</p>"""
    export: "capo_bcm_data_exports.types.export.Export"
    """<p>The name and query details for the export.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateExportRequest) -> dict:
    out: dict = {}
    out["ExportArn"] = value["export_arn"]
    import capo_bcm_data_exports.types.export

    out["Export"] = capo_bcm_data_exports.types.export.serialize_aws_json_1_1(
        value["export"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateExportRequest:
    out: UpdateExportRequest = {}  # type: ignore[typeddict-item]
    if data.get("ExportArn") is not None:
        out["export_arn"] = data["ExportArn"]
    else:
        out["export_arn"] = ""
    if data.get("Export") is not None:
        import capo_bcm_data_exports.types.export

        out["export"] = capo_bcm_data_exports.types.export.deserialize_aws_json_1_1(
            data["Export"]
        )
    else:
        raise DeserializationError("UpdateExportRequest.export required")
    return out
