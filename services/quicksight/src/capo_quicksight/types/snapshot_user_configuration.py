"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotUserConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.snapshot_anonymous_user_list


class SnapshotUserConfiguration(TypedDict, closed=True):
    anonymous_users: NotRequired[
        "capo_quicksight.types.snapshot_anonymous_user_list.SnapshotAnonymousUserList"
    ]
    """<p>An array of records that describe the anonymous users that the dashboard snapshot is generated for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotUserConfiguration) -> dict:
    out: dict = {}
    if "anonymous_users" in value:
        import capo_quicksight.types.snapshot_anonymous_user_list

        out["AnonymousUsers"] = (
            capo_quicksight.types.snapshot_anonymous_user_list.serialize_json(
                value["anonymous_users"]
            )
        )
    return out


def deserialize_json(data: dict) -> SnapshotUserConfiguration:
    out: SnapshotUserConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AnonymousUsers") is not None:
        import capo_quicksight.types.snapshot_anonymous_user_list

        out["anonymous_users"] = (
            capo_quicksight.types.snapshot_anonymous_user_list.deserialize_json(
                data["AnonymousUsers"]
            )
        )
    return out


def redact_sensitive(value: SnapshotUserConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "anonymous_users" in value:
        import capo_quicksight.types.snapshot_anonymous_user_list

        out["anonymous_users"] = (
            capo_quicksight.types.snapshot_anonymous_user_list.redact_sensitive(
                value["anonymous_users"]
            )
        )
    return out
