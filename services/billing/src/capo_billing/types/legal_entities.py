"""Generated from Smithy shape ``com.amazonaws.billing#LegalEntities``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.legal_entity

LegalEntities: TypeAlias = list["capo_billing.types.legal_entity.LegalEntity"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LegalEntities) -> list:
    import capo_billing.types.legal_entity

    out: list = []
    for item in value:
        out.append(capo_billing.types.legal_entity.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> LegalEntities:
    import capo_billing.types.legal_entity

    out: LegalEntities = []
    for item in data:
        if item is None:
            continue
        out.append(capo_billing.types.legal_entity.deserialize_aws_json_1_0(item))
    return out


def redact_sensitive(value: LegalEntities) -> list[Any]:
    import capo_billing.types.legal_entity

    return [capo_billing.types.legal_entity.redact_sensitive(item) for item in value]
