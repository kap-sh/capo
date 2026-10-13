"""Generated from Smithy shape ``com.amazonaws.lambda#CheckpointUpdatedExecutionState``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.operations
    import capo_lambda.types.string


class CheckpointUpdatedExecutionState(TypedDict, closed=True):
    operations: NotRequired["capo_lambda.types.operations.Operations"]
    """<p>A list of operations that have been updated since the last checkpoint.</p>"""
    next_marker: NotRequired["capo_lambda.types.string.String"]
    """<p>Indicates that more results are available. Use this value in a subsequent call to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CheckpointUpdatedExecutionState) -> dict:
    out: dict = {}
    if "operations" in value:
        import capo_lambda.types.operations

        out["Operations"] = capo_lambda.types.operations.serialize_json(
            value["operations"]
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> CheckpointUpdatedExecutionState:
    out: CheckpointUpdatedExecutionState = {}  # type: ignore[typeddict-item]
    if data.get("Operations") is not None:
        import capo_lambda.types.operations

        out["operations"] = capo_lambda.types.operations.deserialize_json(
            data["Operations"]
        )
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    return out


def redact_sensitive(value: CheckpointUpdatedExecutionState) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "operations" in value:
        import capo_lambda.types.operations

        out["operations"] = capo_lambda.types.operations.redact_sensitive(
            value["operations"]
        )
    return out
