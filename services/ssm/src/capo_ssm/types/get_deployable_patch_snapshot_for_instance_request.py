"""Generated from Smithy shape ``com.amazonaws.ssm#GetDeployablePatchSnapshotForInstanceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.baseline_override
    import capo_ssm.types.boolean
    import capo_ssm.types.instance_id
    import capo_ssm.types.snapshot_id


class GetDeployablePatchSnapshotForInstanceRequest(TypedDict, closed=True):
    instance_id: "capo_ssm.types.instance_id.InstanceId"
    """<p>The ID of the managed node for which the appropriate patch snapshot should be retrieved.</p>"""
    snapshot_id: "capo_ssm.types.snapshot_id.SnapshotId"
    """<p>The snapshot ID provided by the user when running <code>AWS-RunPatchBaseline</code>.</p>"""
    baseline_override: NotRequired["capo_ssm.types.baseline_override.BaselineOverride"]
    """<p>Defines the basic information about a patch baseline override.</p>"""
    use_s3_dual_stack_endpoint: "capo_ssm.types.boolean.Boolean"
    """<p>Specifies whether to use S3 dualstack endpoints for the patch snapshot download URL. Set to <code>true</code> to receive a presigned URL that supports both IPv4 and IPv6 connectivity. Set to <code>false</code> to use standard IPv4-only endpoints. Default is <code>false</code>. This parameter is required for managed nodes in IPv6-only environments. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeployablePatchSnapshotForInstanceRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["SnapshotId"] = value["snapshot_id"]
    if "baseline_override" in value:
        import capo_ssm.types.baseline_override

        out["BaselineOverride"] = (
            capo_ssm.types.baseline_override.serialize_aws_json_1_1(
                value["baseline_override"]
            )
        )
    out["UseS3DualStackEndpoint"] = value.get("use_s3_dual_stack_endpoint", False)
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetDeployablePatchSnapshotForInstanceRequest:
    out: GetDeployablePatchSnapshotForInstanceRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError(
            "GetDeployablePatchSnapshotForInstanceRequest.instance_id required"
        )
    if data.get("SnapshotId") is not None:
        out["snapshot_id"] = data["SnapshotId"]
    else:
        raise DeserializationError(
            "GetDeployablePatchSnapshotForInstanceRequest.snapshot_id required"
        )
    if data.get("BaselineOverride") is not None:
        import capo_ssm.types.baseline_override

        out["baseline_override"] = (
            capo_ssm.types.baseline_override.deserialize_aws_json_1_1(
                data["BaselineOverride"]
            )
        )
    if data.get("UseS3DualStackEndpoint") is not None:
        out["use_s3_dual_stack_endpoint"] = data["UseS3DualStackEndpoint"]
    else:
        out["use_s3_dual_stack_endpoint"] = False
    return out


def redact_sensitive(
    value: GetDeployablePatchSnapshotForInstanceRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "baseline_override" in value:
        import capo_ssm.types.baseline_override

        out["baseline_override"] = capo_ssm.types.baseline_override.redact_sensitive(
            value["baseline_override"]
        )
    return out
