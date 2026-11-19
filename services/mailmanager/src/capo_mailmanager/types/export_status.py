"""Generated from Smithy shape ``com.amazonaws.mailmanager#ExportStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mailmanager.types.error_message
    import capo_mailmanager.types.export_state


class ExportStatus(TypedDict, closed=True):
    submission_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the export job was submitted.</p>"""
    completion_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the export job completed (if finished).</p>"""
    state: NotRequired["capo_mailmanager.types.export_state.ExportState"]
    """<p>The current state of the export job.</p>"""
    error_message: NotRequired["capo_mailmanager.types.error_message.ErrorMessage"]
    """<p>An error message if the export job failed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportStatus) -> dict:
    out: dict = {}
    if "submission_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["SubmissionTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["submission_timestamp"]
            )
        )
    if "completion_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["CompletionTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["completion_timestamp"]
            )
        )
    if "state" in value:
        import capo_mailmanager.types.export_state

        out["State"] = capo_mailmanager.types.export_state.serialize_aws_json_1_0(
            value["state"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportStatus:
    out: ExportStatus = {}  # type: ignore[typeddict-item]
    if data.get("SubmissionTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["submission_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["SubmissionTimestamp"]
            )
        )
    if data.get("CompletionTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["completion_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CompletionTimestamp"]
            )
        )
    if data.get("State") is not None:
        import capo_mailmanager.types.export_state

        out["state"] = capo_mailmanager.types.export_state.deserialize_aws_json_1_0(
            data["State"]
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExportStatus) -> dict:
    out: dict = {}
    if "submission_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["SubmissionTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_cbor(
                value["submission_timestamp"]
            )
        )
    if "completion_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["CompletionTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_cbor(
                value["completion_timestamp"]
            )
        )
    if "state" in value:
        import capo_mailmanager.types.export_state

        out["State"] = capo_mailmanager.types.export_state.serialize_cbor(
            value["state"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_cbor(data: dict) -> ExportStatus:
    out: ExportStatus = {}  # type: ignore[typeddict-item]
    if data.get("SubmissionTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["submission_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_cbor(
                data["SubmissionTimestamp"]
            )
        )
    if data.get("CompletionTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["completion_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_cbor(
                data["CompletionTimestamp"]
            )
        )
    if data.get("State") is not None:
        import capo_mailmanager.types.export_state

        out["state"] = capo_mailmanager.types.export_state.deserialize_cbor(
            data["State"]
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
