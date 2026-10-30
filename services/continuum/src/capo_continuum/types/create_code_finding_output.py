"""Generated from Smithy shape ``com.amazonaws.continuum#CreateCodeFindingOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_continuum.types.finding_arn
    import capo_continuum.types.finding_id
    import capo_continuum.types.finding_status
    import capo_continuum.types.finding_title


class CreateCodeFindingOutput(TypedDict, closed=True):
    finding_id: "capo_continuum.types.finding_id.FindingId"
    """The unique identifier assigned to the finding."""
    finding_arn: "capo_continuum.types.finding_arn.FindingArn"
    """The ARN of the ingested finding."""
    title: "capo_continuum.types.finding_title.FindingTitle"
    """The title extracted from the submitted document. Always populated at ingestion."""
    status: "capo_continuum.types.finding_status.FindingStatus"
    """The finding's current lifecycle status -- SUBMITTED for a newly ingested finding, or the finding's present status when an idempotent retry replays an already-processed finding."""
    created_at: "datetime.datetime"
    """The timestamp when the finding was ingested."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCodeFindingOutput) -> dict:
    out: dict = {}
    out["findingId"] = value["finding_id"]
    out["findingArn"] = value["finding_arn"]
    out["title"] = value["title"]
    import capo_continuum.types.finding_status

    out["status"] = capo_continuum.types.finding_status.serialize_json(value["status"])
    import capo_continuum._protocol.serialize

    out["createdAt"] = capo_continuum._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> CreateCodeFindingOutput:
    out: CreateCodeFindingOutput = {}  # type: ignore[typeddict-item]
    if data.get("findingId") is not None:
        out["finding_id"] = data["findingId"]
    else:
        out["finding_id"] = ""
    if data.get("findingArn") is not None:
        out["finding_arn"] = data["findingArn"]
    else:
        out["finding_arn"] = ""
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("status") is not None:
        import capo_continuum.types.finding_status

        out["status"] = capo_continuum.types.finding_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_continuum.types.finding_status.FindingStatus", ""
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
