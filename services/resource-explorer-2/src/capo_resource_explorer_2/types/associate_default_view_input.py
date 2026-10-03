"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#AssociateDefaultViewInput``."""

from typing_extensions import TypedDict

from capo_resource_explorer_2.errors import DeserializationError


class AssociateDefaultViewInput(TypedDict, closed=True):
    view_arn: "str"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the view to set as the default for the Amazon Web Services Region and Amazon Web Services account in which you call this operation. The specified view must already exist in the called Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateDefaultViewInput) -> dict:
    out: dict = {}
    out["ViewArn"] = value["view_arn"]
    return out


def deserialize_json(data: dict) -> AssociateDefaultViewInput:
    out: AssociateDefaultViewInput = {}  # type: ignore[typeddict-item]
    if data.get("ViewArn") is not None:
        out["view_arn"] = data["ViewArn"]
    else:
        raise DeserializationError("AssociateDefaultViewInput.view_arn required")
    return out
