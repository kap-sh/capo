"""Generated from Smithy shape ``com.amazonaws.organizations#TerminateResponsibilityTransferRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.responsibility_transfer_id
    import capo_organizations.types.timestamp


class TerminateResponsibilityTransferRequest(TypedDict, closed=True):
    id: "capo_organizations.types.responsibility_transfer_id.ResponsibilityTransferId"
    """<p>ID for the transfer.</p>"""
    end_timestamp: NotRequired["capo_organizations.types.timestamp.Timestamp"]
    """<p>Timestamp when the responsibility transfer is to end.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateResponsibilityTransferRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "end_timestamp" in value:
        import capo_organizations.types.timestamp

        out["EndTimestamp"] = capo_organizations.types.timestamp.serialize_aws_json_1_1(
            value["end_timestamp"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminateResponsibilityTransferRequest:
    out: TerminateResponsibilityTransferRequest = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("EndTimestamp") is not None:
        import capo_organizations.types.timestamp

        out["end_timestamp"] = (
            capo_organizations.types.timestamp.deserialize_aws_json_1_1(
                data["EndTimestamp"]
            )
        )
    return out
