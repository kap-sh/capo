"""Generated from Smithy shape ``com.amazonaws.codeconnections#GetRepositorySyncStatusOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeconnections.types.repository_sync_attempt


class GetRepositorySyncStatusOutput(TypedDict, closed=True):
    latest_sync: (
        "capo_codeconnections.types.repository_sync_attempt.RepositorySyncAttempt"
    )
    """<p>The status of the latest sync returned for a specified repository and branch.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRepositorySyncStatusOutput) -> dict:
    out: dict = {}
    import capo_codeconnections.types.repository_sync_attempt

    out["LatestSync"] = (
        capo_codeconnections.types.repository_sync_attempt.serialize_aws_json_1_0(
            value["latest_sync"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRepositorySyncStatusOutput:
    out: GetRepositorySyncStatusOutput = {}  # type: ignore[typeddict-item]
    if data.get("LatestSync") is not None:
        import capo_codeconnections.types.repository_sync_attempt

        out["latest_sync"] = (
            capo_codeconnections.types.repository_sync_attempt.deserialize_aws_json_1_0(
                data["LatestSync"]
            )
        )
    else:
        raise DeserializationError("GetRepositorySyncStatusOutput.latest_sync required")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetRepositorySyncStatusOutput) -> dict:
    out: dict = {}
    import capo_codeconnections.types.repository_sync_attempt

    out["LatestSync"] = (
        capo_codeconnections.types.repository_sync_attempt.serialize_cbor(
            value["latest_sync"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> GetRepositorySyncStatusOutput:
    out: GetRepositorySyncStatusOutput = {}  # type: ignore[typeddict-item]
    if data.get("LatestSync") is not None:
        import capo_codeconnections.types.repository_sync_attempt

        out["latest_sync"] = (
            capo_codeconnections.types.repository_sync_attempt.deserialize_cbor(
                data["LatestSync"]
            )
        )
    else:
        raise DeserializationError("GetRepositorySyncStatusOutput.latest_sync required")
    return out
