"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SegmentGroupStructure``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.include_options
    import capo_customer_profiles.types.segment_group_list


class SegmentGroupStructure(TypedDict, closed=True):
    groups: NotRequired[
        "capo_customer_profiles.types.segment_group_list.SegmentGroupList"
    ]
    """<p>Holds the list of groups within the segment definition.</p>"""
    include: NotRequired["capo_customer_profiles.types.include_options.IncludeOptions"]
    """<p>Define whether to include or exclude the profiles that fit the segment criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SegmentGroupStructure) -> dict:
    out: dict = {}
    if "groups" in value:
        import capo_customer_profiles.types.segment_group_list

        out["Groups"] = capo_customer_profiles.types.segment_group_list.serialize_json(
            value["groups"]
        )
    if "include" in value:
        import capo_customer_profiles.types.include_options

        out["Include"] = capo_customer_profiles.types.include_options.serialize_json(
            value["include"]
        )
    return out


def deserialize_json(data: dict) -> SegmentGroupStructure:
    out: SegmentGroupStructure = {}  # type: ignore[typeddict-item]
    if data.get("Groups") is not None:
        import capo_customer_profiles.types.segment_group_list

        out["groups"] = (
            capo_customer_profiles.types.segment_group_list.deserialize_json(
                data["Groups"]
            )
        )
    if data.get("Include") is not None:
        import capo_customer_profiles.types.include_options

        out["include"] = capo_customer_profiles.types.include_options.deserialize_json(
            data["Include"]
        )
    return out


def redact_sensitive(value: SegmentGroupStructure) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "groups" in value:
        import capo_customer_profiles.types.segment_group_list

        out["groups"] = (
            capo_customer_profiles.types.segment_group_list.redact_sensitive(
                value["groups"]
            )
        )
    return out
