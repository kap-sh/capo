"""Generated from Smithy shape ``com.amazonaws.mailmanager#StartArchiveExportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mailmanager.types.archive_filters
    import capo_mailmanager.types.archive_id
    import capo_mailmanager.types.export_destination_configuration
    import capo_mailmanager.types.export_max_results


class StartArchiveExportRequest(TypedDict, closed=True):
    archive_id: "capo_mailmanager.types.archive_id.ArchiveId"
    """<p>The identifier of the archive to export emails from.</p>"""
    filters: NotRequired["capo_mailmanager.types.archive_filters.ArchiveFilters"]
    """<p>Criteria to filter which emails are included in the export.</p>"""
    from_timestamp: "datetime.datetime"
    """<p>The start of the timestamp range to include emails from.</p>"""
    to_timestamp: "datetime.datetime"
    """<p>The end of the timestamp range to include emails from.</p>"""
    max_results: NotRequired[
        "capo_mailmanager.types.export_max_results.ExportMaxResults"
    ]
    """<p>The maximum number of email items to include in the export.</p>"""
    export_destination_configuration: "capo_mailmanager.types.export_destination_configuration.ExportDestinationConfiguration"
    """<p>Details on where to deliver the exported email data.</p>"""
    include_metadata: NotRequired["bool"]
    """<p>Whether to include message metadata as JSON files in the export.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartArchiveExportRequest) -> dict:
    out: dict = {}
    out["ArchiveId"] = value["archive_id"]
    if "filters" in value:
        import capo_mailmanager.types.archive_filters

        out["Filters"] = capo_mailmanager.types.archive_filters.serialize_aws_json_1_0(
            value["filters"]
        )
    import capo_mailmanager.types._prelude.timestamp

    out["FromTimestamp"] = (
        capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
            value["from_timestamp"]
        )
    )
    import capo_mailmanager.types._prelude.timestamp

    out["ToTimestamp"] = (
        capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
            value["to_timestamp"]
        )
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    import capo_mailmanager.types.export_destination_configuration

    out["ExportDestinationConfiguration"] = (
        capo_mailmanager.types.export_destination_configuration.serialize_aws_json_1_0(
            value["export_destination_configuration"]
        )
    )
    if "include_metadata" in value:
        out["IncludeMetadata"] = value["include_metadata"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartArchiveExportRequest:
    out: StartArchiveExportRequest = {}  # type: ignore[typeddict-item]
    if data.get("ArchiveId") is not None:
        out["archive_id"] = data["ArchiveId"]
    else:
        out["archive_id"] = ""
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
    else:
        import datetime

        out["from_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("ToTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["to_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["ToTimestamp"]
            )
        )
    else:
        import datetime

        out["to_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
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
    else:
        out["export_destination_configuration"] = {"$unknown": {"name": ""}}
    if data.get("IncludeMetadata") is not None:
        out["include_metadata"] = data["IncludeMetadata"]
    return out
