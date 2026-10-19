"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#UpdateSecurityConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.config_description
    import capo_opensearchserverless.types.iam_federation_config_options
    import capo_opensearchserverless.types.policy_version
    import capo_opensearchserverless.types.saml_config_options
    import capo_opensearchserverless.types.security_config_id
    import capo_opensearchserverless.types.update_iam_identity_center_config_options


class UpdateSecurityConfigRequest(TypedDict, closed=True):
    id: "capo_opensearchserverless.types.security_config_id.SecurityConfigId"
    """<p>The security configuration identifier. For SAML the ID will be <code>saml/&lt;accountId&gt;/&lt;idpProviderName&gt;</code>. For example, <code>saml/123456789123/OKTADev</code>.</p>"""
    config_version: "capo_opensearchserverless.types.policy_version.PolicyVersion"
    """<p>The version of the security configuration to be updated. You can find the most recent version of a security configuration using the <code>GetSecurityPolicy</code> command.</p>"""
    description: NotRequired[
        "capo_opensearchserverless.types.config_description.ConfigDescription"
    ]
    """<p>A description of the security configuration.</p>"""
    saml_options: NotRequired[
        "capo_opensearchserverless.types.saml_config_options.SamlConfigOptions"
    ]
    """<p>SAML options in in the form of a key-value map.</p>"""
    iam_identity_center_options_updates: NotRequired[
        "capo_opensearchserverless.types.update_iam_identity_center_config_options.UpdateIamIdentityCenterConfigOptions"
    ]
    """<p>Describes IAM Identity Center options in the form of a key-value map.</p>"""
    iam_federation_options: NotRequired[
        "capo_opensearchserverless.types.iam_federation_config_options.IamFederationConfigOptions"
    ]
    """<p>Describes IAM federation options in the form of a key-value map for updating an existing security configuration. Use this field to modify IAM federation settings for the security configuration.</p>"""
    client_token: NotRequired[
        "capo_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateSecurityConfigRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["configVersion"] = value["config_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "saml_options" in value:
        import capo_opensearchserverless.types.saml_config_options

        out["samlOptions"] = (
            capo_opensearchserverless.types.saml_config_options.serialize_aws_json_1_0(
                value["saml_options"]
            )
        )
    if "iam_identity_center_options_updates" in value:
        import capo_opensearchserverless.types.update_iam_identity_center_config_options

        out["iamIdentityCenterOptionsUpdates"] = (
            capo_opensearchserverless.types.update_iam_identity_center_config_options.serialize_aws_json_1_0(
                value["iam_identity_center_options_updates"]
            )
        )
    if "iam_federation_options" in value:
        import capo_opensearchserverless.types.iam_federation_config_options

        out["iamFederationOptions"] = (
            capo_opensearchserverless.types.iam_federation_config_options.serialize_aws_json_1_0(
                value["iam_federation_options"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateSecurityConfigRequest:
    out: UpdateSecurityConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("configVersion") is not None:
        out["config_version"] = data["configVersion"]
    else:
        out["config_version"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("samlOptions") is not None:
        import capo_opensearchserverless.types.saml_config_options

        out["saml_options"] = (
            capo_opensearchserverless.types.saml_config_options.deserialize_aws_json_1_0(
                data["samlOptions"]
            )
        )
    if data.get("iamIdentityCenterOptionsUpdates") is not None:
        import capo_opensearchserverless.types.update_iam_identity_center_config_options

        out["iam_identity_center_options_updates"] = (
            capo_opensearchserverless.types.update_iam_identity_center_config_options.deserialize_aws_json_1_0(
                data["iamIdentityCenterOptionsUpdates"]
            )
        )
    if data.get("iamFederationOptions") is not None:
        import capo_opensearchserverless.types.iam_federation_config_options

        out["iam_federation_options"] = (
            capo_opensearchserverless.types.iam_federation_config_options.deserialize_aws_json_1_0(
                data["iamFederationOptions"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
