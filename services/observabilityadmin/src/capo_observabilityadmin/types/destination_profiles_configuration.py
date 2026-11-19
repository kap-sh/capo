"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#DestinationProfilesConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.profiles_backup_configuration


class DestinationProfilesConfiguration(TypedDict, closed=True):
    backup_configuration: NotRequired[
        "capo_observabilityadmin.types.profiles_backup_configuration.ProfilesBackupConfiguration"
    ]
    """<p>Configuration that defines the backup Region for the profiles backup destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationProfilesConfiguration) -> dict:
    out: dict = {}
    if "backup_configuration" in value:
        import capo_observabilityadmin.types.profiles_backup_configuration

        out["BackupConfiguration"] = (
            capo_observabilityadmin.types.profiles_backup_configuration.serialize_json(
                value["backup_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DestinationProfilesConfiguration:
    out: DestinationProfilesConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("BackupConfiguration") is not None:
        import capo_observabilityadmin.types.profiles_backup_configuration

        out["backup_configuration"] = (
            capo_observabilityadmin.types.profiles_backup_configuration.deserialize_json(
                data["BackupConfiguration"]
            )
        )
    return out
