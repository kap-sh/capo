"""Generated from Smithy shape ``com.amazonaws.opensearch#AdvancedSecurityOptionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.boolean
    import capo_opensearch.types.iam_federation_options_input
    import capo_opensearch.types.jwt_options_input
    import capo_opensearch.types.master_user_options
    import capo_opensearch.types.saml_options_input


class AdvancedSecurityOptionsInput(TypedDict, closed=True):
    enabled: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>True to enable fine-grained access control.</p>"""
    internal_user_database_enabled: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>True to enable the internal user database.</p>"""
    master_user_options: NotRequired[
        "capo_opensearch.types.master_user_options.MasterUserOptions"
    ]
    """<p>Container for information about the master user.</p>"""
    saml_options: NotRequired[
        "capo_opensearch.types.saml_options_input.SAMLOptionsInput"
    ]
    """<p>Container for information about the SAML configuration for OpenSearch Dashboards.</p>"""
    jwt_options: NotRequired["capo_opensearch.types.jwt_options_input.JWTOptionsInput"]
    """<p>Container for information about the JWT configuration of the Amazon OpenSearch Service. </p>"""
    iam_federation_options: NotRequired[
        "capo_opensearch.types.iam_federation_options_input.IAMFederationOptionsInput"
    ]
    """<p>Input configuration for IAM identity federation within advanced security options.</p>"""
    anonymous_auth_enabled: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>True to enable a 30-day migration period during which administrators can create role mappings. Only necessary when <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html#fgac-enabling-existing">enabling fine-grained access control on an existing domain</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedSecurityOptionsInput) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "internal_user_database_enabled" in value:
        out["InternalUserDatabaseEnabled"] = value["internal_user_database_enabled"]
    if "master_user_options" in value:
        import capo_opensearch.types.master_user_options

        out["MasterUserOptions"] = (
            capo_opensearch.types.master_user_options.serialize_json(
                value["master_user_options"]
            )
        )
    if "saml_options" in value:
        import capo_opensearch.types.saml_options_input

        out["SAMLOptions"] = capo_opensearch.types.saml_options_input.serialize_json(
            value["saml_options"]
        )
    if "jwt_options" in value:
        import capo_opensearch.types.jwt_options_input

        out["JWTOptions"] = capo_opensearch.types.jwt_options_input.serialize_json(
            value["jwt_options"]
        )
    if "iam_federation_options" in value:
        import capo_opensearch.types.iam_federation_options_input

        out["IAMFederationOptions"] = (
            capo_opensearch.types.iam_federation_options_input.serialize_json(
                value["iam_federation_options"]
            )
        )
    if "anonymous_auth_enabled" in value:
        out["AnonymousAuthEnabled"] = value["anonymous_auth_enabled"]
    return out


def deserialize_json(data: dict) -> AdvancedSecurityOptionsInput:
    out: AdvancedSecurityOptionsInput = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("InternalUserDatabaseEnabled") is not None:
        out["internal_user_database_enabled"] = data["InternalUserDatabaseEnabled"]
    if data.get("MasterUserOptions") is not None:
        import capo_opensearch.types.master_user_options

        out["master_user_options"] = (
            capo_opensearch.types.master_user_options.deserialize_json(
                data["MasterUserOptions"]
            )
        )
    if data.get("SAMLOptions") is not None:
        import capo_opensearch.types.saml_options_input

        out["saml_options"] = capo_opensearch.types.saml_options_input.deserialize_json(
            data["SAMLOptions"]
        )
    if data.get("JWTOptions") is not None:
        import capo_opensearch.types.jwt_options_input

        out["jwt_options"] = capo_opensearch.types.jwt_options_input.deserialize_json(
            data["JWTOptions"]
        )
    if data.get("IAMFederationOptions") is not None:
        import capo_opensearch.types.iam_federation_options_input

        out["iam_federation_options"] = (
            capo_opensearch.types.iam_federation_options_input.deserialize_json(
                data["IAMFederationOptions"]
            )
        )
    if data.get("AnonymousAuthEnabled") is not None:
        out["anonymous_auth_enabled"] = data["AnonymousAuthEnabled"]
    return out
