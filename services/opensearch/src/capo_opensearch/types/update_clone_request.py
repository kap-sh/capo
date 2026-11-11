"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdateCloneRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.cutover_request_options
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.retention_options
    import capo_opensearch.types.traffic_split_request_options


class UpdateCloneRequest(TypedDict, closed=True):
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    """<p>The name of the domain that has a cloned blue/green upgrade in progress.</p>"""
    traffic_split_options: NotRequired[
        "capo_opensearch.types.traffic_split_request_options.TrafficSplitRequestOptions"
    ]
    """<p>Shifts a percentage of search traffic from the primary cluster to the cloned cluster.</p>"""
    cutover_options: NotRequired[
        "capo_opensearch.types.cutover_request_options.CutoverRequestOptions"
    ]
    """<p>Cuts the domain over to the cloned cluster or back to the primary cluster.</p>"""
    retention_options: NotRequired[
        "capo_opensearch.types.retention_options.RetentionOptions"
    ]
    """<p>Changes the retention period, or ends it after cutover completes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCloneRequest) -> dict:
    out: dict = {}
    if "traffic_split_options" in value:
        import capo_opensearch.types.traffic_split_request_options

        out["TrafficSplitOptions"] = (
            capo_opensearch.types.traffic_split_request_options.serialize_json(
                value["traffic_split_options"]
            )
        )
    if "cutover_options" in value:
        import capo_opensearch.types.cutover_request_options

        out["CutoverOptions"] = (
            capo_opensearch.types.cutover_request_options.serialize_json(
                value["cutover_options"]
            )
        )
    if "retention_options" in value:
        import capo_opensearch.types.retention_options

        out["RetentionOptions"] = (
            capo_opensearch.types.retention_options.serialize_json(
                value["retention_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateCloneRequest:
    out: UpdateCloneRequest = {}  # type: ignore[typeddict-item]
    if data.get("TrafficSplitOptions") is not None:
        import capo_opensearch.types.traffic_split_request_options

        out["traffic_split_options"] = (
            capo_opensearch.types.traffic_split_request_options.deserialize_json(
                data["TrafficSplitOptions"]
            )
        )
    if data.get("CutoverOptions") is not None:
        import capo_opensearch.types.cutover_request_options

        out["cutover_options"] = (
            capo_opensearch.types.cutover_request_options.deserialize_json(
                data["CutoverOptions"]
            )
        )
    if data.get("RetentionOptions") is not None:
        import capo_opensearch.types.retention_options

        out["retention_options"] = (
            capo_opensearch.types.retention_options.deserialize_json(
                data["RetentionOptions"]
            )
        )
    return out
