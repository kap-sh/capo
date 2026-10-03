"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#DeleteIndexOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resource_explorer_2.types.index_state


class DeleteIndexOutput(TypedDict, closed=True):
    arn: NotRequired["str"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the index that you successfully started the deletion process.</p> <note> <p>This operation is asynchronous. To check its status, call the <a>GetIndex</a> operation.</p> </note>"""
    state: NotRequired["capo_resource_explorer_2.types.index_state.IndexState"]
    """<p>Indicates the current state of the index. </p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time when you last updated this index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIndexOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
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


def deserialize_json(data: dict) -> DeleteIndexOutput:
    out: DeleteIndexOutput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("LastUpdatedAt") is not None:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromisoformat(
            data["LastUpdatedAt"].replace("Z", "+00:00")
        )
    return out
