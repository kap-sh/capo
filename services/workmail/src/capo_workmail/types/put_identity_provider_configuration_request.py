"""Generated from Smithy shape ``com.amazonaws.workmail#PutIdentityProviderConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.identity_center_configuration
    import capo_workmail.types.identity_provider_authentication_mode
    import capo_workmail.types.organization_id
    import capo_workmail.types.personal_access_token_configuration


class PutIdentityProviderConfigurationRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p> The ID of the WorkMail Organization. </p>"""
    authentication_mode: "capo_workmail.types.identity_provider_authentication_mode.IdentityProviderAuthenticationMode"
    """<p> The authentication mode used in WorkMail.</p>"""
    identity_center_configuration: (
        "capo_workmail.types.identity_center_configuration.IdentityCenterConfiguration"
    )
    """<p> The details of the IAM Identity Center configuration.</p>"""
    personal_access_token_configuration: "capo_workmail.types.personal_access_token_configuration.PersonalAccessTokenConfiguration"
    """<p> The details of the Personal Access Token configuration. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutIdentityProviderConfigurationRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    import capo_workmail.types.identity_provider_authentication_mode

    out["AuthenticationMode"] = (
        capo_workmail.types.identity_provider_authentication_mode.serialize_aws_json_1_1(
            value["authentication_mode"]
        )
    )
    import capo_workmail.types.identity_center_configuration

    out["IdentityCenterConfiguration"] = (
        capo_workmail.types.identity_center_configuration.serialize_aws_json_1_1(
            value["identity_center_configuration"]
        )
    )
    import capo_workmail.types.personal_access_token_configuration

    out["PersonalAccessTokenConfiguration"] = (
        capo_workmail.types.personal_access_token_configuration.serialize_aws_json_1_1(
            value["personal_access_token_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutIdentityProviderConfigurationRequest:
    out: PutIdentityProviderConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("AuthenticationMode") is not None:
        import capo_workmail.types.identity_provider_authentication_mode

        out["authentication_mode"] = (
            capo_workmail.types.identity_provider_authentication_mode.deserialize_aws_json_1_1(
                data["AuthenticationMode"]
            )
        )
    else:
        import typing

        out["authentication_mode"] = typing.cast(
            "capo_workmail.types.identity_provider_authentication_mode.IdentityProviderAuthenticationMode",
            "",
        )
    if data.get("IdentityCenterConfiguration") is not None:
        import capo_workmail.types.identity_center_configuration

        out["identity_center_configuration"] = (
            capo_workmail.types.identity_center_configuration.deserialize_aws_json_1_1(
                data["IdentityCenterConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutIdentityProviderConfigurationRequest.identity_center_configuration required"
        )
    if data.get("PersonalAccessTokenConfiguration") is not None:
        import capo_workmail.types.personal_access_token_configuration

        out["personal_access_token_configuration"] = (
            capo_workmail.types.personal_access_token_configuration.deserialize_aws_json_1_1(
                data["PersonalAccessTokenConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutIdentityProviderConfigurationRequest.personal_access_token_configuration required"
        )
    return out
