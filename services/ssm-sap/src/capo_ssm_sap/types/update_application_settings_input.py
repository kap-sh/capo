"""Generated from Smithy shape ``com.amazonaws.ssmsap#UpdateApplicationSettingsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ssm_sap.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_sap.types.application_credential_list
    import capo_ssm_sap.types.application_id
    import capo_ssm_sap.types.backint_config
    import capo_ssm_sap.types.ssm_sap_arn


class UpdateApplicationSettingsInput(TypedDict, closed=True):
    application_id: "capo_ssm_sap.types.application_id.ApplicationId"
    """<p>The ID of the application.</p>"""
    credentials_to_add_or_update: NotRequired[
        "capo_ssm_sap.types.application_credential_list.ApplicationCredentialList"
    ]
    """<p>The credentials to be added or updated.</p>"""
    credentials_to_remove: NotRequired[
        "capo_ssm_sap.types.application_credential_list.ApplicationCredentialList"
    ]
    """<p>The credentials to be removed.</p>"""
    backint: NotRequired["capo_ssm_sap.types.backint_config.BackintConfig"]
    """<p>Installation of AWS Backint Agent for SAP HANA.</p>"""
    database_arn: NotRequired["capo_ssm_sap.types.ssm_sap_arn.SsmSapArn"]
    """<p>The Amazon Resource Name of the SAP HANA database that replaces the current SAP HANA connection with the SAP_ABAP application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationSettingsInput) -> dict:
    out: dict = {}
    out["ApplicationId"] = value["application_id"]
    if "credentials_to_add_or_update" in value:
        import capo_ssm_sap.types.application_credential_list

        out["CredentialsToAddOrUpdate"] = (
            capo_ssm_sap.types.application_credential_list.serialize_json(
                value["credentials_to_add_or_update"]
            )
        )
    if "credentials_to_remove" in value:
        import capo_ssm_sap.types.application_credential_list

        out["CredentialsToRemove"] = (
            capo_ssm_sap.types.application_credential_list.serialize_json(
                value["credentials_to_remove"]
            )
        )
    if "backint" in value:
        import capo_ssm_sap.types.backint_config

        out["Backint"] = capo_ssm_sap.types.backint_config.serialize_json(
            value["backint"]
        )
    if "database_arn" in value:
        out["DatabaseArn"] = value["database_arn"]
    return out


def deserialize_json(data: dict) -> UpdateApplicationSettingsInput:
    out: UpdateApplicationSettingsInput = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    else:
        raise DeserializationError(
            "UpdateApplicationSettingsInput.application_id required"
        )
    if data.get("CredentialsToAddOrUpdate") is not None:
        import capo_ssm_sap.types.application_credential_list

        out["credentials_to_add_or_update"] = (
            capo_ssm_sap.types.application_credential_list.deserialize_json(
                data["CredentialsToAddOrUpdate"]
            )
        )
    if data.get("CredentialsToRemove") is not None:
        import capo_ssm_sap.types.application_credential_list

        out["credentials_to_remove"] = (
            capo_ssm_sap.types.application_credential_list.deserialize_json(
                data["CredentialsToRemove"]
            )
        )
    if data.get("Backint") is not None:
        import capo_ssm_sap.types.backint_config

        out["backint"] = capo_ssm_sap.types.backint_config.deserialize_json(
            data["Backint"]
        )
    if data.get("DatabaseArn") is not None:
        out["database_arn"] = data["DatabaseArn"]
    return out


def redact_sensitive(value: UpdateApplicationSettingsInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credentials_to_add_or_update" in value:
        import capo_ssm_sap.types.application_credential_list

        out["credentials_to_add_or_update"] = (
            capo_ssm_sap.types.application_credential_list.redact_sensitive(
                value["credentials_to_add_or_update"]
            )
        )
    if "credentials_to_remove" in value:
        import capo_ssm_sap.types.application_credential_list

        out["credentials_to_remove"] = (
            capo_ssm_sap.types.application_credential_list.redact_sensitive(
                value["credentials_to_remove"]
            )
        )
    return out
