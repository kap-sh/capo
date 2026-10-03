"""Generated from Smithy shape ``com.amazonaws.connect#ReplicationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.aws_region
    import capo_connect.types.global_sign_in_endpoint
    import capo_connect.types.replication_status_summary_list


class ReplicationConfiguration(TypedDict, closed=True):
    replication_status_summary_list: NotRequired[
        "capo_connect.types.replication_status_summary_list.ReplicationStatusSummaryList"
    ]
    """<p>A list of replication status summaries. The summaries contain details about the replication of configuration information for Connect Customer resources, for each Amazon Web Services Region.</p>"""
    source_region: NotRequired["capo_connect.types.aws_region.AwsRegion"]
    """<p>The Amazon Web Services Region where the source Connect Customer instance was created. This is the Region where the <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_ReplicateInstance.html">ReplicateInstance</a> API was called to start the replication process.</p>"""
    global_sign_in_endpoint: NotRequired[
        "capo_connect.types.global_sign_in_endpoint.GlobalSignInEndpoint"
    ]
    """<p>The URL that is used to sign-in to your Connect Customer instance according to your traffic distribution group configuration. For more information about sign-in and traffic distribution groups, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/setup-traffic-distribution-groups.html">Important things to know</a> in the <i>Create traffic distribution groups</i> topic in the <i>Connect Customer Administrator Guide</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationConfiguration) -> dict:
    out: dict = {}
    if "replication_status_summary_list" in value:
        import capo_connect.types.replication_status_summary_list

        out["ReplicationStatusSummaryList"] = (
            capo_connect.types.replication_status_summary_list.serialize_json(
                value["replication_status_summary_list"]
            )
        )
    if "source_region" in value:
        out["SourceRegion"] = value["source_region"]
    if "global_sign_in_endpoint" in value:
        out["GlobalSignInEndpoint"] = value["global_sign_in_endpoint"]
    return out


def deserialize_json(data: dict) -> ReplicationConfiguration:
    out: ReplicationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationStatusSummaryList") is not None:
        import capo_connect.types.replication_status_summary_list

        out["replication_status_summary_list"] = (
            capo_connect.types.replication_status_summary_list.deserialize_json(
                data["ReplicationStatusSummaryList"]
            )
        )
    if data.get("SourceRegion") is not None:
        out["source_region"] = data["SourceRegion"]
    if data.get("GlobalSignInEndpoint") is not None:
        out["global_sign_in_endpoint"] = data["GlobalSignInEndpoint"]
    return out
