"""Generated from Smithy shape ``com.amazonaws.securitylake#AwsIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.aws_principal
    import capo_securitylake.types.external_id


class AwsIdentity(TypedDict, closed=True):
    principal: "capo_securitylake.types.aws_principal.AwsPrincipal"
    """<p>The Amazon Web Services identity principal.</p>"""
    external_id: "capo_securitylake.types.external_id.ExternalId"
    """<p>The external ID used to establish trust relationship with the Amazon Web Services identity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsIdentity) -> dict:
    out: dict = {}
    out["principal"] = value["principal"]
    out["externalId"] = value["external_id"]
    return out


def deserialize_json(data: dict) -> AwsIdentity:
    out: AwsIdentity = {}  # type: ignore[typeddict-item]
    if data.get("principal") is not None:
        out["principal"] = data["principal"]
    else:
        out["principal"] = ""
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    else:
        out["external_id"] = ""
    return out
