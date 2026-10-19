"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InstanceRequirements``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.instance_type_list


class InstanceRequirements(TypedDict, closed=True):
    allowed_instance_types: (
        "capo_bedrock_agentcore_control.types.instance_type_list.InstanceTypeList"
    )
    """<p>The list of allowed instance types. You can specify up to 30 instance types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceRequirements) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.instance_type_list

    out["allowedInstanceTypes"] = (
        capo_bedrock_agentcore_control.types.instance_type_list.serialize_json(
            value["allowed_instance_types"]
        )
    )
    return out


def deserialize_json(data: dict) -> InstanceRequirements:
    out: InstanceRequirements = {}  # type: ignore[typeddict-item]
    if data.get("allowedInstanceTypes") is not None:
        import capo_bedrock_agentcore_control.types.instance_type_list

        out["allowed_instance_types"] = (
            capo_bedrock_agentcore_control.types.instance_type_list.deserialize_json(
                data["allowedInstanceTypes"]
            )
        )
    else:
        out["allowed_instance_types"] = []
    return out
