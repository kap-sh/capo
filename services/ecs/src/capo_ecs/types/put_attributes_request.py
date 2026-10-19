"""Generated from Smithy shape ``com.amazonaws.ecs#PutAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.attributes
    import capo_ecs.types.string


class PutAttributesRequest(TypedDict, closed=True):
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that contains the resource to apply attributes. If you do not specify a cluster, the default cluster is assumed.</p>"""
    attributes: "capo_ecs.types.attributes.Attributes"
    """<p>The attributes to apply to your resource. You can specify up to 10 custom attributes for each resource. You can specify up to 10 attributes in a single call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAttributesRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    import capo_ecs.types.attributes

    out["attributes"] = capo_ecs.types.attributes.serialize_aws_json_1_1(
        value["attributes"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAttributesRequest:
    out: PutAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    if data.get("attributes") is not None:
        import capo_ecs.types.attributes

        out["attributes"] = capo_ecs.types.attributes.deserialize_aws_json_1_1(
            data["attributes"]
        )
    else:
        out["attributes"] = []
    return out
