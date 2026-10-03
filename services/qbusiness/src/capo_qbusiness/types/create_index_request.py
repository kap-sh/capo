"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateIndexRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.client_token
    import capo_qbusiness.types.description
    import capo_qbusiness.types.index_capacity_configuration
    import capo_qbusiness.types.index_name
    import capo_qbusiness.types.index_type
    import capo_qbusiness.types.tags


class CreateIndexRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application using the index.</p>"""
    display_name: "capo_qbusiness.types.index_name.IndexName"
    """<p>A name for the Amazon Q Business index.</p>"""
    description: NotRequired["capo_qbusiness.types.description.Description"]
    """<p>A description for the Amazon Q Business index.</p>"""
    type: NotRequired["capo_qbusiness.types.index_type.IndexType"]
    """<p>The index type that's suitable for your needs. For more information on what's included in each type of index, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html#index-tiers">Amazon Q Business tiers</a>.</p>"""
    tags: NotRequired["capo_qbusiness.types.tags.Tags"]
    """<p>A list of key-value pairs that identify or categorize the index. You can also use tags to help control access to the index. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>"""
    capacity_configuration: NotRequired[
        "capo_qbusiness.types.index_capacity_configuration.IndexCapacityConfiguration"
    ]
    """<p>The capacity units you want to provision for your index. You can add and remove capacity to fit your usage needs.</p>"""
    client_token: NotRequired["capo_qbusiness.types.client_token.ClientToken"]
    """<p>A token that you provide to identify the request to create an index. Multiple calls to the <code>CreateIndex</code> API with the same client token will create only one index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIndexRequest) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "type" in value:
        import capo_qbusiness.types.index_type

        out["type"] = capo_qbusiness.types.index_type.serialize_json(value["type"])
    if "tags" in value:
        import capo_qbusiness.types.tags

        out["tags"] = capo_qbusiness.types.tags.serialize_json(value["tags"])
    if "capacity_configuration" in value:
        import capo_qbusiness.types.index_capacity_configuration

        out["capacityConfiguration"] = (
            capo_qbusiness.types.index_capacity_configuration.serialize_json(
                value["capacity_configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateIndexRequest:
    out: CreateIndexRequest = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("CreateIndexRequest.display_name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("type") is not None:
        import capo_qbusiness.types.index_type

        out["type"] = capo_qbusiness.types.index_type.deserialize_json(data["type"])
    if data.get("tags") is not None:
        import capo_qbusiness.types.tags

        out["tags"] = capo_qbusiness.types.tags.deserialize_json(data["tags"])
    if data.get("capacityConfiguration") is not None:
        import capo_qbusiness.types.index_capacity_configuration

        out["capacity_configuration"] = (
            capo_qbusiness.types.index_capacity_configuration.deserialize_json(
                data["capacityConfiguration"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
