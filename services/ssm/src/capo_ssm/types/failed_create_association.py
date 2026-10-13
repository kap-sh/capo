"""Generated from Smithy shape ``com.amazonaws.ssm#FailedCreateAssociation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.batch_error_message
    import capo_ssm.types.create_association_batch_request_entry
    import capo_ssm.types.fault


class FailedCreateAssociation(TypedDict, closed=True):
    entry: NotRequired[
        "capo_ssm.types.create_association_batch_request_entry.CreateAssociationBatchRequestEntry"
    ]
    """<p>The association.</p>"""
    message: NotRequired["capo_ssm.types.batch_error_message.BatchErrorMessage"]
    """<p>A description of the failure.</p>"""
    fault: NotRequired["capo_ssm.types.fault.Fault"]
    """<p>The source of the failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedCreateAssociation) -> dict:
    out: dict = {}
    if "entry" in value:
        import capo_ssm.types.create_association_batch_request_entry

        out["Entry"] = (
            capo_ssm.types.create_association_batch_request_entry.serialize_aws_json_1_1(
                value["entry"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "fault" in value:
        import capo_ssm.types.fault

        out["Fault"] = capo_ssm.types.fault.serialize_aws_json_1_1(value["fault"])
    return out


def deserialize_aws_json_1_1(data: dict) -> FailedCreateAssociation:
    out: FailedCreateAssociation = {}  # type: ignore[typeddict-item]
    if data.get("Entry") is not None:
        import capo_ssm.types.create_association_batch_request_entry

        out["entry"] = (
            capo_ssm.types.create_association_batch_request_entry.deserialize_aws_json_1_1(
                data["Entry"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Fault") is not None:
        import capo_ssm.types.fault

        out["fault"] = capo_ssm.types.fault.deserialize_aws_json_1_1(data["Fault"])
    return out


def redact_sensitive(value: FailedCreateAssociation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "entry" in value:
        import capo_ssm.types.create_association_batch_request_entry

        out["entry"] = (
            capo_ssm.types.create_association_batch_request_entry.redact_sensitive(
                value["entry"]
            )
        )
    return out
