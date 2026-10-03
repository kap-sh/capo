"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#AssociateDefaultViewOutput``."""

from typing_extensions import NotRequired, TypedDict


class AssociateDefaultViewOutput(TypedDict, closed=True):
    view_arn: NotRequired["str"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the view that the operation set as the default for queries made in the Amazon Web Services Region and Amazon Web Services account in which you called this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateDefaultViewOutput) -> dict:
    out: dict = {}
    if "view_arn" in value:
        out["ViewArn"] = value["view_arn"]
    return out


def deserialize_json(data: dict) -> AssociateDefaultViewOutput:
    out: AssociateDefaultViewOutput = {}  # type: ignore[typeddict-item]
    if data.get("ViewArn") is not None:
        out["view_arn"] = data["ViewArn"]
    return out
