"""Generated from Smithy shape ``com.amazonaws.kms#GetKeyLastUsageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.date_type
    import capo_kms.types.key_id_type
    import capo_kms.types.key_last_usage_data


class GetKeyLastUsageResponse(TypedDict, closed=True):
    key_id: NotRequired["capo_kms.types.key_id_type.KeyIdType"]
    """<p>The globally unique identifier for the KMS key.</p>"""
    key_last_usage: NotRequired["capo_kms.types.key_last_usage_data.KeyLastUsageData"]
    """<p>Contains usage information about the last time the KMS key was used for a successful cryptographic operation. If the key has not been used since tracking began, this response element is an empty object.</p>"""
    tracking_start_date: NotRequired["capo_kms.types.date_type.DateType"]
    """<p>The date from which KMS began recording cryptographic activity for this key, or the date the KMS key was created, whichever is later.</p>"""
    key_creation_date: NotRequired["capo_kms.types.date_type.DateType"]
    """<p>The date and time when the KMS key was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetKeyLastUsageResponse) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "key_last_usage" in value:
        import capo_kms.types.key_last_usage_data

        out["KeyLastUsage"] = capo_kms.types.key_last_usage_data.serialize_aws_json_1_1(
            value["key_last_usage"]
        )
    if "tracking_start_date" in value:
        import capo_kms.types.date_type

        out["TrackingStartDate"] = capo_kms.types.date_type.serialize_aws_json_1_1(
            value["tracking_start_date"]
        )
    if "key_creation_date" in value:
        import capo_kms.types.date_type

        out["KeyCreationDate"] = capo_kms.types.date_type.serialize_aws_json_1_1(
            value["key_creation_date"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetKeyLastUsageResponse:
    out: GetKeyLastUsageResponse = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    if data.get("KeyLastUsage") is not None:
        import capo_kms.types.key_last_usage_data

        out["key_last_usage"] = (
            capo_kms.types.key_last_usage_data.deserialize_aws_json_1_1(
                data["KeyLastUsage"]
            )
        )
    if data.get("TrackingStartDate") is not None:
        import capo_kms.types.date_type

        out["tracking_start_date"] = capo_kms.types.date_type.deserialize_aws_json_1_1(
            data["TrackingStartDate"]
        )
    if data.get("KeyCreationDate") is not None:
        import capo_kms.types.date_type

        out["key_creation_date"] = capo_kms.types.date_type.deserialize_aws_json_1_1(
            data["KeyCreationDate"]
        )
    return out
