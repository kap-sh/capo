"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeServicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.service_field_list
    import capo_ecs.types.string
    import capo_ecs.types.string_list


class DescribeServicesRequest(TypedDict, closed=True):
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN)the cluster that hosts the service to describe. If you do not specify a cluster, the default cluster is assumed. This parameter is required if the service or services you are describing were launched in any cluster other than the default cluster.</p>"""
    services: "capo_ecs.types.string_list.StringList"
    """<p>A list of services to describe. You may specify up to 10 services to describe in a single operation.</p>"""
    include: NotRequired["capo_ecs.types.service_field_list.ServiceFieldList"]
    """<p>Determines whether you want to see the resource tags for the service. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeServicesRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    import capo_ecs.types.string_list

    out["services"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
        value["services"]
    )
    if "include" in value:
        import capo_ecs.types.service_field_list

        out["include"] = capo_ecs.types.service_field_list.serialize_aws_json_1_1(
            value["include"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeServicesRequest:
    out: DescribeServicesRequest = {}  # type: ignore[typeddict-item]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    if data.get("services") is not None:
        import capo_ecs.types.string_list

        out["services"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["services"]
        )
    else:
        out["services"] = []
    if data.get("include") is not None:
        import capo_ecs.types.service_field_list

        out["include"] = capo_ecs.types.service_field_list.deserialize_aws_json_1_1(
            data["include"]
        )
    return out
