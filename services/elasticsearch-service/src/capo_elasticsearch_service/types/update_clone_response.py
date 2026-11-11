"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#UpdateCloneResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.cutover_options
    import capo_elasticsearch_service.types.domain_name
    import capo_elasticsearch_service.types.guid
    import capo_elasticsearch_service.types.retention_options
    import capo_elasticsearch_service.types.traffic_split_options


class UpdateCloneResponse(TypedDict, closed=True):
    domain_name: "capo_elasticsearch_service.types.domain_name.DomainName"
    """<p>The name of the domain.</p>"""
    change_id: "capo_elasticsearch_service.types.guid.GUID"
    """<p>The unique identifier of the configuration change. Use it with <code>DescribeDomainChangeProgress</code> to track the change.</p>"""
    cutover_options: NotRequired[
        "capo_elasticsearch_service.types.cutover_options.CutoverOptions"
    ]
    """<p>The requested cutover target and the status of the cutover.</p>"""
    traffic_split_options: NotRequired[
        "capo_elasticsearch_service.types.traffic_split_options.TrafficSplitOptions"
    ]
    """<p>The current and requested traffic split, and the status of the traffic shift.</p>"""
    retention_options: NotRequired[
        "capo_elasticsearch_service.types.retention_options.RetentionOptions"
    ]
    """<p>The retention settings for the upgrade.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCloneResponse) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    out["ChangeId"] = value["change_id"]
    if "cutover_options" in value:
        import capo_elasticsearch_service.types.cutover_options

        out["CutoverOptions"] = (
            capo_elasticsearch_service.types.cutover_options.serialize_json(
                value["cutover_options"]
            )
        )
    if "traffic_split_options" in value:
        import capo_elasticsearch_service.types.traffic_split_options

        out["TrafficSplitOptions"] = (
            capo_elasticsearch_service.types.traffic_split_options.serialize_json(
                value["traffic_split_options"]
            )
        )
    if "retention_options" in value:
        import capo_elasticsearch_service.types.retention_options

        out["RetentionOptions"] = (
            capo_elasticsearch_service.types.retention_options.serialize_json(
                value["retention_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateCloneResponse:
    out: UpdateCloneResponse = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("ChangeId") is not None:
        out["change_id"] = data["ChangeId"]
    else:
        out["change_id"] = ""
    if data.get("CutoverOptions") is not None:
        import capo_elasticsearch_service.types.cutover_options

        out["cutover_options"] = (
            capo_elasticsearch_service.types.cutover_options.deserialize_json(
                data["CutoverOptions"]
            )
        )
    if data.get("TrafficSplitOptions") is not None:
        import capo_elasticsearch_service.types.traffic_split_options

        out["traffic_split_options"] = (
            capo_elasticsearch_service.types.traffic_split_options.deserialize_json(
                data["TrafficSplitOptions"]
            )
        )
    if data.get("RetentionOptions") is not None:
        import capo_elasticsearch_service.types.retention_options

        out["retention_options"] = (
            capo_elasticsearch_service.types.retention_options.deserialize_json(
                data["RetentionOptions"]
            )
        )
    return out
