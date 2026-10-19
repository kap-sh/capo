"""Generated from Smithy shape ``com.amazonaws.groundstation#UpdateConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.config_capability_type
    import capo_groundstation.types.config_type_data
    import capo_groundstation.types.safe_name
    import capo_groundstation.types.uuid


class UpdateConfigRequest(TypedDict, closed=True):
    config_id: "capo_groundstation.types.uuid.Uuid"
    """<p>UUID of a <code>Config</code>.</p>"""
    name: "capo_groundstation.types.safe_name.SafeName"
    """<p>Name of a <code>Config</code>.</p>"""
    config_type: "capo_groundstation.types.config_capability_type.ConfigCapabilityType"
    """<p>Type of a <code>Config</code>.</p>"""
    config_data: "capo_groundstation.types.config_type_data.ConfigTypeData"
    """<p>Parameters of a <code>Config</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfigRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_groundstation.types.config_type_data

    out["configData"] = capo_groundstation.types.config_type_data.serialize_json(
        value["config_data"]
    )
    return out


def deserialize_json(data: dict) -> UpdateConfigRequest:
    out: UpdateConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("configData") is not None:
        import capo_groundstation.types.config_type_data

        out["config_data"] = capo_groundstation.types.config_type_data.deserialize_json(
            data["configData"]
        )
    else:
        import capo_groundstation.types._unknown

        out["config_data"] = capo_groundstation.types._unknown.UnknownUnionMember("")
    return out
