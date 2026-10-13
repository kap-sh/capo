"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#RestoreFromRecoveryPointResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.namespace


class RestoreFromRecoveryPointResponse(TypedDict, closed=True):
    recovery_point_id: NotRequired["str"]
    """<p>The unique identifier of the recovery point used for the restore.</p>"""
    namespace: NotRequired["capo_redshift_serverless.types.namespace.Namespace"]
    """<p>The namespace that data was restored into.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreFromRecoveryPointResponse) -> dict:
    out: dict = {}
    if "recovery_point_id" in value:
        out["recoveryPointId"] = value["recovery_point_id"]
    if "namespace" in value:
        import capo_redshift_serverless.types.namespace

        out["namespace"] = (
            capo_redshift_serverless.types.namespace.serialize_aws_json_1_1(
                value["namespace"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RestoreFromRecoveryPointResponse:
    out: RestoreFromRecoveryPointResponse = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPointId") is not None:
        out["recovery_point_id"] = data["recoveryPointId"]
    if data.get("namespace") is not None:
        import capo_redshift_serverless.types.namespace

        out["namespace"] = (
            capo_redshift_serverless.types.namespace.deserialize_aws_json_1_1(
                data["namespace"]
            )
        )
    return out


def redact_sensitive(value: RestoreFromRecoveryPointResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "namespace" in value:
        import capo_redshift_serverless.types.namespace

        out["namespace"] = capo_redshift_serverless.types.namespace.redact_sensitive(
            value["namespace"]
        )
    return out
