"""Generated from Smithy shape ``com.amazonaws.ssm#CreateAssociationBatchRequestEntries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.create_association_batch_request_entry

CreateAssociationBatchRequestEntries: TypeAlias = list[
    "capo_ssm.types.create_association_batch_request_entry.CreateAssociationBatchRequestEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAssociationBatchRequestEntries) -> list:
    import capo_ssm.types.create_association_batch_request_entry

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.create_association_batch_request_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CreateAssociationBatchRequestEntries:
    import capo_ssm.types.create_association_batch_request_entry

    out: CreateAssociationBatchRequestEntries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ssm.types.create_association_batch_request_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: CreateAssociationBatchRequestEntries) -> list[Any]:
    import capo_ssm.types.create_association_batch_request_entry

    return [
        capo_ssm.types.create_association_batch_request_entry.redact_sensitive(item)
        for item in value
    ]
