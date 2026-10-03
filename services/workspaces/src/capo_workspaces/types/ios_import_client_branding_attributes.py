"""Generated from Smithy shape ``com.amazonaws.workspaces#IosImportClientBrandingAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.client_email
    import capo_workspaces.types.client_url
    import capo_workspaces.types.ios2_x_logo
    import capo_workspaces.types.ios3_x_logo
    import capo_workspaces.types.ios_logo
    import capo_workspaces.types.login_message


class IosImportClientBrandingAttributes(TypedDict, closed=True):
    logo: NotRequired["capo_workspaces.types.ios_logo.IosLogo"]
    """<p>The logo. This is the standard-resolution display that has a 1:1 pixel density (or @1x), where one pixel is equal to one point. The only image format accepted is a binary data object that is converted from a <code>.png</code> file.</p>"""
    logo2x: NotRequired["capo_workspaces.types.ios2_x_logo.Ios2XLogo"]
    """<p>The @2x version of the logo. This is the higher resolution display that offers a scale factor of 2.0 (or @2x). The only image format accepted is a binary data object that is converted from a <code>.png</code> file.</p> <note> <p> For more information about iOS image size and resolution, see <a href="https://developer.apple.com/design/human-interface-guidelines/ios/icons-and-images/image-size-and-resolution/">Image Size and Resolution </a> in the <i>Apple Human Interface Guidelines</i>.</p> </note>"""
    logo3x: NotRequired["capo_workspaces.types.ios3_x_logo.Ios3XLogo"]
    """<p>The @3x version of the logo. This is the higher resolution display that offers a scale factor of 3.0 (or @3x). The only image format accepted is a binary data object that is converted from a <code>.png</code> file.</p> <note> <p> For more information about iOS image size and resolution, see <a href="https://developer.apple.com/design/human-interface-guidelines/ios/icons-and-images/image-size-and-resolution/">Image Size and Resolution </a> in the <i>Apple Human Interface Guidelines</i>.</p> </note>"""
    support_email: NotRequired["capo_workspaces.types.client_email.ClientEmail"]
    """<p>The support email. The company's customer support email address.</p> <note> <ul> <li> <p>In each platform type, the <code>SupportEmail</code> and <code>SupportLink</code> parameters are mutually exclusive. You can specify one parameter for each platform type, but not both.</p> </li> <li> <p>The default email is <code>workspaces-feedback@amazon.com</code>.</p> </li> </ul> </note>"""
    support_link: NotRequired["capo_workspaces.types.client_url.ClientUrl"]
    """<p>The support link. The link for the company's customer support page for their WorkSpace.</p> <note> <ul> <li> <p>In each platform type, the <code>SupportEmail</code> and <code>SupportLink</code> parameters are mutually exclusive. You can specify one parameter for each platform type, but not both.</p> </li> <li> <p>The default support link is <code>workspaces-feedback@amazon.com</code>.</p> </li> </ul> </note>"""
    forgot_password_link: NotRequired["capo_workspaces.types.client_url.ClientUrl"]
    """<p>The forgotten password link. This is the web address that users can go to if they forget the password for their WorkSpace.</p>"""
    login_message: NotRequired["capo_workspaces.types.login_message.LoginMessage"]
    """<p>The login message. Specified as a key value pair, in which the key is a locale and the value is the localized message for that locale. The only key supported is <code>en_US</code>. The HTML tags supported include the following: <code>a, b, blockquote, br, cite, code, dd, dl, dt, div, em, i, li, ol, p, pre, q, small, span, strike, strong, sub, sup, u, ul</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IosImportClientBrandingAttributes) -> dict:
    out: dict = {}
    if "logo" in value:
        import capo_workspaces.types.ios_logo

        out["Logo"] = capo_workspaces.types.ios_logo.serialize_aws_json_1_1(
            value["logo"]
        )
    if "logo2x" in value:
        import capo_workspaces.types.ios2_x_logo

        out["Logo2x"] = capo_workspaces.types.ios2_x_logo.serialize_aws_json_1_1(
            value["logo2x"]
        )
    if "logo3x" in value:
        import capo_workspaces.types.ios3_x_logo

        out["Logo3x"] = capo_workspaces.types.ios3_x_logo.serialize_aws_json_1_1(
            value["logo3x"]
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


def deserialize_aws_json_1_1(data: dict) -> IosImportClientBrandingAttributes:
    out: IosImportClientBrandingAttributes = {}  # type: ignore[typeddict-item]
    if data.get("Logo") is not None:
        import capo_workspaces.types.ios_logo

        out["logo"] = capo_workspaces.types.ios_logo.deserialize_aws_json_1_1(
            data["Logo"]
        )
    if data.get("Logo2x") is not None:
        import capo_workspaces.types.ios2_x_logo

        out["logo2x"] = capo_workspaces.types.ios2_x_logo.deserialize_aws_json_1_1(
            data["Logo2x"]
        )
    if data.get("Logo3x") is not None:
        import capo_workspaces.types.ios3_x_logo

        out["logo3x"] = capo_workspaces.types.ios3_x_logo.deserialize_aws_json_1_1(
            data["Logo3x"]
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
