"""Generated from Smithy shape ``com.amazonaws.ssm#PatchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.patch_filter_key
    import capo_ssm.types.patch_filter_value_list


class PatchFilter(TypedDict, closed=True):
    key: "capo_ssm.types.patch_filter_key.PatchFilterKey"
    """<p>The key for the filter.</p> <p>Run the <a>DescribePatchProperties</a> command to view lists of valid keys for each operating system type.</p>"""
    values: "capo_ssm.types.patch_filter_value_list.PatchFilterValueList"
    """<p>The value for the filter key.</p> <p>Run the <a>DescribePatchProperties</a> command to view lists of valid values for each key based on operating system type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchFilter) -> dict:
    out: dict = {}
    import capo_ssm.types.patch_filter_key

    out["Key"] = capo_ssm.types.patch_filter_key.serialize_aws_json_1_1(value["key"])
    import capo_ssm.types.patch_filter_value_list

    out["Values"] = capo_ssm.types.patch_filter_value_list.serialize_aws_json_1_1(
        value["values"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PatchFilter:
    out: PatchFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        import capo_ssm.types.patch_filter_key

        out["key"] = capo_ssm.types.patch_filter_key.deserialize_aws_json_1_1(
            data["Key"]
        )
    else:
        import typing

        out["key"] = typing.cast("capo_ssm.types.patch_filter_key.PatchFilterKey", "")
    if data.get("Values") is not None:
        import capo_ssm.types.patch_filter_value_list

        out["values"] = capo_ssm.types.patch_filter_value_list.deserialize_aws_json_1_1(
            data["Values"]
        )
    else:
        out["values"] = []
    return out
