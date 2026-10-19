"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdateProductInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.add_tags
    import capo_service_catalog.types.id
    import capo_service_catalog.types.product_view_name
    import capo_service_catalog.types.product_view_owner
    import capo_service_catalog.types.product_view_short_description
    import capo_service_catalog.types.source_connection
    import capo_service_catalog.types.support_description
    import capo_service_catalog.types.support_email
    import capo_service_catalog.types.support_url
    import capo_service_catalog.types.tag_keys


class UpdateProductInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    id: "capo_service_catalog.types.id.Id"
    """<p>The product identifier.</p>"""
    name: NotRequired["capo_service_catalog.types.product_view_name.ProductViewName"]
    """<p>The updated product name.</p>"""
    owner: NotRequired["capo_service_catalog.types.product_view_owner.ProductViewOwner"]
    """<p>The updated owner of the product.</p>"""
    description: NotRequired[
        "capo_service_catalog.types.product_view_short_description.ProductViewShortDescription"
    ]
    """<p>The updated description of the product.</p>"""
    distributor: NotRequired[
        "capo_service_catalog.types.product_view_owner.ProductViewOwner"
    ]
    """<p>The updated distributor of the product.</p>"""
    support_description: NotRequired[
        "capo_service_catalog.types.support_description.SupportDescription"
    ]
    """<p>The updated support description for the product.</p>"""
    support_email: NotRequired["capo_service_catalog.types.support_email.SupportEmail"]
    """<p>The updated support email for the product.</p>"""
    support_url: NotRequired["capo_service_catalog.types.support_url.SupportUrl"]
    """<p>The updated support URL for the product.</p>"""
    add_tags: NotRequired["capo_service_catalog.types.add_tags.AddTags"]
    """<p>The tags to add to the product.</p>"""
    remove_tags: NotRequired["capo_service_catalog.types.tag_keys.TagKeys"]
    """<p>The tags to remove from the product.</p>"""
    source_connection: NotRequired[
        "capo_service_catalog.types.source_connection.SourceConnection"
    ]
    """<p>Specifies connection details for the updated product and syncs the product to the connection source artifact. This automatically manages the product's artifacts based on changes to the source. The <code>SourceConnection</code> parameter consists of the following sub-fields.</p> <ul> <li> <p> <code>Type</code> </p> </li> <li> <p> <code>ConnectionParamters</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProductInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "description" in value:
        out["Description"] = value["description"]
    if "distributor" in value:
        out["Distributor"] = value["distributor"]
    if "support_description" in value:
        out["SupportDescription"] = value["support_description"]
    if "support_email" in value:
        out["SupportEmail"] = value["support_email"]
    if "support_url" in value:
        out["SupportUrl"] = value["support_url"]
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
    if "source_connection" in value:
        import capo_service_catalog.types.source_connection

        out["SourceConnection"] = (
            capo_service_catalog.types.source_connection.serialize_aws_json_1_1(
                value["source_connection"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProductInput:
    out: UpdateProductInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Distributor") is not None:
        out["distributor"] = data["Distributor"]
    if data.get("SupportDescription") is not None:
        out["support_description"] = data["SupportDescription"]
    if data.get("SupportEmail") is not None:
        out["support_email"] = data["SupportEmail"]
    if data.get("SupportUrl") is not None:
        out["support_url"] = data["SupportUrl"]
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
    if data.get("SourceConnection") is not None:
        import capo_service_catalog.types.source_connection

        out["source_connection"] = (
            capo_service_catalog.types.source_connection.deserialize_aws_json_1_1(
                data["SourceConnection"]
            )
        )
    return out
