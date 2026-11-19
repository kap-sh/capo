"""Generated from Smithy shape ``com.amazonaws.pi#DescribeDimensionKeysResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.dimension_key_description_list
    import capo_pi.types.iso_timestamp
    import capo_pi.types.next_token
    import capo_pi.types.response_partition_key_list


class DescribeDimensionKeysResponse(TypedDict, closed=True):
    aligned_start_time: NotRequired["capo_pi.types.iso_timestamp.ISOTimestamp"]
    """<p>The start time for the returned dimension keys, after alignment to a granular boundary (as specified by <code>PeriodInSeconds</code>). <code>AlignedStartTime</code> will be less than or equal to the value of the user-specified <code>StartTime</code>. </p>"""
    aligned_end_time: NotRequired["capo_pi.types.iso_timestamp.ISOTimestamp"]
    """<p>The end time for the returned dimension keys, after alignment to a granular boundary (as specified by <code>PeriodInSeconds</code>). <code>AlignedEndTime</code> will be greater than or equal to the value of the user-specified <code>Endtime</code>. </p>"""
    partition_keys: NotRequired[
        "capo_pi.types.response_partition_key_list.ResponsePartitionKeyList"
    ]
    """<p>If <code>PartitionBy</code> was present in the request, <code>PartitionKeys</code> contains the breakdown of dimension keys by the specified partitions. </p>"""
    keys: NotRequired[
        "capo_pi.types.dimension_key_description_list.DimensionKeyDescriptionList"
    ]
    """<p>The dimension keys that were requested.</p>"""
    next_token: NotRequired["capo_pi.types.next_token.NextToken"]
    """<p>A pagination token that indicates the response didn’t return all available records because <code>MaxRecords</code> was specified in the previous request. To get the remaining records, specify <code>NextToken</code> in a separate request with this value. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDimensionKeysResponse) -> dict:
    out: dict = {}
    if "aligned_start_time" in value:
        import capo_pi.types.iso_timestamp

        out["AlignedStartTime"] = capo_pi.types.iso_timestamp.serialize_aws_json_1_1(
            value["aligned_start_time"]
        )
    if "aligned_end_time" in value:
        import capo_pi.types.iso_timestamp

        out["AlignedEndTime"] = capo_pi.types.iso_timestamp.serialize_aws_json_1_1(
            value["aligned_end_time"]
        )
    if "partition_keys" in value:
        import capo_pi.types.response_partition_key_list

        out["PartitionKeys"] = (
            capo_pi.types.response_partition_key_list.serialize_aws_json_1_1(
                value["partition_keys"]
            )
        )
    if "keys" in value:
        import capo_pi.types.dimension_key_description_list

        out["Keys"] = (
            capo_pi.types.dimension_key_description_list.serialize_aws_json_1_1(
                value["keys"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDimensionKeysResponse:
    out: DescribeDimensionKeysResponse = {}  # type: ignore[typeddict-item]
    if data.get("AlignedStartTime") is not None:
        import capo_pi.types.iso_timestamp

        out["aligned_start_time"] = (
            capo_pi.types.iso_timestamp.deserialize_aws_json_1_1(
                data["AlignedStartTime"]
            )
        )
    if data.get("AlignedEndTime") is not None:
        import capo_pi.types.iso_timestamp

        out["aligned_end_time"] = capo_pi.types.iso_timestamp.deserialize_aws_json_1_1(
            data["AlignedEndTime"]
        )
    if data.get("PartitionKeys") is not None:
        import capo_pi.types.response_partition_key_list

        out["partition_keys"] = (
            capo_pi.types.response_partition_key_list.deserialize_aws_json_1_1(
                data["PartitionKeys"]
            )
        )
    if data.get("Keys") is not None:
        import capo_pi.types.dimension_key_description_list

        out["keys"] = (
            capo_pi.types.dimension_key_description_list.deserialize_aws_json_1_1(
                data["Keys"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeDimensionKeysResponse) -> dict:
    out: dict = {}
    if "aligned_start_time" in value:
        import capo_pi.types.iso_timestamp

        out["AlignedStartTime"] = capo_pi.types.iso_timestamp.serialize_cbor(
            value["aligned_start_time"]
        )
    if "aligned_end_time" in value:
        import capo_pi.types.iso_timestamp

        out["AlignedEndTime"] = capo_pi.types.iso_timestamp.serialize_cbor(
            value["aligned_end_time"]
        )
    if "partition_keys" in value:
        import capo_pi.types.response_partition_key_list

        out["PartitionKeys"] = capo_pi.types.response_partition_key_list.serialize_cbor(
            value["partition_keys"]
        )
    if "keys" in value:
        import capo_pi.types.dimension_key_description_list

        out["Keys"] = capo_pi.types.dimension_key_description_list.serialize_cbor(
            value["keys"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeDimensionKeysResponse:
    out: DescribeDimensionKeysResponse = {}  # type: ignore[typeddict-item]
    if data.get("AlignedStartTime") is not None:
        import capo_pi.types.iso_timestamp

        out["aligned_start_time"] = capo_pi.types.iso_timestamp.deserialize_cbor(
            data["AlignedStartTime"]
        )
    if data.get("AlignedEndTime") is not None:
        import capo_pi.types.iso_timestamp

        out["aligned_end_time"] = capo_pi.types.iso_timestamp.deserialize_cbor(
            data["AlignedEndTime"]
        )
    if data.get("PartitionKeys") is not None:
        import capo_pi.types.response_partition_key_list

        out["partition_keys"] = (
            capo_pi.types.response_partition_key_list.deserialize_cbor(
                data["PartitionKeys"]
            )
        )
    if data.get("Keys") is not None:
        import capo_pi.types.dimension_key_description_list

        out["keys"] = capo_pi.types.dimension_key_description_list.deserialize_cbor(
            data["Keys"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
