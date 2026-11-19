"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeConformancePacksFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_type_list


class DescribeConformancePacksFilters(TypedDict, closed=True):
    types: NotRequired[
        "capo_config_service.types.conformance_pack_type_list.ConformancePackTypeList"
    ]
    """<p>Filters results by conformance pack type. Valid values:</p> <ul> <li> <p> <code>CUSTOM</code> – A custom conformance pack.</p> </li> <li> <p> <code>MANAGED</code> – A managed conformance pack.</p> </li> </ul> <p>If you specify both values, Config returns conformance packs of either type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConformancePacksFilters) -> dict:
    out: dict = {}
    if "types" in value:
        import capo_config_service.types.conformance_pack_type_list

        out["Types"] = (
            capo_config_service.types.conformance_pack_type_list.serialize_aws_json_1_1(
                value["types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConformancePacksFilters:
    out: DescribeConformancePacksFilters = {}  # type: ignore[typeddict-item]
    if data.get("Types") is not None:
        import capo_config_service.types.conformance_pack_type_list

        out["types"] = (
            capo_config_service.types.conformance_pack_type_list.deserialize_aws_json_1_1(
                data["Types"]
            )
        )
    return out
