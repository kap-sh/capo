"""Generated from Smithy shape ``com.amazonaws.appflow#CustomConnectorSourceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.custom_properties
    import capo_appflow.types.data_transfer_api
    import capo_appflow.types.entity_name


class CustomConnectorSourceProperties(TypedDict, closed=True):
    entity_name: "capo_appflow.types.entity_name.EntityName"
    """<p>The entity specified in the custom connector as a source in the flow.</p>"""
    custom_properties: NotRequired[
        "capo_appflow.types.custom_properties.CustomProperties"
    ]
    """<p>Custom properties that are required to use the custom connector as a source.</p>"""
    data_transfer_api: NotRequired[
        "capo_appflow.types.data_transfer_api.DataTransferApi"
    ]
    """<p>The API of the connector application that Amazon AppFlow uses to transfer your data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomConnectorSourceProperties) -> dict:
    out: dict = {}
    out["entityName"] = value["entity_name"]
    if "custom_properties" in value:
        import capo_appflow.types.custom_properties

        out["customProperties"] = capo_appflow.types.custom_properties.serialize_json(
            value["custom_properties"]
        )
    if "data_transfer_api" in value:
        import capo_appflow.types.data_transfer_api

        out["dataTransferApi"] = capo_appflow.types.data_transfer_api.serialize_json(
            value["data_transfer_api"]
        )
    return out


def deserialize_json(data: dict) -> CustomConnectorSourceProperties:
    out: CustomConnectorSourceProperties = {}  # type: ignore[typeddict-item]
    if data.get("entityName") is not None:
        out["entity_name"] = data["entityName"]
    else:
        out["entity_name"] = ""
    if data.get("customProperties") is not None:
        import capo_appflow.types.custom_properties

        out["custom_properties"] = (
            capo_appflow.types.custom_properties.deserialize_json(
                data["customProperties"]
            )
        )
    if data.get("dataTransferApi") is not None:
        import capo_appflow.types.data_transfer_api

        out["data_transfer_api"] = (
            capo_appflow.types.data_transfer_api.deserialize_json(
                data["dataTransferApi"]
            )
        )
    return out
