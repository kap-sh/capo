"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchReadRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.batch_read_operation_list
    import capo_clouddirectory.types.consistency_level


class BatchReadRequest(TypedDict, closed=True):
    directory_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a>. For more information, see <a>arns</a>.</p>"""
    operations: (
        "capo_clouddirectory.types.batch_read_operation_list.BatchReadOperationList"
    )
    """<p>A list of operations that are part of the batch.</p>"""
    consistency_level: NotRequired[
        "capo_clouddirectory.types.consistency_level.ConsistencyLevel"
    ]
    """<p>Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchReadRequest) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.batch_read_operation_list

    out["Operations"] = (
        capo_clouddirectory.types.batch_read_operation_list.serialize_json(
            value["operations"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchReadRequest:
    out: BatchReadRequest = {}  # type: ignore[typeddict-item]
    if data.get("Operations") is not None:
        import capo_clouddirectory.types.batch_read_operation_list

        out["operations"] = (
            capo_clouddirectory.types.batch_read_operation_list.deserialize_json(
                data["Operations"]
            )
        )
    else:
        out["operations"] = []
    return out
