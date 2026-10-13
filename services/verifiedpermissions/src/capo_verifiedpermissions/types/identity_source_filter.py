"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#IdentitySourceFilter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.principal_entity_type


class IdentitySourceFilter(TypedDict, closed=True):
    principal_entity_type: NotRequired[
        "capo_verifiedpermissions.types.principal_entity_type.PrincipalEntityType"
    ]
    """<p>The Cedar entity type of the principals returned by the identity provider (IdP) associated with this identity source.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdentitySourceFilter) -> dict:
    out: dict = {}
    if "principal_entity_type" in value:
        out["principalEntityType"] = value["principal_entity_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IdentitySourceFilter:
    out: IdentitySourceFilter = {}  # type: ignore[typeddict-item]
    if data.get("principalEntityType") is not None:
        out["principal_entity_type"] = data["principalEntityType"]
    return out


def redact_sensitive(value: IdentitySourceFilter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "principal_entity_type" in value:
        out["principal_entity_type"] = "*** Sensitive Data Redacted ***"
    return out
