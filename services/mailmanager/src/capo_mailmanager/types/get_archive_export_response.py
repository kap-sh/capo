"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetArchiveExportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mailmanager.types.archive_filters
    import capo_mailmanager.types.archive_id
    import capo_mailmanager.types.export_destination_configuration
    import capo_mailmanager.types.export_max_results
    import capo_mailmanager.types.export_status


class GetArchiveExportResponse(TypedDict, closed=True):
    archive_id: NotRequired["capo_mailmanager.types.archive_id.ArchiveId"]
    """<p>The identifier of the archive the email export was performed from.</p>"""
    filters: NotRequired["capo_mailmanager.types.archive_filters.ArchiveFilters"]
    """<p>The criteria used to filter emails included in the export.</p>"""
    from_timestamp: NotRequired["datetime.datetime"]
    """<p>The start of the timestamp range the exported emails cover.</p>"""
    to_timestamp: NotRequired["datetime.datetime"]
    """<p>The end of the date range the exported emails cover.</p>"""
    max_results: NotRequired[
        "capo_mailmanager.types.export_max_results.ExportMaxResults"
    ]
    """<p>The maximum number of email items included in the export.</p>"""
    export_destination_configuration: NotRequired[
        "capo_mailmanager.types.export_destination_configuration.ExportDestinationConfiguration"
    ]
    """<p>Where the exported emails are being delivered.</p>"""
    status: NotRequired["capo_mailmanager.types.export_status.ExportStatus"]
    """<p>The current status of the export job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetArchiveExportResponse) -> dict:
    out: dict = {}
    if "archive_id" in value:
        out["ArchiveId"] = value["archive_id"]
    if "filters" in value:
        import capo_mailmanager.types.archive_filters

        out["Filters"] = capo_mailmanager.types.archive_filters.serialize_aws_json_1_0(
            value["filters"]
        )
    if "from_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["FromTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["from_timestamp"]
            )
        )
    if "to_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["ToTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["to_timestamp"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "export_destination_configuration" in value:
        import capo_mailmanager.types.export_destination_configuration

        out["ExportDestinationConfiguration"] = (
            capo_mailmanager.types.export_destination_configuration.serialize_aws_json_1_0(
                value["export_destination_configuration"]
            )
        )
    if "status" in value:
        import capo_mailmanager.types.export_status

        out["Status"] = capo_mailmanager.types.export_status.serialize_aws_json_1_0(
            value["status"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetArchiveExportResponse:
    out: GetArchiveExportResponse = {}  # type: ignore[typeddict-item]
    if data.get("ArchiveId") is not None:
        out["archive_id"] = data["ArchiveId"]
    if data.get("Filters") is not None:
        import capo_mailmanager.types.archive_filters

        out["filters"] = (
            capo_mailmanager.types.archive_filters.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if data.get("FromTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["from_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["FromTimestamp"]
            )
        )
    if data.get("ToTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["to_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["ToTimestamp"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("ExportDestinationConfiguration") is not None:
        import capo_mailmanager.types.export_destination_configuration

        out["export_destination_configuration"] = (
            capo_mailmanager.types.export_destination_configuration.deserialize_aws_json_1_0(
                data["ExportDestinationConfiguration"]
            )
        )
    if data.get("Status") is not None:
        import capo_mailmanager.types.export_status

        out["status"] = capo_mailmanager.types.export_status.deserialize_aws_json_1_0(
            data["Status"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetArchiveExportResponse) -> dict:
    out: dict = {}
    if "archive_id" in value:
        out["ArchiveId"] = value["archive_id"]
    if "filters" in value:
        import capo_mailmanager.types.archive_filters

        out["Filters"] = capo_mailmanager.types.archive_filters.serialize_cbor(
            value["filters"]
        )
    if "from_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["FromTimestamp"] = capo_mailmanager.types._prelude.timestamp.serialize_cbor(
            value["from_timestamp"]
        )
    if "to_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["ToTimestamp"] = capo_mailmanager.types._prelude.timestamp.serialize_cbor(
            value["to_timestamp"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "export_destination_configuration" in value:
        import capo_mailmanager.types.export_destination_configuration

        out["ExportDestinationConfiguration"] = (
            capo_mailmanager.types.export_destination_configuration.serialize_cbor(
                value["export_destination_configuration"]
            )
        )
    if "status" in value:
        import capo_mailmanager.types.export_status

        out["Status"] = capo_mailmanager.types.export_status.serialize_cbor(
            value["status"]
        )
    return out


def deserialize_cbor(data: dict) -> GetArchiveExportResponse:
    out: GetArchiveExportResponse = {}  # type: ignore[typeddict-item]
    if data.get("ArchiveId") is not None:
        out["archive_id"] = data["ArchiveId"]
    if data.get("Filters") is not None:
        import capo_mailmanager.types.archive_filters

        out["filters"] = capo_mailmanager.types.archive_filters.deserialize_cbor(
            data["Filters"]
        )
    if data.get("FromTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["from_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_cbor(
                data["FromTimestamp"]
            )
        )
    if data.get("ToTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["to_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_cbor(
                data["ToTimestamp"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("ExportDestinationConfiguration") is not None:
        import capo_mailmanager.types.export_destination_configuration

        out["export_destination_configuration"] = (
            capo_mailmanager.types.export_destination_configuration.deserialize_cbor(
                data["ExportDestinationConfiguration"]
            )
        )
    if data.get("Status") is not None:
        import capo_mailmanager.types.export_status

        out["status"] = capo_mailmanager.types.export_status.deserialize_cbor(
            data["Status"]
        )
    return out
