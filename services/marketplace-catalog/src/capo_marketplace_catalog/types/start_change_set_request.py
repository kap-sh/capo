"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#StartChangeSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.catalog
    import capo_marketplace_catalog.types.change_set_name
    import capo_marketplace_catalog.types.client_request_token
    import capo_marketplace_catalog.types.intent
    import capo_marketplace_catalog.types.requested_change_list
    import capo_marketplace_catalog.types.tag_list


class StartChangeSetRequest(TypedDict, closed=True):
    catalog: "capo_marketplace_catalog.types.catalog.Catalog"
    """<p>The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>"""
    change_set: (
        "capo_marketplace_catalog.types.requested_change_list.RequestedChangeList"
    )
    """<p>Array of <code>change</code> object.</p>"""
    change_set_name: NotRequired[
        "capo_marketplace_catalog.types.change_set_name.ChangeSetName"
    ]
    """<p>Optional case sensitive string of up to 100 ASCII characters. The change set name can be used to filter the list of change sets. </p>"""
    client_request_token: NotRequired[
        "capo_marketplace_catalog.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique token to identify the request to ensure idempotency.</p>"""
    change_set_tags: NotRequired["capo_marketplace_catalog.types.tag_list.TagList"]
    """<p>A list of objects specifying each key name and value for the <code>ChangeSetTags</code> property.</p>"""
    intent: NotRequired["capo_marketplace_catalog.types.intent.Intent"]
    """<p>The intent related to the request. The default is <code>APPLY</code>. To test your request before applying changes to your entities, use <code>VALIDATE</code>. This feature is currently available for adding versions to single-AMI products. For more information, see <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/ami-products.html#ami-add-version">Add a new version</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartChangeSetRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    import capo_marketplace_catalog.types.requested_change_list

    out["ChangeSet"] = (
        capo_marketplace_catalog.types.requested_change_list.serialize_json(
            value["change_set"]
        )
    )
    if "change_set_name" in value:
        out["ChangeSetName"] = value["change_set_name"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "change_set_tags" in value:
        import capo_marketplace_catalog.types.tag_list

        out["ChangeSetTags"] = capo_marketplace_catalog.types.tag_list.serialize_json(
            value["change_set_tags"]
        )
    if "intent" in value:
        import capo_marketplace_catalog.types.intent

        out["Intent"] = capo_marketplace_catalog.types.intent.serialize_json(
            value["intent"]
        )
    return out


def deserialize_json(data: dict) -> StartChangeSetRequest:
    out: StartChangeSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("StartChangeSetRequest.catalog required")
    if data.get("ChangeSet") is not None:
        import capo_marketplace_catalog.types.requested_change_list

        out["change_set"] = (
            capo_marketplace_catalog.types.requested_change_list.deserialize_json(
                data["ChangeSet"]
            )
        )
    else:
        raise DeserializationError("StartChangeSetRequest.change_set required")
    if data.get("ChangeSetName") is not None:
        out["change_set_name"] = data["ChangeSetName"]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("ChangeSetTags") is not None:
        import capo_marketplace_catalog.types.tag_list

        out["change_set_tags"] = (
            capo_marketplace_catalog.types.tag_list.deserialize_json(
                data["ChangeSetTags"]
            )
        )
    if data.get("Intent") is not None:
        import capo_marketplace_catalog.types.intent

        out["intent"] = capo_marketplace_catalog.types.intent.deserialize_json(
            data["Intent"]
        )
    return out
