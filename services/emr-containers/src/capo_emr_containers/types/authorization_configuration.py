"""Generated from Smithy shape ``com.amazonaws.emrcontainers#AuthorizationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.encryption_configuration
    import capo_emr_containers.types.lake_formation_configuration


class AuthorizationConfiguration(TypedDict, closed=True):
    lake_formation_configuration: NotRequired[
        "capo_emr_containers.types.lake_formation_configuration.LakeFormationConfiguration"
    ]
    """<p> Lake Formation related configuration inputs for the security configuration.</p>"""
    encryption_configuration: NotRequired[
        "capo_emr_containers.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>Encryption-related configuration input for the security configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizationConfiguration) -> dict:
    out: dict = {}
    if "lake_formation_configuration" in value:
        import capo_emr_containers.types.lake_formation_configuration

        out["lakeFormationConfiguration"] = (
            capo_emr_containers.types.lake_formation_configuration.serialize_json(
                value["lake_formation_configuration"]
            )
        )
    if "encryption_configuration" in value:
        import capo_emr_containers.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_emr_containers.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AuthorizationConfiguration:
    out: AuthorizationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("lakeFormationConfiguration") is not None:
        import capo_emr_containers.types.lake_formation_configuration

        out["lake_formation_configuration"] = (
            capo_emr_containers.types.lake_formation_configuration.deserialize_json(
                data["lakeFormationConfiguration"]
            )
        )
    if data.get("encryptionConfiguration") is not None:
        import capo_emr_containers.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_emr_containers.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    return out
