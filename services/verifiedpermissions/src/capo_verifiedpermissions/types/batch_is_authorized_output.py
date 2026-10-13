"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchIsAuthorizedOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.batch_is_authorized_output_list


class BatchIsAuthorizedOutput(TypedDict, closed=True):
    results: "capo_verifiedpermissions.types.batch_is_authorized_output_list.BatchIsAuthorizedOutputList"
    """<p>A series of <code>Allow</code> or <code>Deny</code> decisions for each request, and the policies that produced them. These results are returned in the order they were requested.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchIsAuthorizedOutput) -> dict:
    out: dict = {}
    import capo_verifiedpermissions.types.batch_is_authorized_output_list

    out["results"] = (
        capo_verifiedpermissions.types.batch_is_authorized_output_list.serialize_aws_json_1_0(
            value["results"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchIsAuthorizedOutput:
    out: BatchIsAuthorizedOutput = {}  # type: ignore[typeddict-item]
    if data.get("results") is not None:
        import capo_verifiedpermissions.types.batch_is_authorized_output_list

        out["results"] = (
            capo_verifiedpermissions.types.batch_is_authorized_output_list.deserialize_aws_json_1_0(
                data["results"]
            )
        )
    else:
        raise DeserializationError("BatchIsAuthorizedOutput.results required")
    return out


def redact_sensitive(value: BatchIsAuthorizedOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "results" in value:
        import capo_verifiedpermissions.types.batch_is_authorized_output_list

        out["results"] = (
            capo_verifiedpermissions.types.batch_is_authorized_output_list.redact_sensitive(
                value["results"]
            )
        )
    return out
