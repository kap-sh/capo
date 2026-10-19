"""Generated from Smithy shape ``com.amazonaws.codebuild#RegistryCredential``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.credential_provider_type
    import capo_codebuild.types.non_empty_string


class RegistryCredential(TypedDict, closed=True):
    credential: "capo_codebuild.types.non_empty_string.NonEmptyString"
    """<p> The Amazon Resource Name (ARN) or name of credentials created using Secrets Manager. </p> <note> <p> The <code>credential</code> can use the name of the credentials only if they exist in your current Amazon Web Services Region. </p> </note>"""
    credential_provider: (
        "capo_codebuild.types.credential_provider_type.CredentialProviderType"
    )
    """<p> The service that created the credentials to access a private Docker registry. The valid value, SECRETS_MANAGER, is for Secrets Manager. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegistryCredential) -> dict:
    out: dict = {}
    out["credential"] = value["credential"]
    import capo_codebuild.types.credential_provider_type

    out["credentialProvider"] = (
        capo_codebuild.types.credential_provider_type.serialize_aws_json_1_1(
            value["credential_provider"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegistryCredential:
    out: RegistryCredential = {}  # type: ignore[typeddict-item]
    if data.get("credential") is not None:
        out["credential"] = data["credential"]
    else:
        out["credential"] = ""
    if data.get("credentialProvider") is not None:
        import capo_codebuild.types.credential_provider_type

        out["credential_provider"] = (
            capo_codebuild.types.credential_provider_type.deserialize_aws_json_1_1(
                data["credentialProvider"]
            )
        )
    else:
        import typing

        out["credential_provider"] = typing.cast(
            "capo_codebuild.types.credential_provider_type.CredentialProviderType", ""
        )
    return out
