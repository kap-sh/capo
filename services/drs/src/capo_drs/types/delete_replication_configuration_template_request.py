"""Generated from Smithy shape ``com.amazonaws.drs#DeleteReplicationConfigurationTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.replication_configuration_template_id


class DeleteReplicationConfigurationTemplateRequest(TypedDict, closed=True):
    replication_configuration_template_id: "capo_drs.types.replication_configuration_template_id.ReplicationConfigurationTemplateID"
    """<p>The ID of the Replication Configuration Template to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteReplicationConfigurationTemplateRequest) -> dict:
    out: dict = {}
    out["replicationConfigurationTemplateID"] = value[
        "replication_configuration_template_id"
    ]
    return out


def deserialize_json(data: dict) -> DeleteReplicationConfigurationTemplateRequest:
    out: DeleteReplicationConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("replicationConfigurationTemplateID") is not None:
        out["replication_configuration_template_id"] = data[
            "replicationConfigurationTemplateID"
        ]
    else:
        out["replication_configuration_template_id"] = ""
    return out
