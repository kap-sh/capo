"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedWebAppCustomization``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.arn
    import capo_transfer.types.web_app_favicon_file
    import capo_transfer.types.web_app_id
    import capo_transfer.types.web_app_logo_file
    import capo_transfer.types.web_app_title


class DescribedWebAppCustomization(TypedDict, closed=True):
    arn: "capo_transfer.types.arn.Arn"
    """<p>Returns the Amazon Resource Name (ARN) for the web app.</p>"""
    web_app_id: "capo_transfer.types.web_app_id.WebAppId"
    """<p>Returns the unique identifier for your web app.</p>"""
    title: NotRequired["capo_transfer.types.web_app_title.WebAppTitle"]
    """<p>Returns the page title that you defined for your web app.</p>"""
    logo_file: NotRequired["capo_transfer.types.web_app_logo_file.WebAppLogoFile"]
    """<p>Returns a logo file data string (in base64 encoding).</p>"""
    favicon_file: NotRequired[
        "capo_transfer.types.web_app_favicon_file.WebAppFaviconFile"
    ]
    """<p>Returns an icon file data string (in base64 encoding).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedWebAppCustomization) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["WebAppId"] = value["web_app_id"]
    if "title" in value:
        out["Title"] = value["title"]
    if "logo_file" in value:
        import capo_transfer.types.web_app_logo_file

        out["LogoFile"] = capo_transfer.types.web_app_logo_file.serialize_aws_json_1_1(
            value["logo_file"]
        )
    if "favicon_file" in value:
        import capo_transfer.types.web_app_favicon_file

        out["FaviconFile"] = (
            capo_transfer.types.web_app_favicon_file.serialize_aws_json_1_1(
                value["favicon_file"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribedWebAppCustomization:
    out: DescribedWebAppCustomization = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("WebAppId") is not None:
        out["web_app_id"] = data["WebAppId"]
    else:
        out["web_app_id"] = ""
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("LogoFile") is not None:
        import capo_transfer.types.web_app_logo_file

        out["logo_file"] = (
            capo_transfer.types.web_app_logo_file.deserialize_aws_json_1_1(
                data["LogoFile"]
            )
        )
    if data.get("FaviconFile") is not None:
        import capo_transfer.types.web_app_favicon_file

        out["favicon_file"] = (
            capo_transfer.types.web_app_favicon_file.deserialize_aws_json_1_1(
                data["FaviconFile"]
            )
        )
    return out


def redact_sensitive(value: DescribedWebAppCustomization) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "logo_file" in value:
        out["logo_file"] = "*** Sensitive Data Redacted ***"
    if "favicon_file" in value:
        out["favicon_file"] = "*** Sensitive Data Redacted ***"
    return out
