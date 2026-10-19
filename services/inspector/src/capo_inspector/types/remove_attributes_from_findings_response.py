"""Generated from Smithy shape ``com.amazonaws.inspector#RemoveAttributesFromFindingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.failed_items


class RemoveAttributesFromFindingsResponse(TypedDict, closed=True):
    failed_items: "capo_inspector.types.failed_items.FailedItems"
    """<p>Attributes details that cannot be described. An error code is provided for each failed item.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveAttributesFromFindingsResponse) -> dict:
    out: dict = {}
    import capo_inspector.types.failed_items

    out["failedItems"] = capo_inspector.types.failed_items.serialize_aws_json_1_1(
        value["failed_items"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveAttributesFromFindingsResponse:
    out: RemoveAttributesFromFindingsResponse = {}  # type: ignore[typeddict-item]
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
