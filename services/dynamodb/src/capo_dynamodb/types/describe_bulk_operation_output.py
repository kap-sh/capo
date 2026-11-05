"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeBulkOperationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.bulk_operation_description


class DescribeBulkOperationOutput(TypedDict, closed=True):
    bulk_operation_description: (
        "capo_dynamodb.types.bulk_operation_description.BulkOperationDescription"
    )
    """<p>Contains detailed information about the bulk operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeBulkOperationOutput) -> dict:
    out: dict = {}
    import capo_dynamodb.types.bulk_operation_description

    out["BulkOperationDescription"] = (
        capo_dynamodb.types.bulk_operation_description.serialize_aws_json_1_0(
            value["bulk_operation_description"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeBulkOperationOutput:
    out: DescribeBulkOperationOutput = {}  # type: ignore[typeddict-item]
    if data.get("BulkOperationDescription") is not None:
        import capo_dynamodb.types.bulk_operation_description

        out["bulk_operation_description"] = (
            capo_dynamodb.types.bulk_operation_description.deserialize_aws_json_1_0(
                data["BulkOperationDescription"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeBulkOperationOutput.bulk_operation_description required"
        )
    return out
