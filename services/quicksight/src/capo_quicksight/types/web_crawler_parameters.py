"""Generated from Smithy shape ``com.amazonaws.quicksight#WebCrawlerParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.host
    import capo_quicksight.types.optional_port
    import capo_quicksight.types.site_base_url
    import capo_quicksight.types.web_crawler_auth_type
    import capo_quicksight.types.xpath_fields


class WebCrawlerParameters(TypedDict, closed=True):
    web_crawler_auth_type: (
        "capo_quicksight.types.web_crawler_auth_type.WebCrawlerAuthType"
    )
    """<p>The authentication type for the web crawler. The type can be one of the following:</p> <ul> <li> <p> <code>NO_AUTH</code>: No authentication required.</p> </li> <li> <p> <code>BASIC_AUTH</code>: Basic authentication using username and password.</p> </li> <li> <p> <code>SAML</code>: SAML-based authentication.</p> </li> <li> <p> <code>FORM</code>: Form-based authentication.</p> </li> </ul>"""
    username_field_xpath: NotRequired["capo_quicksight.types.xpath_fields.XpathFields"]
    """<p>The XPath expression for locating the username field on the login page.</p>"""
    password_field_xpath: NotRequired["capo_quicksight.types.xpath_fields.XpathFields"]
    """<p>The XPath expression for locating the password field on the login page.</p>"""
    username_button_xpath: NotRequired["capo_quicksight.types.xpath_fields.XpathFields"]
    """<p>The XPath expression for locating the username submit button on the login page.</p>"""
    password_button_xpath: NotRequired["capo_quicksight.types.xpath_fields.XpathFields"]
    """<p>The XPath expression for locating the password submit button on the login page.</p>"""
    login_page_url: NotRequired["capo_quicksight.types.site_base_url.SiteBaseUrl"]
    """<p>The URL of the login page for the web crawler to authenticate.</p>"""
    web_proxy_host_name: NotRequired["capo_quicksight.types.host.Host"]
    """<p>The hostname of the web proxy server for the web crawler.</p>"""
    web_proxy_port_number: "capo_quicksight.types.optional_port.OptionalPort"
    """<p>The port number of the web proxy server for the web crawler.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebCrawlerParameters) -> dict:
    out: dict = {}
    import capo_quicksight.types.web_crawler_auth_type

    out["WebCrawlerAuthType"] = (
        capo_quicksight.types.web_crawler_auth_type.serialize_json(
            value["web_crawler_auth_type"]
        )
    )
    if "username_field_xpath" in value:
        out["UsernameFieldXpath"] = value["username_field_xpath"]
    if "password_field_xpath" in value:
        out["PasswordFieldXpath"] = value["password_field_xpath"]
    if "username_button_xpath" in value:
        out["UsernameButtonXpath"] = value["username_button_xpath"]
    if "password_button_xpath" in value:
        out["PasswordButtonXpath"] = value["password_button_xpath"]
    if "login_page_url" in value:
        out["LoginPageUrl"] = value["login_page_url"]
    if "web_proxy_host_name" in value:
        out["WebProxyHostName"] = value["web_proxy_host_name"]
    out["WebProxyPortNumber"] = value.get("web_proxy_port_number", 0)
    return out


def deserialize_json(data: dict) -> WebCrawlerParameters:
    out: WebCrawlerParameters = {}  # type: ignore[typeddict-item]
    if data.get("WebCrawlerAuthType") is not None:
        import capo_quicksight.types.web_crawler_auth_type

        out["web_crawler_auth_type"] = (
            capo_quicksight.types.web_crawler_auth_type.deserialize_json(
                data["WebCrawlerAuthType"]
            )
        )
    else:
        import typing

        out["web_crawler_auth_type"] = typing.cast(
            "capo_quicksight.types.web_crawler_auth_type.WebCrawlerAuthType", ""
        )
    if data.get("UsernameFieldXpath") is not None:
        out["username_field_xpath"] = data["UsernameFieldXpath"]
    if data.get("PasswordFieldXpath") is not None:
        out["password_field_xpath"] = data["PasswordFieldXpath"]
    if data.get("UsernameButtonXpath") is not None:
        out["username_button_xpath"] = data["UsernameButtonXpath"]
    if data.get("PasswordButtonXpath") is not None:
        out["password_button_xpath"] = data["PasswordButtonXpath"]
    if data.get("LoginPageUrl") is not None:
        out["login_page_url"] = data["LoginPageUrl"]
    if data.get("WebProxyHostName") is not None:
        out["web_proxy_host_name"] = data["WebProxyHostName"]
    if data.get("WebProxyPortNumber") is not None:
        out["web_proxy_port_number"] = data["WebProxyPortNumber"]
    else:
        out["web_proxy_port_number"] = 0
    return out
