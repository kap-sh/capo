"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchWriteRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.batch_write_operation_list


class BatchWriteRequest(TypedDict, closed=True):
    directory_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a>. For more information, see <a>arns</a>.</p>"""
    operations: (
        "capo_clouddirectory.types.batch_write_operation_list.BatchWriteOperationList"
    )
    """<p>A list of operations that are part of the batch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchWriteRequest) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.batch_write_operation_list

    out["Operations"] = (
        capo_clouddirectory.types.batch_write_operation_list.serialize_json(
            value["operations"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchWriteRequest:
    out: BatchWriteRequest = {}  # type: ignore[typeddict-item]
    if data.get("Operations") is not None:
        import capo_clouddirectory.types.batch_write_operation_list

        out["operations"] = (
            capo_clouddirectory.types.batch_write_operation_list.deserialize_json(
                data["Operations"]
            )
        )
    else:
        out["operations"] = []
    return out
