"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ListTargetsResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codestar_notifications.types.next_token
    import capo_codestar_notifications.types.targets_batch


class ListTargetsResult(TypedDict, closed=True):
    targets: NotRequired["capo_codestar_notifications.types.targets_batch.TargetsBatch"]
    """<p>The list of notification rule targets. </p>"""
    next_token: NotRequired["capo_codestar_notifications.types.next_token.NextToken"]
    """<p>An enumeration token that can be used in a request to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTargetsResult) -> dict:
    out: dict = {}
    if "targets" in value:
        import capo_codestar_notifications.types.targets_batch

        out["Targets"] = capo_codestar_notifications.types.targets_batch.serialize_json(
            value["targets"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTargetsResult:
    out: ListTargetsResult = {}  # type: ignore[typeddict-item]
    if data.get("Targets") is not None:
        import capo_codestar_notifications.types.targets_batch

        out["targets"] = (
            capo_codestar_notifications.types.targets_batch.deserialize_json(
                data["Targets"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListTargetsResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "targets" in value:
        import capo_codestar_notifications.types.targets_batch

        out["targets"] = (
            capo_codestar_notifications.types.targets_batch.redact_sensitive(
                value["targets"]
            )
        )
    return out
