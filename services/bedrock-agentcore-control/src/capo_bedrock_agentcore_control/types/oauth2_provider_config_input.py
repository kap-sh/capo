"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Oauth2ProviderConfigInput``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.atlassian_oauth2_provider_config_input
    import capo_bedrock_agentcore_control.types.custom_oauth2_provider_config_input
    import capo_bedrock_agentcore_control.types.github_oauth2_provider_config_input
    import capo_bedrock_agentcore_control.types.google_oauth2_provider_config_input
    import capo_bedrock_agentcore_control.types.included_oauth2_provider_config_input
    import capo_bedrock_agentcore_control.types.linkedin_oauth2_provider_config_input
    import capo_bedrock_agentcore_control.types.microsoft_oauth2_provider_config_input
    import capo_bedrock_agentcore_control.types.salesforce_oauth2_provider_config_input
    import capo_bedrock_agentcore_control.types.slack_oauth2_provider_config_input


class _Oauth2ProviderConfigInput_customOauth2ProviderConfig(TypedDict, closed=True):
    customOauth2ProviderConfig: "capo_bedrock_agentcore_control.types.custom_oauth2_provider_config_input.CustomOauth2ProviderConfigInput"


class _Oauth2ProviderConfigInput_googleOauth2ProviderConfig(TypedDict, closed=True):
    googleOauth2ProviderConfig: "capo_bedrock_agentcore_control.types.google_oauth2_provider_config_input.GoogleOauth2ProviderConfigInput"


class _Oauth2ProviderConfigInput_githubOauth2ProviderConfig(TypedDict, closed=True):
    githubOauth2ProviderConfig: "capo_bedrock_agentcore_control.types.github_oauth2_provider_config_input.GithubOauth2ProviderConfigInput"


class _Oauth2ProviderConfigInput_slackOauth2ProviderConfig(TypedDict, closed=True):
    slackOauth2ProviderConfig: "capo_bedrock_agentcore_control.types.slack_oauth2_provider_config_input.SlackOauth2ProviderConfigInput"


class _Oauth2ProviderConfigInput_salesforceOauth2ProviderConfig(TypedDict, closed=True):
    salesforceOauth2ProviderConfig: "capo_bedrock_agentcore_control.types.salesforce_oauth2_provider_config_input.SalesforceOauth2ProviderConfigInput"


class _Oauth2ProviderConfigInput_microsoftOauth2ProviderConfig(TypedDict, closed=True):
    microsoftOauth2ProviderConfig: "capo_bedrock_agentcore_control.types.microsoft_oauth2_provider_config_input.MicrosoftOauth2ProviderConfigInput"


class _Oauth2ProviderConfigInput_atlassianOauth2ProviderConfig(TypedDict, closed=True):
    atlassianOauth2ProviderConfig: "capo_bedrock_agentcore_control.types.atlassian_oauth2_provider_config_input.AtlassianOauth2ProviderConfigInput"


class _Oauth2ProviderConfigInput_linkedinOauth2ProviderConfig(TypedDict, closed=True):
    linkedinOauth2ProviderConfig: "capo_bedrock_agentcore_control.types.linkedin_oauth2_provider_config_input.LinkedinOauth2ProviderConfigInput"


class _Oauth2ProviderConfigInput_includedOauth2ProviderConfig(TypedDict, closed=True):
    includedOauth2ProviderConfig: "capo_bedrock_agentcore_control.types.included_oauth2_provider_config_input.IncludedOauth2ProviderConfigInput"


Oauth2ProviderConfigInput: TypeAlias = (
    _Oauth2ProviderConfigInput_customOauth2ProviderConfig
    | _Oauth2ProviderConfigInput_googleOauth2ProviderConfig
    | _Oauth2ProviderConfigInput_githubOauth2ProviderConfig
    | _Oauth2ProviderConfigInput_slackOauth2ProviderConfig
    | _Oauth2ProviderConfigInput_salesforceOauth2ProviderConfig
    | _Oauth2ProviderConfigInput_microsoftOauth2ProviderConfig
    | _Oauth2ProviderConfigInput_atlassianOauth2ProviderConfig
    | _Oauth2ProviderConfigInput_linkedinOauth2ProviderConfig
    | _Oauth2ProviderConfigInput_includedOauth2ProviderConfig
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Oauth2ProviderConfigInput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Oauth2ProviderConfigInput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "customOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.custom_oauth2_provider_config_input

        return {
            "customOauth2ProviderConfig": capo_bedrock_agentcore_control.types.custom_oauth2_provider_config_input.serialize_json(
                value["customOauth2ProviderConfig"]
            )
        }
    elif "googleOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.google_oauth2_provider_config_input

        return {
            "googleOauth2ProviderConfig": capo_bedrock_agentcore_control.types.google_oauth2_provider_config_input.serialize_json(
                value["googleOauth2ProviderConfig"]
            )
        }
    elif "githubOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.github_oauth2_provider_config_input

        return {
            "githubOauth2ProviderConfig": capo_bedrock_agentcore_control.types.github_oauth2_provider_config_input.serialize_json(
                value["githubOauth2ProviderConfig"]
            )
        }
    elif "slackOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.slack_oauth2_provider_config_input

        return {
            "slackOauth2ProviderConfig": capo_bedrock_agentcore_control.types.slack_oauth2_provider_config_input.serialize_json(
                value["slackOauth2ProviderConfig"]
            )
        }
    elif "salesforceOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.salesforce_oauth2_provider_config_input

        return {
            "salesforceOauth2ProviderConfig": capo_bedrock_agentcore_control.types.salesforce_oauth2_provider_config_input.serialize_json(
                value["salesforceOauth2ProviderConfig"]
            )
        }
    elif "microsoftOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.microsoft_oauth2_provider_config_input

        return {
            "microsoftOauth2ProviderConfig": capo_bedrock_agentcore_control.types.microsoft_oauth2_provider_config_input.serialize_json(
                value["microsoftOauth2ProviderConfig"]
            )
        }
    elif "atlassianOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.atlassian_oauth2_provider_config_input

        return {
            "atlassianOauth2ProviderConfig": capo_bedrock_agentcore_control.types.atlassian_oauth2_provider_config_input.serialize_json(
                value["atlassianOauth2ProviderConfig"]
            )
        }
    elif "linkedinOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.linkedin_oauth2_provider_config_input

        return {
            "linkedinOauth2ProviderConfig": capo_bedrock_agentcore_control.types.linkedin_oauth2_provider_config_input.serialize_json(
                value["linkedinOauth2ProviderConfig"]
            )
        }
    elif "includedOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.included_oauth2_provider_config_input

        return {
            "includedOauth2ProviderConfig": capo_bedrock_agentcore_control.types.included_oauth2_provider_config_input.serialize_json(
                value["includedOauth2ProviderConfig"]
            )
        }
    else:
        raise SerializationError("Oauth2ProviderConfigInput: no variant present")


def deserialize_json(data: dict) -> Oauth2ProviderConfigInput:
    if data.get("customOauth2ProviderConfig") is not None:
        import capo_bedrock_agentcore_control.types.custom_oauth2_provider_config_input

        return {
            "customOauth2ProviderConfig": capo_bedrock_agentcore_control.types.custom_oauth2_provider_config_input.deserialize_json(
                data["customOauth2ProviderConfig"]
            )
        }
    elif data.get("googleOauth2ProviderConfig") is not None:
        import capo_bedrock_agentcore_control.types.google_oauth2_provider_config_input

        return {
            "googleOauth2ProviderConfig": capo_bedrock_agentcore_control.types.google_oauth2_provider_config_input.deserialize_json(
                data["googleOauth2ProviderConfig"]
            )
        }
    elif data.get("githubOauth2ProviderConfig") is not None:
        import capo_bedrock_agentcore_control.types.github_oauth2_provider_config_input

        return {
            "githubOauth2ProviderConfig": capo_bedrock_agentcore_control.types.github_oauth2_provider_config_input.deserialize_json(
                data["githubOauth2ProviderConfig"]
            )
        }
    elif data.get("slackOauth2ProviderConfig") is not None:
        import capo_bedrock_agentcore_control.types.slack_oauth2_provider_config_input

        return {
            "slackOauth2ProviderConfig": capo_bedrock_agentcore_control.types.slack_oauth2_provider_config_input.deserialize_json(
                data["slackOauth2ProviderConfig"]
            )
        }
    elif data.get("salesforceOauth2ProviderConfig") is not None:
        import capo_bedrock_agentcore_control.types.salesforce_oauth2_provider_config_input

        return {
            "salesforceOauth2ProviderConfig": capo_bedrock_agentcore_control.types.salesforce_oauth2_provider_config_input.deserialize_json(
                data["salesforceOauth2ProviderConfig"]
            )
        }
    elif data.get("microsoftOauth2ProviderConfig") is not None:
        import capo_bedrock_agentcore_control.types.microsoft_oauth2_provider_config_input

        return {
            "microsoftOauth2ProviderConfig": capo_bedrock_agentcore_control.types.microsoft_oauth2_provider_config_input.deserialize_json(
                data["microsoftOauth2ProviderConfig"]
            )
        }
    elif data.get("atlassianOauth2ProviderConfig") is not None:
        import capo_bedrock_agentcore_control.types.atlassian_oauth2_provider_config_input

        return {
            "atlassianOauth2ProviderConfig": capo_bedrock_agentcore_control.types.atlassian_oauth2_provider_config_input.deserialize_json(
                data["atlassianOauth2ProviderConfig"]
            )
        }
    elif data.get("linkedinOauth2ProviderConfig") is not None:
        import capo_bedrock_agentcore_control.types.linkedin_oauth2_provider_config_input

        return {
            "linkedinOauth2ProviderConfig": capo_bedrock_agentcore_control.types.linkedin_oauth2_provider_config_input.deserialize_json(
                data["linkedinOauth2ProviderConfig"]
            )
        }
    elif data.get("includedOauth2ProviderConfig") is not None:
        import capo_bedrock_agentcore_control.types.included_oauth2_provider_config_input

        return {
            "includedOauth2ProviderConfig": capo_bedrock_agentcore_control.types.included_oauth2_provider_config_input.deserialize_json(
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
            "Oauth2ProviderConfigInput: no recognized variant key"
        )


def redact_sensitive(value: Oauth2ProviderConfigInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.custom_oauth2_provider_config_input

        out["customOauth2ProviderConfig"] = (
            capo_bedrock_agentcore_control.types.custom_oauth2_provider_config_input.redact_sensitive(
                value["customOauth2ProviderConfig"]
            )
        )
    if "googleOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.google_oauth2_provider_config_input

        out["googleOauth2ProviderConfig"] = (
            capo_bedrock_agentcore_control.types.google_oauth2_provider_config_input.redact_sensitive(
                value["googleOauth2ProviderConfig"]
            )
        )
    if "githubOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.github_oauth2_provider_config_input

        out["githubOauth2ProviderConfig"] = (
            capo_bedrock_agentcore_control.types.github_oauth2_provider_config_input.redact_sensitive(
                value["githubOauth2ProviderConfig"]
            )
        )
    if "slackOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.slack_oauth2_provider_config_input

        out["slackOauth2ProviderConfig"] = (
            capo_bedrock_agentcore_control.types.slack_oauth2_provider_config_input.redact_sensitive(
                value["slackOauth2ProviderConfig"]
            )
        )
    if "salesforceOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.salesforce_oauth2_provider_config_input

        out["salesforceOauth2ProviderConfig"] = (
            capo_bedrock_agentcore_control.types.salesforce_oauth2_provider_config_input.redact_sensitive(
                value["salesforceOauth2ProviderConfig"]
            )
        )
    if "microsoftOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.microsoft_oauth2_provider_config_input

        out["microsoftOauth2ProviderConfig"] = (
            capo_bedrock_agentcore_control.types.microsoft_oauth2_provider_config_input.redact_sensitive(
                value["microsoftOauth2ProviderConfig"]
            )
        )
    if "atlassianOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.atlassian_oauth2_provider_config_input

        out["atlassianOauth2ProviderConfig"] = (
            capo_bedrock_agentcore_control.types.atlassian_oauth2_provider_config_input.redact_sensitive(
                value["atlassianOauth2ProviderConfig"]
            )
        )
    if "linkedinOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.linkedin_oauth2_provider_config_input

        out["linkedinOauth2ProviderConfig"] = (
            capo_bedrock_agentcore_control.types.linkedin_oauth2_provider_config_input.redact_sensitive(
                value["linkedinOauth2ProviderConfig"]
            )
        )
    if "includedOauth2ProviderConfig" in value:
        import capo_bedrock_agentcore_control.types.included_oauth2_provider_config_input

        out["includedOauth2ProviderConfig"] = (
            capo_bedrock_agentcore_control.types.included_oauth2_provider_config_input.redact_sensitive(
                value["includedOauth2ProviderConfig"]
            )
        )
    return out
