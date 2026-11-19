"""Generated from Smithy shape ``com.amazonaws.codeconnections#GetResourceSyncStatusOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeconnections.types.resource_sync_attempt
    import capo_codeconnections.types.revision


class GetResourceSyncStatusOutput(TypedDict, closed=True):
    desired_state: NotRequired["capo_codeconnections.types.revision.Revision"]
    """<p>The desired state of the Amazon Web Services resource for the sync status with the Git repository.</p>"""
    latest_successful_sync: NotRequired[
        "capo_codeconnections.types.resource_sync_attempt.ResourceSyncAttempt"
    ]
    """<p>The latest successful sync for the sync status with the Git repository.</p>"""
    latest_sync: "capo_codeconnections.types.resource_sync_attempt.ResourceSyncAttempt"
    """<p>The latest sync for the sync status with the Git repository, whether successful or not.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetResourceSyncStatusOutput) -> dict:
    out: dict = {}
    if "desired_state" in value:
        import capo_codeconnections.types.revision

        out["DesiredState"] = (
            capo_codeconnections.types.revision.serialize_aws_json_1_0(
                value["desired_state"]
            )
        )
    if "latest_successful_sync" in value:
        import capo_codeconnections.types.resource_sync_attempt

        out["LatestSuccessfulSync"] = (
            capo_codeconnections.types.resource_sync_attempt.serialize_aws_json_1_0(
                value["latest_successful_sync"]
            )
        )
    import capo_codeconnections.types.resource_sync_attempt

    out["LatestSync"] = (
        capo_codeconnections.types.resource_sync_attempt.serialize_aws_json_1_0(
            value["latest_sync"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetResourceSyncStatusOutput:
    out: GetResourceSyncStatusOutput = {}  # type: ignore[typeddict-item]
    if data.get("DesiredState") is not None:
        import capo_codeconnections.types.revision

        out["desired_state"] = (
            capo_codeconnections.types.revision.deserialize_aws_json_1_0(
                data["DesiredState"]
            )
        )
    if data.get("LatestSuccessfulSync") is not None:
        import capo_codeconnections.types.resource_sync_attempt

        out["latest_successful_sync"] = (
            capo_codeconnections.types.resource_sync_attempt.deserialize_aws_json_1_0(
                data["LatestSuccessfulSync"]
            )
        )
    if data.get("LatestSync") is not None:
        import capo_codeconnections.types.resource_sync_attempt

        out["latest_sync"] = (
            capo_codeconnections.types.resource_sync_attempt.deserialize_aws_json_1_0(
                data["LatestSync"]
            )
        )
    else:
        raise DeserializationError("GetResourceSyncStatusOutput.latest_sync required")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetResourceSyncStatusOutput) -> dict:
    out: dict = {}
    if "desired_state" in value:
        import capo_codeconnections.types.revision

        out["DesiredState"] = capo_codeconnections.types.revision.serialize_cbor(
            value["desired_state"]
        )
    if "latest_successful_sync" in value:
        import capo_codeconnections.types.resource_sync_attempt

        out["LatestSuccessfulSync"] = (
            capo_codeconnections.types.resource_sync_attempt.serialize_cbor(
                value["latest_successful_sync"]
            )
        )
    import capo_codeconnections.types.resource_sync_attempt

    out["LatestSync"] = capo_codeconnections.types.resource_sync_attempt.serialize_cbor(
        value["latest_sync"]
    )
    return out


def deserialize_cbor(data: dict) -> GetResourceSyncStatusOutput:
    out: GetResourceSyncStatusOutput = {}  # type: ignore[typeddict-item]
    if data.get("DesiredState") is not None:
        import capo_codeconnections.types.revision

        out["desired_state"] = capo_codeconnections.types.revision.deserialize_cbor(
            data["DesiredState"]
        )
    if data.get("LatestSuccessfulSync") is not None:
        import capo_codeconnections.types.resource_sync_attempt

        out["latest_successful_sync"] = (
            capo_codeconnections.types.resource_sync_attempt.deserialize_cbor(
                data["LatestSuccessfulSync"]
            )
        )
    if data.get("LatestSync") is not None:
        import capo_codeconnections.types.resource_sync_attempt

        out["latest_sync"] = (
            capo_codeconnections.types.resource_sync_attempt.deserialize_cbor(
                data["LatestSync"]
            )
        )
    else:
        raise DeserializationError("GetResourceSyncStatusOutput.latest_sync required")
    return out
