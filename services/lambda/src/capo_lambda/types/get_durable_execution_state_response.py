"""Generated from Smithy shape ``com.amazonaws.lambda#GetDurableExecutionStateResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.operations
    import capo_lambda.types.string


class GetDurableExecutionStateResponse(TypedDict, closed=True):
    operations: "capo_lambda.types.operations.Operations"
    """<p>An array of operations that represent the current state of the durable execution. Operations are ordered by their start sequence number in ascending order and include information needed for replay processing.</p>"""
    next_marker: NotRequired["capo_lambda.types.string.String"]
    """<p>If present, indicates that more operations are available. Use this value as the <code>Marker</code> parameter in a subsequent request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDurableExecutionStateResponse) -> dict:
    out: dict = {}
    import capo_lambda.types.operations

    out["Operations"] = capo_lambda.types.operations.serialize_json(value["operations"])
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> GetDurableExecutionStateResponse:
    out: GetDurableExecutionStateResponse = {}  # type: ignore[typeddict-item]
    if data.get("Operations") is not None:
        import capo_lambda.types.operations

        out["operations"] = capo_lambda.types.operations.deserialize_json(
            data["Operations"]
        )
    else:
        out["operations"] = []
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    return out


def redact_sensitive(value: GetDurableExecutionStateResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "operations" in value:
        import capo_lambda.types.operations

        out["operations"] = capo_lambda.types.operations.redact_sensitive(
            value["operations"]
        )
    return out
