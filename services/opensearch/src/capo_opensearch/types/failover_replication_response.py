"""Generated from Smithy shape ``com.amazonaws.opensearch#FailoverReplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_arn
    import capo_opensearch.types.replication_status


class FailoverReplicationResponse(TypedDict, closed=True):
    domain_arn: NotRequired["capo_opensearch.types.domain_arn.DomainArn"]
    """<p>The Amazon Resource Name (ARN) of the domain being promoted.</p>"""
    status: NotRequired["capo_opensearch.types.replication_status.ReplicationStatus"]
    """<p>The state of the replication relationship. This is <code>FAILING_OVER</code> while the promotion is in progress.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailoverReplicationResponse) -> dict:
    out: dict = {}
    if "domain_arn" in value:
        out["DomainArn"] = value["domain_arn"]
    if "status" in value:
        import capo_opensearch.types.replication_status

        out["Status"] = capo_opensearch.types.replication_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> FailoverReplicationResponse:
    out: FailoverReplicationResponse = {}  # type: ignore[typeddict-item]
    if data.get("DomainArn") is not None:
        out["domain_arn"] = data["DomainArn"]
    if data.get("Status") is not None:
        import capo_opensearch.types.replication_status

        out["status"] = capo_opensearch.types.replication_status.deserialize_json(
            data["Status"]
        )
    return out
