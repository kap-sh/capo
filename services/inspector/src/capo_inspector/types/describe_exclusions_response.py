"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeExclusionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.exclusion_map
    import capo_inspector.types.failed_items


class DescribeExclusionsResponse(TypedDict, closed=True):
    exclusions: "capo_inspector.types.exclusion_map.ExclusionMap"
    """<p>Information about the exclusions.</p>"""
    failed_items: "capo_inspector.types.failed_items.FailedItems"
    """<p>Exclusion details that cannot be described. An error code is provided for each failed item.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeExclusionsResponse) -> dict:
    out: dict = {}
    import capo_inspector.types.exclusion_map

    out["exclusions"] = capo_inspector.types.exclusion_map.serialize_aws_json_1_1(
        value["exclusions"]
    )
    import capo_inspector.types.failed_items

    out["failedItems"] = capo_inspector.types.failed_items.serialize_aws_json_1_1(
        value["failed_items"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeExclusionsResponse:
    out: DescribeExclusionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("exclusions") is not None:
        import capo_inspector.types.exclusion_map

        out["exclusions"] = capo_inspector.types.exclusion_map.deserialize_aws_json_1_1(
            data["exclusions"]
        )
    else:
        out["exclusions"] = {}
    if data.get("failedItems") is not None:
        import capo_inspector.types.failed_items

        out["failed_items"] = (
            capo_inspector.types.failed_items.deserialize_aws_json_1_1(
                data["failedItems"]
            )
        )
    else:
        out["failed_items"] = {}
    return out
