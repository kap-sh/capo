"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#RegionSsmDocumentMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.region
    import capo_arc_region_switch.types.ssm_document_config

RegionSsmDocumentMap: TypeAlias = dict[
    "capo_arc_region_switch.types.region.Region",
    "capo_arc_region_switch.types.ssm_document_config.SsmDocumentConfig",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: RegionSsmDocumentMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_arc_region_switch.types.ssm_document_config

        out[key] = (
            capo_arc_region_switch.types.ssm_document_config.serialize_aws_json_1_0(
                value
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RegionSsmDocumentMap:
    out: RegionSsmDocumentMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_arc_region_switch.types.ssm_document_config

        out[key] = (
            capo_arc_region_switch.types.ssm_document_config.deserialize_aws_json_1_0(
                value
            )
        )
    return out
