"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.resource_value_type


class ResourceValue(TypedDict, closed=True):
    value: "capo_config_service.types.resource_value_type.ResourceValueType"
    """<p>The value is a resource ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceValue) -> dict:
    out: dict = {}
    import capo_config_service.types.resource_value_type

    out["Value"] = capo_config_service.types.resource_value_type.serialize_aws_json_1_1(
        value["value"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceValue:
    out: ResourceValue = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        import capo_config_service.types.resource_value_type

        out["value"] = (
            capo_config_service.types.resource_value_type.deserialize_aws_json_1_1(
                data["Value"]
            )
        )
    else:
        import typing

        out["value"] = typing.cast(
            "capo_config_service.types.resource_value_type.ResourceValueType", ""
        )
    return out
