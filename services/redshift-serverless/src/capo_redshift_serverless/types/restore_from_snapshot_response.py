"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#RestoreFromSnapshotResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.namespace


class RestoreFromSnapshotResponse(TypedDict, closed=True):
    snapshot_name: NotRequired["str"]
    """<p>The name of the snapshot used to restore the namespace.</p>"""
    owner_account: NotRequired["str"]
    """<p>The owner Amazon Web Services; account of the snapshot that was restored.</p>"""
    namespace: NotRequired["capo_redshift_serverless.types.namespace.Namespace"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreFromSnapshotResponse) -> dict:
    out: dict = {}
    if "snapshot_name" in value:
        out["snapshotName"] = value["snapshot_name"]
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "namespace" in value:
        import capo_redshift_serverless.types.namespace

        out["namespace"] = (
            capo_redshift_serverless.types.namespace.serialize_aws_json_1_1(
                value["namespace"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RestoreFromSnapshotResponse:
    out: RestoreFromSnapshotResponse = {}  # type: ignore[typeddict-item]
    if data.get("snapshotName") is not None:
        out["snapshot_name"] = data["snapshotName"]
    if data.get("ownerAccount") is not None:
        out["owner_account"] = data["ownerAccount"]
    if data.get("namespace") is not None:
        import capo_redshift_serverless.types.namespace

        out["namespace"] = (
            capo_redshift_serverless.types.namespace.deserialize_aws_json_1_1(
                data["namespace"]
            )
        )
    return out


def redact_sensitive(value: RestoreFromSnapshotResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "namespace" in value:
        import capo_redshift_serverless.types.namespace

        out["namespace"] = capo_redshift_serverless.types.namespace.redact_sensitive(
            value["namespace"]
        )
    return out
