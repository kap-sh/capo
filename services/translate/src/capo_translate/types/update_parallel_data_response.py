"""Generated from Smithy shape ``com.amazonaws.translate#UpdateParallelDataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.parallel_data_status
    import capo_translate.types.resource_name
    import capo_translate.types.timestamp


class UpdateParallelDataResponse(TypedDict, closed=True):
    name: NotRequired["capo_translate.types.resource_name.ResourceName"]
    """<p>The name of the parallel data resource being updated.</p>"""
    status: NotRequired["capo_translate.types.parallel_data_status.ParallelDataStatus"]
    """<p>The status of the parallel data resource that you are attempting to update. Your update request is accepted only if this status is either <code>ACTIVE</code> or <code>FAILED</code>.</p>"""
    latest_update_attempt_status: NotRequired[
        "capo_translate.types.parallel_data_status.ParallelDataStatus"
    ]
    """<p>The status of the parallel data update attempt. When the updated parallel data resource is ready for you to use, the status is <code>ACTIVE</code>.</p>"""
    latest_update_attempt_at: NotRequired["capo_translate.types.timestamp.Timestamp"]
    """<p>The time that the most recent update was attempted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateParallelDataResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_translate.types.parallel_data_status

        out["Status"] = (
            capo_translate.types.parallel_data_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "latest_update_attempt_status" in value:
        import capo_translate.types.parallel_data_status

        out["LatestUpdateAttemptStatus"] = (
            capo_translate.types.parallel_data_status.serialize_aws_json_1_1(
                value["latest_update_attempt_status"]
            )
        )
    if "latest_update_attempt_at" in value:
        import capo_translate.types.timestamp

        out["LatestUpdateAttemptAt"] = (
            capo_translate.types.timestamp.serialize_aws_json_1_1(
                value["latest_update_attempt_at"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateParallelDataResponse:
    out: UpdateParallelDataResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        import capo_translate.types.parallel_data_status

        out["status"] = (
            capo_translate.types.parallel_data_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("LatestUpdateAttemptStatus") is not None:
        import capo_translate.types.parallel_data_status

        out["latest_update_attempt_status"] = (
            capo_translate.types.parallel_data_status.deserialize_aws_json_1_1(
                data["LatestUpdateAttemptStatus"]
            )
        )
    if data.get("LatestUpdateAttemptAt") is not None:
        import capo_translate.types.timestamp

        out["latest_update_attempt_at"] = (
            capo_translate.types.timestamp.deserialize_aws_json_1_1(
                data["LatestUpdateAttemptAt"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateParallelDataResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_translate.types.parallel_data_status

        out["Status"] = capo_translate.types.parallel_data_status.serialize_cbor(
            value["status"]
        )
    if "latest_update_attempt_status" in value:
        import capo_translate.types.parallel_data_status

        out["LatestUpdateAttemptStatus"] = (
            capo_translate.types.parallel_data_status.serialize_cbor(
                value["latest_update_attempt_status"]
            )
        )
    if "latest_update_attempt_at" in value:
        import capo_translate.types.timestamp

        out["LatestUpdateAttemptAt"] = capo_translate.types.timestamp.serialize_cbor(
            value["latest_update_attempt_at"]
        )
    return out


def deserialize_cbor(data: dict) -> UpdateParallelDataResponse:
    out: UpdateParallelDataResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        import capo_translate.types.parallel_data_status

        out["status"] = capo_translate.types.parallel_data_status.deserialize_cbor(
            data["Status"]
        )
    if data.get("LatestUpdateAttemptStatus") is not None:
        import capo_translate.types.parallel_data_status

        out["latest_update_attempt_status"] = (
            capo_translate.types.parallel_data_status.deserialize_cbor(
                data["LatestUpdateAttemptStatus"]
            )
        )
    if data.get("LatestUpdateAttemptAt") is not None:
        import capo_translate.types.timestamp

        out["latest_update_attempt_at"] = (
            capo_translate.types.timestamp.deserialize_cbor(
                data["LatestUpdateAttemptAt"]
            )
        )
    return out
