"""Generated from Smithy shape ``com.amazonaws.mgn#Connector``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.arn
    import capo_mgn.types.connector_id
    import capo_mgn.types.connector_name
    import capo_mgn.types.connector_ssm_command_config
    import capo_mgn.types.ssm_instance_id
    import capo_mgn.types.tags_map


class Connector(TypedDict, closed=True):
    connector_id: NotRequired["capo_mgn.types.connector_id.ConnectorID"]
    """<p>Connector ID.</p>"""
    name: NotRequired["capo_mgn.types.connector_name.ConnectorName"]
    """<p>Connector name.</p>"""
    ssm_instance_id: NotRequired["capo_mgn.types.ssm_instance_id.SsmInstanceID"]
    """<p>Connector SSM instance ID.</p>"""
    arn: NotRequired["capo_mgn.types.arn.ARN"]
    """<p>Connector arn.</p>"""
    tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Connector tags.</p>"""
    ssm_command_config: NotRequired[
        "capo_mgn.types.connector_ssm_command_config.ConnectorSsmCommandConfig"
    ]
    """<p>Connector SSM command config.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Connector) -> dict:
    out: dict = {}
    if "connector_id" in value:
        out["connectorID"] = value["connector_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "ssm_instance_id" in value:
        out["ssmInstanceID"] = value["ssm_instance_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "tags" in value:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.serialize_json(value["tags"])
    if "ssm_command_config" in value:
        import capo_mgn.types.connector_ssm_command_config

        out["ssmCommandConfig"] = (
            capo_mgn.types.connector_ssm_command_config.serialize_json(
                value["ssm_command_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> Connector:
    out: Connector = {}  # type: ignore[typeddict-item]
    if data.get("connectorID") is not None:
        out["connector_id"] = data["connectorID"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("ssmInstanceID") is not None:
        out["ssm_instance_id"] = data["ssmInstanceID"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("tags") is not None:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.deserialize_json(data["tags"])
    if data.get("ssmCommandConfig") is not None:
        import capo_mgn.types.connector_ssm_command_config

        out["ssm_command_config"] = (
            capo_mgn.types.connector_ssm_command_config.deserialize_json(
                data["ssmCommandConfig"]
            )
        )
    return out


def redact_sensitive(value: Connector) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
