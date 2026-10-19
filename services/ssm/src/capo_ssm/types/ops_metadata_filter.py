"""Generated from Smithy shape ``com.amazonaws.ssm#OpsMetadataFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.ops_metadata_filter_key
    import capo_ssm.types.ops_metadata_filter_value_list


class OpsMetadataFilter(TypedDict, closed=True):
    key: "capo_ssm.types.ops_metadata_filter_key.OpsMetadataFilterKey"
    """<p>A filter key.</p>"""
    values: "capo_ssm.types.ops_metadata_filter_value_list.OpsMetadataFilterValueList"
    """<p>A filter value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsMetadataFilter) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    import capo_ssm.types.ops_metadata_filter_value_list

    out["Values"] = (
        capo_ssm.types.ops_metadata_filter_value_list.serialize_aws_json_1_1(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsMetadataFilter:
    out: OpsMetadataFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Values") is not None:
        import capo_ssm.types.ops_metadata_filter_value_list

        out["values"] = (
            capo_ssm.types.ops_metadata_filter_value_list.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    return out
