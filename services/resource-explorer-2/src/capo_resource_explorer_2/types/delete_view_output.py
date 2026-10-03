"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#DeleteViewOutput``."""

from typing_extensions import NotRequired, TypedDict


class DeleteViewOutput(TypedDict, closed=True):
    view_arn: NotRequired["str"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the view that you successfully deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteViewOutput) -> dict:
    out: dict = {}
    if "view_arn" in value:
        out["ViewArn"] = value["view_arn"]
    return out


def deserialize_json(data: dict) -> DeleteViewOutput:
    out: DeleteViewOutput = {}  # type: ignore[typeddict-item]
    if data.get("ViewArn") is not None:
        out["view_arn"] = data["ViewArn"]
    return out
