"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchIsAuthorizedWithTokenOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.batch_is_authorized_with_token_output_list
    import capo_verifiedpermissions.types.entity_identifier


class BatchIsAuthorizedWithTokenOutput(TypedDict, closed=True):
    principal: NotRequired[
        "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
    ]
    """<p>The identifier of the principal in the ID or access token.</p>"""
    results: "capo_verifiedpermissions.types.batch_is_authorized_with_token_output_list.BatchIsAuthorizedWithTokenOutputList"
    """<p>A series of <code>Allow</code> or <code>Deny</code> decisions for each request, and the policies that produced them. These results are returned in the order they were requested.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchIsAuthorizedWithTokenOutput) -> dict:
    out: dict = {}
    if "principal" in value:
        import capo_verifiedpermissions.types.entity_identifier

        out["principal"] = (
            capo_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
                value["principal"]
            )
        )
    import capo_verifiedpermissions.types.batch_is_authorized_with_token_output_list

    out["results"] = (
        capo_verifiedpermissions.types.batch_is_authorized_with_token_output_list.serialize_aws_json_1_0(
            value["results"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchIsAuthorizedWithTokenOutput:
    out: BatchIsAuthorizedWithTokenOutput = {}  # type: ignore[typeddict-item]
    if data.get("principal") is not None:
        import capo_verifiedpermissions.types.entity_identifier

        out["principal"] = (
            capo_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                data["principal"]
            )
        )
    if data.get("results") is not None:
        import capo_verifiedpermissions.types.batch_is_authorized_with_token_output_list

        out["results"] = (
            capo_verifiedpermissions.types.batch_is_authorized_with_token_output_list.deserialize_aws_json_1_0(
                data["results"]
            )
        )
    else:
        out["results"] = []
    return out


def redact_sensitive(value: BatchIsAuthorizedWithTokenOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "principal" in value:
        import capo_verifiedpermissions.types.entity_identifier

        out["principal"] = (
            capo_verifiedpermissions.types.entity_identifier.redact_sensitive(
                value["principal"]
            )
        )
    if "results" in value:
        import capo_verifiedpermissions.types.batch_is_authorized_with_token_output_list

        out["results"] = (
            capo_verifiedpermissions.types.batch_is_authorized_with_token_output_list.redact_sensitive(
                value["results"]
            )
        )
    return out
