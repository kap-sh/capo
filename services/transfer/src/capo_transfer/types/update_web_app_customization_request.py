"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateWebAppCustomizationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.web_app_favicon_file
    import capo_transfer.types.web_app_id
    import capo_transfer.types.web_app_logo_file
    import capo_transfer.types.web_app_title


class UpdateWebAppCustomizationRequest(TypedDict, closed=True):
    web_app_id: "capo_transfer.types.web_app_id.WebAppId"
    """<p>Provide the identifier of the web app that you are updating.</p>"""
    title: NotRequired["capo_transfer.types.web_app_title.WebAppTitle"]
    """<p>Provide an updated title.</p>"""
    logo_file: NotRequired["capo_transfer.types.web_app_logo_file.WebAppLogoFile"]
    """<p>Specify logo file data string (in base64 encoding).</p>"""
    favicon_file: NotRequired[
        "capo_transfer.types.web_app_favicon_file.WebAppFaviconFile"
    ]
    """<p>Specify an icon file data string (in base64 encoding).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWebAppCustomizationRequest) -> dict:
    out: dict = {}
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


def deserialize_aws_json_1_1(data: dict) -> UpdateWebAppCustomizationRequest:
    out: UpdateWebAppCustomizationRequest = {}  # type: ignore[typeddict-item]
    if data.get("WebAppId") is not None:
        out["web_app_id"] = data["WebAppId"]
    else:
        raise DeserializationError(
            "UpdateWebAppCustomizationRequest.web_app_id required"
        )
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


def redact_sensitive(value: UpdateWebAppCustomizationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "logo_file" in value:
        out["logo_file"] = "*** Sensitive Data Redacted ***"
    if "favicon_file" in value:
        out["favicon_file"] = "*** Sensitive Data Redacted ***"
    return out
