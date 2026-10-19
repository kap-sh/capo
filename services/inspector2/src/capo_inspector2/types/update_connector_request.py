"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.connector_arn
    import capo_inspector2.types.connector_description
    import capo_inspector2.types.provider_detail_update


class UpdateConnectorRequest(TypedDict, closed=True):
    connector_arn: "capo_inspector2.types.connector_arn.ConnectorArn"
    """<p>The Amazon Resource Name (ARN) of the connector to update.</p>"""
    description: NotRequired[
        "capo_inspector2.types.connector_description.ConnectorDescription"
    ]
    """<p>The updated description of the connector.</p>"""
    provider_detail: NotRequired[
        "capo_inspector2.types.provider_detail_update.ProviderDetailUpdate"
    ]
    """<p>The updated provider-specific configuration details for the connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectorRequest) -> dict:
    out: dict = {}
    out["connectorArn"] = value["connector_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "provider_detail" in value:
        import capo_inspector2.types.provider_detail_update

        out["providerDetail"] = (
            capo_inspector2.types.provider_detail_update.serialize_json(
                value["provider_detail"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateConnectorRequest:
    out: UpdateConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("connectorArn") is not None:
        out["connector_arn"] = data["connectorArn"]
    else:
        out["connector_arn"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("providerDetail") is not None:
        import capo_inspector2.types.provider_detail_update

        out["provider_detail"] = (
            capo_inspector2.types.provider_detail_update.deserialize_json(
                data["providerDetail"]
            )
        )
    return out
