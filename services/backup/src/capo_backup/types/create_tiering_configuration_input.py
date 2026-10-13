"""Generated from Smithy shape ``com.amazonaws.backup#CreateTieringConfigurationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.creator_request_id
    import capo_backup.types.tags
    import capo_backup.types.tiering_configuration_input_for_create


class CreateTieringConfigurationInput(TypedDict, closed=True):
    tiering_configuration: "capo_backup.types.tiering_configuration_input_for_create.TieringConfigurationInputForCreate"
    """<p>A tiering configuration must contain a unique <code>TieringConfigurationName</code> string you create and must contain a <code>BackupVaultName</code> and <code>ResourceSelection</code>. You may optionally include a <code>CreatorRequestId</code> string.</p> <p>The <code>TieringConfigurationName</code> is a unique string that is the name of the tiering configuration. This cannot be changed after creation, and it must consist of only alphanumeric characters and underscores.</p>"""
    tiering_configuration_tags: NotRequired["capo_backup.types.tags.Tags"]
    """<p>The tags to assign to the tiering configuration.</p>"""
    creator_request_id: NotRequired[
        "capo_backup.types.creator_request_id.CreatorRequestId"
    ]
    """<p>This is a unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice. This parameter is optional. If used, this parameter must contain 1 to 50 alphanumeric or '-_.' characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTieringConfigurationInput) -> dict:
    out: dict = {}
    import capo_backup.types.tiering_configuration_input_for_create

    out["TieringConfiguration"] = (
        capo_backup.types.tiering_configuration_input_for_create.serialize_json(
            value["tiering_configuration"]
        )
    )
    if "tiering_configuration_tags" in value:
        import capo_backup.types.tags

        out["TieringConfigurationTags"] = capo_backup.types.tags.serialize_json(
            value["tiering_configuration_tags"]
        )
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    return out


def deserialize_json(data: dict) -> CreateTieringConfigurationInput:
    out: CreateTieringConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("TieringConfiguration") is not None:
        import capo_backup.types.tiering_configuration_input_for_create

        out["tiering_configuration"] = (
            capo_backup.types.tiering_configuration_input_for_create.deserialize_json(
                data["TieringConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateTieringConfigurationInput.tiering_configuration required"
        )
    if data.get("TieringConfigurationTags") is not None:
        import capo_backup.types.tags

        out["tiering_configuration_tags"] = capo_backup.types.tags.deserialize_json(
            data["TieringConfigurationTags"]
        )
    if data.get("CreatorRequestId") is not None:
        out["creator_request_id"] = data["CreatorRequestId"]
    return out


def redact_sensitive(value: CreateTieringConfigurationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tiering_configuration_tags" in value:
        out["tiering_configuration_tags"] = "*** Sensitive Data Redacted ***"
    return out
