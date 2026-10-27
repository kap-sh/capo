"""Generated from Smithy shape ``com.amazonaws.billing#LegalEntity``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.sensitive_string


class LegalEntity(TypedDict, closed=True):
    legal_entity_name: "capo_billing.types.sensitive_string.SensitiveString"
    """<p>The name of the legal entity as it appears on the contract document. This value can be up to 256 characters.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LegalEntity) -> dict:
    out: dict = {}
    out["legalEntityName"] = value["legal_entity_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LegalEntity:
    out: LegalEntity = {}  # type: ignore[typeddict-item]
    if data.get("legalEntityName") is not None:
        out["legal_entity_name"] = data["legalEntityName"]
    else:
        out["legal_entity_name"] = ""
    return out


def redact_sensitive(value: LegalEntity) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "legal_entity_name" in value:
        out["legal_entity_name"] = "*** Sensitive Data Redacted ***"
    return out
