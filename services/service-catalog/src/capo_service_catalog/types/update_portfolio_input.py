"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdatePortfolioInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.add_tags
    import capo_service_catalog.types.id
    import capo_service_catalog.types.portfolio_description
    import capo_service_catalog.types.portfolio_display_name
    import capo_service_catalog.types.provider_name
    import capo_service_catalog.types.tag_keys


class UpdatePortfolioInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    id: "capo_service_catalog.types.id.Id"
    """<p>The portfolio identifier.</p>"""
    display_name: NotRequired[
        "capo_service_catalog.types.portfolio_display_name.PortfolioDisplayName"
    ]
    """<p>The name to use for display purposes.</p>"""
    description: NotRequired[
        "capo_service_catalog.types.portfolio_description.PortfolioDescription"
    ]
    """<p>The updated description of the portfolio.</p>"""
    provider_name: NotRequired["capo_service_catalog.types.provider_name.ProviderName"]
    """<p>The updated name of the portfolio provider.</p>"""
    add_tags: NotRequired["capo_service_catalog.types.add_tags.AddTags"]
    """<p>The tags to add.</p>"""
    remove_tags: NotRequired["capo_service_catalog.types.tag_keys.TagKeys"]
    """<p>The tags to remove.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePortfolioInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["Id"] = value["id"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "provider_name" in value:
        out["ProviderName"] = value["provider_name"]
    if "add_tags" in value:
        import capo_service_catalog.types.add_tags

        out["AddTags"] = capo_service_catalog.types.add_tags.serialize_aws_json_1_1(
            value["add_tags"]
        )
    if "remove_tags" in value:
        import capo_service_catalog.types.tag_keys

        out["RemoveTags"] = capo_service_catalog.types.tag_keys.serialize_aws_json_1_1(
            value["remove_tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePortfolioInput:
    out: UpdatePortfolioInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ProviderName") is not None:
        out["provider_name"] = data["ProviderName"]
    if data.get("AddTags") is not None:
        import capo_service_catalog.types.add_tags

        out["add_tags"] = capo_service_catalog.types.add_tags.deserialize_aws_json_1_1(
            data["AddTags"]
        )
    if data.get("RemoveTags") is not None:
        import capo_service_catalog.types.tag_keys

        out["remove_tags"] = (
            capo_service_catalog.types.tag_keys.deserialize_aws_json_1_1(
                data["RemoveTags"]
            )
        )
    return out
