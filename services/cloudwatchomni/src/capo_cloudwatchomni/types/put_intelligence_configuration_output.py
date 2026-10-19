"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#PutIntelligenceConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cloudwatchomni.types.account_id
    import capo_cloudwatchomni.types.intelligence_kms_key_arn


class PutIntelligenceConfigurationOutput(TypedDict, closed=True):
    account_id: "capo_cloudwatchomni.types.account_id.AccountId"
    """The AWS account ID this configuration applies to."""
    kms_key_arn: NotRequired[
        "capo_cloudwatchomni.types.intelligence_kms_key_arn.IntelligenceKmsKeyArn"
    ]
    """The currently active KMS key ARN for customer-managed encryption, if configured."""
    updated_at: "datetime.datetime"
    """ISO-8601 timestamp of the last update."""
    created_at: "datetime.datetime"
    """ISO-8601 timestamp of initial creation."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutIntelligenceConfigurationOutput) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    import capo_cloudwatchomni.types._prelude.timestamp

    out["updatedAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["updated_at"]
    )
    import capo_cloudwatchomni.types._prelude.timestamp

    out["createdAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["created_at"]
    )
    return out


def deserialize_cbor(data: dict) -> PutIntelligenceConfigurationOutput:
    out: PutIntelligenceConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("updatedAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["updated_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("createdAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["created_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
