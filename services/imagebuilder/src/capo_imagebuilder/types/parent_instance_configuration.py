"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ParentInstanceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.auto_scaling_group_configuration


class ParentInstanceConfiguration(TypedDict, closed=True):
    auto_scaling_group: "capo_imagebuilder.types.auto_scaling_group_configuration.AutoScalingGroupConfiguration"
    """<p>The Amazon EC2 Auto Scaling group that Image Builder takes the build instance from. This is required when you specify <code>parentInstance</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParentInstanceConfiguration) -> dict:
    out: dict = {}
    import capo_imagebuilder.types.auto_scaling_group_configuration

    out["autoScalingGroup"] = (
        capo_imagebuilder.types.auto_scaling_group_configuration.serialize_json(
            value["auto_scaling_group"]
        )
    )
    return out


def deserialize_json(data: dict) -> ParentInstanceConfiguration:
    out: ParentInstanceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("autoScalingGroup") is not None:
        import capo_imagebuilder.types.auto_scaling_group_configuration

        out["auto_scaling_group"] = (
            capo_imagebuilder.types.auto_scaling_group_configuration.deserialize_json(
                data["autoScalingGroup"]
            )
        )
    else:
        raise DeserializationError(
            "ParentInstanceConfiguration.auto_scaling_group required"
        )
    return out
