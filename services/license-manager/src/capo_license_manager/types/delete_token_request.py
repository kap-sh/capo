"""Generated from Smithy shape ``com.amazonaws.licensemanager#DeleteTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.string


class DeleteTokenRequest(TypedDict, closed=True):
    token_id: "capo_license_manager.types.string.String"
    """<p>Token ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTokenRequest) -> dict:
    out: dict = {}
    out["TokenId"] = value["token_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTokenRequest:
    out: DeleteTokenRequest = {}  # type: ignore[typeddict-item]
    if data.get("TokenId") is not None:
        out["token_id"] = data["TokenId"]
    else:
        out["token_id"] = ""
    return out
