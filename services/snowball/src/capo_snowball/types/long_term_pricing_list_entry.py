"""Generated from Smithy shape ``com.amazonaws.snowball#LongTermPricingListEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.java_boolean
    import capo_snowball.types.job_id
    import capo_snowball.types.long_term_pricing_associated_job_id_list
    import capo_snowball.types.long_term_pricing_id
    import capo_snowball.types.long_term_pricing_type
    import capo_snowball.types.snowball_type
    import capo_snowball.types.string
    import capo_snowball.types.timestamp


class LongTermPricingListEntry(TypedDict, closed=True):
    long_term_pricing_id: NotRequired[
        "capo_snowball.types.long_term_pricing_id.LongTermPricingId"
    ]
    """<p>The ID of the long-term pricing type for the device.</p>"""
    long_term_pricing_end_date: NotRequired["capo_snowball.types.timestamp.Timestamp"]
    """<p>The end date the long-term pricing contract.</p>"""
    long_term_pricing_start_date: NotRequired["capo_snowball.types.timestamp.Timestamp"]
    """<p>The start date of the long-term pricing contract.</p>"""
    long_term_pricing_type: NotRequired[
        "capo_snowball.types.long_term_pricing_type.LongTermPricingType"
    ]
    """<p>The type of long-term pricing that was selected for the device.</p>"""
    current_active_job: NotRequired["capo_snowball.types.job_id.JobId"]
    """<p>The current active jobs on the device the long-term pricing type.</p>"""
    replacement_job: NotRequired["capo_snowball.types.job_id.JobId"]
    """<p>A new device that replaces a device that is ordered with long-term pricing.</p>"""
    is_long_term_pricing_auto_renew: NotRequired[
        "capo_snowball.types.java_boolean.JavaBoolean"
    ]
    """<p>If set to <code>true</code>, specifies that the current long-term pricing type for the device should be automatically renewed before the long-term pricing contract expires.</p>"""
    long_term_pricing_status: NotRequired["capo_snowball.types.string.String"]
    """<p>The status of the long-term pricing type.</p>"""
    snowball_type: NotRequired["capo_snowball.types.snowball_type.SnowballType"]
    """<p>The type of Snow Family devices associated with this long-term pricing job.</p>"""
    job_ids: NotRequired[
        "capo_snowball.types.long_term_pricing_associated_job_id_list.LongTermPricingAssociatedJobIdList"
    ]
    """<p>The IDs of the jobs that are associated with a long-term pricing type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LongTermPricingListEntry) -> dict:
    out: dict = {}
    if "long_term_pricing_id" in value:
        out["LongTermPricingId"] = value["long_term_pricing_id"]
    if "long_term_pricing_end_date" in value:
        import capo_snowball.types.timestamp

        out["LongTermPricingEndDate"] = (
            capo_snowball.types.timestamp.serialize_aws_json_1_1(
                value["long_term_pricing_end_date"]
            )
        )
    if "long_term_pricing_start_date" in value:
        import capo_snowball.types.timestamp

        out["LongTermPricingStartDate"] = (
            capo_snowball.types.timestamp.serialize_aws_json_1_1(
                value["long_term_pricing_start_date"]
            )
        )
    if "long_term_pricing_type" in value:
        import capo_snowball.types.long_term_pricing_type

        out["LongTermPricingType"] = (
            capo_snowball.types.long_term_pricing_type.serialize_aws_json_1_1(
                value["long_term_pricing_type"]
            )
        )
    if "current_active_job" in value:
        out["CurrentActiveJob"] = value["current_active_job"]
    if "replacement_job" in value:
        out["ReplacementJob"] = value["replacement_job"]
    if "is_long_term_pricing_auto_renew" in value:
        out["IsLongTermPricingAutoRenew"] = value["is_long_term_pricing_auto_renew"]
    if "long_term_pricing_status" in value:
        out["LongTermPricingStatus"] = value["long_term_pricing_status"]
    if "snowball_type" in value:
        import capo_snowball.types.snowball_type

        out["SnowballType"] = capo_snowball.types.snowball_type.serialize_aws_json_1_1(
            value["snowball_type"]
        )
    if "job_ids" in value:
        import capo_snowball.types.long_term_pricing_associated_job_id_list

        out["JobIds"] = (
            capo_snowball.types.long_term_pricing_associated_job_id_list.serialize_aws_json_1_1(
                value["job_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LongTermPricingListEntry:
    out: LongTermPricingListEntry = {}  # type: ignore[typeddict-item]
    if data.get("LongTermPricingId") is not None:
        out["long_term_pricing_id"] = data["LongTermPricingId"]
    if data.get("LongTermPricingEndDate") is not None:
        import capo_snowball.types.timestamp

        out["long_term_pricing_end_date"] = (
            capo_snowball.types.timestamp.deserialize_aws_json_1_1(
                data["LongTermPricingEndDate"]
            )
        )
    if data.get("LongTermPricingStartDate") is not None:
        import capo_snowball.types.timestamp

        out["long_term_pricing_start_date"] = (
            capo_snowball.types.timestamp.deserialize_aws_json_1_1(
                data["LongTermPricingStartDate"]
            )
        )
    if data.get("LongTermPricingType") is not None:
        import capo_snowball.types.long_term_pricing_type

        out["long_term_pricing_type"] = (
            capo_snowball.types.long_term_pricing_type.deserialize_aws_json_1_1(
                data["LongTermPricingType"]
            )
        )
    if data.get("CurrentActiveJob") is not None:
        out["current_active_job"] = data["CurrentActiveJob"]
    if data.get("ReplacementJob") is not None:
        out["replacement_job"] = data["ReplacementJob"]
    if data.get("IsLongTermPricingAutoRenew") is not None:
        out["is_long_term_pricing_auto_renew"] = data["IsLongTermPricingAutoRenew"]
    if data.get("LongTermPricingStatus") is not None:
        out["long_term_pricing_status"] = data["LongTermPricingStatus"]
    if data.get("SnowballType") is not None:
        import capo_snowball.types.snowball_type

        out["snowball_type"] = (
            capo_snowball.types.snowball_type.deserialize_aws_json_1_1(
                data["SnowballType"]
            )
        )
    if data.get("JobIds") is not None:
        import capo_snowball.types.long_term_pricing_associated_job_id_list

        out["job_ids"] = (
            capo_snowball.types.long_term_pricing_associated_job_id_list.deserialize_aws_json_1_1(
                data["JobIds"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LongTermPricingListEntry) -> dict:
    out: dict = {}
    if "long_term_pricing_id" in value:
        out["LongTermPricingId"] = value["long_term_pricing_id"]
    if "long_term_pricing_end_date" in value:
        import capo_snowball.types.timestamp

        out["LongTermPricingEndDate"] = capo_snowball.types.timestamp.serialize_cbor(
            value["long_term_pricing_end_date"]
        )
    if "long_term_pricing_start_date" in value:
        import capo_snowball.types.timestamp

        out["LongTermPricingStartDate"] = capo_snowball.types.timestamp.serialize_cbor(
            value["long_term_pricing_start_date"]
        )
    if "long_term_pricing_type" in value:
        import capo_snowball.types.long_term_pricing_type

        out["LongTermPricingType"] = (
            capo_snowball.types.long_term_pricing_type.serialize_cbor(
                value["long_term_pricing_type"]
            )
        )
    if "current_active_job" in value:
        out["CurrentActiveJob"] = value["current_active_job"]
    if "replacement_job" in value:
        out["ReplacementJob"] = value["replacement_job"]
    if "is_long_term_pricing_auto_renew" in value:
        out["IsLongTermPricingAutoRenew"] = value["is_long_term_pricing_auto_renew"]
    if "long_term_pricing_status" in value:
        out["LongTermPricingStatus"] = value["long_term_pricing_status"]
    if "snowball_type" in value:
        import capo_snowball.types.snowball_type

        out["SnowballType"] = capo_snowball.types.snowball_type.serialize_cbor(
            value["snowball_type"]
        )
    if "job_ids" in value:
        import capo_snowball.types.long_term_pricing_associated_job_id_list

        out["JobIds"] = (
            capo_snowball.types.long_term_pricing_associated_job_id_list.serialize_cbor(
                value["job_ids"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> LongTermPricingListEntry:
    out: LongTermPricingListEntry = {}  # type: ignore[typeddict-item]
    if data.get("LongTermPricingId") is not None:
        out["long_term_pricing_id"] = data["LongTermPricingId"]
    if data.get("LongTermPricingEndDate") is not None:
        import capo_snowball.types.timestamp

        out["long_term_pricing_end_date"] = (
            capo_snowball.types.timestamp.deserialize_cbor(
                data["LongTermPricingEndDate"]
            )
        )
    if data.get("LongTermPricingStartDate") is not None:
        import capo_snowball.types.timestamp

        out["long_term_pricing_start_date"] = (
            capo_snowball.types.timestamp.deserialize_cbor(
                data["LongTermPricingStartDate"]
            )
        )
    if data.get("LongTermPricingType") is not None:
        import capo_snowball.types.long_term_pricing_type

        out["long_term_pricing_type"] = (
            capo_snowball.types.long_term_pricing_type.deserialize_cbor(
                data["LongTermPricingType"]
            )
        )
    if data.get("CurrentActiveJob") is not None:
        out["current_active_job"] = data["CurrentActiveJob"]
    if data.get("ReplacementJob") is not None:
        out["replacement_job"] = data["ReplacementJob"]
    if data.get("IsLongTermPricingAutoRenew") is not None:
        out["is_long_term_pricing_auto_renew"] = data["IsLongTermPricingAutoRenew"]
    if data.get("LongTermPricingStatus") is not None:
        out["long_term_pricing_status"] = data["LongTermPricingStatus"]
    if data.get("SnowballType") is not None:
        import capo_snowball.types.snowball_type

        out["snowball_type"] = capo_snowball.types.snowball_type.deserialize_cbor(
            data["SnowballType"]
        )
    if data.get("JobIds") is not None:
        import capo_snowball.types.long_term_pricing_associated_job_id_list

        out["job_ids"] = (
            capo_snowball.types.long_term_pricing_associated_job_id_list.deserialize_cbor(
                data["JobIds"]
            )
        )
    return out
