"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#SsmDocumentParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.ssm_parameter_key
    import capo_arc_region_switch.types.ssm_parameter_values

SsmDocumentParameters: TypeAlias = dict[
    "capo_arc_region_switch.types.ssm_parameter_key.SsmParameterKey",
    "capo_arc_region_switch.types.ssm_parameter_values.SsmParameterValues",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: SsmDocumentParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_arc_region_switch.types.ssm_parameter_values

        out[key] = (
            capo_arc_region_switch.types.ssm_parameter_values.serialize_aws_json_1_0(
                value
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SsmDocumentParameters:
    out: SsmDocumentParameters = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_arc_region_switch.types.ssm_parameter_values

        out[key] = (
            capo_arc_region_switch.types.ssm_parameter_values.deserialize_aws_json_1_0(
                value
            )
        )
    return out
