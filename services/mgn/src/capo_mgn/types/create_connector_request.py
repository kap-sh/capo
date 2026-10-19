"""Generated from Smithy shape ``com.amazonaws.mgn#CreateConnectorRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.connector_name
    import capo_mgn.types.connector_ssm_command_config
    import capo_mgn.types.ssm_instance_id
    import capo_mgn.types.tags_map


class CreateConnectorRequest(TypedDict, closed=True):
    name: "capo_mgn.types.connector_name.ConnectorName"
    """<p>Create Connector request name.</p>"""
    ssm_instance_id: "capo_mgn.types.ssm_instance_id.SsmInstanceID"
    """<p>Create Connector request SSM instance ID.</p>"""
    tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Create Connector request tags.</p>"""
    ssm_command_config: NotRequired[
        "capo_mgn.types.connector_ssm_command_config.ConnectorSsmCommandConfig"
    ]
    """<p>Create Connector request SSM command config.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectorRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["ssmInstanceID"] = value["ssm_instance_id"]
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


def deserialize_json(data: dict) -> CreateConnectorRequest:
    out: CreateConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("ssmInstanceID") is not None:
        out["ssm_instance_id"] = data["ssmInstanceID"]
    else:
        out["ssm_instance_id"] = ""
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


def redact_sensitive(value: CreateConnectorRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
