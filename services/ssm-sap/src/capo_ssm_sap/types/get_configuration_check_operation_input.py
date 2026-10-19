"""Generated from Smithy shape ``com.amazonaws.ssmsap#GetConfigurationCheckOperationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.operation_id


class GetConfigurationCheckOperationInput(TypedDict, closed=True):
    operation_id: "capo_ssm_sap.types.operation_id.OperationId"
    """<p>The ID of the configuration check operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationCheckOperationInput) -> dict:
    out: dict = {}
    out["OperationId"] = value["operation_id"]
    return out


def deserialize_json(data: dict) -> GetConfigurationCheckOperationInput:
    out: GetConfigurationCheckOperationInput = {}  # type: ignore[typeddict-item]
    if data.get("OperationId") is not None:
        out["operation_id"] = data["OperationId"]
    else:
        out["operation_id"] = ""
    return out
