"""Generated from Smithy shape ``com.amazonaws.comprehend#EndpointFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.comprehend_model_arn
    import capo_comprehend.types.endpoint_status
    import capo_comprehend.types.timestamp


class EndpointFilter(TypedDict, closed=True):
    model_arn: NotRequired[
        "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the model to which the endpoint is attached.</p>"""
    status: NotRequired["capo_comprehend.types.endpoint_status.EndpointStatus"]
    """<p>Specifies the status of the endpoint being returned. Possible values are: Creating, Ready, Updating, Deleting, Failed.</p>"""
    creation_time_before: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>Specifies a date before which the returned endpoint or endpoints were created.</p>"""
    creation_time_after: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>Specifies a date after which the returned endpoint or endpoints were created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointFilter) -> dict:
    out: dict = {}
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    if "status" in value:
        import capo_comprehend.types.endpoint_status

        out["Status"] = capo_comprehend.types.endpoint_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "creation_time_before" in value:
        import capo_comprehend.types.timestamp

        out["CreationTimeBefore"] = (
            capo_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "creation_time_after" in value:
        import capo_comprehend.types.timestamp

        out["CreationTimeAfter"] = (
            capo_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointFilter:
    out: EndpointFilter = {}  # type: ignore[typeddict-item]
    if data.get("ModelArn") is not None:
        out["model_arn"] = data["ModelArn"]
    if data.get("Status") is not None:
        import capo_comprehend.types.endpoint_status

        out["status"] = capo_comprehend.types.endpoint_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("CreationTimeBefore") is not None:
        import capo_comprehend.types.timestamp

        out["creation_time_before"] = (
            capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    if data.get("CreationTimeAfter") is not None:
        import capo_comprehend.types.timestamp

        out["creation_time_after"] = (
            capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EndpointFilter) -> dict:
    out: dict = {}
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    if "status" in value:
        import capo_comprehend.types.endpoint_status

        out["Status"] = capo_comprehend.types.endpoint_status.serialize_cbor(
            value["status"]
        )
    if "creation_time_before" in value:
        import capo_comprehend.types.timestamp

        out["CreationTimeBefore"] = capo_comprehend.types.timestamp.serialize_cbor(
            value["creation_time_before"]
        )
    if "creation_time_after" in value:
        import capo_comprehend.types.timestamp

        out["CreationTimeAfter"] = capo_comprehend.types.timestamp.serialize_cbor(
            value["creation_time_after"]
        )
    return out


def deserialize_cbor(data: dict) -> EndpointFilter:
    out: EndpointFilter = {}  # type: ignore[typeddict-item]
    if data.get("ModelArn") is not None:
        out["model_arn"] = data["ModelArn"]
    if data.get("Status") is not None:
        import capo_comprehend.types.endpoint_status

        out["status"] = capo_comprehend.types.endpoint_status.deserialize_cbor(
            data["Status"]
        )
    if data.get("CreationTimeBefore") is not None:
        import capo_comprehend.types.timestamp

        out["creation_time_before"] = capo_comprehend.types.timestamp.deserialize_cbor(
            data["CreationTimeBefore"]
        )
    if data.get("CreationTimeAfter") is not None:
        import capo_comprehend.types.timestamp

        out["creation_time_after"] = capo_comprehend.types.timestamp.deserialize_cbor(
            data["CreationTimeAfter"]
        )
    return out
