"""Generated from Smithy shape ``com.amazonaws.controlcatalog#GetControlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_controlcatalog.types.control_arn


class GetControlRequest(TypedDict, closed=True):
    control_arn: "capo_controlcatalog.types.control_arn.ControlArn"
    r"""<p>The Amazon Resource Name (ARN) of the control. It has one of the following formats:</p> <p> <i>Global format</i> </p> <p> <code>arn:{PARTITION}:controlcatalog:::control/{CONTROL_CATALOG_OPAQUE_ID}</code> </p> <p> <i>Or Regional format</i> </p> <p> <code>arn:{PARTITION}:controltower:{REGION}::control/{CONTROL_TOWER_OPAQUE_ID}</code> </p> <p>Here is a more general pattern that covers Amazon Web Services Control Tower and Control Catalog ARNs:</p> <p> <code>^arn:(aws(?:[-a-z]*)?):(controlcatalog|controltower):[a-zA-Z0-9-]*::control/[0-9a-zA-Z_\\-]+$</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetControlRequest) -> dict:
    out: dict = {}
    out["ControlArn"] = value["control_arn"]
    return out


def deserialize_json(data: dict) -> GetControlRequest:
    out: GetControlRequest = {}  # type: ignore[typeddict-item]
    if data.get("ControlArn") is not None:
        out["control_arn"] = data["ControlArn"]
    else:
        out["control_arn"] = ""
    return out
