"""Generated from Smithy shape ``com.amazonaws.directoryservice#UpdateTrustRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.selective_auth
    import capo_directory_service.types.trust_id


class UpdateTrustRequest(TypedDict, closed=True):
    trust_id: "capo_directory_service.types.trust_id.TrustId"
    """<p>Identifier of the trust relationship.</p>"""
    selective_auth: NotRequired[
        "capo_directory_service.types.selective_auth.SelectiveAuth"
    ]
    """<p>Updates selective authentication for the trust.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTrustRequest) -> dict:
    out: dict = {}
    out["TrustId"] = value["trust_id"]
    if "selective_auth" in value:
        import capo_directory_service.types.selective_auth

        out["SelectiveAuth"] = (
            capo_directory_service.types.selective_auth.serialize_aws_json_1_1(
                value["selective_auth"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTrustRequest:
    out: UpdateTrustRequest = {}  # type: ignore[typeddict-item]
    if data.get("TrustId") is not None:
        out["trust_id"] = data["TrustId"]
    else:
        out["trust_id"] = ""
    if data.get("SelectiveAuth") is not None:
        import capo_directory_service.types.selective_auth

        out["selective_auth"] = (
            capo_directory_service.types.selective_auth.deserialize_aws_json_1_1(
                data["SelectiveAuth"]
            )
        )
    return out
