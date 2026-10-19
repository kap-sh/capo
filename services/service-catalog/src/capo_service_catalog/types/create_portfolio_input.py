"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CreatePortfolioInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.add_tags
    import capo_service_catalog.types.idempotency_token
    import capo_service_catalog.types.portfolio_description
    import capo_service_catalog.types.portfolio_display_name
    import capo_service_catalog.types.provider_name


class CreatePortfolioInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    display_name: (
        "capo_service_catalog.types.portfolio_display_name.PortfolioDisplayName"
    )
    """<p>The name to use for display purposes.</p>"""
    description: NotRequired[
        "capo_service_catalog.types.portfolio_description.PortfolioDescription"
    ]
    """<p>The description of the portfolio.</p>"""
    provider_name: "capo_service_catalog.types.provider_name.ProviderName"
    """<p>The name of the portfolio provider.</p>"""
    tags: NotRequired["capo_service_catalog.types.add_tags.AddTags"]
    """<p>One or more tags.</p>"""
    idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken"
    """<p>A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePortfolioInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["ProviderName"] = value["provider_name"]
    if "tags" in value:
        import capo_service_catalog.types.add_tags

        out["Tags"] = capo_service_catalog.types.add_tags.serialize_aws_json_1_1(
            value["tags"]
        )
    out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePortfolioInput:
    out: CreatePortfolioInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    else:
        out["display_name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ProviderName") is not None:
        out["provider_name"] = data["ProviderName"]
    else:
        out["provider_name"] = ""
    if data.get("Tags") is not None:
        import capo_service_catalog.types.add_tags

        out["tags"] = capo_service_catalog.types.add_tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        out["idempotency_token"] = ""
    return out
