"""Generated from Smithy shape ``com.amazonaws.backup#CreateLegalHoldInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.recovery_point_selection
    import capo_backup.types.string
    import capo_backup.types.tags


class CreateLegalHoldInput(TypedDict, closed=True):
    title: "capo_backup.types.string.string"
    """<p>The title of the legal hold.</p>"""
    description: "capo_backup.types.string.string"
    """<p>The description of the legal hold.</p>"""
    idempotency_token: NotRequired["capo_backup.types.string.string"]
    """<p>This is a user-chosen string used to distinguish between otherwise identical calls. Retrying a successful request with the same idempotency token results in a success message with no action taken.</p>"""
    recovery_point_selection: NotRequired[
        "capo_backup.types.recovery_point_selection.RecoveryPointSelection"
    ]
    """<p>The criteria to assign a set of resources, such as resource types or backup vaults.</p>"""
    tags: NotRequired["capo_backup.types.tags.Tags"]
    """<p>Optional tags to include. A tag is a key-value pair you can use to manage, filter, and search for your resources. Allowed characters include UTF-8 letters, numbers, spaces, and the following characters: + - = . _ : /. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLegalHoldInput) -> dict:
    out: dict = {}
    out["Title"] = value["title"]
    out["Description"] = value["description"]
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    if "recovery_point_selection" in value:
        import capo_backup.types.recovery_point_selection

        out["RecoveryPointSelection"] = (
            capo_backup.types.recovery_point_selection.serialize_json(
                value["recovery_point_selection"]
            )
        )
    if "tags" in value:
        import capo_backup.types.tags

        out["Tags"] = capo_backup.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateLegalHoldInput:
    out: CreateLegalHoldInput = {}  # type: ignore[typeddict-item]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("CreateLegalHoldInput.title required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("CreateLegalHoldInput.description required")
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    if data.get("RecoveryPointSelection") is not None:
        import capo_backup.types.recovery_point_selection

        out["recovery_point_selection"] = (
            capo_backup.types.recovery_point_selection.deserialize_json(
                data["RecoveryPointSelection"]
            )
        )
    if data.get("Tags") is not None:
        import capo_backup.types.tags

        out["tags"] = capo_backup.types.tags.deserialize_json(data["Tags"])
    return out


def redact_sensitive(value: CreateLegalHoldInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
