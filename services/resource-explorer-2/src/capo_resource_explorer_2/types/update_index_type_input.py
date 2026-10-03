"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#UpdateIndexTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resource_explorer_2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.index_type


class UpdateIndexTypeInput(TypedDict, closed=True):
    arn: "str"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the index that you want to update.</p>"""
    type: "capo_resource_explorer_2.types.index_type.IndexType"
    """<p>The type of the index. To understand the difference between <code>LOCAL</code> and <code>AGGREGATOR</code>, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html">Turning on cross-Region search</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIndexTypeInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> UpdateIndexTypeInput:
    out: UpdateIndexTypeInput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("UpdateIndexTypeInput.arn required")
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("UpdateIndexTypeInput.type required")
    return out
