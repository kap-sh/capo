"""Generated from Smithy shape ``com.amazonaws.quicksight#MicrosoftPurviewCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.secret_manager_arn


class MicrosoftPurviewCredentials(TypedDict, closed=True):
    secret_arn: "capo_quicksight.types.secret_manager_arn.SecretManagerArn"
    """<p>The ARN of the Amazon Web Services Secrets Manager secret that contains the Microsoft Purview OAuth credentials. The secret includes the Azure tenant ID, client ID, and client secret or certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MicrosoftPurviewCredentials) -> dict:
    out: dict = {}
    out["SecretArn"] = value["secret_arn"]
    return out


def deserialize_json(data: dict) -> MicrosoftPurviewCredentials:
    out: MicrosoftPurviewCredentials = {}  # type: ignore[typeddict-item]
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    else:
        out["secret_arn"] = ""
    return out
