"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#GetMpaTeamAssociationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.mpa_operation


class GetMpaTeamAssociationInput(TypedDict, closed=True):
    action: "capo_payment_cryptography.types.mpa_operation.MpaOperation"
    """<p>The protected operation whose MPA team association you want to retrieve. Currently, the only supported value is <code>IMPORT_ROOT_PUBLIC_KEY_CERTIFICATE</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetMpaTeamAssociationInput) -> dict:
    out: dict = {}
    out["Action"] = value["action"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetMpaTeamAssociationInput:
    out: GetMpaTeamAssociationInput = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        out["action"] = data["Action"]
    else:
        out["action"] = ""
    return out
