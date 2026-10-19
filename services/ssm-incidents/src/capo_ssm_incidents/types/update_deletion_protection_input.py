"""Generated from Smithy shape ``com.amazonaws.ssmincidents#UpdateDeletionProtectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.client_token


class UpdateDeletionProtectionInput(TypedDict, closed=True):
    arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the replication set to update.</p>"""
    deletion_protected: "bool"
    """<p>Specifies if deletion protection is turned on or off in your account. </p>"""
    client_token: NotRequired["capo_ssm_incidents.types.client_token.ClientToken"]
    """<p>A token that ensures that the operation is called only once with the specified details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDeletionProtectionInput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["deletionProtected"] = value["deletion_protected"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateDeletionProtectionInput:
    out: UpdateDeletionProtectionInput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("deletionProtected") is not None:
        out["deletion_protected"] = data["deletionProtected"]
    else:
        out["deletion_protected"] = False
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
