"""Generated from Smithy shape ``com.amazonaws.simpledbv2#ExportSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_simpledbv2.types.domain_name
    import capo_simpledbv2.types.export_arn
    import capo_simpledbv2.types.export_status
    import capo_simpledbv2.types.requested_at


class ExportSummary(TypedDict, closed=True):
    export_arn: "capo_simpledbv2.types.export_arn.ExportArn"
    """Unique ARN identifier of the export."""
    export_status: "capo_simpledbv2.types.export_status.ExportStatus"
    """The current state of the export. Current possible values include : PENDING - export request received, IN_PROGRESS - export is being processed, SUCCEEDED - export completed successfully, and FAILED - export encountered an error."""
    requested_at: "capo_simpledbv2.types.requested_at.RequestedAt"
    """Timestamp when the export request was received by the service"""
    domain_name: "capo_simpledbv2.types.domain_name.DomainName"
    """The name of the domain for which the export was created."""


# --- restJson1 ser/de ---
def serialize_json(value: ExportSummary) -> dict:
    out: dict = {}
    out["exportArn"] = value["export_arn"]
    import capo_simpledbv2.types.export_status

    out["exportStatus"] = capo_simpledbv2.types.export_status.serialize_json(
        value["export_status"]
    )
    import capo_simpledbv2.types.requested_at

    out["requestedAt"] = capo_simpledbv2.types.requested_at.serialize_json(
        value["requested_at"]
    )
    out["domainName"] = value["domain_name"]
    return out


def deserialize_json(data: dict) -> ExportSummary:
    out: ExportSummary = {}  # type: ignore[typeddict-item]
    if data.get("exportArn") is not None:
        out["export_arn"] = data["exportArn"]
    else:
        out["export_arn"] = ""
    if data.get("exportStatus") is not None:
        import capo_simpledbv2.types.export_status

        out["export_status"] = capo_simpledbv2.types.export_status.deserialize_json(
            data["exportStatus"]
        )
    else:
        import typing

        out["export_status"] = typing.cast(
            "capo_simpledbv2.types.export_status.ExportStatus", ""
        )
    if data.get("requestedAt") is not None:
        import capo_simpledbv2.types.requested_at

        out["requested_at"] = capo_simpledbv2.types.requested_at.deserialize_json(
            data["requestedAt"]
        )
    else:
        import datetime

        out["requested_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    else:
        out["domain_name"] = ""
    return out
