"""Generated from Smithy shape ``com.amazonaws.ssmsap#ApplicationCredential``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_ssm_sap.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_sap.types.credential_type
    import capo_ssm_sap.types.database_name
    import capo_ssm_sap.types.secret_id


class ApplicationCredential(TypedDict, closed=True):
    database_name: "capo_ssm_sap.types.database_name.DatabaseName"
    """<p>The name of the SAP HANA database.</p>"""
    credential_type: "capo_ssm_sap.types.credential_type.CredentialType"
    """<p>The type of the application credentials. </p>"""
    secret_id: "capo_ssm_sap.types.secret_id.SecretId"
    """<p>The secret ID created in AWS Secrets Manager to store the credentials of the SAP application. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationCredential) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    import capo_ssm_sap.types.credential_type

    out["CredentialType"] = capo_ssm_sap.types.credential_type.serialize_json(
        value["credential_type"]
    )
    out["SecretId"] = value["secret_id"]
    return out


def deserialize_json(data: dict) -> ApplicationCredential:
    out: ApplicationCredential = {}  # type: ignore[typeddict-item]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("ApplicationCredential.database_name required")
    if data.get("CredentialType") is not None:
        import capo_ssm_sap.types.credential_type

        out["credential_type"] = capo_ssm_sap.types.credential_type.deserialize_json(
            data["CredentialType"]
        )
    else:
        raise DeserializationError("ApplicationCredential.credential_type required")
    if data.get("SecretId") is not None:
        out["secret_id"] = data["SecretId"]
    else:
        raise DeserializationError("ApplicationCredential.secret_id required")
    return out


def redact_sensitive(value: ApplicationCredential) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "secret_id" in value:
        out["secret_id"] = "*** Sensitive Data Redacted ***"
    return out
