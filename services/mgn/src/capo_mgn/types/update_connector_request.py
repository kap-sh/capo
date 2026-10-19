"""Generated from Smithy shape ``com.amazonaws.mgn#UpdateConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.connector_id
    import capo_mgn.types.connector_name
    import capo_mgn.types.connector_ssm_command_config


class UpdateConnectorRequest(TypedDict, closed=True):
    connector_id: "capo_mgn.types.connector_id.ConnectorID"
    """<p>Update Connector request connector ID.</p>"""
    name: NotRequired["capo_mgn.types.connector_name.ConnectorName"]
    """<p>Update Connector request name.</p>"""
    ssm_command_config: NotRequired[
        "capo_mgn.types.connector_ssm_command_config.ConnectorSsmCommandConfig"
    ]
    """<p>Update Connector request SSM command config.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectorRequest) -> dict:
    out: dict = {}
    out["connectorID"] = value["connector_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "ssm_command_config" in value:
        import capo_mgn.types.connector_ssm_command_config

        out["ssmCommandConfig"] = (
            capo_mgn.types.connector_ssm_command_config.serialize_json(
                value["ssm_command_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateConnectorRequest:
    out: UpdateConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("connectorID") is not None:
        out["connector_id"] = data["connectorID"]
    else:
        out["connector_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("ssmCommandConfig") is not None:
        import capo_mgn.types.connector_ssm_command_config

        out["ssm_command_config"] = (
            capo_mgn.types.connector_ssm_command_config.deserialize_json(
                data["ssmCommandConfig"]
            )
        )
    return out
