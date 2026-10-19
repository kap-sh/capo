"""Generated from Smithy shape ``com.amazonaws.ssm#PatchFilterGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.patch_filter_list


class PatchFilterGroup(TypedDict, closed=True):
    patch_filters: "capo_ssm.types.patch_filter_list.PatchFilterList"
    """<p>The set of patch filters that make up the group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchFilterGroup) -> dict:
    out: dict = {}
    import capo_ssm.types.patch_filter_list

    out["PatchFilters"] = capo_ssm.types.patch_filter_list.serialize_aws_json_1_1(
        value["patch_filters"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PatchFilterGroup:
    out: PatchFilterGroup = {}  # type: ignore[typeddict-item]
    if data.get("PatchFilters") is not None:
        import capo_ssm.types.patch_filter_list

        out["patch_filters"] = (
            capo_ssm.types.patch_filter_list.deserialize_aws_json_1_1(
                data["PatchFilters"]
            )
        )
    else:
        out["patch_filters"] = []
    return out
