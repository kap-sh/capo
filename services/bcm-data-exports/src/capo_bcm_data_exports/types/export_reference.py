"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ExportReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bcm_data_exports.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.arn
    import capo_bcm_data_exports.types.export_name
    import capo_bcm_data_exports.types.export_status


class ExportReference(TypedDict, closed=True):
    export_arn: "capo_bcm_data_exports.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for this export.</p>"""
    export_name: "capo_bcm_data_exports.types.export_name.ExportName"
    """<p>The name of this specific data export.</p>"""
    export_status: "capo_bcm_data_exports.types.export_status.ExportStatus"
    """<p>The status of this specific data export.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportReference) -> dict:
    out: dict = {}
    out["ExportArn"] = value["export_arn"]
    out["ExportName"] = value["export_name"]
    import capo_bcm_data_exports.types.export_status

    out["ExportStatus"] = (
        capo_bcm_data_exports.types.export_status.serialize_aws_json_1_1(
            value["export_status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportReference:
    out: ExportReference = {}  # type: ignore[typeddict-item]
    if data.get("ExportArn") is not None:
        out["export_arn"] = data["ExportArn"]
    else:
        out["export_arn"] = ""
    if data.get("ExportName") is not None:
        out["export_name"] = data["ExportName"]
    else:
        out["export_name"] = ""
    if data.get("ExportStatus") is not None:
        import capo_bcm_data_exports.types.export_status

        out["export_status"] = (
            capo_bcm_data_exports.types.export_status.deserialize_aws_json_1_1(
                data["ExportStatus"]
            )
        )
    else:
        raise DeserializationError("ExportReference.export_status required")
    return out
