"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#UpdateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.__list_of__string
    import capo_serverlessapplicationrepository.types.__string


class UpdateApplicationRequest(TypedDict, closed=True):
    application_id: "capo_serverlessapplicationrepository.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    author: NotRequired["capo_serverlessapplicationrepository.types.__string.__string"]
    """<p>The name of the author publishing the app.</p><p>Minimum length=1. Maximum length=127.</p><p>Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";</p>"""
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
    readme_body: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A text readme file in Markdown language that contains a more detailed description of the application and how it works.</p><p>Maximum size 5 MB</p>"""
    readme_url: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A link to the readme file in Markdown language that contains a more detailed description of the application and how it works.</p><p>Maximum size 5 MB</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationRequest) -> dict:
    out: dict = {}
    if "author" in value:
        out["author"] = value["author"]
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
    if "readme_body" in value:
        out["readmeBody"] = value["readme_body"]
    if "readme_url" in value:
        out["readmeUrl"] = value["readme_url"]
    return out


def deserialize_json(data: dict) -> UpdateApplicationRequest:
    out: UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("author") is not None:
        out["author"] = data["author"]
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
    if data.get("readmeBody") is not None:
        out["readme_body"] = data["readmeBody"]
    if data.get("readmeUrl") is not None:
        out["readme_url"] = data["readmeUrl"]
    return out
