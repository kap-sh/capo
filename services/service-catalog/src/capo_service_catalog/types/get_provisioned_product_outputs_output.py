"""Generated from Smithy shape ``com.amazonaws.servicecatalog#GetProvisionedProductOutputsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.page_token
    import capo_service_catalog.types.record_outputs


class GetProvisionedProductOutputsOutput(TypedDict, closed=True):
    outputs: NotRequired["capo_service_catalog.types.record_outputs.RecordOutputs"]
    """<p>Information about the product created as the result of a request. For example, the output for a CloudFormation-backed product that creates an S3 bucket would include the S3 bucket URL. </p>"""
    next_page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetProvisionedProductOutputsOutput) -> dict:
    out: dict = {}
    if "outputs" in value:
        import capo_service_catalog.types.record_outputs

        out["Outputs"] = (
            capo_service_catalog.types.record_outputs.serialize_aws_json_1_1(
                value["outputs"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetProvisionedProductOutputsOutput:
    out: GetProvisionedProductOutputsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Outputs") is not None:
        import capo_service_catalog.types.record_outputs

        out["outputs"] = (
            capo_service_catalog.types.record_outputs.deserialize_aws_json_1_1(
                data["Outputs"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetProvisionedProductOutputsOutput) -> dict:
    out: dict = {}
    if "outputs" in value:
        import capo_service_catalog.types.record_outputs

        out["Outputs"] = capo_service_catalog.types.record_outputs.serialize_cbor(
            value["outputs"]
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_cbor(data: dict) -> GetProvisionedProductOutputsOutput:
    out: GetProvisionedProductOutputsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Outputs") is not None:
        import capo_service_catalog.types.record_outputs

        out["outputs"] = capo_service_catalog.types.record_outputs.deserialize_cbor(
            data["Outputs"]
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
