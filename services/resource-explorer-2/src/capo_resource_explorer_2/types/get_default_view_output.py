"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#GetDefaultViewOutput``."""

from typing_extensions import NotRequired, TypedDict


class GetDefaultViewOutput(TypedDict, closed=True):
    view_arn: NotRequired["str"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the view that is the current default for the Amazon Web Services Region in which you called this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDefaultViewOutput) -> dict:
    out: dict = {}
    if "view_arn" in value:
        out["ViewArn"] = value["view_arn"]
    return out


def deserialize_json(data: dict) -> GetDefaultViewOutput:
    out: GetDefaultViewOutput = {}  # type: ignore[typeddict-item]
    if data.get("ViewArn") is not None:
        out["view_arn"] = data["ViewArn"]
    return out
