"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeRecordOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.page_token
    import capo_service_catalog.types.record_detail
    import capo_service_catalog.types.record_outputs


class DescribeRecordOutput(TypedDict, closed=True):
    record_detail: NotRequired["capo_service_catalog.types.record_detail.RecordDetail"]
    """<p>Information about the product.</p>"""
    record_outputs: NotRequired[
        "capo_service_catalog.types.record_outputs.RecordOutputs"
    ]
    """<p>Information about the product created as the result of a request. For example, the output for a CloudFormation-backed product that creates an S3 bucket would include the S3 bucket URL.</p>"""
    next_page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRecordOutput) -> dict:
    out: dict = {}
    if "record_detail" in value:
        import capo_service_catalog.types.record_detail

        out["RecordDetail"] = (
            capo_service_catalog.types.record_detail.serialize_aws_json_1_1(
                value["record_detail"]
            )
        )
    if "record_outputs" in value:
        import capo_service_catalog.types.record_outputs

        out["RecordOutputs"] = (
            capo_service_catalog.types.record_outputs.serialize_aws_json_1_1(
                value["record_outputs"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRecordOutput:
    out: DescribeRecordOutput = {}  # type: ignore[typeddict-item]
    if data.get("RecordDetail") is not None:
        import capo_service_catalog.types.record_detail

        out["record_detail"] = (
            capo_service_catalog.types.record_detail.deserialize_aws_json_1_1(
                data["RecordDetail"]
            )
        )
    if data.get("RecordOutputs") is not None:
        import capo_service_catalog.types.record_outputs

        out["record_outputs"] = (
            capo_service_catalog.types.record_outputs.deserialize_aws_json_1_1(
                data["RecordOutputs"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeRecordOutput) -> dict:
    out: dict = {}
    if "record_detail" in value:
        import capo_service_catalog.types.record_detail

        out["RecordDetail"] = capo_service_catalog.types.record_detail.serialize_cbor(
            value["record_detail"]
        )
    if "record_outputs" in value:
        import capo_service_catalog.types.record_outputs

        out["RecordOutputs"] = capo_service_catalog.types.record_outputs.serialize_cbor(
            value["record_outputs"]
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeRecordOutput:
    out: DescribeRecordOutput = {}  # type: ignore[typeddict-item]
    if data.get("RecordDetail") is not None:
        import capo_service_catalog.types.record_detail

        out["record_detail"] = (
            capo_service_catalog.types.record_detail.deserialize_cbor(
                data["RecordDetail"]
            )
        )
    if data.get("RecordOutputs") is not None:
        import capo_service_catalog.types.record_outputs

        out["record_outputs"] = (
            capo_service_catalog.types.record_outputs.deserialize_cbor(
                data["RecordOutputs"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
