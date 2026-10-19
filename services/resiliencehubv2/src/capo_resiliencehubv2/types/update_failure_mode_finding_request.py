"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdateFailureModeFindingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.finding_status
    import capo_resiliencehubv2.types.uuid


class UpdateFailureModeFindingRequest(TypedDict, closed=True):
    finding_id: "capo_resiliencehubv2.types.uuid.Uuid"
    """<p>The identifier of the finding to update.</p>"""
    status: "capo_resiliencehubv2.types.finding_status.FindingStatus"
    """<p>The new status for the finding.</p>"""
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    comment: NotRequired["str"]
    """<p>A comment about the finding update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFailureModeFindingRequest) -> dict:
    out: dict = {}
    out["findingId"] = value["finding_id"]
    import capo_resiliencehubv2.types.finding_status

    out["status"] = capo_resiliencehubv2.types.finding_status.serialize_json(
        value["status"]
    )
    out["serviceArn"] = value["service_arn"]
    if "comment" in value:
        out["comment"] = value["comment"]
    return out


def deserialize_json(data: dict) -> UpdateFailureModeFindingRequest:
    out: UpdateFailureModeFindingRequest = {}  # type: ignore[typeddict-item]
    if data.get("findingId") is not None:
        out["finding_id"] = data["findingId"]
    else:
        out["finding_id"] = ""
    if data.get("status") is not None:
        import capo_resiliencehubv2.types.finding_status

        out["status"] = capo_resiliencehubv2.types.finding_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_resiliencehubv2.types.finding_status.FindingStatus", ""
        )
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        out["service_arn"] = ""
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    return out
