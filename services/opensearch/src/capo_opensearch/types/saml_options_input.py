"""Generated from Smithy shape ``com.amazonaws.opensearch#SAMLOptionsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.backend_role
    import capo_opensearch.types.boolean
    import capo_opensearch.types.integer_class
    import capo_opensearch.types.saml_idp
    import capo_opensearch.types.string
    import capo_opensearch.types.username


class SAMLOptionsInput(TypedDict, closed=True):
    enabled: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>True to enable SAML authentication for a domain.</p>"""
    idp: NotRequired["capo_opensearch.types.saml_idp.SAMLIdp"]
    """<p>The SAML Identity Provider's information.</p>"""
    master_user_name: NotRequired["capo_opensearch.types.username.Username"]
    """<p>The SAML master user name, which is stored in the domain's internal user database.</p>"""
    master_backend_role: NotRequired["capo_opensearch.types.backend_role.BackendRole"]
    """<p>The backend role that the SAML master user is mapped to.</p>"""
    subject_key: NotRequired["capo_opensearch.types.string.String"]
    """<p>Element of the SAML assertion to use for the user name. Default is <code>NameID</code>.</p>"""
    roles_key: NotRequired["capo_opensearch.types.string.String"]
    """<p>Element of the SAML assertion to use for backend roles. Default is <code>roles</code>.</p>"""
    session_timeout_minutes: NotRequired[
        "capo_opensearch.types.integer_class.IntegerClass"
    ]
    """<p>The duration, in minutes, after which a user session becomes inactive. Acceptable values are between 1 and 1440, and the default value is 60.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SAMLOptionsInput) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "idp" in value:
        import capo_opensearch.types.saml_idp

        out["Idp"] = capo_opensearch.types.saml_idp.serialize_json(value["idp"])
    if "master_user_name" in value:
        out["MasterUserName"] = value["master_user_name"]
    if "master_backend_role" in value:
        out["MasterBackendRole"] = value["master_backend_role"]
    if "subject_key" in value:
        out["SubjectKey"] = value["subject_key"]
    if "roles_key" in value:
        out["RolesKey"] = value["roles_key"]
    if "session_timeout_minutes" in value:
        out["SessionTimeoutMinutes"] = value["session_timeout_minutes"]
    return out


def deserialize_json(data: dict) -> SAMLOptionsInput:
    out: SAMLOptionsInput = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("Idp") is not None:
        import capo_opensearch.types.saml_idp

        out["idp"] = capo_opensearch.types.saml_idp.deserialize_json(data["Idp"])
    if data.get("MasterUserName") is not None:
        out["master_user_name"] = data["MasterUserName"]
    if data.get("MasterBackendRole") is not None:
        out["master_backend_role"] = data["MasterBackendRole"]
    if data.get("SubjectKey") is not None:
        out["subject_key"] = data["SubjectKey"]
    if data.get("RolesKey") is not None:
        out["roles_key"] = data["RolesKey"]
    if data.get("SessionTimeoutMinutes") is not None:
        out["session_timeout_minutes"] = data["SessionTimeoutMinutes"]
    return out


def redact_sensitive(value: SAMLOptionsInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "master_user_name" in value:
        out["master_user_name"] = "*** Sensitive Data Redacted ***"
    return out
