"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#ApplicationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.__list_of__string
    import capo_serverlessapplicationrepository.types.__string


class ApplicationSummary(TypedDict, closed=True):
    application_id: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The application Amazon Resource Name (ARN).</p>"""
    author: NotRequired["capo_serverlessapplicationrepository.types.__string.__string"]
    """<p>The name of the author publishing the app.</p><p>Minimum length=1. Maximum length=127.</p><p>Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";</p>"""
    creation_time: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The date and time this resource was created.</p>"""
    description: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The description of the application.</p><p>Minimum length=1. Maximum length=256</p>"""
    home_page_url: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A URL with more information about the application, for example the location of your GitHub repository for the application.</p>"""
    labels: NotRequired[
        "capo_serverlessapplicationrepository.types.__list_of__string.__listOf__string"
    ]
    r"""<p>Labels to improve discovery of apps in search results.</p><p>Minimum length=1. Maximum length=127. Maximum number of labels: 10</p><p>Pattern: "^[a-zA-Z0-9+\\-_:\\/@]+$";</p>"""
    name: NotRequired["capo_serverlessapplicationrepository.types.__string.__string"]
    r"""<p>The name of the application.</p><p>Minimum length=1. Maximum length=140</p><p>Pattern: "[a-zA-Z0-9\\-]+";</p>"""
    spdx_license_id: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A valid identifier from <a href="https://spdx.org/licenses/">https://spdx.org/licenses/</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationSummary) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "author" in value:
        out["author"] = value["author"]
    if "creation_time" in value:
        out["creationTime"] = value["creation_time"]
    if "description" in value:
        out["description"] = value["description"]
    if "home_page_url" in value:
        out["homePageUrl"] = value["home_page_url"]
    if "labels" in value:
        import capo_serverlessapplicationrepository.types.__list_of__string

        out["labels"] = (
            capo_serverlessapplicationrepository.types.__list_of__string.serialize_json(
                value["labels"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "spdx_license_id" in value:
        out["spdxLicenseId"] = value["spdx_license_id"]
    return out


def deserialize_json(data: dict) -> ApplicationSummary:
    out: ApplicationSummary = {}  # type: ignore[typeddict-item]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    if data.get("author") is not None:
        out["author"] = data["author"]
    if data.get("creationTime") is not None:
        out["creation_time"] = data["creationTime"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("homePageUrl") is not None:
        out["home_page_url"] = data["homePageUrl"]
    if data.get("labels") is not None:
        import capo_serverlessapplicationrepository.types.__list_of__string

        out["labels"] = (
            capo_serverlessapplicationrepository.types.__list_of__string.deserialize_json(
                data["labels"]
            )
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("spdxLicenseId") is not None:
        out["spdx_license_id"] = data["spdxLicenseId"]
    return out
