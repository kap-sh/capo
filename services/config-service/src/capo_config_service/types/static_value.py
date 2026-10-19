"""Generated from Smithy shape ``com.amazonaws.configservice#StaticValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.static_parameter_values


class StaticValue(TypedDict, closed=True):
    values: "capo_config_service.types.static_parameter_values.StaticParameterValues"
    """<p>A list of values. For example, the ARN of the assumed role. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StaticValue) -> dict:
    out: dict = {}
    import capo_config_service.types.static_parameter_values

    out["Values"] = (
        capo_config_service.types.static_parameter_values.serialize_aws_json_1_1(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StaticValue:
    out: StaticValue = {}  # type: ignore[typeddict-item]
    if data.get("Values") is not None:
        import capo_config_service.types.static_parameter_values

        out["values"] = (
            capo_config_service.types.static_parameter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    return out
