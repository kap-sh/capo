"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#GetApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.__boolean
    import capo_serverlessapplicationrepository.types.__list_of__string
    import capo_serverlessapplicationrepository.types.__string
    import capo_serverlessapplicationrepository.types.version


class GetApplicationResponse(TypedDict, closed=True):
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
    is_verified_author: NotRequired[
        "capo_serverlessapplicationrepository.types.__boolean.__boolean"
    ]
    """<p>Whether the author of this application has been verified. This means means that AWS has made a good faith review, as a reasonable and prudent service provider, of the information provided by the requester and has confirmed that the requester's identity is as claimed.</p>"""
    labels: NotRequired[
        "capo_serverlessapplicationrepository.types.__list_of__string.__listOf__string"
    ]
    r"""<p>Labels to improve discovery of apps in search results.</p><p>Minimum length=1. Maximum length=127. Maximum number of labels: 10</p><p>Pattern: "^[a-zA-Z0-9+\\-_:\\/@]+$";</p>"""
    license_url: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A link to a license file of the app that matches the spdxLicenseID value of your application.</p><p>Maximum size 5 MB</p>"""
    name: NotRequired["capo_serverlessapplicationrepository.types.__string.__string"]
    r"""<p>The name of the application.</p><p>Minimum length=1. Maximum length=140</p><p>Pattern: "[a-zA-Z0-9\\-]+";</p>"""
    readme_url: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A link to the readme file in Markdown language that contains a more detailed description of the application and how it works.</p><p>Maximum size 5 MB</p>"""
    spdx_license_id: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A valid identifier from https://spdx.org/licenses/.</p>"""
    verified_author_url: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The URL to the public profile of a verified author. This URL is submitted by the author.</p>"""
    version: NotRequired["capo_serverlessapplicationrepository.types.version.Version"]
    """<p>Version information about the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationResponse) -> dict:
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
    if "is_verified_author" in value:
        out["isVerifiedAuthor"] = value["is_verified_author"]
    if "labels" in value:
        import capo_serverlessapplicationrepository.types.__list_of__string

        out["labels"] = (
            capo_serverlessapplicationrepository.types.__list_of__string.serialize_json(
                value["labels"]
            )
        )
    if "license_url" in value:
        out["licenseUrl"] = value["license_url"]
    if "name" in value:
        out["name"] = value["name"]
    if "readme_url" in value:
        out["readmeUrl"] = value["readme_url"]
    if "spdx_license_id" in value:
        out["spdxLicenseId"] = value["spdx_license_id"]
    if "verified_author_url" in value:
        out["verifiedAuthorUrl"] = value["verified_author_url"]
    if "version" in value:
        import capo_serverlessapplicationrepository.types.version

        out["version"] = (
            capo_serverlessapplicationrepository.types.version.serialize_json(
                value["version"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetApplicationResponse:
    out: GetApplicationResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("isVerifiedAuthor") is not None:
        out["is_verified_author"] = data["isVerifiedAuthor"]
    if data.get("labels") is not None:
        import capo_serverlessapplicationrepository.types.__list_of__string

        out["labels"] = (
            capo_serverlessapplicationrepository.types.__list_of__string.deserialize_json(
                data["labels"]
            )
        )
    if data.get("licenseUrl") is not None:
        out["license_url"] = data["licenseUrl"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("readmeUrl") is not None:
        out["readme_url"] = data["readmeUrl"]
    if data.get("spdxLicenseId") is not None:
        out["spdx_license_id"] = data["spdxLicenseId"]
    if data.get("verifiedAuthorUrl") is not None:
        out["verified_author_url"] = data["verifiedAuthorUrl"]
    if data.get("version") is not None:
        import capo_serverlessapplicationrepository.types.version

        out["version"] = (
            capo_serverlessapplicationrepository.types.version.deserialize_json(
                data["version"]
            )
        )
    return out
