"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateWebExperienceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.browser_extension_configuration
    import capo_qbusiness.types.client_token
    import capo_qbusiness.types.customization_configuration
    import capo_qbusiness.types.identity_provider_configuration
    import capo_qbusiness.types.role_arn
    import capo_qbusiness.types.tags
    import capo_qbusiness.types.web_experience_origins
    import capo_qbusiness.types.web_experience_sample_prompts_control_mode
    import capo_qbusiness.types.web_experience_subtitle
    import capo_qbusiness.types.web_experience_title
    import capo_qbusiness.types.web_experience_welcome_message


class CreateWebExperienceRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business web experience.</p>"""
    title: NotRequired["capo_qbusiness.types.web_experience_title.WebExperienceTitle"]
    """<p>The title for your Amazon Q Business web experience.</p>"""
    subtitle: NotRequired[
        "capo_qbusiness.types.web_experience_subtitle.WebExperienceSubtitle"
    ]
    """<p>A subtitle to personalize your Amazon Q Business web experience.</p>"""
    welcome_message: NotRequired[
        "capo_qbusiness.types.web_experience_welcome_message.WebExperienceWelcomeMessage"
    ]
    """<p>The customized welcome message for end users of an Amazon Q Business web experience.</p>"""
    sample_prompts_control_mode: NotRequired[
        "capo_qbusiness.types.web_experience_sample_prompts_control_mode.WebExperienceSamplePromptsControlMode"
    ]
    """<p>Determines whether sample prompts are enabled in the web experience for an end user.</p>"""
    origins: NotRequired[
        "capo_qbusiness.types.web_experience_origins.WebExperienceOrigins"
    ]
    """<p>Sets the website domain origins that are allowed to embed the Amazon Q Business web experience. The <i>domain origin</i> refers to the base URL for accessing a website including the protocol (<code>http/https</code>), the domain name, and the port number (if specified). </p> <note> <p>You must only submit a <i>base URL</i> and not a full path. For example, <code>https://docs.aws.amazon.com</code>.</p> </note>"""
    role_arn: NotRequired["capo_qbusiness.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the service role attached to your web experience.</p> <note> <p>The <code>roleArn</code> parameter is required when your Amazon Q Business application is created with IAM Identity Center. It is not required for SAML-based applications.</p> </note>"""
    tags: NotRequired["capo_qbusiness.types.tags.Tags"]
    """<p>A list of key-value pairs that identify or categorize your Amazon Q Business web experience. You can also use tags to help control access to the web experience. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>"""
    client_token: NotRequired["capo_qbusiness.types.client_token.ClientToken"]
    """<p>A token you provide to identify a request to create an Amazon Q Business web experience. </p>"""
    identity_provider_configuration: NotRequired[
        "capo_qbusiness.types.identity_provider_configuration.IdentityProviderConfiguration"
    ]
    """<p>Information about the identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.</p>"""
    browser_extension_configuration: NotRequired[
        "capo_qbusiness.types.browser_extension_configuration.BrowserExtensionConfiguration"
    ]
    """<p>The browser extension configuration for an Amazon Q Business web experience.</p> <note> <p> For Amazon Q Business application using external OIDC-compliant identity providers (IdPs). The IdP administrator must add the browser extension sign-in redirect URLs to the IdP application. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/browser-extensions.html">Configure external OIDC identity provider for your browser extensions.</a>. </p> </note>"""
    customization_configuration: NotRequired[
        "capo_qbusiness.types.customization_configuration.CustomizationConfiguration"
    ]
    """<p>Sets the custom logo, favicon, font, and color used in the Amazon Q web experience. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWebExperienceRequest) -> dict:
    out: dict = {}
    if "title" in value:
        out["title"] = value["title"]
    if "subtitle" in value:
        out["subtitle"] = value["subtitle"]
    if "welcome_message" in value:
        out["welcomeMessage"] = value["welcome_message"]
    if "sample_prompts_control_mode" in value:
        import capo_qbusiness.types.web_experience_sample_prompts_control_mode

        out["samplePromptsControlMode"] = (
            capo_qbusiness.types.web_experience_sample_prompts_control_mode.serialize_json(
                value["sample_prompts_control_mode"]
            )
        )
    if "origins" in value:
        import capo_qbusiness.types.web_experience_origins

        out["origins"] = capo_qbusiness.types.web_experience_origins.serialize_json(
            value["origins"]
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_qbusiness.types.tags

        out["tags"] = capo_qbusiness.types.tags.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "identity_provider_configuration" in value:
        import capo_qbusiness.types.identity_provider_configuration

        out["identityProviderConfiguration"] = (
            capo_qbusiness.types.identity_provider_configuration.serialize_json(
                value["identity_provider_configuration"]
            )
        )
    if "browser_extension_configuration" in value:
        import capo_qbusiness.types.browser_extension_configuration

        out["browserExtensionConfiguration"] = (
            capo_qbusiness.types.browser_extension_configuration.serialize_json(
                value["browser_extension_configuration"]
            )
        )
    if "customization_configuration" in value:
        import capo_qbusiness.types.customization_configuration

        out["customizationConfiguration"] = (
            capo_qbusiness.types.customization_configuration.serialize_json(
                value["customization_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateWebExperienceRequest:
    out: CreateWebExperienceRequest = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("subtitle") is not None:
        out["subtitle"] = data["subtitle"]
    if data.get("welcomeMessage") is not None:
        out["welcome_message"] = data["welcomeMessage"]
    if data.get("samplePromptsControlMode") is not None:
        import capo_qbusiness.types.web_experience_sample_prompts_control_mode

        out["sample_prompts_control_mode"] = (
            capo_qbusiness.types.web_experience_sample_prompts_control_mode.deserialize_json(
                data["samplePromptsControlMode"]
            )
        )
    if data.get("origins") is not None:
        import capo_qbusiness.types.web_experience_origins

        out["origins"] = capo_qbusiness.types.web_experience_origins.deserialize_json(
            data["origins"]
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("tags") is not None:
        import capo_qbusiness.types.tags

        out["tags"] = capo_qbusiness.types.tags.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("identityProviderConfiguration") is not None:
        import capo_qbusiness.types.identity_provider_configuration

        out["identity_provider_configuration"] = (
            capo_qbusiness.types.identity_provider_configuration.deserialize_json(
                data["identityProviderConfiguration"]
            )
        )
    if data.get("browserExtensionConfiguration") is not None:
        import capo_qbusiness.types.browser_extension_configuration

        out["browser_extension_configuration"] = (
            capo_qbusiness.types.browser_extension_configuration.deserialize_json(
                data["browserExtensionConfiguration"]
            )
        )
    if data.get("customizationConfiguration") is not None:
        import capo_qbusiness.types.customization_configuration

        out["customization_configuration"] = (
            capo_qbusiness.types.customization_configuration.deserialize_json(
                data["customizationConfiguration"]
            )
        )
    return out
