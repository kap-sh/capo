"""Generated from Smithy shape ``com.amazonaws.controltower#EnableBaselineOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.arn
    import capo_controltower.types.operation_identifier


class EnableBaselineOutput(TypedDict, closed=True):
    operation_identifier: (
        "capo_controltower.types.operation_identifier.OperationIdentifier"
    )
    """<p>The ID (in UUID format) of the asynchronous <code>EnableBaseline</code> operation. This <code>operationIdentifier</code> is used to track status through calls to the <code>GetBaselineOperation</code> API.</p>"""
    arn: "capo_controltower.types.arn.Arn"
    """<p>The ARN of the <code>EnabledBaseline</code> resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableBaselineOutput) -> dict:
    out: dict = {}
    out["operationIdentifier"] = value["operation_identifier"]
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> EnableBaselineOutput:
    out: EnableBaselineOutput = {}  # type: ignore[typeddict-item]
    if data.get("operationIdentifier") is not None:
        out["operation_identifier"] = data["operationIdentifier"]
    else:
        out["operation_identifier"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
