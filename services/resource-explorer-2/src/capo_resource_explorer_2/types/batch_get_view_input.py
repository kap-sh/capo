"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#BatchGetViewInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.view_arn_list


class BatchGetViewInput(TypedDict, closed=True):
    view_arns: NotRequired["capo_resource_explorer_2.types.view_arn_list.ViewArnList"]
    """<p>A list of <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource names (ARNs)</a> that identify the views you want details for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetViewInput) -> dict:
    out: dict = {}
    if "view_arns" in value:
        import capo_resource_explorer_2.types.view_arn_list

        out["ViewArns"] = capo_resource_explorer_2.types.view_arn_list.serialize_json(
            value["view_arns"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetViewInput:
    out: BatchGetViewInput = {}  # type: ignore[typeddict-item]
    if data.get("ViewArns") is not None:
        import capo_resource_explorer_2.types.view_arn_list

        out["view_arns"] = (
            capo_resource_explorer_2.types.view_arn_list.deserialize_json(
                data["ViewArns"]
            )
        )
    return out
