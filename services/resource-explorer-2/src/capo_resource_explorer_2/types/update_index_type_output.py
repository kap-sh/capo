"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#UpdateIndexTypeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resource_explorer_2.types.index_state
    import capo_resource_explorer_2.types.index_type


class UpdateIndexTypeOutput(TypedDict, closed=True):
    arn: NotRequired["str"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the index that you updated.</p>"""
    type: NotRequired["capo_resource_explorer_2.types.index_type.IndexType"]
    """<p>Specifies the type of the specified index after the operation completes.</p>"""
    state: NotRequired["capo_resource_explorer_2.types.index_state.IndexState"]
    """<p>Indicates the state of the request to update the index. This operation is asynchronous. Call the <a>GetIndex</a> operation to check for changes.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The date and timestamp when the index was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIndexTypeOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "type" in value:
        out["Type"] = value["type"]
    if "state" in value:
        out["State"] = value["state"]
    if "last_updated_at" in value:
        import capo_resource_explorer_2._protocol.serialize

        out["LastUpdatedAt"] = (
            capo_resource_explorer_2._protocol.serialize.fmt_date_time(
                value["last_updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateIndexTypeOutput:
    out: UpdateIndexTypeOutput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("LastUpdatedAt") is not None:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromisoformat(
            data["LastUpdatedAt"].replace("Z", "+00:00")
        )
    return out
