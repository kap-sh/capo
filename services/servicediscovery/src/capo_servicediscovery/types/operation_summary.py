"""Generated from Smithy shape ``com.amazonaws.servicediscovery#OperationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.operation_id
    import capo_servicediscovery.types.operation_status


class OperationSummary(TypedDict, closed=True):
    id: NotRequired["capo_servicediscovery.types.operation_id.OperationId"]
    """<p>The ID for an operation.</p>"""
    status: NotRequired["capo_servicediscovery.types.operation_status.OperationStatus"]
    """<p>The status of the operation. Values include the following:</p> <ul> <li> <p> <b>SUBMITTED</b>: This is the initial state immediately after you submit a request.</p> </li> <li> <p> <b>PENDING</b>: Cloud Map is performing the operation.</p> </li> <li> <p> <b>SUCCESS</b>: The operation succeeded.</p> </li> <li> <p> <b>FAIL</b>: The operation failed. For the failure reason, see <code>ErrorMessage</code>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "status" in value:
        import capo_servicediscovery.types.operation_status

        out["Status"] = (
            capo_servicediscovery.types.operation_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OperationSummary:
    out: OperationSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Status") is not None:
        import capo_servicediscovery.types.operation_status

        out["status"] = (
            capo_servicediscovery.types.operation_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OperationSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "status" in value:
        import capo_servicediscovery.types.operation_status

        out["Status"] = capo_servicediscovery.types.operation_status.serialize_cbor(
            value["status"]
        )
    return out


def deserialize_cbor(data: dict) -> OperationSummary:
    out: OperationSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Status") is not None:
        import capo_servicediscovery.types.operation_status

        out["status"] = capo_servicediscovery.types.operation_status.deserialize_cbor(
            data["Status"]
        )
    return out
