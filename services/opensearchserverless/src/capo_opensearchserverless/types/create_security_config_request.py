"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CreateSecurityConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.config_description
    import capo_opensearchserverless.types.config_name
    import capo_opensearchserverless.types.create_iam_identity_center_config_options
    import capo_opensearchserverless.types.iam_federation_config_options
    import capo_opensearchserverless.types.saml_config_options
    import capo_opensearchserverless.types.security_config_type


class CreateSecurityConfigRequest(TypedDict, closed=True):
    type: "capo_opensearchserverless.types.security_config_type.SecurityConfigType"
    """<p>The type of security configuration.</p>"""
    name: "capo_opensearchserverless.types.config_name.ConfigName"
    """<p>The name of the security configuration.</p>"""
    description: NotRequired[
        "capo_opensearchserverless.types.config_description.ConfigDescription"
    ]
    """<p>A description of the security configuration.</p>"""
    saml_options: NotRequired[
        "capo_opensearchserverless.types.saml_config_options.SamlConfigOptions"
    ]
    """<p>Describes SAML options in the form of a key-value map. This field is required if you specify <code>SAML</code> for the <code>type</code> parameter.</p>"""
    iam_identity_center_options: NotRequired[
        "capo_opensearchserverless.types.create_iam_identity_center_config_options.CreateIamIdentityCenterConfigOptions"
    ]
    """<p>Describes IAM Identity Center options in the form of a key-value map. This field is required if you specify <code>iamidentitycenter</code> for the <code>type</code> parameter.</p>"""
    iam_federation_options: NotRequired[
        "capo_opensearchserverless.types.iam_federation_config_options.IamFederationConfigOptions"
    ]
    """<p>Describes IAM federation options in the form of a key-value map. This field is required if you specify <code>iamFederation</code> for the <code>type</code> parameter.</p>"""
    client_token: NotRequired[
        "capo_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateSecurityConfigRequest) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "saml_options" in value:
        import capo_opensearchserverless.types.saml_config_options

        out["samlOptions"] = (
            capo_opensearchserverless.types.saml_config_options.serialize_aws_json_1_0(
                value["saml_options"]
            )
        )
    if "iam_identity_center_options" in value:
        import capo_opensearchserverless.types.create_iam_identity_center_config_options

        out["iamIdentityCenterOptions"] = (
            capo_opensearchserverless.types.create_iam_identity_center_config_options.serialize_aws_json_1_0(
                value["iam_identity_center_options"]
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


def deserialize_aws_json_1_0(data: dict) -> CreateSecurityConfigRequest:
    out: CreateSecurityConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("samlOptions") is not None:
        import capo_opensearchserverless.types.saml_config_options

        out["saml_options"] = (
            capo_opensearchserverless.types.saml_config_options.deserialize_aws_json_1_0(
                data["samlOptions"]
            )
        )
    if data.get("iamIdentityCenterOptions") is not None:
        import capo_opensearchserverless.types.create_iam_identity_center_config_options

        out["iam_identity_center_options"] = (
            capo_opensearchserverless.types.create_iam_identity_center_config_options.deserialize_aws_json_1_0(
                data["iamIdentityCenterOptions"]
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
