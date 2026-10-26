"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Oauth2ProviderConfigOutput``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.atlassian_oauth2_provider_config_output
    import capo_bedrock_agentcore_control.types.custom_oauth2_provider_config_output
    import capo_bedrock_agentcore_control.types.github_oauth2_provider_config_output
    import capo_bedrock_agentcore_control.types.google_oauth2_provider_config_output
    import capo_bedrock_agentcore_control.types.included_oauth2_provider_config_output
    import capo_bedrock_agentcore_control.types.linkedin_oauth2_provider_config_output
    import capo_bedrock_agentcore_control.types.microsoft_oauth2_provider_config_output
    import capo_bedrock_agentcore_control.types.salesforce_oauth2_provider_config_output
    import capo_bedrock_agentcore_control.types.slack_oauth2_provider_config_output


class _Oauth2ProviderConfigOutput_customOauth2ProviderConfig(TypedDict, closed=True):
    customOauth2ProviderConfig: "capo_bedrock_agentcore_control.types.custom_oauth2_provider_config_output.CustomOauth2ProviderConfigOutput"


class _Oauth2ProviderConfigOutput_googleOauth2ProviderConfig(TypedDict, closed=True):
    googleOauth2ProviderConfig: "capo_bedrock_agentcore_control.types.google_oauth2_provider_config_output.GoogleOauth2ProviderConfigOutput"


class _Oauth2ProviderConfigOutput_githubOauth2ProviderConfig(TypedDict, closed=True):
    githubOauth2ProviderConfig: "capo_bedrock_agentcore_control.types.github_oauth2_provider_config_output.GithubOauth2ProviderConfigOutput"


class _Oauth2ProviderConfigOutput_slackOauth2ProviderConfig(TypedDict, closed=True):
    slackOauth2ProviderConfig: "capo_bedrock_agentcore_control.types.slack_oauth2_provider_config_output.SlackOauth2ProviderConfigOutput"


class _Oauth2ProviderConfigOutput_salesforceOauth2ProviderConfig(
    TypedDict, closed=True
):
    salesforceOauth2ProviderConfig: "capo_bedrock_agentcore_control.types.salesforce_oauth2_provider_config_output.SalesforceOauth2ProviderConfigOutput"


class _Oauth2ProviderConfigOutput_microsoftOauth2ProviderConfig(TypedDict, closed=True):
    microsoftOauth2ProviderConfig: "capo_bedrock_agentcore_control.types.microsoft_oauth2_provider_config_output.MicrosoftOauth2ProviderConfigOutput"


class _Oauth2ProviderConfigOutput_atlassianOauth2ProviderConfig(TypedDict, closed=True):
    atlassianOauth2ProviderConfig: "capo_bedrock_agentcore_control.types.atlassian_oauth2_provider_config_output.AtlassianOauth2ProviderConfigOutput"


class _Oauth2ProviderConfigOutput_linkedinOauth2ProviderConfig(TypedDict, closed=True):
    linkedinOauth2ProviderConfig: "capo_bedrock_agentcore_control.types.linkedin_oauth2_provider_config_output.LinkedinOauth2ProviderConfigOutput"


class _Oauth2ProviderConfigOutput_includedOauth2ProviderConfig(TypedDict, closed=True):
    includedOauth2ProviderConfig: "capo_bedrock_agentcore_control.types.included_oauth2_provider_config_output.IncludedOauth2ProviderConfigOutput"


Oauth2ProviderConfigOutput: TypeAlias = (
    _Oauth2ProviderConfigOutput_customOauth2ProviderConfig
    | _Oauth2ProviderConfigOutput_googleOauth2ProviderConfig
    | _Oauth2ProviderConfigOutput_githubOauth2ProviderConfig
    | _Oauth2ProviderConfigOutput_slackOauth2ProviderConfig
    | _Oauth2ProviderConfigOutput_salesforceOauth2ProviderConfig
    | _Oauth2ProviderConfigOutput_microsoftOauth2ProviderConfig
    | _Oauth2ProviderConfigOutput_atlassianOauth2ProviderConfig
    | _Oauth2ProviderConfigOutput_linkedinOauth2ProviderConfig
    | _Oauth2ProviderConfigOutput_includedOauth2ProviderConfig
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Oauth2ProviderConfigOutput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Oauth2ProviderConfigOutput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "customOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.custom_oauth2_provider_config_output

        return {
            "customOauth2ProviderConfig": capo_bedrock_agentcore_control.types.custom_oauth2_provider_config_output.serialize_json(
                value["customOauth2ProviderConfig"]
            )
        }
    elif "googleOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.google_oauth2_provider_config_output

        return {
            "googleOauth2ProviderConfig": capo_bedrock_agentcore_control.types.google_oauth2_provider_config_output.serialize_json(
                value["googleOauth2ProviderConfig"]
            )
        }
    elif "githubOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.github_oauth2_provider_config_output

        return {
            "githubOauth2ProviderConfig": capo_bedrock_agentcore_control.types.github_oauth2_provider_config_output.serialize_json(
                value["githubOauth2ProviderConfig"]
            )
        }
    elif "slackOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.slack_oauth2_provider_config_output

        return {
            "slackOauth2ProviderConfig": capo_bedrock_agentcore_control.types.slack_oauth2_provider_config_output.serialize_json(
                value["slackOauth2ProviderConfig"]
            )
        }
    elif "salesforceOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.salesforce_oauth2_provider_config_output

        return {
            "salesforceOauth2ProviderConfig": capo_bedrock_agentcore_control.types.salesforce_oauth2_provider_config_output.serialize_json(
                value["salesforceOauth2ProviderConfig"]
            )
        }
    elif "microsoftOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.microsoft_oauth2_provider_config_output

        return {
            "microsoftOauth2ProviderConfig": capo_bedrock_agentcore_control.types.microsoft_oauth2_provider_config_output.serialize_json(
                value["microsoftOauth2ProviderConfig"]
            )
        }
    elif "atlassianOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.atlassian_oauth2_provider_config_output

        return {
            "atlassianOauth2ProviderConfig": capo_bedrock_agentcore_control.types.atlassian_oauth2_provider_config_output.serialize_json(
                value["atlassianOauth2ProviderConfig"]
            )
        }
    elif "linkedinOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.linkedin_oauth2_provider_config_output

        return {
            "linkedinOauth2ProviderConfig": capo_bedrock_agentcore_control.types.linkedin_oauth2_provider_config_output.serialize_json(
                value["linkedinOauth2ProviderConfig"]
            )
        }
    elif "includedOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.included_oauth2_provider_config_output

        return {
            "includedOauth2ProviderConfig": capo_bedrock_agentcore_control.types.included_oauth2_provider_config_output.serialize_json(
                value["includedOauth2ProviderConfig"]
            )
        }
    else:
        raise SerializationError("Oauth2ProviderConfigOutput: no variant present")


def deserialize_json(data: dict) -> Oauth2ProviderConfigOutput:
    if data.get("customOauth2ProviderConfig") is not None:
        import capo_bedrock_agentcore_control.types.custom_oauth2_provider_config_output

        return {
            "customOauth2ProviderConfig": capo_bedrock_agentcore_control.types.custom_oauth2_provider_config_output.deserialize_json(
                data["customOauth2ProviderConfig"]
            )
        }
    elif data.get("googleOauth2ProviderConfig") is not None:
        import capo_bedrock_agentcore_control.types.google_oauth2_provider_config_output

        return {
            "googleOauth2ProviderConfig": capo_bedrock_agentcore_control.types.google_oauth2_provider_config_output.deserialize_json(
                data["googleOauth2ProviderConfig"]
            )
        }
    elif data.get("githubOauth2ProviderConfig") is not None:
        import capo_bedrock_agentcore_control.types.github_oauth2_provider_config_output

        return {
            "githubOauth2ProviderConfig": capo_bedrock_agentcore_control.types.github_oauth2_provider_config_output.deserialize_json(
                data["githubOauth2ProviderConfig"]
            )
        }
    elif data.get("slackOauth2ProviderConfig") is not None:
        import capo_bedrock_agentcore_control.types.slack_oauth2_provider_config_output

        return {
            "slackOauth2ProviderConfig": capo_bedrock_agentcore_control.types.slack_oauth2_provider_config_output.deserialize_json(
                data["slackOauth2ProviderConfig"]
            )
        }
    elif data.get("salesforceOauth2ProviderConfig") is not None:
        import capo_bedrock_agentcore_control.types.salesforce_oauth2_provider_config_output

        return {
            "salesforceOauth2ProviderConfig": capo_bedrock_agentcore_control.types.salesforce_oauth2_provider_config_output.deserialize_json(
                data["salesforceOauth2ProviderConfig"]
            )
        }
    elif data.get("microsoftOauth2ProviderConfig") is not None:
        import capo_bedrock_agentcore_control.types.microsoft_oauth2_provider_config_output

        return {
            "microsoftOauth2ProviderConfig": capo_bedrock_agentcore_control.types.microsoft_oauth2_provider_config_output.deserialize_json(
                data["microsoftOauth2ProviderConfig"]
            )
        }
    elif data.get("atlassianOauth2ProviderConfig") is not None:
        import capo_bedrock_agentcore_control.types.atlassian_oauth2_provider_config_output

        return {
            "atlassianOauth2ProviderConfig": capo_bedrock_agentcore_control.types.atlassian_oauth2_provider_config_output.deserialize_json(
                data["atlassianOauth2ProviderConfig"]
            )
        }
    elif data.get("linkedinOauth2ProviderConfig") is not None:
        import capo_bedrock_agentcore_control.types.linkedin_oauth2_provider_config_output

        return {
            "linkedinOauth2ProviderConfig": capo_bedrock_agentcore_control.types.linkedin_oauth2_provider_config_output.deserialize_json(
                data["linkedinOauth2ProviderConfig"]
            )
        }
    elif data.get("includedOauth2ProviderConfig") is not None:
        import capo_bedrock_agentcore_control.types.included_oauth2_provider_config_output

        return {
            "includedOauth2ProviderConfig": capo_bedrock_agentcore_control.types.included_oauth2_provider_config_output.deserialize_json(
                data["includedOauth2ProviderConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "Oauth2ProviderConfigOutput: no recognized variant key"
        )


def redact_sensitive(value: Oauth2ProviderConfigOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.custom_oauth2_provider_config_output

        out["customOauth2ProviderConfig"] = (
            capo_bedrock_agentcore_control.types.custom_oauth2_provider_config_output.redact_sensitive(
                value["customOauth2ProviderConfig"]
            )
        )
    return out
