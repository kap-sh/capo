"""Generated from Smithy shape ``com.amazonaws.workspaces#DefaultImportClientBrandingAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.client_email
    import capo_workspaces.types.client_url
    import capo_workspaces.types.default_logo
    import capo_workspaces.types.login_message


class DefaultImportClientBrandingAttributes(TypedDict, closed=True):
    logo: NotRequired["capo_workspaces.types.default_logo.DefaultLogo"]
    """<p>The logo. The only image format accepted is a binary data object that is converted from a <code>.png</code> file.</p>"""
    support_email: NotRequired["capo_workspaces.types.client_email.ClientEmail"]
    """<p>The support email. The company's customer support email address.</p> <note> <ul> <li> <p>In each platform type, the <code>SupportEmail</code> and <code>SupportLink</code> parameters are mutually exclusive. You can specify one parameter for each platform type, but not both.</p> </li> <li> <p>The default email is <code>workspaces-feedback@amazon.com</code>.</p> </li> </ul> </note>"""
    support_link: NotRequired["capo_workspaces.types.client_url.ClientUrl"]
    """<p>The support link. The link for the company's customer support page for their WorkSpace.</p> <note> <ul> <li> <p>In each platform type, the <code>SupportEmail</code> and <code>SupportLink</code> parameters are mutually exclusive. You can specify one parameter for each platform type, but not both.</p> </li> <li> <p>The default support link is <code>workspaces-feedback@amazon.com</code>.</p> </li> </ul> </note>"""
    forgot_password_link: NotRequired["capo_workspaces.types.client_url.ClientUrl"]
    """<p>The forgotten password link. This is the web address that users can go to if they forget the password for their WorkSpace.</p>"""
    login_message: NotRequired["capo_workspaces.types.login_message.LoginMessage"]
    """<p>The login message. Specified as a key value pair, in which the key is a locale and the value is the localized message for that locale. The only key supported is <code>en_US</code>. The HTML tags supported include the following: <code>a, b, blockquote, br, cite, code, dd, dl, dt, div, em, i, li, ol, p, pre, q, small, span, strike, strong, sub, sup, u, ul</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DefaultImportClientBrandingAttributes) -> dict:
    out: dict = {}
    if "logo" in value:
        import capo_workspaces.types.default_logo

        out["Logo"] = capo_workspaces.types.default_logo.serialize_aws_json_1_1(
            value["logo"]
        )
    if "support_email" in value:
        out["SupportEmail"] = value["support_email"]
    if "support_link" in value:
        out["SupportLink"] = value["support_link"]
    if "forgot_password_link" in value:
        out["ForgotPasswordLink"] = value["forgot_password_link"]
    if "login_message" in value:
        import capo_workspaces.types.login_message

        out["LoginMessage"] = (
            capo_workspaces.types.login_message.serialize_aws_json_1_1(
                value["login_message"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DefaultImportClientBrandingAttributes:
    out: DefaultImportClientBrandingAttributes = {}  # type: ignore[typeddict-item]
    if data.get("Logo") is not None:
        import capo_workspaces.types.default_logo

        out["logo"] = capo_workspaces.types.default_logo.deserialize_aws_json_1_1(
            data["Logo"]
        )
    if data.get("SupportEmail") is not None:
        out["support_email"] = data["SupportEmail"]
    if data.get("SupportLink") is not None:
        out["support_link"] = data["SupportLink"]
    if data.get("ForgotPasswordLink") is not None:
        out["forgot_password_link"] = data["ForgotPasswordLink"]
    if data.get("LoginMessage") is not None:
        import capo_workspaces.types.login_message

        out["login_message"] = (
            capo_workspaces.types.login_message.deserialize_aws_json_1_1(
                data["LoginMessage"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DefaultImportClientBrandingAttributes) -> dict:
    out: dict = {}
    if "logo" in value:
        import capo_workspaces.types.default_logo

        out["Logo"] = capo_workspaces.types.default_logo.serialize_cbor(value["logo"])
    if "support_email" in value:
        out["SupportEmail"] = value["support_email"]
    if "support_link" in value:
        out["SupportLink"] = value["support_link"]
    if "forgot_password_link" in value:
        out["ForgotPasswordLink"] = value["forgot_password_link"]
    if "login_message" in value:
        import capo_workspaces.types.login_message

        out["LoginMessage"] = capo_workspaces.types.login_message.serialize_cbor(
            value["login_message"]
        )
    return out


def deserialize_cbor(data: dict) -> DefaultImportClientBrandingAttributes:
    out: DefaultImportClientBrandingAttributes = {}  # type: ignore[typeddict-item]
    if data.get("Logo") is not None:
        import capo_workspaces.types.default_logo

        out["logo"] = capo_workspaces.types.default_logo.deserialize_cbor(data["Logo"])
    if data.get("SupportEmail") is not None:
        out["support_email"] = data["SupportEmail"]
    if data.get("SupportLink") is not None:
        out["support_link"] = data["SupportLink"]
    if data.get("ForgotPasswordLink") is not None:
        out["forgot_password_link"] = data["ForgotPasswordLink"]
    if data.get("LoginMessage") is not None:
        import capo_workspaces.types.login_message

        out["login_message"] = capo_workspaces.types.login_message.deserialize_cbor(
            data["LoginMessage"]
        )
    return out
