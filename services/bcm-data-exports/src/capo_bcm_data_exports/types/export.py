"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#Export``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bcm_data_exports.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.arn
    import capo_bcm_data_exports.types.data_query
    import capo_bcm_data_exports.types.destination_configurations
    import capo_bcm_data_exports.types.export_name
    import capo_bcm_data_exports.types.generic_string
    import capo_bcm_data_exports.types.refresh_cadence


class Export(TypedDict, closed=True):
    export_arn: NotRequired["capo_bcm_data_exports.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for this export.</p>"""
    name: "capo_bcm_data_exports.types.export_name.ExportName"
    """<p>The name of this specific data export.</p>"""
    description: NotRequired["capo_bcm_data_exports.types.generic_string.GenericString"]
    """<p>The description for this specific data export.</p>"""
    data_query: "capo_bcm_data_exports.types.data_query.DataQuery"
    """<p>The data query for this specific data export.</p>"""
    destination_configurations: "capo_bcm_data_exports.types.destination_configurations.DestinationConfigurations"
    """<p>The destination configuration for this specific data export.</p>"""
    refresh_cadence: "capo_bcm_data_exports.types.refresh_cadence.RefreshCadence"
    """<p>The cadence for Amazon Web Services to update the export in your S3 bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Export) -> dict:
    out: dict = {}
    if "export_arn" in value:
        out["ExportArn"] = value["export_arn"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_bcm_data_exports.types.data_query

    out["DataQuery"] = capo_bcm_data_exports.types.data_query.serialize_aws_json_1_1(
        value["data_query"]
    )
    import capo_bcm_data_exports.types.destination_configurations

    out["DestinationConfigurations"] = (
        capo_bcm_data_exports.types.destination_configurations.serialize_aws_json_1_1(
            value["destination_configurations"]
        )
    )
    import capo_bcm_data_exports.types.refresh_cadence

    out["RefreshCadence"] = (
        capo_bcm_data_exports.types.refresh_cadence.serialize_aws_json_1_1(
            value["refresh_cadence"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Export:
    out: Export = {}  # type: ignore[typeddict-item]
    if data.get("ExportArn") is not None:
        out["export_arn"] = data["ExportArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DataQuery") is not None:
        import capo_bcm_data_exports.types.data_query

        out["data_query"] = (
            capo_bcm_data_exports.types.data_query.deserialize_aws_json_1_1(
                data["DataQuery"]
            )
        )
    else:
        raise DeserializationError("Export.data_query required")
    if data.get("DestinationConfigurations") is not None:
        import capo_bcm_data_exports.types.destination_configurations

        out["destination_configurations"] = (
            capo_bcm_data_exports.types.destination_configurations.deserialize_aws_json_1_1(
                data["DestinationConfigurations"]
            )
        )
    else:
        raise DeserializationError("Export.destination_configurations required")
    if data.get("RefreshCadence") is not None:
        import capo_bcm_data_exports.types.refresh_cadence

        out["refresh_cadence"] = (
            capo_bcm_data_exports.types.refresh_cadence.deserialize_aws_json_1_1(
                data["RefreshCadence"]
            )
        )
    else:
        raise DeserializationError("Export.refresh_cadence required")
    return out
