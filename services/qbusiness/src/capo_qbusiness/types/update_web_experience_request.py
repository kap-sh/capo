"""Generated from Smithy shape ``com.amazonaws.qbusiness#UpdateWebExperienceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.browser_extension_configuration
    import capo_qbusiness.types.customization_configuration
    import capo_qbusiness.types.identity_provider_configuration
    import capo_qbusiness.types.role_arn
    import capo_qbusiness.types.web_experience_auth_configuration
    import capo_qbusiness.types.web_experience_id
    import capo_qbusiness.types.web_experience_origins
    import capo_qbusiness.types.web_experience_sample_prompts_control_mode
    import capo_qbusiness.types.web_experience_subtitle
    import capo_qbusiness.types.web_experience_title
    import capo_qbusiness.types.web_experience_welcome_message


class UpdateWebExperienceRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application attached to the web experience.</p>"""
    web_experience_id: "capo_qbusiness.types.web_experience_id.WebExperienceId"
    """<p>The identifier of the Amazon Q Business web experience.</p>"""
    role_arn: NotRequired["capo_qbusiness.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the role with permission to access the Amazon Q Business web experience and required resources.</p>"""
    authentication_configuration: NotRequired[
        "capo_qbusiness.types.web_experience_auth_configuration.WebExperienceAuthConfiguration"
    ]
    """<p>The authentication configuration of the Amazon Q Business web experience.</p>"""
    title: NotRequired["capo_qbusiness.types.web_experience_title.WebExperienceTitle"]
    """<p>The title of the Amazon Q Business web experience.</p>"""
    subtitle: NotRequired[
        "capo_qbusiness.types.web_experience_subtitle.WebExperienceSubtitle"
    ]
    """<p>The subtitle of the Amazon Q Business web experience.</p>"""
    welcome_message: NotRequired[
        "capo_qbusiness.types.web_experience_welcome_message.WebExperienceWelcomeMessage"
    ]
    """<p>A customized welcome message for an end user in an Amazon Q Business web experience.</p>"""
    sample_prompts_control_mode: NotRequired[
        "capo_qbusiness.types.web_experience_sample_prompts_control_mode.WebExperienceSamplePromptsControlMode"
    ]
    """<p>Determines whether sample prompts are enabled in the web experience for an end user.</p>"""
    identity_provider_configuration: NotRequired[
        "capo_qbusiness.types.identity_provider_configuration.IdentityProviderConfiguration"
    ]
    """<p>Information about the identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.</p>"""
    origins: NotRequired[
        "capo_qbusiness.types.web_experience_origins.WebExperienceOrigins"
    ]
    """<p>Updates the website domain origins that are allowed to embed the Amazon Q Business web experience. The <i>domain origin</i> refers to the <i>base URL</i> for accessing a website including the protocol (<code>http/https</code>), the domain name, and the port number (if specified).</p> <note> <ul> <li> <p>Any values except <code>null</code> submitted as part of this update will replace all previous values.</p> </li> <li> <p>You must only submit a <i>base URL</i> and not a full path. For example, <code>https://docs.aws.amazon.com</code>.</p> </li> </ul> </note>"""
    browser_extension_configuration: NotRequired[
        "capo_qbusiness.types.browser_extension_configuration.BrowserExtensionConfiguration"
    ]
    """<p>The browser extension configuration for an Amazon Q Business web experience.</p> <note> <p> For Amazon Q Business application using external OIDC-compliant identity providers (IdPs). The IdP administrator must add the browser extension sign-in redirect URLs to the IdP application. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/browser-extensions.html">Configure external OIDC identity provider for your browser extensions.</a>. </p> </note>"""
    customization_configuration: NotRequired[
        "capo_qbusiness.types.customization_configuration.CustomizationConfiguration"
    ]
    """<p>Updates the custom logo, favicon, font, and color used in the Amazon Q web experience. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWebExperienceRequest) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "authentication_configuration" in value:
        import capo_qbusiness.types.web_experience_auth_configuration

        out["authenticationConfiguration"] = (
            capo_qbusiness.types.web_experience_auth_configuration.serialize_json(
                value["authentication_configuration"]
            )
        )
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
    if "identity_provider_configuration" in value:
        import capo_qbusiness.types.identity_provider_configuration

        out["identityProviderConfiguration"] = (
            capo_qbusiness.types.identity_provider_configuration.serialize_json(
                value["identity_provider_configuration"]
            )
        )
    if "origins" in value:
        import capo_qbusiness.types.web_experience_origins

        out["origins"] = capo_qbusiness.types.web_experience_origins.serialize_json(
            value["origins"]
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


def deserialize_json(data: dict) -> UpdateWebExperienceRequest:
    out: UpdateWebExperienceRequest = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("authenticationConfiguration") is not None:
        import capo_qbusiness.types.web_experience_auth_configuration

        out["authentication_configuration"] = (
            capo_qbusiness.types.web_experience_auth_configuration.deserialize_json(
                data["authenticationConfiguration"]
            )
        )
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
    if data.get("identityProviderConfiguration") is not None:
        import capo_qbusiness.types.identity_provider_configuration

        out["identity_provider_configuration"] = (
            capo_qbusiness.types.identity_provider_configuration.deserialize_json(
                data["identityProviderConfiguration"]
            )
        )
    if data.get("origins") is not None:
        import capo_qbusiness.types.web_experience_origins

        out["origins"] = capo_qbusiness.types.web_experience_origins.deserialize_json(
            data["origins"]
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
